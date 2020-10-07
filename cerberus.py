import pandas as pd 
import numpy as np 

''' 
Note that the total runtime from start till the printing out of the values took a total of 8 minutes & 55 seconds 
Input:
    MyMaster.xlsx (from 11B_DDM_REPORTING) renamed to pob.xlsx, with a file size of 334MB
    segmentStatCheck(full_table, 2047, segment_tuple)

Output:
    this is:  WUXI CC
    this is:  SIN TS
    this is:  WUXI DS
    this is:  WUXI DS
    this is:  MAL SCC
    this is:  MAL PLT
    this is:  MAL DS
    this is:  BATAM POB
    BATAM POB's stats are 110, 755
    (110, 755)
    MAL DS's stats are 199, 1677
    (199, 1677)
    MAL PLT's stats are 535, 6915
    (535, 6915)
    MAL SCC's stats are 44, 2532
    (44, 2532)
    WUXI DS's stats are 74, 850
    (74, 850)
    SIN TS's stats are 1029, 6207
    (1029, 6207)
    WUXI CC's stats are 0, 1069
    (0, 1069)
'''

def statCheck(df, logweek, segment):
    '''
    takes in the following parameters:
    df -> DataFrame containing all ASSESSED sheets of the different segments 
    logweek -> int representing the logweek we wish to look up
    segment -> String representing the segment we wish to look up
    '''
    '''
    returns a tuple (loh_count, ttl_count)
    '''

    # TODO 
    # consider chaining filtering of columns (refer to Haikal's Catalog)

    # check if the 'sheet' column contains the segment 
    #df1 = df[df['sheet'].contains(segment)]

    loh_count = 0
    ttl_count = 0

    df1 = df[df['sheet'].str.contains(segment)]

    # checking for LOH - Lot On Hold 
    '''
    df1 = df[df['LW'] == logweek]
    df2 = df1[df1['ALF_DISPOSITION'] == 'ON-HOLD']'''
    df2 = df1[(df1['LW'] == logweek) & (df1['ALF_DISPOSITION'] == 'ON-HOLD')]

    loh_count = len(df2.index)
    '''
    print('LOH count is ', end='')
    print(loh_count)'''

    # checking for TTL - Total Lot Count 
    #df3 = df1[df1['ALF_DISPOSITION'] == 'AUTO RELEASE']
    df3 = df1[(df1['LW'] == logweek) & (df1['ALF_DISPOSITION'] == 'AUTO RELEASE')]

    ttl_count = len(df3.index)
    '''
    print('TTL count is ', end='')
    print(ttl_count)'''

    print(f'{segment}\'s stats are {loh_count}, {ttl_count}')

    return loh_count, ttl_count 


def segmentStatCheck(df, logweek, segment_tuple=None):
    '''
    takes in the following parameters:
    df -> DataFrame containing all ASSESSED sheets of the different segments
    logweek -> int representing the logweek we wish to look up
    '''
    '''
    segment_compiled_data = pd.DataFrame()

    for segment in segment_tuple:
        segment_data = statCheck(df, logweek, segment)
        
        # these few lines could be incorrect, need to check on the exact method
        row_index = segment.strip('_') # row index = name of segment 
        segment_compiled_data.append(segment_data)
    '''
    for segment in segment_tuple:
        print(statCheck(df, logweek, segment))
     



#filename = r'C:\Users\MohamadYusuf\Desktop\Haikal\Personal Projects\pob.xlsx'
filename = r"C:\Users\MohamadYusuf\Desktop\Haikal\Personal Projects\CerberusCheck.xlsx"
sheets_dict = pd.read_excel(filename, sheet_name=None)


full_table = pd.DataFrame()

#segment_tuple = ('BATAM POB_ASSESSED', 'MAL DS_ASSESSED', 'MAL PLT_ASSESSED', 'MAL SCC_ASSESSED', 'WUXI DS_ASSESSED', 'SIN TS_ASSESSED', 'WUXI CC_ASSESSED')
segment_tuple = ('BATAM POB', 'MAL DS', 'MAL PLT', 'MAL SCC', 'WUXI DS', 'SIN TS', 'WUXI CC')


# name is a key, sheet is a value (key-value pair)
# name is a String, sheet is a DataFrame 
for name, sheet in sheets_dict.items():
    # taking only the Excel Worksheets containing "ASSESSED" in their names 
    if 'ASSESSED' in name:
        # this adds another column containing the Worksheet name
        sheet['sheet'] = name.split('_')[0]
        #print('this is: ', name.split('_')[0])
        #sheet = sheet.rename(columns=lambda x: x.split('_')[0]) can't split because of column ALF_DISPOSITION
        full_table = full_table.append(sheet)
    else:
        continue 


full_table.reset_index(inplace=True, drop=True)

'''
pob_stats = statCheck(full_table, 2047, 'BATAM POB')
print(pob_stats) '''

segmentStatCheck(full_table, 2051, segment_tuple)


#print (full_table.shape)
#print (full_table.head())


'''

time is 05:33 for LW2051

'''