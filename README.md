# Discord Bot for Sky: Children of the Light

SkyBot is a Discord bot designed to provide information about the game Sky: Children of the Light. It includes features such as shard eruption times and the ability to automatically clean out a specified text channel before the daily reset, allowing for the organization of webhook messages from the Sky: Infographics Database server's `#daily-quest` channel on your server daily.

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

- **Shard Eruption Information:** Get information about the shard of the day, including details about red and black shards, their realms, maps, and reward Ascended Candles.

- **Next Shards:** Retrieve information about the next upcoming shards, either red or black, with details on their occurrence dates and maps.

- **Daily Quest Channel Cleanup:** Automatically clear out a specified text channel before the daily reset to organize prior day webhook messages.

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

To use SkyBot, you'll need to create a Discord Bot and set it up in the Discord Developer Portal. Follow these steps:

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

## Usage

- Use the `!shard_of_the_day` command to get information about the shard of the day.
- Use the `!next_shards` command to retrieve details about the next upcoming shards.
- Use the `!set_daily_quest_channel` command to set up the channel to be cleared daily.
- Use the `!hug` command to send a hug to another member.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or want to contribute to the project, feel free to open an issue or create a pull request.
