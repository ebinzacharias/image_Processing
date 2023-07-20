from PIL import Image
import os

def compress_images_in_directory(input_dir, output_dir, quality, optimize):
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

                # Save the compressed image in the output directory with the desired settings
                output_path = os.path.join(output_dir, f"{filename.split('.')[0]}_compressed.png")
                img.save(output_path, optimize=optimize, quality=quality)

        print("Image compression successful!")
    except Exception as e:
        print(f"Error during image compression: {e}")

# Example usage
input_image_directory = "images/"
output_directory = "images/"
compress_images_in_directory(input_image_directory, output_directory, quality=50, optimize=True)


