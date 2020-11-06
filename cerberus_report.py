import pandas as pd 
import numpy as np 

#from . import cerberus_v2 
#from . import cerberusCheck
# apparently the above 2 methods don't work... it worked when used in the CS50 projects (recall from . import views)

import cerberus_v2
import cerberusCheck
import os

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

        Flow:

        csv_export.vb (which consists of cerberus4 sub & POB_CSV2 sub)
            |
            V
        cerberus_v2.py
            |
            V
        cerberusCheck.py
            |
            V
        cerberus_report.py
'''


'''
docstring

'''

# interesting observation, the import cerberus_v2 statement above causes the tabulate() function to run
tableau_data = cerberus_v2.tabulate()
cerberus_data = cerberusCheck.tabulate()

#print( tableau_data )
#print( cerberus_data )

segment_range = {'DSMAL': [2,3],
                 'TS': [0.50, 1],
                 'Others': [0, 1]
                }

# each of the variables above hold a list of lists. each list item is as follows:
#   segment_tuple, segment_loh, segment_ttl, segment_LRR
#   name, LOH, TTL, LRR

lrr_diff_list = []
lrr_diff_list_full = []

for i, cerb in enumerate(cerberus_data):
    tab = tableau_data[i]
    #print("tab is", tab)

    tab_name = tab[0]
    cerb_name = cerb[0]

    tab_LRR = tab[-1]
    #tab_LRR = tableau_data[i][-1]
    cerb_LRR = cerb[-1]

    new_segment = ""
    old_segment = ""

    #lrr_diff = abs(tab_LRR - cerb_LRR)
    lrr_diff = round(abs(tab_LRR - cerb_LRR) * 100, 5)

    if cerb_name == "DSMAL":
        # new_segment = cerb_name if lrr_diff < 2 or lrr_diff > 3 else new_segment
        # we still need to report on the value of DSMAL, so the assignment of new_segment still needs to be done regardless
        new_segment = cerb_name
    elif cerb_name == "TS":
        new_segment = cerb_name if lrr_diff < 0.50 or lrr_diff > 1 else new_segment
    else:
        new_segment = cerb_name if lrr_diff > 1 else new_segment

    if old_segment != new_segment:
        lrr_diff_str = '\x1b[0;30;41m' + str(lrr_diff) + '\x1b[0m'
        s = f"{new_segment}\'s values are outside of the acceptable range, {lrr_diff_str}%"
        old_segment = new_segment
        lrr_diff_list.append(new_segment)
        lrr_diff_list_full.append([new_segment, lrr_diff])
        print(s)
        print("lrr diff list is:", lrr_diff_list)

'''
if not lrr_diff_list:
    error_segments = " except for " + ", ".join(lrr_diff_list)
    report = f"Good morning KT, just finished the Weekly Cerberus Check & here are the findings.\nAll segments' LRR% are within the acceptable range{error_segments}."
    print(report)
else:
'''

error_segments = " except for " + ", ".join(lrr_diff_list)
report = f"Good morning KT, just finished the Weekly Cerberus Check & here are the findings.\n\nAll segments' LRR% are within the acceptable range{error_segments}."

#for segment in lrr_diff_list:
for segment in lrr_diff_list_full:
    report += f"\n\n{segment[0]}\'s difference is {segment[1]}% \n\n" 
    #report += f"{segment} \n Cerberus vs Tableau \n LOH {} vs {} \n TTL {} vs {} \n LRR% {} vs {}"

print(report)


























'''
this section was an experiment to have Python automatically find the latest Excel file in Weekly LRR Reports & then read it
this could carry over to cerberus_v2.py where the user would not need to key in the latest LogWeek, instead the Python module
reads the path of the latest file, splits it & extracts the LogWeek value

def latestFile(path):
    # 2nd answer in 
    # https://stackoverflow.com/questions/39327032/how-to-get-the-latest-file-in-a-folder-using-python
    # might also be useful: https://realpython.com/working-with-files-in-python/
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)

# latest Cerberus report  

path = r'Z:\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly LRR Reports'
#path = repr(path)
filename = latestFile(path)

print(filename)
print("the type of this file is", type(filename))

df = pd.read_excel(io=filename, sheet_name=None)
#print (df)
'''