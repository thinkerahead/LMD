import numpy as np 
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
j=0

# Initialize communication with TMP102


# This function is called periodically from FuncAnimation
def animate(i, xs, ys):
    j+=1
    xs.append(int(j))
    ys.append(int(j*2))
    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Real-time plot of fly traces over time')
    plt.ylabel('Location of fly')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()

import cv2
import tkinter as tk
from PIL.ImageTk import PhotoImage
window = tk.Tk()
img = cv2.imread("frame_000.tiff")
height, width, no_channels = img.shape
canvas = tk.Canvas(window, width = width, height = height)
canvas.pack()
photo = PhotoImage(image = PIL.Image.fromarray(img))
canvas.create_image(0, 0, image=photo, anchor=tk.NW)
window.mainloop()

while True:
    img = capture.read()
    Canvas.create_image(0,0, image=img)
    if cv2.WaitKey(10) == 27:
        break

root.mainloop()
