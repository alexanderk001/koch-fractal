from PIL import Image

# List of image file paths (use placeholders)
image_files = [
    "path/to/images/koch_snowflake_00.png",
    "path/to/images/koch_snowflake_01.png",
    "path/to/images/koch_snowflake_02.png",
    "path/to/images/koch_snowflake_03.png",
    "path/to/images/koch_snowflake_04.png",
    "path/to/images/koch_snowflake_05.png"
]

# Open the images and load them into a list
frames = [Image.open(image) for image in image_files]

# Create the GIF
frames[0].save(
    "output.gif",   # Output file name
    save_all=True,  # Save all frames
    append_images=frames[1:],  # Add the remaining frames
    duration=500,  # Duration per frame in milliseconds (550 ms = 0.5 seconds)
    loop=0  # Infinite loop (0 = endless)
)

print("GIF created and saved as 'output.gif'.")
