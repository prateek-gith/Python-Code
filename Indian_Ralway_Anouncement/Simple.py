import pandas as pd
from gtts import gTTS
import os


def text_to_speech(text, filename):
    mytext=str(text)
    lanuage='hi'
    myobj=gTTS(mytext, lang=lanuage, slow=True)
    myobj.save(filename)


def generate_announcement(filename):
    df= pd.read_excel(filename)
    for index, item in df.iterrows():
        text_to_speech(f"Yatrigan Kripya Dhyan de Gadi Sankhya {item['Train_Number']} Gadi naam {item['Train_Name']} Paltform Number {item['Platform']} Par Aa rahi H ", f"NewAudio_{index+1}.mp3")
        


if __name__=='__main__':
    print("!! Jai Shree Ram !!")
    
    #Generate Announcement
    # generate_announcement("Indian_Railway_Hindi.xlsx")
    
    n=1
    
    # current_dir=os.getcwd()
    # File_List=os.listdir()
    
    # for i in File_List:
    #     if os.path.splitext(i)[1]=='.mp3':
    #         os.startfile(i)
    #         n=n+1
    
    
    