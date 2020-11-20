def gui():
    import PySimpleGUI as sg 
    from PySimpleGUI import *

    sg.theme('GreenTan')

    '''
    layout = [[sg.Text('Persistent window')],      
            [sg.Input(key='-IN-')],
            [sg.Checkbox('Checkbox 1', sg.OK()), sg.Checkbox('Checkbox 2'), sg.OK()],      
            [sg.Button('Read'), sg.Exit()]]      
    '''
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