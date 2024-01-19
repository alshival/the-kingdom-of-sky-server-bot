from datetime import datetime, timedelta

early_sky_offset = timedelta(minutes=-32, seconds=-10)
eruption_offset = timedelta(minutes=7)
land_offset = timedelta(minutes=8, seconds=40)
end_offset = timedelta(hours=4)

black_shard_interval = timedelta(hours=8)
red_shard_interval = timedelta(hours=6)

realms = ['prairie', 'forest', 'valley', 'wasteland', 'vault']
areas_translation = {
    'prairie.butterfly': ['Butterfly Field', 'Village Islands'],
    'forest.brook': ['Forest Brook', 'Boneyard'],
    'valley.rink': ['Ice Rink'],
    'wasteland.temple': ['Broken Temple', 'Battlefield'],
    'vault.starlight': ['Starlight Desert'],
    'prairie.village': ['Village Islands', 'Boneyard'],
    'forest.boneyard': ['Boneyard', 'Forest Garden', 'Treehouse'],
    'valley.rink': ['Ice Rink'],
    'wasteland.battlefield': ['Battlefield', 'Graveyard', 'Crabfield'],
    'vault.starlight': ['Starlight Desert'],
    'prairie.cave': ['Cave', 'Forest Garden', 'Village of Dreams'],
    'forest.end': ['Forest Garden', 'Treehouse', 'Elevated Clearing'],
    'valley.dreams': ['Village of Dreams', 'Hermit valley'],
    'wasteland.graveyard': ['Graveyard', 'Crabfield', 'Forgotten Ark'],
    'vault.jelly': ['Jellyfish Cove']
}

shards_info = [
    {
        'noShardWkDay': [5,6],
        'interval': black_shard_interval,
        'offset': timedelta(hours=1, minutes=50),
        'maps': ['prairie.butterfly', 'forest.brook', 'valley.rink', 'wasteland.temple', 'vault.starlight']
    },
    {
        'noShardWkDay': [6,0],
        'interval': black_shard_interval,
        'offset': timedelta(hours=2, minutes=10),
        'maps': ['prairie.village', 'forest.boneyard', 'valley.rink', 'wasteland.battlefield', 'vault.starlight']
    },
    {
        'noShardWkDay': [0,1],
        'interval': red_shard_interval,
        'offset': timedelta(hours=7, minutes=40),
        'maps': ['prairie.cave', 'forest.end', 'valley.dreams', 'wasteland.graveyard', 'vault.jelly'],
        'defRewardAC': 2
    },
    {
        'noShardWkDay': [1,2],
        'interval': red_shard_interval,
        'offset': timedelta(hours=2, minutes=20),
        'maps': ['prairie.bird', 'forest.tree', 'valley.dreams', 'wasteland.crab', 'vault.jelly'],
        'defRewardAC': 2.5
    },
    {
        'noShardWkDay': [2,3],
        'interval': red_shard_interval,
        'offset': timedelta(hours=3, minutes=30),
        'maps': ['prairie.island', 'forest.sunny', 'valley.hermit', 'wasteland.ark', 'vault.jelly'],
        'defRewardAC': 3.5
    }
]

override_reward_AC = {
    'forest.end': 2.5,
    'valley.dreams': 2.5,
    'forest.tree': 3.5,
    'vault.jelly': 3.5
}

def get_shard_info(date):
    today = date.replace(hour=0, minute=0, second=0, microsecond=0)
    day_of_month = today.day
    day_of_week = today.weekday()
    is_red = day_of_month % 2 == 1
    realm_idx = (day_of_month - 1) % 5
    info_index = ((day_of_month - 1) // 2) % 3 + 2 if is_red else (day_of_month // 2) % 2
    shard_info = shards_info[info_index]
    no_shard_weekday = shard_info['noShardWkDay']
    have_shard = day_of_week not in no_shard_weekday
    map_key = shard_info['maps'][realm_idx]
    reward_AC = override_reward_AC.get(map_key, shard_info.get('defRewardAC'))
    occurrences = [
        (today + shard_info['offset'] + shard_info['interval'] * i) for i in range(3)
    ]
    return {
        'date': date,
        'isRed': is_red,
        'haveShard': have_shard,
        'offset': shard_info['offset'],
        'interval': shard_info['interval'],
        'lastEnd': occurrences[-1] + end_offset,
        'realm': realms[realm_idx],
        'map': map_key,
        'rewardAC': reward_AC,
        'occurrences': occurrences
    }

def get_upcoming_shard_phase(now, info=None):
    if info is None:
        info = get_shard_info(now)
    interval, last_end = info['interval'], info['lastEnd']
    if now > last_end:
        return None
    second_end = last_end - interval
    if now > second_end:
        start = last_end - end_offset
        return {'index': 2, 'start': start, 'land': start + land_offset, 'end': last_end}
    first_end = second_end - interval
    if now > first_end:
        start = second_end - end_offset
        return {'index': 1, 'start': start, 'land': start + land_offset, 'end': second_end}
    start = first_end - end_offset
    return {'index': 0, 'start': start, 'land': start + land_offset, 'end': first_end}

def get_all_shard_full_phases(now, info=None):
    today = now.replace(hour=0, minute=0, second=0, microsecond=0)
    if info is None:
        info = get_shard_info(now)
    offset, interval = info['offset'], info['interval']
    return [
        {
            'start': today + offset + interval * i,
            'earlySky': today + offset + interval * i + early_sky_offset,
            'eruption': today + offset + interval * i + eruption_offset,
            'land': today + offset + interval * i + land_offset,
            'end': today + offset + interval * i + end_offset
        } for i in range(3)
    ]

def find_next_shard(from_date, opts=None):
    opts = opts or {}
    info = get_shard_info(from_date)
    have_shard, is_red, last_end = info['haveShard'], info['isRed'], info['lastEnd']
    only = opts.get('only')
    if have_shard and from_date < last_end and (not only or (only == 'red') == is_red):
        return info
    else:
        return find_next_shard(from_date + timedelta(days=1), opts)

def find_next_n_shards(n=5, opts=None):
    from_date = datetime.today()
    opts = opts or {}
    result = []
    
    while len(result) < n:
        info = get_shard_info(from_date)
        have_shard, is_red, last_end = info['haveShard'], info['isRed'], info['lastEnd']
        only = opts.get('only')
        
        if have_shard and from_date < last_end and (not only or (only == 'red') == is_red):
            result.append(info)
        
        from_date += timedelta(days=1)
    
    return result