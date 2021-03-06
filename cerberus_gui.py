
def gui():
    import PySimpleGUI as sg 
    import cerberus_report as cr

    # Main GUI Window
    sg.theme('GreenTan')   
    layout = [[sg.Text('Automated Cerberus Check!')],      
             
             # checkboxes for certain functionalities of the program 
             [sg.Checkbox('Cerberus Transfer', default=True, tooltip='Check if you want to extract the latest Tableau data')],
             [sg.Checkbox('LW Query', default=True, tooltip='Check if you want to auto-query the latest LW')],
             [sg.Checkbox('Generate & save report', default=True, tooltip='Check if you want to generate & save the report')],
             [sg.Checkbox('Open report after completion', default=True, tooltip='Check if you want to open the report')],

             [sg.Text('LW to Query')],
             [sg.Input(key='-IN-')],  
             [sg.Button('Read'), sg.Exit()]]

    window = sg.Window('Cerberus Check', layout)   

    # The Event Loop
    while True:  
        
        event, values = window.read() 
        if event == sg.WIN_CLOSED or event == 'Exit':
            break 

        print(event, values)

        # GUI Window for Progress   
        layout_progress = [[sg.Text('Automated Cerberus Check underway ...')]]
        window_progress = sg.Window('In Progress', layout_progress)
        # the read() method will keep the pop-up window active & wait for inputs.
        # basically, the code stops here & waits for inputs 
        window_progress.read()

        # boolean to track if Cerberus Macro is to be run
        bool_CerberusMacro = values[0]

        # boolean to track if auto query for most recent LW is to be done
        bool_RecentLW = values[1]

        # boolean to track if report is to be generated & saved
        bool_GenerateAndSaveReport = values[2]

        # boolean to track if report is to be opened
        bool_OpenReport = values[3]

        # Path containing Weekly Cerberus Data
        path_CerberusData = r'\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly LRR Reports'
        # Path containing Weekly Cerberus Reports
        path_CerberusReport = r"\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly Cerberus Check (KT Report)"

        ''' Run Macro '''
        if bool_CerberusMacro:
            cr.cerberusTransfer()

        if bool_RecentLW:
            filename = cr.latestFile(path_CerberusData)
            st = filename.split("\\")
            logweek = st[-1].split(" ")[0]
            logweek = int( logweek[2:] )
        else:
            logweek = values['-IN-'] #find from values what user typed in for LW
            logweek = int(logweek)
            
            filename = cr.find_file(path=path_CerberusData, logweek=logweek)
            print("The filename is:", filename)

        if bool_GenerateAndSaveReport and bool_RecentLW:
            report = cr.report_generator(logweek=logweek, filename=filename)
            cr.copy_files(report=report, logweek=logweek)

        if bool_OpenReport:
            import os
            if bool_RecentLW:
                filename = cr.latestFile(path_CerberusReport)
            else:
                filename = cr.find_file(path=path_CerberusReport, logweek=logweek)
            os.startfile(filename)

        # Close the GUI Window for Progress
        window_progress.close()

        # A GUI Window for completed task
        layout_done = [[sg.Text('Automated Cerberus Check completed!')]]
        window_done = sg.Window('Done!', layout_done)
        window_done.read()

    window.close()

    ''' references:
        https://opensource.com/article/18/8/pysimplegui
        https://pysimplegui.readthedocs.io/en/latest/cookbook/
        https://pysimplegui.readthedocs.io/en/latest/call%20reference/#checkbox-element
        
    '''

def main():
    gui()   


if __name__ == "__main__":
    main()
