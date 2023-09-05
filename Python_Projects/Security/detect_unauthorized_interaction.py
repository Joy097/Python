from pynput.mouse import Controller 
from time import sleep 
import datetime


def sound():
    import numpy as np
    import pyaudio

    # Parameters
    duration = 1.0  # Duration of the sound in seconds
    frequency = 480  # Frequency of the sine wave (in Hz)

    # Generate the sine wave
    t = np.linspace(0, duration, int(44100 * duration), endpoint=False)
    signal = 0.5 * np.sin(2 * np.pi * frequency * t)

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open a stream
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=44100,
                    output=True)

    # Play the sound
    stream.write(signal.tobytes())

    # Close the stream and terminate PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()



#time of inactivity

savedpos = list(Controller().position)

count = 0
while(True):

    curpos = list(Controller().position)
    time = datetime.datetime.now().strftime("%H:%M:%S")
    if savedpos != curpos:
        count = count +1
        savedpos = curpos
        print("Mouse Movement # ", count, "| move : ",curpos, "| Time :",time )
        if count >18: sound()
    sleep(1)

'''
This helps to determine whether someone used my mouse when I was far from my pc.
'''
