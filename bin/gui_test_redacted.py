import PySimpleGUI as sg 
from PySimpleGUI import *

'''
sg.theme('GreenTan')

layout = [[Text('Persistent window')],      
        [Input(key='-IN-')],
        #[Checkbox('Checkbox 1', OK()), Checkbox('Checkbox 2'), OK()],      
        [Checkbox('Cerberus Transfer', OK())], 
        [Checkbox('Auto LW Query', default=True, tooltip="Check if you want to auto-query the latest LW")],
        [Button('Read'), Exit()]]   

window = sg.Window('Window that stays open', layout)      

while True:                            
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      

window.close()
'''

sg.theme('GreenTan')    # Keep things interesting for your users

layout = [[Text('Persistent window')],
          [Input(key='-IN-')],      
          [Checkbox('Cerberus Transfer', OK())], 
          #[Checkbox('Auto LW Query', default=True, tooltip="Check if you want to auto-query the latest LW")],      
          [Checkbox('Auto LW Query', OK())],
          [Button('Read'), Exit()]]      

window = Window('Window that stays open', layout)      

while True:                             # The Event Loop
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      

window.close()


