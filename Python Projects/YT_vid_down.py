import pytube
link = 'https://www.youtube.com/watch?v=xe_iCkFsQKE'
yt = pytube.YouTube(link)
yt.streams.get_highest_resolution().download()