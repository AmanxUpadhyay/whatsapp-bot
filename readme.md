# WhatsApp Bot

## Description
The WhatsApp Bot is a Python-based application that allows users to download Instagram Reels and YouTube Shorts videos by sharing the respective links with the bot. The bot will retrieve the videos and send them back to the users. It leverages the Instagram and YouTube APIs for fetching video details and the Flask framework for handling HTTP requests.

## Features
- Download Instagram Reels videos by sharing the link with the bot.
- Download YouTube Shorts videos by sharing the link with the bot.
- Send the downloaded videos back to the users on WhatsApp.

## Tech Stack
- Python
- Flask
- WhatsApp Business API
- Instagram API
- YouTube API

## Installation
1. Clone the repository:
   ```shell
   git clone https://github.com/your-username/whatsapp-bot.git
   cd whatsapp-bot
   ```

2. Create and activate a virtual environment:
   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
   ```

4. Set up the necessary API keys:
   - Instagram API key: Obtain an API key from the Facebook Developers website and update the `INSTAGRAM_API_KEY` variable in `config/api_keys.py`.
   - YouTube API key: Obtain an API key from the Google Cloud Console and update the `YOUTUBE_API_KEY` variable in `config/api_keys.py`.

5. Start the Flask server:
   ```shell
   python main.py
   ```

6. Configure the WhatsApp Business API:
   - Set up a WhatsApp Business Account and obtain the necessary credentials.
   - Follow the documentation of the WhatsApp Business API to configure and integrate it with the bot.

7. Once the server is running and the WhatsApp Business API is configured, you can share Instagram Reels and YouTube Shorts links with the bot on WhatsApp to download the videos.

## Usage
1. Start the Flask server:
   ```shell
   python main.py
   ```

2. Connect the WhatsApp Business API to handle incoming messages and send the downloaded videos.

3. Share Instagram Reels and YouTube Shorts links with the bot on WhatsApp to download the videos.

## License
[MIT License](LICENSE)