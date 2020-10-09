import pandas as pd
import numpy as np 

df_pob, df_dsmal, df_plt, df_sens, df_ts, df_wuxicc, df_wuxids = "", "", "", "", "", "", ""

path_pob = ""
path_dsmal = ""
path_plt = ""
path_sens = ""
path_ts = ""
path_wuxicc = ""
path_wuxids = ""

'''
df = pd.read_csv(path_pob, skiprows=0)
print(df.head()) '''

# df_pob, path_pob, 

df_tuple = [df_dsmal, df_plt, df_sens, df_ts, df_wuxicc, df_wuxids]
path_tuple = [path_dsmal, path_plt, path_sens, path_ts, path_wuxicc, path_wuxids]

for df, path in zip(df_tuple, path_tuple):
    df = pd.read_csv(path, skiprows=0)

    # variables tracking LOH & TTL
    loh_count = 0
    ttl_count = 0

    # Logweek
    logweek = 2052

    # segment's name
    segment_list = path.split("\\")
    segment = segment_list[len(segment_list)-1].split(".")[0]

    # checking for LOH - Lot On Hold
    df_loh = df[(df['LW'] == logweek) & (df['ALF_DISPOSITION'] == 'ON-HOLD')]
    loh_count = len(df_loh.index)

    # checking for TTL - Total Lot Count
    df_ttl = df[(df['LW'] == logweek) & (df['ALF_DISPOSITION'] == 'AUTO RELEASE')]
    ttl_count = len(df_ttl.index)

    # print out segment's stats
    print(f'{segment}\'s stats are {loh_count}, {ttl_count}')


'''
INITIAL FINDINGS:
1. TS & DSMAL differ in values between Tableau & this Python code (which looks at the underlying excel data for Tableau) ((so by right shouldn't be diff...))
    - TS has the filter for "NO" under the "100% Hold" column, that's why my initial results differed, cos i didn't consider the "100% Hold" condition
        -> Difference in values RESOLVED
    - DSMAL 
        -> Difference in values uncertain 

2. POB is temporarily left out because the CSV file contains the POB_OPEN worksheet instead of the DDM_FINAL worksheet
    
3. Segments' stats:
    MAL DS's stats are 339, 1720 (*)
    MAL PLT's stats are 633, 7575 
    MAL SCC's stats are 60, 2523 
    SIN TS's stats are 947, 6130 (*)
    WUXI CC's stats are 8, 949 
    WUXI DS's stats are 69, 747 

4. Errors raised for each segment:
    sys:1: DtypeWarning
    -> this error occurs when there are different dtypes in a column from a file 

    - possible solution is to put the read_csv code in a try-catch block

'''