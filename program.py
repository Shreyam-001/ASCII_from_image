import requests
from PIL import Image

# Define ASCII characters to use for the conversion
ASCII_CHARS = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

# Define the size of the output ASCII art
WIDTH = 100

# Function to convert an image to ASCII art
def convert_to_ascii(image):
    # Load the image and resize it to the desired width
    image = Image.open(image)
    width, height = image.size
    ratio = height / width
    new_height = int(WIDTH * ratio * 0.55)
    resized_image = image.resize((WIDTH, new_height))

    # Convert the resized image to grayscale
    grayscale_image = resized_image.convert('L')

    # Generate the ASCII art
    pixels = grayscale_image.getdata()
    ascii_chars = [ASCII_CHARS[pixel // 25] for pixel in pixels]
    ascii_art = ''.join(ascii_chars)

    # Return the ASCII art
    return ascii_art

# Prompt the user for an image URL and convert it to ASCII art
url = input('Enter the image URL: ')
response = requests.get(url, stream=True)
image = Image.open(response.raw)
ascii_art = convert_to_ascii(image)
print(ascii_art)
