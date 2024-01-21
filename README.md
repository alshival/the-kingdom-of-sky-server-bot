# Discord Bot for Sky: Children of the Light

A Discord bot designed to provide information about the game Sky: Children of the Light. It includes features such as shard eruption times and the ability to automatically clean out a specified text channel before the daily reset, allowing for the organization of webhooks or followed messages from the [Sky: Infographics Database server's `#daily-quest`](https://discord.com/channels/736912435654688868/801778605486374943) channel on your server daily. 

Live Demo: [The Kingdom of Sky](https://discord.gg/22s2GTWSPp)

Note: The infographics, as well as the shard prediction algorithm, was provided and translated from javascript code written by [Plutoy](https://github.com/PlutoyDev/sky-shards).

<html>
<body>
    <table style="width: 100%;" cellspacing="0" cellpadding="0">
        <tr>
            <td style="width: 50%;">
                <img src="https://github.com/alshival/the-kingdom-of-sky-server-bot/blob/main/public/demo1.png">
            </td>
            <td style="width: 50%;">
                <img src="https://github.com/alshival/the-kingdom-of-sky-server-bot/blob/main/public/demo2.png">
            </td>
        </tr>
    </table>
</body>
</html>

## Features

- **Shard Eruption Information:** Obtain details about the shard of the day, including information on red and black shards, their realms, maps, and reward Ascended Candles.

- **Next Shards:** Retrieve information about the next upcoming shards, whether red or black, with details on their occurrence dates and maps.

- **Live Shard Updates:** Set up and manage a channel for live shard updates, allowing users to receive real-time information about shard eruptions.

- **Daily Quest Channel Cleanup:** Automatically clear a specified text channel before the daily reset, ensuring a clean slate for the next day's activities.

- **Virtual Hugs:** Use the /hug command to send virtual hugs to other members, spreading positivity in your Discord server.

The `/help` command provides information on how to use the bot.

### Shard Functions
Utilize the following commands to gather information about shards:

- **/current_shard**
  - Get information about the current shard. Provides a map of the eruption area.

- **/next_shards**
  - Retrieve details about the next upcoming shards.
    - Options:
        - n: Number of shards to predict.
        - only: Predict only Red or Black shards.

### Channel Functions
Manage channels for shard updates and daily quest-related messages:

- **/set_live_shard_channel**
  - Set up the channel for live shard updates.
    - Required Parameter: Channel (discord.TextChannel)
    - Permissions: Administrator

- **/remove_live_shard_channel**
  - Remove all live shard updates from the server.
    - Permissions: Administrator

- **/set_daily_quest_channel**
  - Set up a channel to be cleared daily before resets.
    - Required Parameter: Channel (discord.TextChannel)
    - Permissions: Administrator

### Virtual Hugs
Spread positivity with the following command:

- **/hug**
  - Send a virtual hug to another member.
    - Required Parameter: Member (discord.Member)
    - Permissions: Use Application Commands

These commands provide distinct functionalities for managing shard information and channel settings, enhancing user experience in your Discord server.

### Realm Functions
Users can utilize the following commands to retrieve map and spirit information for each realm:

#### Isle of Dawn
- Command: `/isle_of_dawn`
- Options: Map Art, Map Pics
- Spirits: Trees, Pointing Candlemaker, Rejecting Voyager, Ushering Stargazer

#### Daylight Prairie
- Command: `/daylight_prairie`
- Options: Map Art, Map Pics
- Spirits: Trees, Applauding Bellmaker, Bird Whisperer, Butterfly Charmer, Ceremonial Worshipper, Exhausted Dock Worker, Laughing Light Catcher, Slumbering Shipwright, Waving Bellmaker

#### Hidden Forest
- Command: `/hidden_forest`
- Options: Map Art, Map Pics
- Spirits: Trees, Apologetic Lumberjack, Blushing Prospector, Dismayed Hunter, Hide'n'Seek Pioneer, Shivering Trailblazer, Tearful Light Miner, Whale Whisperer

#### Valley of Triumph
- Command: `/valley_of_triumph`
- Options: Map Art, Map Pics
- Spirits: Trees, Backflipping Champion, Bowing Medalist, Cheerful Spectator, Confident Sightseer, Handstanding Thrillseeker, Manta Whisperer, Proud Victor

#### Golden Wasteland
- Command: `/golden_wasteland`
- Options: Map Art, Map Pics
- Spirits: Trees, Courageous Soldier, Fainting Warrior, Frightened Refugee, Lookout Scout, Saluting Captain, Stealthy Survivor

#### Vault of Knowledge
- Command: `/vault_of_knowledge`
- Options: Map Art, Map Pics
- Spirits: Trees, Levitating Adept, Meditating Monastic, Memory Whisperer, Polite Scholar, Praying Acolyte

These commands offer a comprehensive way for users to explore and gather information about different realms, including map art, map pics, and details about specific spirits within each realm.

## Why Set Up a Daily Quest Text Channel?

In Sky: Children of the Light, daily quests are an integral part of the gameplay, providing players with unique challenges and rewards. To enhance the organization and visibility of these daily quests, our Discord bot allows you to set up a dedicated TextChannel exclusively for daily quest-related messages.

### Benefits:

1. **Organization:** Having a designated TextChannel ensures that all daily quest-related messages, webhooks, or followed messages from the [Sky: Infographics Database server's `#daily-quest`](https://discord.com/channels/736912435654688868/801778605486374943) channel are neatly organized in one place.

2. **Easy Access:** Players can easily refer to the channel to stay updated on the latest shard eruption times, upcoming shards, and other relevant information without cluttering the main chat.

Our bot offers an automated solution to maintain the cleanliness of the daily quest TextChannel. Before the daily reset, the bot will automatically clear out the specified TextChannel, removing any outdated messages and preparing it for the new day's quests.

<html>
<body>
    <table style="width: 100%;" cellspacing="0" cellpadding="0">
        <tr>
            <td style="width: 100%; text-align: center;">
                <img src="https://github.com/alshival/the-kingdom-of-sky-server-bot/blob/main/public/demo3.png" style="display: block; margin: 0 auto;">
            </td>
        </tr>
    </table>
</body>
</html>

# Installation

**Clone the repository**:

   ```bash
   git clone https://github.com/your-username/SkyBot.git
   ```

**Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Setting Up in Discord Developer Portal

To use the bot, you'll need to create a Discord Bot and set it up in the Discord Developer Portal. Follow these steps:

**Create a Discord Application:**

   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Click on "New Application" and give your application a name (e.g., SkyBot).

**Create a Bot User:**

   - In the application settings, navigate to the "Bot" tab.
   - Click on "Add Bot" to create a bot user.

**Copy Token:**

   - In the same "Bot" tab, under the "TOKEN" section, click on "Copy" to copy your bot token.

**Set Environment Variable:**

   - Open the `.env` file in your project.
   - Replace `YOUR_DISCORD_BOT_TOKEN` with the copied token:

     ```env
     fefe_light_token=YOUR_COPIED_DISCORD_BOT_TOKEN
     ```

**Invite the Bot to Your Server:**

   - In the Discord Developer Portal, go to the "OAuth2" tab.
   - In the "OAuth2 URL Generator" section, select the `bot` and `applications.commands` scopes.
   - Copy the generated URL and paste it in your browser to invite the bot to your server.

**Set Up Slash Commands:**

   - In the Discord Developer Portal, go to the "Bot" tab.
   - Under "Token Privileged Intent," enable the "applications.commands" scope.
   - Click on "Add Slash Command" to add the following commands:
     - `shard_of_the_day`
     - `next_shards`
     - `set_daily_quest_channel`
     - `hug`

**Set up the environment variables**:

   - Create a file named `.env` in the project root.
   - Add the following content to `.env`:

     ```env
     sky_bot_token=YOUR_DISCORD_BOT_TOKEN
     ```

**Run the bot**:

   ```bash
   python bot.py
   ```

# Emojis
If the emojis are not displaying on your server, upload the Emojis in `public/emojis` to your server:

1. Open your Discord server where you want to use these emojis.
Access Server Settings:

2. Click on the server name at the top of the channel list to open the server menu.
Select "Server Settings" from the dropdown menu.

3. Emoji Tab:
In the Server Settings menu, click on the "Emoji" tab on the left sidebar.

4. Upload Emoji:
Click the "Upload Emoji" button.
Select the emoji file from the public/emoji directory on your computer.
Customize the emoji name if needed.
Click "Save" to upload the emoji to your server.

5. Find Emoji ID:
Open the guild that has the emoji
In the Message box, type `\:emoji_name:` in the message box (notice the backslash).
Send the message.
The message you sent will now say `"<:emoji_name:xxxxxxxx>`.

6. Replace IDs in bot.py:
Replace the placeholders in your config dictionary in bot.py with the actual emoji IDs you copied:
```
config = {
    # Replace right-side with your emoji IDs
    'ShardRed_emoji':'<:ShardRed:1198069899973636137>',
    'ShardBlack_emoji':'<:ShardBlack:1198069944697503894>',
    'AscendedCandle_emoji':'<:AscendedCandle:1198069985017331852>'
}
```

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or want to contribute to the project, feel free to open an issue or create a pull request.
