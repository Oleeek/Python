import pyttsx3

tts = pyttsx3.init()
save = str(input("Do you want to save speech to file y/n: "))
sayInFile = str(input("What am I supposed to say?: "))

if save == str("y" or "Y"):
    saveFileName = str(input("How can I name an mp3 file?: "))
    tts.save_to_file(sayInFile, saveFileName + ".mp3")
elif save == str('n' or 'N'):
    tts.say(sayInFile)

tts.runAndWait()
