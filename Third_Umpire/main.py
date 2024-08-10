# Python Tkinter is the fastest and easiest way to create GUI applications
import tkinter

# It provides various functions for image and video processing, including reading images, detecting objects, and applying filters.
import cv2

# PIL stands for Python Imaging Library, and it's the original library that enabled Python to deal with images.
import PIL.Image, PIL.ImageTk

from functools import partial
import threading
import imutils
import time

# set width or height of screen/app
SET_WIDTH=650
SET_HEIGHT=368

# tkinter GUI start Here
window=tkinter.Tk()

# title of the app
window.title("Third Umpire")

cv_img=cv2.cvtColor(cv2.imread("Main.jpeg"),cv2.COLOR_BGR2RGB)

# Canvas widget to display graphical elements like lines or text. 
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)

# Image: Either a PIL image, or a mode string. If a mode string is
# fromarray : Creates an image memory from an object exporting the array interface (using the buffer protocol):
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))

image_on_canvas=canvas.create_image(0,0,anchor=tkinter.NW, image=photo)
canvas.pack()

def pending(decision):
    # Step 1 : Display Decision pending Screen (Image)
    
    frame = cv2.cvtColor(cv2.imread("Decision-pending.jpeg"), cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    
    # convert our fram a image object that is read by tkinter
    # A Tkinter-compatible photo image. This can be used everywhere Tkinter expects an image object. If the image is an RGBA image, pixels having alpha 0 are treated as transparent. {mtlb direct hm photo ko tkinter me nhi use kr skte h uske liye photo ka object bnana pdta h Jo ki PIL se bnta h }
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    
    # Step 2 : Wait Or Sponser (wait and sponser image)
    time.sleep(1)
    
    frame = cv2.cvtColor(cv2.imread("Sponser.jpeg"), cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    
    # Step 2 : Display Decision (wait and decision image)
    time.sleep(2)
    
    if decision=='out':
        decision_photo="Out.png"

    if decision=='not-out':
        decision_photo="Not-out.png"
        
    frame = cv2.cvtColor(cv2.imread(decision_photo), cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)


# it collect the video or camara and if we give file name then it capture from file video
stream=cv2.VideoCapture("videoplayback2.mp4")
def play(speed):
    # play video in reverse order
    # it read the strem prosses and cv2.CAP_PROP_POS_FRAMES read the frame it mean kya speed h frame ki 
    # yani video hmari kya h ek photo frame hi h to vh dekh raha h ki hmara fram se move kr raha h 
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES) # we find the speed of fream and store in frame1
        
    # we set the frame speed or manage the frame speed { manage kr rhe ki kitni speed se chale }
    # frame1 + speed  : yani jo original speed h us speed me jod to jo speed variable ke roop me mil rhi h function ko
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed) 
    
    grabbed, frame =stream.read()
    frame=imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    canvas.create_text(100, 25, fill="green", font="Times 20 italic bold", text="Now Decision Is Pending")

    print(f"The speed is {speed}")
    
def out():
    thread= threading.Thread(target=pending, args=("out",))
    thread.daemon=1
    thread.start()
    print("The decision is OUT")
    
def not_out():
    thread= threading.Thread(target=pending, args=("not-out",))
    thread.daemon=1
    thread.start()
    print("The decision is NOT-OUT")

# buttons
btn= tkinter.Button(window,text="<< previous fast", width=50, command=partial(play, -25))
btn.pack()

btn= tkinter.Button(window,text="<< previous slow", width=50, command=partial(play, -2))
btn.pack()

# command = "NAME OF FUNCTION" it ta ke a function without argument
# command mean run function onclick
# in this case we take argument in the function it is possible through functool, partial Library which is import on top
btn= tkinter.Button(window,text="next fast >>", width=50, command=partial(play, 25))
btn.pack()

btn= tkinter.Button(window,text="next slow >>", width=50, command=partial(play, 2))
btn.pack()

# btn= tkinter.Button(window,text="play", width=50, command=partial(play,100))
# btn.pack()

btn= tkinter.Button(window,text="OUT", width=50,command=out)
btn.pack()

btn= tkinter.Button(window,text="NOT OUT", width=50, command=not_out)
btn.pack()


window.mainloop()