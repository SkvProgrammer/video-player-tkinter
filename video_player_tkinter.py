import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

# Function to open a video file
def open_video():
    file_path = filedialog.askopenfilename()
    if file_path:
        cap = cv2.VideoCapture(file_path)
        play_video(cap)

# Function to play a video
def play_video(cap):
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image)
        canvas.config(image=photo)
        canvas.image = photo
        canvas.after(10, play_video, cap) # Update every 10 milliseconds

# Create the main window
root = tk.Tk()
root.title("Simple Video Player")

# Create a canvas for displaying video frames
canvas = tk.Label(root)
canvas.pack()

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a file menu
file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_video)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Run the main event loop
root.mainloop()
