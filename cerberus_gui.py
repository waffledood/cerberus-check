
def gui():
    import PySimpleGUI as sg 
    import cerberus_report as cr

    sg.theme('GreenTan')   

    layout = [[sg.Text('Automated Cerberus Check!')],      
             [sg.Checkbox('Cerberus Transfer', default=True, tooltip='')],
             [sg.Checkbox('LW Query', default=True, tooltip='Check if you want to auto-query the latest LW')],
             [sg.Text('LW to Query')],
             [sg.Input(key='-IN-')],  
             [sg.Button('Read'), sg.Exit()]]      

    window = sg.Window('Cerberus Check', layout)      

    # The Event Loop
    while True:                             
        event, values = window.read() 
        print(event, values)       

        if event == sg.WIN_CLOSED or event == 'Exit':
            break   

        # boolean to track if Cerberus Macro is to be run
        a = values[0]

        # boolean to track if auto query for most recent LW is to be done
        b = values[1]

        ''' Run Macro '''
        if a:
            cr.cerberusTransfer()

        ''' Auto latest LW Query '''
        path = r'\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly LRR Reports'

        if b:
            filename = cr.latestFile(path)
            st = filename.split("\\")
            logweek = st[-1].split(" ")[0]
            logweek = int( logweek[2:] )
        else:
            cr.find_file(path=path, logweek=logweek)
            # filename = function1(path)
            # new function that reads path & finds the path of the file with the 
            logweek = values['-IN-'] #find from values what user typed in for LW

        report = cr.report_generator(logweek=logweek, filename=filename)
        copy_files(report=report, logweek=logweek)

    window.close()

def main():
    gui()   


if __name__ == "__main__":
    main()
