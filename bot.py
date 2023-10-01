import requests
import json
import telegram

# Create a new instance of the `telegram.Bot` class
bot = telegram.Bot('6658689692:AAGcvahLlZz7ZBT1Lw_D8wnjnTjPdaQlgfY')

# Define a function to generate a random image from Google
def get_random_image():
    # Make a request to the Google Image Search API
    response = requests.get('https://www.google.com/search?tbm=isch&q=random+image')

    # Extract the image URLs from the response
    image_urls = []
    for image in response.json()['items']:
        image_urls.append(image['link'])

    # Choose a random image URL
    image_url = random.choice(image_urls)

    # Return the image URL
    return image_url

# Define a function to send an image to the user
def send_image(bot, chat_id, image_url):
    # Create a Telegram photo object
    photo = telegram.PhotoSize(image_url)

    # Send the photo to the user
    bot.sendPhoto(chat_id, photo=photo)

# Listen for the `/img` command
@bot.message_handler(commands=['img'])
def send_random_image_command(message):
    # Get a random image from Google
    image_url = get_random_image()

    # Send the image to the user
    send_image(bot, message.chat.id, image_url)

# Start the bot
bot.start_polling()
