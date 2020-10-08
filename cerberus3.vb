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
    WUXI_CC = ""
    WUXI_CC_WS = "WUXI CC_ASSESSED"
''  WUXI DS
    WUXI_DS = ""
    WUXI_DS_WS = "WUXI DS_ASSESSED"
''  TS
    TS = ""
    TS_WS = "SIN TS_ASSESSED"
''  SENS
    SENS = ""
    SENS_WS = "MAL SCC_ASSESSED"
''  PLT
    PLT = ""
    PLT_WS = "MAL PLT_ASSESSED"
''  DSMAL
    DSMAL = ""
    DSMAL_WS = "MAL DS_ASSESSED"
''  POB
    POB = ""
    POB_WS = "BATAM POB_ASSESSED"
    
    
    ''' The path of the Excel Workbook containing just the ASSESSED Worksheets of the different segments
    ''' can be referred to as "MyMaster"

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