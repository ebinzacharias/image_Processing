import os
import shutil
from PIL import Image

def get_aspect_ratio(image_path):
    try:
        # Open the image
        img = Image.open(image_path)

        # Get the width and height of the image
        width, height = img.size

        # Calculate the aspect ratio
        return width / height
    except Exception as e:
        print(f"Error while calculating aspect ratio: {e}")
        return 0

def is_landscape_image(image_path):
    try:
        # Get the aspect ratio
        aspect_ratio = get_aspect_ratio(image_path)

        # Check if the image is landscape (aspect ratio > 1.5)
        return aspect_ratio > 1.5
    except Exception as e:
        print(f"Error while checking landscape image: {e}")
        return False

def is_portrait_image(image_path):
    try:
        # Get the aspect ratio
        aspect_ratio = get_aspect_ratio(image_path)

        # Check if the image is portrait (aspect ratio < 1.0 / 1.5)
        return  1.0 <= aspect_ratio <= 1.5
    except Exception as e:
        print(f"Error while checking portrait image: {e}")
        return False

def is_vertical_image(image_path):
    try:
        # Get the aspect ratio
        aspect_ratio = get_aspect_ratio(image_path)

        # Check if the image is vertical (1.0 / 1.5 <= aspect ratio <= 1.5)
        return aspect_ratio < 1.0
    except Exception as e:
        print(f"Error while checking vertical image: {e}")
        return False

def is_video_file(file_path):
    # Check if the file has a video extension
    video_extensions = ('.mov', '.mp4')
    return file_path.lower().endswith(video_extensions)

def is_image_file(file_path):
    # Check if the file has an image extension
    image_extensions = ('.jpeg', '.jpg', '.png')
    return file_path.lower().endswith(image_extensions)

def count_files(folder):
    count = 0
    for root, _, files in os.walk(folder):
        count += len(files)
    return count

def detect_and_copy_images(source_folder, destination_folder):
    try:
        # Count total number of files before organizing
        total_files_before = count_files(source_folder)

        # Create the destination folders for each category if they don't exist
        os.makedirs(os.path.join(destination_folder, 'landscape_images'), exist_ok=True)
        os.makedirs(os.path.join(destination_folder, 'portrait_images'), exist_ok=True)
        os.makedirs(os.path.join(destination_folder, 'vertical_images'), exist_ok=True)
        os.makedirs(os.path.join(destination_folder, 'videos'), exist_ok=True)

        # Initialize variables to keep track of the number of files copied
        total_copied = 0

        for root, _, files in os.walk(source_folder):
            for filename in files:
                file_path = os.path.join(root, filename)

                # Check if the file is an image or video
                if is_image_file(file_path):
                    if is_landscape_image(file_path):
                        destination_subfolder = os.path.join(destination_folder, 'landscape_images')
                    elif is_portrait_image(file_path):
                        destination_subfolder = os.path.join(destination_folder, 'portrait_images')
                    elif is_vertical_image(file_path):
                        destination_subfolder = os.path.join(destination_folder, 'vertical_images')
                    else:
                        continue  # Skip if not classified

                    # Copy the image to the appropriate subfolder
                    relative_path = os.path.relpath(file_path, source_folder)
                    destination_path = os.path.join(destination_subfolder, relative_path)
                    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                    shutil.copy(file_path, destination_path)
                    total_copied += 1

                elif is_video_file(file_path):
                    # Copy the video to the "videos" subfolder
                    relative_path = os.path.relpath(file_path, source_folder)
                    destination_path = os.path.join(destination_folder, 'videos', relative_path)
                    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                    shutil.copy(file_path, destination_path)
                    total_copied += 1

        # Count total number of files after organizing
        total_files_after = count_files(destination_folder)

        print(f"Total files before organizing: {total_files_before}")
        print(f"Total files copied to new folders: {total_copied}")
        print(f"Total files after organizing: {total_files_after}")

        print("Images and videos organized successfully!")
    except Exception as e:
        print(f"Error while organizing images and videos: {e}")



# Example usage
source_folder = "ssd/"
destination_folder = "ssd/_sorted/"
detect_and_copy_images(source_folder, destination_folder)

