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

logweek = input("Which logweek do you want to query? ")
logweek = int(logweek)

tableau_data = cerberus_v2.tabulate(logweek)
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
        lrr_diff_list_full.append([new_segment, lrr_diff, cerb, tab])
        print(s)
        #print("lrr diff list is:", lrr_diff_list)
        #print("lrr diff list (full) is:", lrr_diff_list_full)

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
    report += f"\n\n\n{segment[0]}\'s difference is {segment[1]}% \n\n" 

    segment_name = segment[0]

    segment_cerb_stats = segment[2]
    segment_cerb_loh = segment_cerb_stats[1]
    segment_cerb_ttl = segment_cerb_stats[2]
    segment_cerb_lrr = round(segment_cerb_stats[3] * 100, 2)

    segment_tab_stats = segment[3]
    segment_tab_loh = segment_tab_stats[1]
    segment_tab_ttl = segment_tab_stats[2]
    segment_tab_lrr = round(segment_tab_stats[3] * 100, 2)
    
    report += f"{segment_name} \nCerberus vs Tableau \nLOH {segment_cerb_loh} vs {segment_tab_loh} \nTTL {segment_cerb_ttl} vs {segment_tab_ttl} \nLRR% {segment_cerb_lrr} vs {segment_tab_lrr}"

print(report)


'''
Section 3: File Creation
'''

name = "WCC (KT Report) - " + str(logweek)
filename = "%s.txt" % name

# might need to change dir with os.dir (can't remember exact name)

'''
with open("WCC (KT Report) - " + str(logweek) + ".txt", "w") as file:
    file.write(report) 

with open('WCC (KT Report) - LW{0}.txt'.format(str(logweek)),'w') as f:
    f.write(report) '''

with open('C:\\Users\\MohamadYusuf\\Desktop\\Haikal\\Personal Projects\\cerberus-check\\WCC (KT Report) - LW%s.txt' % (str(logweek),), 'w') as f:    
    f.write(report)

'''
references:
- https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row


'''




'''
Section 2:

this section looks into creating new files with dynamic names, where each file's name includes the past 
LogWeek's value, e.g. LW2104. So file names should look like "KT Report LW2104.txt"

generic website: https://www.guru99.com/reading-and-writing-files-in-python.html
detailed answer on StackOverflow (not quite the answer i was looking for): https://stackoverflow.com/questions/47147653/write-to-files-with-dynamic-file-names
the accurate answer i was looking for! https://www.kite.com/python/answers/how-to-create-a-filename-using-variables-in-python


'''



'''
Section 1:

this section was an experiment to have Python automatically find the latest Excel file in Weekly LRR Reports & then read it.
this could carry over to cerberus_v2.py where the user would not need to key in the latest LogWeek, instead the Python module
reads the path of the latest file, splits the path & extracts the LogWeek value

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