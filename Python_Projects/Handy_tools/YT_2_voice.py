import pytube

video = input('Give the link: ')
data = pytube.YouTube(video)
audio = data.streams.filter(only_audio=True, file_extension='mp4').first()
output_path = input("path: ")
output_filename = 'output_audio.mp3'

audio.download(output_path=output_path, filename=output_filename)

