from PIL import Image
import os

def resize_images_fixed_resolution(input_dir, output_dir, width, height, quality=85, optimize=True):
    try:
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Get a list of all files in the input directory
        file_list = os.listdir(input_dir)

        for filename in file_list:
            input_path = os.path.join(input_dir, filename)

            # Check if the file is an image
            if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Open the input image
                img = Image.open(input_path)

                # Resize the image to the fixed width and height while maintaining the aspect ratio
                img = img.resize((width, height))

                # Save the resized image in the output directory with the desired settings
                output_path = os.path.join(output_dir, f"{filename.split('.')[0]}_resized1200.png")
                img.save(output_path, optimize=optimize, quality=quality)

        print("Image resizing with fixed resolution successful!")
    except Exception as e:
        print(f"Error during image resizing with fixed resolution: {e}")

# Example usage
input_image_directory = "images/"
output_directory = "images/resized/"
resize_images_fixed_resolution(input_image_directory, output_directory, width=1518, height=628, quality=85, optimize=True)




