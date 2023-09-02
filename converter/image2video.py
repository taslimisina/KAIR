import cv2
import os

# Path to the directory containing the images
images_dir = 'enhanced_images/'

# List the image files in the directory
image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg') or f.endswith('.png')]

# Sort the image files to maintain order
image_files.sort()

# Specify the video file name and codec
output_video = 'enhanced_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Get the dimensions of the first image (assumes all images have the same dimensions)
first_image = cv2.imread(os.path.join(images_dir, image_files[0]))
height, width, layers = first_image.shape

# Create the VideoWriter object
video = cv2.VideoWriter(output_video, fourcc, 25, (width, height))

# Loop through the image files and add them to the video
for image_file in image_files:
    image_path = os.path.join(images_dir, image_file)
    frame = cv2.imread(image_path)
    video.write(frame)

# Release the VideoWriter and close the video file
video.release()

print("Video created successfully!")

