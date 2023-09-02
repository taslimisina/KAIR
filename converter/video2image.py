import cv2
import os

def video_to_images(input_video_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(input_video_path)

    frame_count = 0
    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # If no frame is read or the video has ended, break the loop
        if not ret:
            break

        # Save the frame as an image
        output_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(output_path, frame)

        frame_count += 1

    # Release the video capture object
    cap.release()

if __name__ == "__main__":
    # Replace 'input_video.mp4' with the path to your input video file.
    # Replace 'output_folder' with the directory where you want to save the images.
    video_to_images("dinet_Dirk_25fps_facial_dubbing_add_audio_v3.mp4", "output_folder")

