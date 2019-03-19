import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import animation

PLOT_ROWS = 10
PLOT_COLUMNS = 2

class ImageProcess():
    def __init__(self):
        self._plotrows = 10
        self._plotcols = 2


    def load(self, img):
        h, w, _ = img.shape
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray, h, w
    
    def rotate(self, img, angle):
        rows, cols = img.shape[:2]
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
        img_rot = cv2.warpAffine(img, M, (cols,rows))
        return img_rot

    def threshold(self, img, upper = 255, lower = 50):
        pass

    def funcname(self, parameter_list):
        pass

    def findArena(self, img):
        pass

def histogram(img):
    n, bins, patches = plt.hist(img, bins = 256, density=True, facecolor='g')
    plt.xlabel('Intensity')
    plt.ylabel('Count')
    plt.title('Histogram of image pixel distribution')
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.grid(True)
    plt.show()


    def histogram2d(self, img):
        fig, axes = plt.subplots(nrows=2, ncols=2)
        axes[0, 0].set_title('Linear normalization')
        axes[0, 0].hist2d(img[:, 0], img[:, 1], bins=100)
        fig.tight_layout()
        plt.show()
        
        
    
def rotate(self, img, angle):
    rows, cols = img.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    img_rot = cv2.warpAffine(img, M, (cols,rows))
    return img_rot    

def plotimage(img):
    plt.imshow(img)
    plt.axis('off')
    plt.show()





plt.axis([0, 10, 0, 1])

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.05)

plt.show()



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
