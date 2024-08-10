import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import platform
# import cv2  # Import OpenCV for camera access
import cv2


# it is use for voice speak
engine=pyttsx3.init('sapi5')

# from pyttsx3 we get the voice property 
voices=engine.getProperty('voices')
# in the system tow type of voice 0 is men 1 is womwn
# print(voices[0].id)

# set the men's voice in the current engine/program
engine.setProperty('voice',voices[0].id)


# This Function Is Use For Specking
def speak(audio):
    # it say the audio which is given
    engine.say(audio)
    engine.runAndWait()
    # os.system(f"say {audio}")


# This Function Is Use For Wish Me according To Time Like Goodmorning 
def wish_me():
    hour =int(datetime.datetime.now().hour)
    
    if hour>0 and hour<12:
        speak("Good Morning Sir.")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening")
    
    speak("I Am jarvis Sir, How can I Help You Sir")

def take_command():
    # it take input from microphone and give output into string (It Listen the user voice and give output a string)
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listing......")
        # pause_threshold is the instance of Recognizer Class
        # When We Stop After Speaking Then It Recognize All (Jitna Bhi Bola H Uske Bad agar Hm ruk Jate h 1 Sec. Ke Liye To Yah bola Hua Recognise Krega)
        #(by Default pause_threshold time is 0.8 In This Case We Change The Pause Time )
        # Wnen We want To Our system Reduce the unnessecery Noice Then Ve increase energy_threshold
        r.pause_threshold=0.5
        r.adjust_for_ambient_noise(source)
        
        # r.listen  is the methid of recognize class which is listien the audio and store in audio variable
        audio =r.listen(source)
        # print(audio)
        # print("The....")
        
    try:
        print("ricognizig......")
        
        # google API recognize the voice and convert into english language
        query = r.recognize_google(audio, language="en-in")
        # query = r.recognize_google_cloud(audio, language="en-in")
        # query = r.recognize_sphinx(audio)
        print(f"User said.....{query} \n")
    except Exception as e:
        print(e)
        print("say Again....")
        return "None"
    # print(query)
    return query

def send_email(to, content):
        sender_email = 'Sender_Email_Address@gmail.com'  # Your email address
        sender_password = 'Sender_Security_Key'      # Your email password

        receiver_email = to
        # subject = subject
        message = content

        # Set up the SMTP server
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(sender_email, sender_password)

        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        # msg['Subject'] = subject

        # Attach the message to the email
        msg.attach(MIMEText(message, 'plain'))

        # Send the email
        smtp_server.send_message(msg)

        # Close the SMTP server
        smtp_server.quit()

        speak('Email sent successfully!')

def open_camera():
    # Initialize the camera (0 is the default camera)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        speak("Could not access the camera.")
        return

    speak("Camera is now open. Say 'capture photo' to take a picture or 'record video' to start recording.")
    
    while True:
        # Read frames from the camera
        ret, frame = cap.read()
        
        if not ret:
            speak("Failed to capture image.")
            break

        # Display the frame
        cv2.imshow('Camera', frame)
        
        # Capture commands
        query = take_command().lower()
        
        if 'capture photo' in query:
            # Save the captured image
            photo_filename = f"photo_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            cv2.imwrite(photo_filename, frame)
            speak(f"Photo saved as {photo_filename}")
        
        elif 'record video' in query:
            # Start recording video
            video_filename = f"video_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.avi"
            fourcc = cv2.VideoWriter.fourcc(*'XVID')
            out = cv2.VideoWriter(video_filename, fourcc, 20.0, (640, 480))
            
            speak("Recording video. Say 'stop recording' to stop.")
            
            while True:
                ret, frame = cap.read()
                
                if not ret:
                    speak("Failed to capture video.")
                    break
                
                out.write(frame)
                cv2.imshow('Camera', frame)
                
                if 'stop recording' in take_command().lower():
                    speak("Stopping video recording.")
                    break
            
            out.release()
            speak(f"Video saved as {video_filename}")
        
        elif 'close camera' in query:
            speak("Closing the camera.")
            break
    
    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


if __name__=='__main__':
    # speak("Hello Sir, How Can I Help You....")
    wish_me()
    
    while True:
        query=take_command().lower()
        # print(query)
        
        if 'wikipedia' in query:
            speak("Searching in wikipidea...")
            
            # it remove only wikipeddia word and update the query
            query=query.replace("wikipedia","")
            # print(query)
            
            # search in the wikipedia with The help of wikipedia API and fetch only two sentences and store in the result variable
            result=wikipedia.summary(query,sentences=2)
            # print(result)
            speak("According To Wikipedia")
            # speak The Result
            speak(result)
        elif 'open youtube' in query:
            # open youtobe in webbrowser with the help of webbrowser module
            speak("What would you like to search for?")
            search_query = take_command()
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
            # webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("What would you like to search for on Google?")
            search_query = take_command()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            # webbrowser.open("google.com")
        elif 'play music' in query:
            # we can play the music which is store in current directory and play wiyh its name
            # os.system("output.mp3")
            
            # we can give the path and play the music from the given path
            music_dir= r"C:\VS_CODE\Python\Quiz"
            # create a list of files wich is store in the given path
            song=os.listdir(music_dir)
            # print(song)
            for i in song:
                # this use for many file in the directory or folder like .txt, .py etc. but we use only .mp3 file
                # os.path.splitext(i)[1]=='.mp3 it mean find only .mp3 file
                if os.path.splitext(i)[1]=='.mp3':
                    # we are playing the music with given path
                    os.startfile(os.path.join(music_dir,i))
                    break
        elif 'time' in query:
            hour=datetime.datetime.now().strftime("%H")
            minu=datetime.datetime.now().strftime("%M")
            speak(f"The Time Is {hour} bjjke {minu}")
        elif 'open program' in query:
            path=r"C:\Users\hp\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(path)
        elif 'send mail' in query:
            try:
                speak("Sir Please say Content.. ")
                content=take_command()
                to="Receiver_Email_Address@gmail.com"
                send_email(to,content)
            except Exception as e:
                speak(str(e))
        elif 'open camera' in query:
            open_camera()
        elif 'stop' in query:
            speak("Goodbye Sir!")
            break;
            
            
            
        