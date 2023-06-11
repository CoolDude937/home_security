from PIL import Image
import sys

def resize_pic(image_path, output_path, new_width):
    # Open the image
    image = Image.open(image_path)

    # Calculate the aspect ratio
    original_width, original_height = image.size
    aspect_ratio = original_width / original_height

    # Calculate the new height
    new_height = int(new_width / aspect_ratio)

    # Resize the image while preserving the aspect ratio
    resized_image = image.resize((new_width, new_height))

    # Save the resized image
    resized_image.save(output_path)

if __name__ == "__main__":
    print(sys.argv)
    resize_pic(sys.argv[1], sys.argv[2], int(sys.argv[3]))