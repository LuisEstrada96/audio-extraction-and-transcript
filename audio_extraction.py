import moviepy.editor

def getAudio(url_video, url_audio):
    video = moviepy.editor.VideoFileClip(url_video)
    audio = video.audio
    audio.write_audiofile(url_audio)

video = "./assets/test1.mp4"
audio = "./assets/test1.wav"
getAudio(video, audio)