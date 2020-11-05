def tabulate():
    import pandas as pd 
    import numpy as np 
    import xlsxwriter as xl
    import os 
    os.system('color')
    #import regex as rg 

    '''
    docstring
    function: this program reads the Cerberus Excel data & returns a list of lists, each containing (Segment Name, LOH, TTL, LRR)
    '''


    filename = r"\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly LRR Reports\LW2104 Compile.xlsx"
    '''
    logweek = input("Which logweek would you like to query?")
    logweek = int(logweek)

    filename = f"\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly LRR Reports\LW{logweek} Compile.xlsx"
    #filename = repr(filename)
    filename = r"{}".format(filename)
    '''

    print("These are the Cerberus values")

    sheets_dict = pd.read_excel(filename, sheet_name=None, skiprows=8)

    full_table = pd.DataFrame()

    # name is a key, sheet is a value (key-value pair)
    # name is a String, sheet is a DataFrame 
    for name, sheet in sheets_dict.items():
        
        # this adds another column containing the Worksheet name
        sheet['sheet'] = name.split("-")[0].strip() + " " + name.split("-")[1].split(" ")[1].strip()
        #sheet = sheet.rename(columns=lambda x: x.split('_')[0]) can't split because of column ALF_DISPOSITION
        full_table = full_table.append(sheet)

    #print('1. unique values in sheet', full_table.sheet.unique())

    # filtering of data in LOH, TTL
    '''
    For 'Hold Comments':
        WUXI DS has no filter applied,
        WUXI CC retains DDM comments, excludes all http comments
    '''

    # Parameter violations that DSMAL lots have to adhere to 
    dsmal_list = ['1WAVIS','2DVIS','2TPVIS','3BOVIS','INTAPE','MBIN1','MISDEV','N.A.','OUTPAD','PADCOV','PADEDG','PADIMM','PNP','PURGE','TWBOTT','TWTOP','VISION_IN_TAPE']

    # preserves these columns 
    full_table = full_table[ ['Owner', 'Hold Comments', 'sheet'] ]

    # strip "!" from "Parameter ..." values in 'Hold Comments column (data cleaning in preparation for DSMAL)
    full_table['Hold Comments'] = full_table['Hold Comments'].str.strip("!")

    # filter for 'Owner' first (TTL count)
    full_table = full_table[ full_table['Owner'].isin(['PROD', 'RISK', 'RISM', 'RWIC', 'SFLA']) ]

    # filter for 'Hold Comments' (LOH count)
    full_table = full_table[ full_table['Hold Comments'].isin(['Configure', 'Lot-Error']) | full_table['Hold Comments'].str.contains('Parameter') 

                            # retains WUXI DS entries
                            | full_table['sheet'].str.contains('WUXI DS') 

                            # retains WUXI CC entries 
                            | ( full_table['sheet'].str.contains('WUXI CC') & full_table['Hold Comments'].str.contains('DDM') ) 

                            # retains DSMAL entries 
                            # filtering for DSMAL entries is done later on

                            # retains TTL lots
                            | ( full_table['sheet'].str.contains('DWHView') )

                            ]

    
    # tuples to store each segment's values: LOH, TTL, LRR
    dsmal_loh, plt_loh, sens_loh, ts_loh, wuxicc_loh, wuxids_loh, pob_loh = "", "", "", "", "", "", ""
    dsmal_ttl, plt_ttl, sens_ttl, ts_ttl, wuxicc_ttl, wuxids_ttl, pob_ttl = "", "", "", "", "", "", ""
    dsmal_LRR, plt_LRR, sens_LRR, ts_LRR, wuxicc_LRR, wuxids_LRR, pob_LRR = "", "", "", "", "", "", ""

    segment_loh = [ dsmal_loh, plt_loh, sens_loh, ts_loh, wuxicc_loh, wuxids_loh, pob_loh ]
    segment_ttl = [ dsmal_ttl, plt_ttl, sens_ttl, ts_ttl, wuxicc_ttl, wuxids_ttl, pob_ttl ]
    segment_LRR = [ dsmal_LRR, plt_LRR, sens_LRR, ts_LRR, wuxicc_LRR, wuxids_LRR, pob_LRR ]
    segment_tuple = ('DSMAL', 'PLT', 'SENS', 'TS', 'WUXI CC', 'WUXI DS', 'POB')
    segment_stats_list = []

    # counting of segment's stats
    #for loh, ttl, lrr, name in zip(segment_loh, segment_ttl, segment_LRR, segment_tuple): zip doesn't work here because assignment isn't done/allowed in zip
    for i, name in enumerate(segment_tuple):

        if 'DSMAL' in name:
            dsmal_df = full_table.copy(deep=True)
            dsmal_df['new'] = dsmal_df['Hold Comments'].str.split(";+|:+")
            dsmal_df = dsmal_df[ dsmal_df['sheet'].str.contains('DSMAL') & dsmal_df['sheet'].str.contains('LOH') ]
            dsmal_df['new 1'] = [ x[1:] for x in dsmal_df['new'] if len(x) > 1 or x in ['Configure', 'Lot-Error'] ]

            k = dsmal_df[ dsmal_df['new 1'].apply(lambda x: set(x).issubset(set(dsmal_list))) ] 

            dsmal_loh = len(dsmal_df.index) - len(k.index)

            import os 
            os.system('color')
            print("DSMAL LOH value is ", end='')
            print('\x1b[6;30;42m' + str(dsmal_loh) + '\x1b[0m')

            segment_loh[i] = dsmal_loh
            segment_ttl[i] = len( full_table[ full_table['sheet'].str.contains(name) & full_table['sheet'].str.contains('DWHView') ].index )
            segment_LRR[i] = round(dsmal_loh / segment_ttl[i], 5)

            continue

        if 'SENS' in name:
            # need to take into consideration for SENS, since the data for TTL is split into 2 worksheets
            ttl1 = len( full_table[ full_table['sheet'].str.contains(name) & full_table['sheet'].str.contains('1') & full_table['sheet'].str.contains('DWHView') ].index )
            ttl2 = len( full_table[ full_table['sheet'].str.contains(name) & full_table['sheet'].str.contains('2') & full_table['sheet'].str.contains('DWHView') ].index )
            ttl = ttl1 + ttl2
            
        else:      
            ttl = len( full_table[ full_table['sheet'].str.contains(name) & full_table['sheet'].str.contains('DWHView') ].index )

        loh = len( full_table[ full_table['sheet'].str.contains(name) & full_table['sheet'].str.contains('LOH') ].index )
        lrr = round(loh / ttl, 5)
        #print(f'{name}\'s stats are {loh}, {ttl}, {lrr*100}%')

        segment_loh[i] = loh
        segment_ttl[i] = ttl
        segment_LRR[i] = lrr
        #segment_stats_list.append( [loh, ttl, lrr] )
    
    segment_stats = zip(segment_tuple, segment_loh, segment_ttl, segment_LRR)
    segment_stats_list = list(segment_stats)

    return segment_stats_list
    

    '''
    #   To set up an Excel workbook to track all segment's values: LOH, TTL & LRR%
    '''


'''
references:
https://stackoverflow.com/questions/41340341/how-to-determine-the-length-of-lists-in-a-pandas-dataframe-column
https://www.kite.com/python/answers/how-to-filter-a-pandas-dataframe-with-a-list-by-%60in%60-or-%60not-in%60-in-python
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.split.html
https://stackoverflow.com/questions/36108377/how-to-use-the-split-function-on-every-row-in-a-dataframe-in-python
https://www.programiz.com/python-programming/list
https://stackoverflow.com/questions/34468983/how-to-check-if-all-elements-in-a-tuple-or-list-are-in-another
https://stackoverflow.com/questions/8113782/split-string-on-whitespace-in-python
https://pandas.pydata.org/pandas-docs/version/0.23.4/text.html
https://medium.com/swlh/3-ways-to-filter-pandas-dataframe-by-column-values-dfb6609b31de
https://www.programiz.com/python-programming/methods/built-in/zip


from friday (30/10)'s session
https://stackoverflow.com/questions/17322109/get-dataframe-row-count-based-on-conditions
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.copy.html
https://stackoverflow.com/questions/20246722/typeerror-object-of-type-float-has-no-len
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html
https://www.programiz.com/python-programming/list-comprehension
https://stackoverflow.com/questions/40646458/list-comprehension-in-pandas
https://www.geeksforgeeks.org/python-retain-list-elements-value-items/
https://towardsdatascience.com/how-to-quickly-create-and-unpack-lists-with-pandas-d0e78e487c75
https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

'''