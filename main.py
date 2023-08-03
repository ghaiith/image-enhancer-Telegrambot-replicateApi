import os
import replicate
import requests
import telebot

TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
REPLICATE_API_TOKEN = "YOUR_REPLICATE_API_TOKEN"

# Set the REPLICATE_API_TOKEN environment variable
os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

# Initialize the Telebot with the bot token
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Send The Image\nand wait ..")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # Get the photo ID and file path
    file_id = message.photo[-1].file_id

    # Get the file_info using the file_id
    file_info = bot.get_file(file_id)

    # Download the photo to the local file system
    downloaded_file = bot.download_file(file_info.file_path)
    with open('received_image.jpg', 'wb') as new_file:
        new_file.write(downloaded_file)

    # Process the image using the Replicate API
    output = replicate.run(
        "tencentarc/gfpgan:9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3",
        input={"img": open("received_image.jpg", "rb")}
    )

    # Remove the downloaded image after processing
    os.remove('received_image.jpg')

    # Send the processed image back to the user
    bot.send_photo(message.chat.id, output, caption="The New Image")

if __name__ == '__main__':
    bot.polling()
