import pandas as pd 
import numpy as np 

'''
Workflow outline of Weekly Cerberus Check

-> This Python program covers points 1, 2 & 3

1) start with data retrieval from Cerberus (for LOH, TTL)
-> can't be automated because there doesn't seem to be an API

2) filtering of dataset as per pre-defined constraints
-> filter by Owner
-> filter by Hold Comments 

3) count of lots in each segment's LOH & TTL
-> total number of rows in each Worksheet 

4) check each segment's LOH/TTL (Cerberus) against LOH/TTL (Tableau/Excel)
'''

filename = r"\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly LRR Reports\LW2103 Compile.xlsx"
'''
logweek = input("Which logweek would you like to query?")
logweek = int(logweek)

filename = f"\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly LRR Reports\LW{logweek} Compile.xlsx"
#filename = repr(filename)
filename = r"{}".format(filename)
'''

sheets_dict = pd.read_excel(filename, sheet_name=None, skiprows=8)


full_table = pd.DataFrame()

segment_tuple = ('BATAM POB', 'MAL DS', 'MAL PLT', 'MAL SCC', 'WUXI DS', 'SIN TS', 'WUXI CC')


# name is a key, sheet is a value (key-value pair)
# name is a String, sheet is a DataFrame 
for name, sheet in sheets_dict.items():
    
    # this adds another column containing the Worksheet name
    sheet['sheet'] = name.split("-")[0].strip() + " " + name.split("-")[1].split(" ")[1].strip()
    #print('this is: ', name.split('_')[0])
    #sheet = sheet.rename(columns=lambda x: x.split('_')[0]) can't split because of column ALF_DISPOSITION
    full_table = full_table.append(sheet)

# filtering of data in LOH, TTL
'''
For 'Hold Comments':
    WUXI DS has no filter applied,
    WUXI CC retains DDM comments, excludes all http comments
'''

dsmal_list = ['1WAVIS','2DVIS','2TPVIS','3BOVIS','INTAPE','MBIN1','MISDEV','N.A.','OUTPAD','PADCOV','PADEDG','PADIMM','PNP','PURGE','TWBOTT','TWTOP','VISION_IN_TAPE']

full_table = full_table[ ['Owner', 'Hold Comments', 'sheet'] ]
# filter for 'Owner' first
full_table = full_table[ full_table['Owner'].isin(['PROD', 'RISK', 'RISM', 'RWIC', 'SFLA']) ]
# filter for 'Hold Comments'
full_table = full_table[ full_table['Hold Comments'].isin(['Configure', 'Lot-Error']) | full_table['Hold Comments'].str.contains('Parameter') 
                         # retains WUXI DS entries
                         | full_table['sheet'].str.contains('WUXI DS') 
                         # retains WUXI CC entries 
                         | ( full_table['sheet'].str.contains('WUXI CC') & full_table['Hold Comments'].str.contains('DDM') ) 
                         # retains DSMAL entries 
                         # TODO
                         #| ( full_table['sheet'].str.contains('DSMAL') & set(full_table['Hold Comments'].str.split(":")[1].split(';')).issubset(dsmal_list) )
                       ]


# counting of LOH & TTL
'''
tuples to store each segment's values: LOH, TTL, LRR
segment_loh = [ dsmal_loh, plt_loh, sens_loh, ts_loh, wuxicc_loh, wuxids_loh, pob_loh ]
segment_ttl = [ dsmal_ttl, plt_ttl, sens_ttl, ts_ttl, wuxicc_ttl, wuxids_ttl, pob_ttl ]
segment_LRR = [ dsmal_LRR, plt_LRR, sens_LRR, ts_LRR, wuxicc_LRR, wuxids_LRR, pob_LRR ]


for loh, ttl, lrr in zip(segment_loh, segment_ttl, segment_LRR):
    # https://www.programiz.com/python-programming/methods/built-in/zip

'''

full_table['new'] = full_table['Hold Comments'].str.split(":")
#full_table['a new'] = full_table[ full_table['new'].map(len) ]
#full_table['a new'] = full_table['new'].apply(lambda x:x[0])

print( full_table.head() )

print( full_table.columns )

print( full_table.shape )

#print( "WUXI DS:", len( full_table[ full_table['sheet'].str.contains('WUXI DS') ].index )  )
print( "WUXI DS LOH:", len( full_table[ full_table['sheet'].str.contains('WUXI DS') & full_table['sheet'].str.contains('LOH') ].index )  )
print( "WUXI DS TTL:", len( full_table[ full_table['sheet'].str.contains('WUXI DS') & full_table['sheet'].str.contains('DWHView') ].index )  )

#print( full_table['Hold Comments'].str )

#print( full_table[ full_table['sheet'].str.contains('WUXI DS') ] )

'''
https://stackoverflow.com/questions/41340341/how-to-determine-the-length-of-lists-in-a-pandas-dataframe-column
https://www.kite.com/python/answers/how-to-filter-a-pandas-dataframe-with-a-list-by-%60in%60-or-%60not-in%60-in-python
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.split.html
https://stackoverflow.com/questions/36108377/how-to-use-the-split-function-on-every-row-in-a-dataframe-in-python
https://www.programiz.com/python-programming/list
https://stackoverflow.com/questions/34468983/how-to-check-if-all-elements-in-a-tuple-or-list-are-in-another
https://stackoverflow.com/questions/8113782/split-string-on-whitespace-in-python
https://pandas.pydata.org/pandas-docs/version/0.23.4/text.html
https://medium.com/swlh/3-ways-to-filter-pandas-dataframe-by-column-values-dfb6609b31de



'''