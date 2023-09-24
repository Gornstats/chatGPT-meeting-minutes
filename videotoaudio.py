import ffmpeg

video = "audio/test_vid_15secs.mp4"

def video_to_audio(video_path):
    input_video = ffmpeg.input(video_path)
    output_audio = ffmpeg.output(input_video, "audio.mp3", format="mp3")
    ffmpeg.run(output_audio)
    
video_to_audio(video)