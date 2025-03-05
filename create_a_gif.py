import imageio.v3 as iio
import os
from PIL import Image
import numpy as np

# Define Image storage
image_folder = 'image_files'

# Get a list of filenames in the folder
filenames = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.endswith(('png', 'jpg', 'jpeg'))]

# Resize images to the same dimensions
images = []
 # Set a standard size (width, height)
target_size = (500, 300) 

# Loop through and resize
for file in filenames:
    img = Image.open(file).convert("RGBA")  # Open image and ensure consistent mode
    img_resized = img.resize(target_size)  # Resize image to target dimensions
    images.append(np.array(img_resized))  # Convert to NumPy array and append

iio.imwrite('teslaModelY.gif', images, duration=500, loop=0)

print("GIF created successfully!")