def tabulate(logweek):
    import pandas as pd
    import numpy as np 

    '''
    docstring
    function: this program reads each Tableau Excel data & returns a list of lists, each containing (Segment Name, LOH, TTL, LRR)

    method: the Tableau Excel data is broken into CSV files containing individual segments' data (achieved through cerberus3.vb). 
            Each CSV file is read for LOH, TTL & LRR values. 
            A list of lists with these data is then returned.
    '''

    # declaration & instantiation of variables (dataframes & paths)
    df_pob, df_dsmal, df_plt, df_sens, df_ts, df_wuxicc, df_wuxids = "", "", "", "", "", "", ""

    path_pob = r"\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly Cerberus Check (Automated)\BATAM POB.csv"
    path_dsmal = r"\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly Cerberus Check (Automated)\MAL DS.csv"
    path_plt = r"\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly Cerberus Check (Automated)\MAL PLT.csv"
    path_sens = r"\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly Cerberus Check (Automated)\MAL SCC.csv"
    path_ts = r"\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly Cerberus Check (Automated)\SIN TS.csv"
    path_wuxicc = r"\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly Cerberus Check (Automated)\WUXI CC.csv"
    path_wuxids = r"\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly Cerberus Check (Automated)\WUXI DS.csv"

    #print("These are the Tableau values")

    # setting a tuple each for dataframes & paths
    df_tuple = [df_dsmal, df_plt, df_sens, df_ts, df_wuxicc, df_wuxids, df_pob]
    path_tuple = [path_dsmal, path_plt, path_sens, path_ts, path_wuxicc, path_wuxids, path_pob]
    segment_stats_list = []

    # Logweek
    '''
    logweek = input("Which logweek do you want to query? ")
    logweek = int(logweek)
    '''


    # main loop to go through the tuples of paths & dataframes & perform LOH & TTL count
    #for df, path in zip(df_tuple, path_tuple):
    for i, path in enumerate(path_tuple):
        try:
            df = pd.read_csv(path, skiprows=0, low_memory=False)
            # bad practice to set low_memory=False

            # variables tracking LOH & TTL
            loh_count = 0
            ttl_count = 0

            # segment's name
            segment_list = path.split("\\")
            segment = segment_list[len(segment_list)-1].split(".")[0]

            # checking for LOH - Lot On Hold
            if "MAL DS" in segment:
                df_loh = df[(df['LW'] == logweek) & (df['ALF_DISPOSITION'] == 'ON-HOLD') & (df['PTE/UPE'] != 'UPE')]
                loh_count = len(df_loh.index)
            elif "TS" in segment:
                df_loh = df[ (df['LW'] == logweek) & (df['ALF_DISPOSITION'] == 'ON-HOLD') & (df['100% Hold'] != 'YES') ]
                loh_count = len(df_loh.index)
            else:
                df_loh = df[(df['LW'] == logweek) & (df['ALF_DISPOSITION'] == 'ON-HOLD')]
                loh_count = len(df_loh.index)

            # checking for TTL - Total Lot Count
            df_ttl = df[(df['LW'] == logweek) & (df['ALF_DISPOSITION'] == 'AUTO RELEASE')]
            ttl_count = len(df_ttl.index)
            df_tuple[i] = df

            # print out segment's stats
            #print(f'{segment}\'s stats are {loh_count}, {ttl_count}')
            segment_stats_list.append([segment, loh_count, ttl_count, round(loh_count / ttl_count, 5)])
            # segment_tuple, segment_loh, segment_ttl, segment_LRR
        except Exception as e:
            print("Error caught")
            print(e)

    #print(df_tuple)

    return segment_stats_list

'''
a = tabulate()
print(a)
'''


'''
    INITIAL FINDINGS:

    1. Results for LW2101
        TS difference (between Tableau's Excel source & Tableau chart)
        - 986/6300 VS 829/6300

        DSMAL difference (RESOLVED) --> difference was because of the PTE/UPE filter
        - 463 / 1323 VS 219/1323

    1. TS & DSMAL differ in values between Tableau & this Python code (which looks at the underlying excel data for Tableau) ((so by right shouldn't be diff...))
        - TS has the filter for "NO" under the "100% Hold" column, that's why my initial results differed, cos i didn't consider the "100% Hold" condition
            -> Difference in values RESOLVED
        - DSMAL 
            -> Difference in values uncertain 

    [RESOLVED]
    2. POB is temporarily left out because the CSV file contains the POB_OPEN worksheet instead of the DDM_FINAL worksheet 
        
    [RESOLVED]
    3. Segments' stats (for 2053):
        MAL DS's stats are 339, 1720 (*)
        MAL PLT's stats are 633, 7575 
        MAL SCC's stats are 60, 2523 
        SIN TS's stats are 947, 6130 (*)
        WUXI CC's stats are 8, 949 
        WUXI DS's stats are 69, 747 
        POB's stats are NULL, NULL (*) -> POB left out because the CSV is POB_OPEN instead of DDM_FINAL

    4. Errors raised for each segment:
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.errors.DtypeWarning.html 
        sys:1: DtypeWarning
        -> this error occurs when there are different dtypes in a column from a file 

        - possible solution is to put the read_csv code in a try-catch block

    '''



