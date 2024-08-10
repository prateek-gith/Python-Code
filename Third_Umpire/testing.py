import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import imutils
import time

# Set width or height of screen/app
SET_WIDTH = 650
SET_HEIGHT = 368

# Initialize tkinter GUI
window = tkinter.Tk()
window.title("Third Umpire")

cv_img = cv2.cvtColor(cv2.imread("Main.jpeg"), cv2.COLOR_BGR2RGB)

canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas.pack()

# Global variables for speed control and playback state
speed = 1  # Default speed for normal playback
speed_lock = threading.Lock()
is_playing = True  # Flag to control playback

def pending(decision):
    # Display Decision pending Screen (Image)
    frame = cv2.cvtColor(cv2.imread("Decision-pending.jpeg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    
    # Wait or Sponsor (image)
    time.sleep(1)
    frame = cv2.cvtColor(cv2.imread("Sponser.jpeg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    
    # Display Decision
    time.sleep(2)
    decision_photo = "Out.png" if decision == 'out' else "Not-out.png"
    frame = cv2.cvtColor(cv2.imread(decision_photo), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

def play():
    global speed, is_playing
    if is_playing:
        with speed_lock:
            frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
            stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
            grabbed, frame = stream.read()
            if grabbed:
                frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
                frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
                canvas.image = frame
                canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
                canvas.create_text(100, 25, fill="green", font="Times 20 italic bold", text="Now Decision Is Pending")
            window.after(40, play)  # Schedule the next frame update
            # Call function once after given time. agrgument(milisecond, function)

def set_speed(new_speed):
    global speed
    with speed_lock:
        speed = new_speed

def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()

def not_out():
    thread = threading.Thread(target=pending, args=("not-out",))
    thread.daemon = 1
    thread.start()

def stop():
    global is_playing
    is_playing = False
    print("Playback stopped")

def resume():
    global is_playing
    is_playing = True
    play()  # Resume playback

# Video capture
stream = cv2.VideoCapture("videoplayback2.mp4")

# Control buttons
btn = tkinter.Button(window, text="<< Previous Fast", width=50, command=lambda: set_speed(-25))
btn.pack()
btn = tkinter.Button(window, text="<< Previous Slow", width=50, command=lambda: set_speed(-2))
btn.pack()
btn = tkinter.Button(window, text="Next Fast >>", width=50, command=lambda: set_speed(25))
btn.pack()
btn = tkinter.Button(window, text="Next Slow >>", width=50, command=lambda: set_speed(2))
btn.pack()
btn = tkinter.Button(window, text="OUT", width=50, command=out)
btn.pack()
btn = tkinter.Button(window, text="NOT OUT", width=50, command=not_out)
btn.pack()
btn = tkinter.Button(window, text="STOP", width=50, command=stop)
btn.pack()
btn = tkinter.Button(window, text="RESUME", width=50, command=resume)
btn.pack()

# Start playback
play()

# Run the Tkinter event loop
window.mainloop()
