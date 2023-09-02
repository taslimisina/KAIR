from moviepy.editor import VideoFileClip, AudioFileClip

# Load video and audio files
video = VideoFileClip('center_enhanced_test_25_jul_40K_moredata.mp4')
audio = AudioFileClip('audio_dirk.mp3')

# Set the audio of the video to the loaded audio
video = video.set_audio(audio)

# Save the final video with audio
video.write_videofile('center_enhanced_test_25_jul_40K_moredata_with_voice.mp4', fps=25, codec='libx264')
