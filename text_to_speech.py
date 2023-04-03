import PySimpleGUI as sg
import pyttsx3

x = pyttsx3.init()

layout = [
    [sg.Text('Enter statement here: '), sg.InputText(), sg.Button('SPEAK')],
    [sg.Text('Select preferred sound:'), sg.Radio("Male", "voice", default=True, key="-FEMALE-"),sg.Radio("Female", "voice", default=False, key="-MALE-")]
]
frame = sg.Window(('Text to Speech converter'), layout)
while True:
    event, values = frame.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "SPEAK":
        text = values[0]
        voice = "male" if values["-MALE-"] else "female"
        if voice == "male":
            x.setProperty('voice', x.getProperty('voices')[1].id)
        else:
            x.setProperty('voice', x.getProperty('voices')[0].id)
        x.say(text)
        x.runAndWait()
frame.close()