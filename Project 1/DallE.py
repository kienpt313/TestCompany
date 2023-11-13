import datetime
import requests
import webbrowser
import openai
from openai.error import InvalidRequestError
import os
from PIL import Image
openai.api_key = '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'

SIZES=('1024x1024','512x512')
image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)
def generate_image(prompt, size='512x512'):
    try:
        images = []
        generation_response  = openai.Image.create(
            prompt=prompt,
            n=1,
            size=size
        )
        image_dir = os.path.join(os.curdir, 'images')

        # If the directory doesn't exist, create it
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Initialize the image path (note the filetype should be png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Retrieve the generated image
        image_url = generation_response["data"][0]["url"]  # extract image URL from response
        generated_image = requests.get(image_url).content  # download the image
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)
    # Display the image in the default image viewer
        image = Image.open(image_path)
        image.show()
    except openai.error.InvalidRequestError as err:
        print(err)

# response = generate_image('cat with a book', size=SIZES[0])


## generate images (byte output)
response = generate_image('San Francisco and Chicago mixed', size=SIZES[1])
