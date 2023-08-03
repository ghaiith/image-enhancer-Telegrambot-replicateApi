# Image Enhancer Telegram Bot with Replicate API

This Telegram bot allows users to send images and receive enhanced versions using the Replicate API, which is based on the gfpgan model.

## Getting Started

To use this bot, you need to follow these steps:

1. Obtain a Telegram bot token by creating a new bot on Telegram. You can do this by talking to the BotFather on Telegram and following these steps:
   - Search for "@BotFather" on Telegram and start a chat with the BotFather.
   - Use the "/newbot" command to create a new bot. Follow the instructions to choose a name and username for your bot.
   - The BotFather will provide you with a bot token. Save this token as it will be required to interact with the Telegram Bot API.

2. Obtain a Replicate API token. Visit the Replicate website or platform to create an account and obtain your API token.

3. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

4. Set the API variables for your Telegram bot token and Replicate API token:

   ```
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
REPLICATE_API_TOKEN = "YOUR_REPLICATE_API_TOKEN"
   ```

5. Run the bot by executing the main Python script:

   ```
   python main.py
   ```

## How to Use

1. Start a chat with your Telegram bot.

2. Send an image to the bot by attaching it to the message.

3. The bot will process the image using the gfpgan model through the Replicate API.

4. The enhanced image will be sent back to you in the same chat.

## Dependencies

This bot relies on the following dependencies:

- `telebot`: The Telegram Bot API wrapper for Python, which enables easy interaction with Telegram bots.

- `replicate`: A Python client for the Replicate API, allowing you to utilize the gfpgan model for image enhancement.

## Acknowledgments

- The gfpgan model used for image enhancement is provided by Replicate. For more information about Replicate and its services, visit their website (URL).

- Special thanks to the developers of the `telebot` library for making Telegram bot development accessible and straightforward.

## Disclaimer

This project is provided for educational and demonstration purposes only. The usage of the gfpgan model and the Replicate API is subject to their terms and conditions. Ensure you comply with the usage policies of the respective services when deploying the bot in production or for commercial purposes.

## License

[MIT License](LICENSE)

Feel free to fork, modify, and use this code in accordance with the license.