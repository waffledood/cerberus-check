Sub cerberus1()

    Application.EnableEvents = False
    Application.ScreenUpdating = False
    Application.DisplayAlerts = False
    Application.AskToUpdateLinks = False
    
    Dim Path_dsmal, Path_wuxicc, Path_sens, Path_Mymaster, Path_ts, Path_wuxids, Path_plt, Path_pob As String
    Dim opendsmal, openwuxicc, opensens, opents, openwuxids, openplt, openpob, openmymaster As Workbook
    

    Path_Mymaster = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\PersonalProjects\CerberusCheck\CerberusCheck.xlsx"
    
    
    Set openmymaster = Workbooks.Open(Path_Mymaster)
    
    openmymaster.Activate
    With ActiveSheet
        Dim worksheet As worksheet
        For Each worksheet In openmymaster.worksheets
            If worksheet.Name <> "Sheet1" Then
               worksheet.Delete
            End If
        Next
    End With
    
''  WUXI CC
    Path_wuxicc = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\11B_DDM_Reporting\WUXICC DDM\Masterfile.xlsx"
    Set openwuxicc = Workbooks.Open(Path_wuxicc)

    For Each worksheet In openwuxicc.worksheets
        If worksheet.Name = "DDM_FINAL" Then
            worksheet.Copy after:=openmymaster.Sheets(openmymaster.Sheets.Count)
        End If
    Next worksheet
    openwuxicc.Close SaveChanges:=False
    
    'change sheets name
    openmymaster.Activate
    With ActiveSheet
        ActiveWorkbook.Sheets("DDM_FINAL").Name = "WUXI CC_ASSESSED"
    End With
    openmymaster.Save

    
''  TS
    Path_ts = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\11B_DDM_Reporting\TS DDM\Masterfile.xlsx"
    Set opents = Workbooks.Open(Path_ts)
    
    For Each worksheet In opents.worksheets
        If worksheet.Name = "DDM_FINAL" Then
            worksheet.Copy after:=openmymaster.Sheets(openmymaster.Sheets.Count)
        End If
    Next worksheet
    opents.Close SaveChanges:=False
    
    'change sheets name
    openmymaster.Activate
    With ActiveSheet
        ActiveWorkbook.Sheets("DDM_FINAL").Name = "SIN TS_ASSESSED"
    End With
    openmymaster.Save

''  WUXI DS
    Path_wuxids = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\11B_DDM_Reporting\WUXIDS DDM\Masterfile.xlsx"
    Set openwuxids = Workbooks.Open(Path_wuxids)

    For Each worksheet In openwuxids.worksheets
        If worksheet.Name = "DDM_FINAL" Then
            worksheet.Copy after:=openmymaster.Sheets(openmymaster.Sheets.Count)
        End If
    Next worksheet
    openwuxids.Close SaveChanges:=False
    
    'change sheets name
    openmymaster.Activate
    With ActiveSheet
        ActiveWorkbook.Sheets("DDM_FINAL").Name = "WUXI DS_ASSESSED"
    End With
    openmymaster.Save
    
''  SENS
    Path_sens = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\11B_DDM_Reporting\SENS DDM\Masterfile.xlsx"
    Set opensens = Workbooks.Open(Path_sens)

    For Each worksheet In opensens.worksheets
        If worksheet.Name = "DDM_FINAL" Then
            worksheet.Copy after:=openmymaster.Sheets(openmymaster.Sheets.Count)
        End If
    Next worksheet
    opensens.Close SaveChanges:=False
    
    'change sheets name
    openmymaster.Activate
    With ActiveSheet
        ActiveWorkbook.Sheets("DDM_FINAL").Name = "MAL SCC_ASSESSED"
    End With
    openmymaster.Save

''  PLT
    Path_plt = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\11B_DDM_Reporting\PLT DDM\Masterfile.xlsx"
    Set openplt = Workbooks.Open(Path_plt)

    For Each worksheet In openplt.worksheets
        If worksheet.Name = "DDM_FINAL" Then
            worksheet.Copy after:=openmymaster.Sheets(openmymaster.Sheets.Count)
        End If
    Next worksheet
    openplt.Close SaveChanges:=False
    
    'change sheets name
    openmymaster.Activate
    With ActiveSheet
        ActiveWorkbook.Sheets("DDM_FINAL").Name = "MAL PLT_ASSESSED"
    End With
    openmymaster.Save

''  DSMAL
    Path_dsmal = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\11B_DDM_Reporting\DSMAL DDM\Masterfile.xlsx"
    Set opendsmal = Workbooks.Open(Path_dsmal)

    For Each worksheet In opendsmal.worksheets
        If worksheet.Name = "DDM_FINAL" Then
            worksheet.Copy after:=openmymaster.Sheets(openmymaster.Sheets.Count)
        End If
    Next worksheet
    opendsmal.Close SaveChanges:=False
    
    'change sheets name
    openmymaster.Activate
    With ActiveSheet
        ActiveWorkbook.Sheets("DDM_FINAL").Name = "MAL DS_ASSESSED"
    End With
    openmymaster.Save


''  POB
    Path_pob = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\11B_DDM_Reporting\POB DDM\Masterfile.xlsx"

    Set openpob = Workbooks.Open(Path_pob)
    'Set openpob = Workbooks.Open("D:\sina360tsd\Masterfile.xlsx")

    For Each worksheet In openpob.worksheets
      worksheet.Copy after:=openmymaster.Sheets(openmymaster.Sheets.Count)
    Next worksheet
    openpob.Close SaveChanges:=False
    'change sheets name
    openmymaster.Activate
    With ActiveSheet
        ActiveWorkbook.Sheets("DDM_FINAL").Name = "BATAM POB_ASSESSED"
    End With
    openmymaster.Save

    
''        Dim statusPath As String
''
''        'statusPath = "\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\11B_DDM_Reporting\DDM_Status_Check.xlsx"
''        'statusPath = "C:\Users\MohamadYusuf\Desktop\Test Environment\DDM_Status_Check.xlsx"
''        statusPath = "\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Test Environment\DDM_Status_Check.xlsx"
''
''        Dim status As Workbook
''        Set status = Workbooks.Open(statusPath)
''
''        Workbooks("DDM_Status_Check.xlsx").Activate
''
''        Range("$I$2").Value = Format(Now, "dd/mm/yyyy HH:mm:ss")
''
''        Workbooks("DDM_Status_Check.xlsx").Close SaveChanges:=True
    
    Application.EnableEvents = True
    Application.ScreenUpdating = True
    Application.DisplayAlerts = True
    Application.AskToUpdateLinks = True

End Sub

Sub cerberus2()
    
    ''' This is the finalized code to use for the Weekly Cerberus Check
    ''' This code is better than the previous code as it is less verbose & emphasises extensability & abstraction

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
    Path_Mymaster = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\PersonalProjects\CerberusCheck\CerberusCheck.xlsx"
    
    ''' Declaration & assignment of different segments' worksheet names & paths
        Dim openWB, openMainWB As Workbook
        Dim Paths As Variant
            Paths = Array(WUXI_CC, WUXI_DS, TS, SENS, PLT, DSMAL, POB)
        Dim worksheets As Variant
            worksheets = Array(WUXI_CC_WS, WUXI_DS_WS, TS_WS, SENS_WS, PLT_WS, DSMAL_WS, POB_WS)
    
    
    ''' Open the MyMaster Excel workbook & delete all existing Worksheets
        Set openMainWB = Workbooks.Open(Path_Mymaster)
        
        openMainWB.Activate
        With ActiveSheet
            For Each worksheet In openMainWB.worksheets
                If worksheet.Name <> "Sheet1" Then
                   worksheet.Delete
                End If
            Next
        End With
    
    
    ''' Compile all segments' worksheets into 1 Workbook
        Dim i As Integer
        
        For i = 0 To UBound(Paths)
            
            Set openWB = Workbooks.Open(Paths(i))
            
            For Each worksheet In openWB.worksheets
                If worksheet.Name = "DDM_FINAL" Then
                    worksheet.Copy after:=openMainWB.Sheets(openMainWB.Sheets.Count)
                End If
            Next worksheet
            openWB.Close SaveChanges:=False
            
            'change sheets name
            openMainWB.Activate
            With ActiveSheet
                ActiveWorkbook.Sheets("DDM_FINAL").Name = worksheets(i)
            End With
            openMainWB.Save
            
        Next i

    
    Application.EnableEvents = True
    Application.ScreenUpdating = True
    Application.DisplayAlerts = True
    Application.AskToUpdateLinks = True

End Sub

Sub cerberus3()
    
    ''' This is the finalized code, with CSV export functionality, to use for the Weekly Cerberus Check
    ''' This code is better than the previous code as it is less verbose & emphasises extensability & abstraction

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
        Dim openWB, openMainWB As Workbook
        Dim Paths As Variant
            Paths = Array(WUXI_CC, WUXI_DS, TS, SENS, PLT, DSMAL, POB)
        Dim worksheets As Variant
            worksheets = Array(WUXI_CC_WS, WUXI_DS_WS, TS_WS, SENS_WS, PLT_WS, DSMAL_WS, POB_WS)
    
    
    ''' Open the MyMaster Excel workbook & delete all existing Worksheets
        Set openMainWB = Workbooks.Open(Path_Mymaster)
        
        openMainWB.Activate
        With ActiveSheet
            For Each worksheet In openMainWB.worksheets
                If worksheet.Name <> "Sheet1" Then
                   worksheet.Delete
                End If
            Next
        End With
    
    
    ''' Compile all segments' worksheets into 1 Workbook
        Dim i As Integer
        
        For i = 0 To UBound(Paths)
            
            Set openWB = Workbooks.Open(Paths(i))
            
            For Each worksheet In openWB.worksheets
                If worksheet.Name = "DDM_FINAL" Then
                    'worksheet.Copy after:=openMainWB.Sheets(openMainWB.Sheets.Count)
                    'CSV_Export (Split(worksheets(i), "_")(0))
                    MyPATH = ActiveWorkbook.Path    '''''''''' TO CHANGE if you don't want the csv files to be saved to the respective segment's folders
                    FileNAME = "" & Split(worksheets(i), "_")(0)
                    FileNAME = FileNAME & ".csv" ' ADD CSV EXTENSION
                    Application.DisplayAlerts = False ' REMOVE DISPLAY MESSAGE: PREVIOUS FILE WILL BE ERASED
                    ActiveWorkbook.SaveAs FileNAME:=MyPATH & "\" & FileNAME, FileFormat:=xlCSV, CreateBackup:=False
                End If
            Next worksheet
            openWB.Close SaveChanges:=False

            
            
            
''            'change sheets name
''            openMainWB.Activate
''            With ActiveSheet
''                ActiveWorkbook.Sheets("DDM_FINAL").Name = worksheets(i)
''                'CSV_Export (Split(worksheets(i), "_")(0))
''            End With
''            openMainWB.Activate
''            CSV_Export (Split(worksheets(i), "_")(0))
''            'openMainWB.Save
            
        Next i

    
    Application.EnableEvents = True
    Application.ScreenUpdating = True
    Application.DisplayAlerts = True
    Application.AskToUpdateLinks = True

End Sub

Sub cerberus4()
    
    ''' Finalized code to create CSV files of each segments' DDM_FINAL.
    ''' Each segments' CSV is stored in one location (Weekly Cerberus Check (Automated) folder in Haikal's folder).
    ''' The CerberusCheck Excel Workbook containing all segments' DDM_FINAL
    ''' is not being altered in this version of the code.
    
    'a1 = Now()
    
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
    
    'a2 = Now()
    
    'MsgBox "Done! Start: " & a1 & ", a2: " & a2

End Sub




Sub POB_CSV()

    Dim openWB As Workbook
    
    pob_path = "\\wproj501\BE_CLUSTER_PTE\04_Data_Management\11B_DDM_Reporting\POB DDM\Masterfile.xlsx"
    pob_worksheet_name = "BATAM POB_ASSESSED"
    
    Set openWB = Workbooks.Open(pob_path)
    
    For Each worksheet In openWB.worksheets
            If worksheet.Name = "DDM_FINAL" Then
                MsgBox "This worksheet is: " & worksheet.Name
                MyPATH = "\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly Cerberus Check (Automated)"
                FileNAME = "" & Split(pob_worksheet_name, "_")(0)
                FileNAME = FileNAME & ".csv" ' ADD CSV EXTENSION
                Application.DisplayAlerts = False ' REMOVE DISPLAY MESSAGE: PREVIOUS FILE WILL BE ERASED
                ActiveWorkbook.SaveAs FileNAME:=MyPATH & "\" & FileNAME, FileFormat:=xlCSV, CreateBackup:=False
            End If
    Next worksheet
    
    
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



Sub CSVsample()
    
    ''' slightly altered copy from the internet that I used as a testbed
    ''''source: https://www.ozgrid.com/forum/index.php?thread/78886-save-workbook-as-csv-macro-code/

    Dim Path_Mymaster As String
    Dim wb As Workbook
    
    Path_Mymaster = "C:\Users\MohamadYusuf\Desktop\Haikal\Personal Projects\CerberusCheck.xlsx"
    
    '   Set openMainWB = Workbooks.Open(Path_Mymaster)
    Set wb = Workbooks.Open(Path_Mymaster)
    
    
    Dim MyPATH As String
    Dim FileNAME As String
    
    
    wb.Activate
    
    With ActiveWorkbook
    
        MyPATH = ActiveWorkbook.Path
        FileNAME = ActiveWorkbook.Name
        FileNAME = Left(FileNAME, Len(FileNAME) - 4) ' REMOVE XLS EXTENSION
        FileNAME = FileNAME & ".csv" ' ADD CSV EXTENSION
        Application.DisplayAlerts = False ' REMOVE DISPLAY MESSAGE: PREVIOUS FILE WILL BE ERASED
        ActiveWorkbook.SaveAs FileNAME:=MyPATH & "\" & FileNAME, FileFormat:=xlCSV, CreateBackup:=False
        ActiveWindow.Close
        Application.DisplayAlerts = True ' RESTAURE DISPLAY MESSAGE
    
    End With
    
    MsgBox "FileName is: " & FileNAME
    MsgBox "MyPath is: " & MyPATH
    
    
End Sub



Sub CSV_Export(Path_Mymaster As String, segment As String)
    
    
    ''' working sub that I intend to incorporate into cerberus2
    
    
    Dim Path_Mymaster As String
    Dim wb As Workbook
    
    'Path_Mymaster = "C:\Users\MohamadYusuf\Desktop\Haikal\Personal Projects\CerberusCheck.xlsx"
    
    '   Set openMainWB = Workbooks.Open(Path_Mymaster)
    Set wb = Workbooks.Open(Path_Mymaster)
    
    
    Dim MyPATH As String
    Dim FileNAME As String
    
    
    wb.Activate
    
    With ActiveWorkbook
    
        MyPATH = ActiveWorkbook.Path
        FileNAME = "" & segment
        FileNAME = FileNAME & ".csv" ' ADD CSV EXTENSION
        Application.DisplayAlerts = False ' REMOVE DISPLAY MESSAGE: PREVIOUS FILE WILL BE ERASED
        ActiveWorkbook.SaveAs FileNAME:=MyPATH & "\" & FileNAME, FileFormat:=xlCSV, CreateBackup:=False
        'ActiveWindow.Close
        Application.DisplayAlerts = True ' RESTAURE DISPLAY MESSAGE
    
    End With
    
    
    
End Sub




Sub Macro1()
'
' Macro1 Macro
'

'

    ActiveWorkbook.SaveAs FileNAME:= _
        "C:\Users\MohamadYusuf\Desktop\Haikal\Personal Projects\CerberusCheck (POB).csv" _
        , FileFormat:=xlCSV, CreateBackup:=False


End Sub

Sub Macro2()
'
' Macro2 Macro
'

'
    Windows("Masterfile.xlsx").Activate
    Sheets("DDM_FINAL").Select
    ChDir "Z:\04_Data_Management\11B_DDM_Reporting\POB DDM"
    ActiveWorkbook.SaveAs FileNAME:= _
        "Z:\04_Data_Management\11B_DDM_Reporting\POB DDM\BATAM POB.csv", FileFormat:= _
        xlCSV, CreateBackup:=False
    Windows("CerberusTransfer.xlsm").Activate
End Sub
