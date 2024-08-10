from gtts import gTTS

def text_to_speech(text, filename):
    mytext=str(text)
    lanuage='hi'
    myobj=gTTS(mytext, lang=lanuage, slow=False)
    myobj.save(filename)
    

text_to_speech("Yatrigan Kripya Dhyan De" + "gadi sankhya", "Yatrigan_Krapya_Dhyan_De_gadi.mp3" )