Sub cerberus4()
    
    ''' Finalized code to create CSV files of each segments' DDM_FINAL.
    ''' Each segments' CSV is stored in one location (Weekly Cerberus Check (Automated) folder in Haikal's folder).
    ''' The CerberusCheck Excel Workbook containing all segments' DDM_FINAL
    ''' is not being altered in this version of the code.
    
    Application.EnableEvents = False
    Application.ScreenUpdating = False
    Application.DisplayAlerts = False
    Application.AskToUpdateLinks = False
    
    Dim WUXI_CC, WUXI_DS, TS, SENS, PLT, DSMAL, POB, Path_Mymaster As String
    Dim WUXI_CC_WS, WUXI_DS_WS, TS_WS, SENS_WS, PLT_WS, DSMAL_WS, POB_WS As String
    Dim worksheet As worksheet
    
    
''  WUXI CC
    WUXI_CC = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\11B_DDM_Reporting\WUXICC DDM\Masterfile.xlsx"
    WUXI_CC_WS = "WUXI CC_ASSESSED"
''  WUXI DS
    WUXI_DS = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\11B_DDM_Reporting\WUXIDS DDM\Masterfile.xlsx"
    WUXI_DS_WS = "WUXI DS_ASSESSED"
''  TS
    TS = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\11B_DDM_Reporting\TS DDM\Masterfile.xlsx"
    TS_WS = "SIN TS_ASSESSED"
''  SENS
    SENS = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\11B_DDM_Reporting\SENS DDM\Masterfile.xlsx"
    SENS_WS = "MAL SCC_ASSESSED"
''  PLT
    PLT = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\11B_DDM_Reporting\PLT DDM\Masterfile.xlsx"
    PLT_WS = "MAL PLT_ASSESSED"
''  DSMAL
    DSMAL = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\11B_DDM_Reporting\DSMAL DDM\Masterfile.xlsx"
    DSMAL_WS = "MAL DS_ASSESSED"
''  POB
    POB = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\11B_DDM_Reporting\POB DDM\Masterfile.xlsx"
    POB_WS = "BATAM POB_ASSESSED"
    
    
    ''' The path of the Excel Workbook containing just the ASSESSED Worksheets of the different segments
    ''' can be referred to as "MyMaster"
    'Path_Mymaster = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\PersonalProjects\CerberusCheck\CerberusCheck.xlsx"
    Path_Mymaster = "C:\Users\MohamadYusuf\Desktop\Haikal\Personal Projects\CerberusCheck.xlsx"
    
    
    ''' Declaration & assignment of different segments' worksheet names & paths
        Dim openWB As Workbook
        Dim Paths As Variant
            'Paths = Array(WUXI_CC, WUXI_DS, TS, SENS, PLT, DSMAL, POB)
            Paths = Array(WUXI_CC, WUXI_DS, TS, SENS, PLT, DSMAL)
        Dim worksheets As Variant
            'worksheets = Array(WUXI_CC_WS, WUXI_DS_WS, TS_WS, SENS_WS, PLT_WS, DSMAL_WS, POB_WS)
            worksheets = Array(WUXI_CC_WS, WUXI_DS_WS, TS_WS, SENS_WS, PLT_WS, DSMAL_WS)
    
    
    ''' Compile all segments' worksheets into 1 Workbook
        Dim i As Integer
        
        For i = 0 To UBound(Paths)
            
            Set openWB = Workbooks.Open(Paths(i))
            
            For Each worksheet In openWB.worksheets
                If worksheet.Name = "DDM_FINAL" Then
''                    MyPATH = ActiveWorkbook.Path    '''''''''' TO CHANGE if you don't want the csv files to be saved to the respective segment's folders
                    MyPATH = "\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly Cerberus Check (Automated)"
                    FileNAME = "" & Split(worksheets(i), "_")(0)
                    FileNAME = FileNAME & ".csv" ' ADD CSV EXTENSION
                    Application.DisplayAlerts = False ' REMOVE DISPLAY MESSAGE: PREVIOUS FILE WILL BE ERASED
                    ActiveWorkbook.SaveAs FileNAME:=MyPATH & "\" & FileNAME, FileFormat:=xlCSV, CreateBackup:=False
                End If
            Next worksheet
            openWB.Close SaveChanges:=False
            
        Next i
        
        
    ''' Separate CSV export for POB, because it can't work in the main loop with the other segments
    POB_CSV2
    
    Application.EnableEvents = True
    Application.ScreenUpdating = True
    Application.DisplayAlerts = True
    Application.AskToUpdateLinks = True
    

End Sub




Sub POB_CSV2()
    
    ''' 2nd version of the POB_CSV code, to extract the DDM_FINAL of POB's Masterfile & save it as a CSV
    
    Application.DisplayAlerts = False

    Dim openWB As Workbook
    
    pob_path = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\11B_DDM_Reporting\POB DDM\Masterfile.xlsx"
    pob_worksheet_name = "BATAM POB_ASSESSED"
    
    MyPATH = "\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly Cerberus Check (Automated)"
    
    Set openWB = Workbooks.Open(pob_path)
    
    Sheets("DDM_FINAL").Select
    
    
    ActiveWorkbook.SaveAs FileNAME:= _
        MyPATH & "\BATAM POB.csv", FileFormat:= _
        xlCSV, CreateBackup:=False
        
    openWB.Close SaveChanges:=False
    
    Application.DisplayAlerts = True
    
End Sub