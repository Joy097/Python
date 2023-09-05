from moviepy.editor import*

clip = VideoFileClip(r'C:\\Users\\User\\Desktop\\small python projects\\ab.mp4').subclip((0),(5)).resize(0.3)
clip.write_gif('aa.gif')