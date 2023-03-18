import pytube

video = 'https://www.youtube.com/watch?v=OLr33BKumVE'
data = pytube.YouTube(video)
audio = data.streams.get_audio_only()
audio.download()