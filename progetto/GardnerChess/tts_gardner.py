import gtts
import os
    
def text_to_speech(text):

    if(len(text) == 2):
        mytext = "Pedone in" + text
    else:
        if(text[0] == "T"):
            mytext = "Torre in" + text[1] + text[2]
        elif(text[0] == "A"):
            mytext = "Alfiere in" + text[1] + text[2]
        elif(text[0] == "C"):
            mytext = "Cavallo in" + text[1] + text[2]
        elif(text[0] == "Q"):
            mytext = "Regina in" + text[1] + text[2]
        elif(text[0] == "R"):
            mytext = "Re in" + text[1] + text[2]
        else:
            mytext = text
    
    # Language in which you want to convert
    language = 'it'
    
    # Passing the text and language to the engine, here we have marked slow=False. Which tells 
    # the module that the converted audio should have a high speed
    myobj = gtts.gTTS(text=mytext, lang=language, slow=False)
    
    # Saving the converted audio in a mp3 file named tts 
    myobj.save("tts.mp3")
    
    # Playing the converted file
    os.system("tts.mp3")


    


