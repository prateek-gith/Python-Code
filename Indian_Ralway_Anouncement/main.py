import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def text_to_speech(text, filename):
    mytext=str(text)
    lanuage='hi'
    myobj=gTTS(mytext, lang=lanuage, slow=True)
    myobj.save(filename)


# This function return pydub audio segment
def merge_audios(audios):
    combine=AudioSegment.empty()
    for audio in audios:
        combine += AudioSegment.from_mp3(audio)
    return combine



def generate_skeleton():
    # generate "kripya dhyan dijiye"
    # audio=AudioSegment.from_mp3("railway_announcement.mp3")
    
    # start=12600
    # finish=15500
    # audio_process = audio[start:finish]
    # audio_process.export("Kripya_Dhyan_Dijiye_Hindi.mp3", format="mp3")
    
    # No. Of Gadi  and name of gadi
    
    # generate se chalkr
    # audio=AudioSegment.from_mp3("railway_announcement2.mp3")
    
    # start=18700
    # finish=19000
    # audio_process = audio[start:finish]
    # audio_process.export("Se_Hindi.mp3", format="mp3")
    
    # thodi hi der me
    
    # audio=AudioSegment.from_mp3("railway_announcement.mp3")
    # start=20000
    # finish=23000
    # audio_process = audio[start:finish]
    # audio_process.export("Thodi_Hi_Der_Me_Hindi.mp3", format="mp3")
    
    # platform No.
    
    # pr ayegi
    # audio=AudioSegment.from_mp3("railway_announcement.mp3")
    # start=23800
    # finish=25000
    # audio_process = audio[start:finish]
    # audio_process.export("Pe_Ayegi_Hindi.mp3", format="mp3")
    
    # yatrigad kripya dhyan dijiye gadi sankha 1234 palform no. pr ayegi
    pass
    
    


def generate_announcement(filename):
    df= pd.read_excel(filename)
    # .iterrows() it is a pandas library function that read the file in row format
    for index, item in df.iterrows():
        # No. Of Gadi  and name of gadi
        # print(item['Train_Number'])
        text_to_speech(item['Train_Number']+ " " + item['Train_Name'], "gadi_no_name.mp3")
        # text_to_speech(item['Train_Name'], "gadi_name.mp3")
        # platform No.
        text_to_speech(item['Platform'], "platform_no.mp3")
        
        audio_list=['Kripya_Dhyan_Dijiye_Hindi.mp3','gadi_no_name.mp3','Thodi_Hi_Der_Me_Hindi.mp3','platform_no.mp3','Pe_Ayegi_Hindi.mp3']
        
        announcement=merge_audios(audio_list)
        announcement.export(f"Announcement_{index+1}.mp3", format="mp3")


if __name__=='__main__':
    print("!! Jai Shree Ram !!")
    
    # Generate Skeleton
    # generate_skeleton()
    
    #Generate Announcement
    generate_announcement("Indian_Railway_Hindi.xlsx")