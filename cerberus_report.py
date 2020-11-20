import pandas as pd 
import numpy as np 
import cerberus_v2
import cerberusCheck
import os
import time 

#from . import cerberus_v2 
#from . import cerberusCheck
# apparently the above 2 methods don't work... it worked when used in the CS50 projects (recall from . import views)
# interesting observation, the import cerberus_v2 statement above causes the tabulate() function to run


'''
docstring
function: this module generates a report if any segment's LRR lie outside of the range of error

'''


def cerberusTransfer():
    '''
    Run the CerberusTransfer.xlsm first to extract the DDM_FINAL of each segment's Masterfile.xlsx as a CSV file

    Parameters:
        None

    Returns:
        None
    '''
    ebs = os.path.getmtime(r'\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly Cerberus Check (Automated)\BATAM POB.csv')

    #Run the macro
    #os.startfile(r'C:\Users\MohamadYusuf\Desktop\Haikal\Personal Projects\cerberus-check\CerberusTransfer.xlsm')
    os.startfile(r"\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly Cerberus Check (Automated)\CerberusTransfer.xlsm")

    #Holding loop to ensure that the macro completes before moving on to prevent the macros from overlapping
    while ebs == os.path.getmtime(r'\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly Cerberus Check (Automated)\BATAM POB.csv'):
        #Recheck condition every 5 seconds
        print("sleeping")
        time.sleep(5)
    time.sleep(30)


'''
Section 2:
    this section was an experiment to have Python automatically find the latest Excel file in Weekly LRR Reports & then read it.
    this could carry over to cerberus_v2.py where the user would not need to key in the latest LogWeek, instead the Python module
    reads the path of the latest file, splits the path & extracts the LogWeek value
'''

def latestFile(path):
    '''
    Returns the latest file created in a folder.

    Parameters:
        path (str): The path of the folder we want to find the latest file created

    Returns:
        max(paths): The latest file created
    '''
    # 2nd answer in 
    # https://stackoverflow.com/questions/39327032/how-to-get-the-latest-file-in-a-folder-using-python
    # might also be useful: https://realpython.com/working-with-files-in-python/
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    # adding an if condition to the list comprehension such that it checks for files that are of a certain extension type, 
    # #@David Of course. Just insert if basename.endswith('.csv') into the list comprehension
    return max(paths, key=os.path.getctime)


def find_file(path, logweek):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]

    for item in paths:
        if str(logweek) in item:
            return item 
    
    return "" 

def report_generator(logweek, filename):
    '''
    Runs the modules that extract the LOH, TTL & LRR values from the Cerberus & Tableau dataset.
    A comparison is then done between the LRR values of each segment & if they are outside the allowed range of error, a 
    report is generated containing further details of the correspondong segments.

    Parameters:
        logweek (int): The previous LogWeek to be queried
        filename (str): The path of the latest Cerberus Report Excel file

    Returns:
        report (str): The contents of the report
    '''

    tableau_data = cerberus_v2.tabulate(logweek)
    cerberus_data = cerberusCheck.tabulate(filename)

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

        tab_name = tab[0]
        cerb_name = cerb[0]

        tab_LRR = tab[-1]
        cerb_LRR = cerb[-1]

        new_segment = ""
        old_segment = ""

        lrr_diff = round(abs(tab_LRR - cerb_LRR) * 100, 5)

        if cerb_name == "DSMAL":
            # new_segment = cerb_name if lrr_diff < 2 or lrr_diff > 3 else new_segment
            # we still need to report on the value of DSMAL, so the assignment of new_segment still needs to be done regardless
            new_segment = cerb_name
        elif cerb_name == "TS":
            # we do not need to report on TS because the Ceberus data accounts for both "YES" & "NO" values for 100% Hold while Tableau data only accounts for "NO"
            # & there isn't a way to filter out the lots with "NO" for 100% Hold
            #new_segment = cerb_name if lrr_diff < 0.50 or lrr_diff > 1 else new_segment
            pass
        else:
            new_segment = cerb_name if lrr_diff > 1 else new_segment

        if old_segment != new_segment:
            lrr_diff_str = '\x1b[0;30;41m' + str(lrr_diff) + '\x1b[0m'
            new_segment = '\x1b[6;30;42m' + new_segment + '\x1b[0m'
            s = f"{new_segment}\'s values are outside of the acceptable range, {lrr_diff_str}%"
            old_segment = new_segment
            lrr_diff_list.append(new_segment)
            lrr_diff_list_full.append([new_segment, lrr_diff, cerb, tab])
            print(s)

    error_segments = " except for " + ", ".join(lrr_diff_list)
    report = f"Good morning KT, just finished the Weekly Cerberus Check & here are the findings.\n\nAll segments' LRR% are within the acceptable range{error_segments}."

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
    
    return report



def copy_files(report, logweek):
    '''
    Saves the Cerberus Report as a txt file to my network drive folder as well as other relevatnt folders

    Parameters:
        report (str): The report
        logweek (int): The LogWeek the report was done for
    
    Returns:
        None

    References:
        generic website: https://www.guru99.com/reading-and-writing-files-in-python.html
        detailed answer on StackOverflow (not quite the answer i was looking for): https://stackoverflow.com/questions/47147653/write-to-files-with-dynamic-file-names
        the accurate answer i was looking for! https://www.kite.com/python/answers/how-to-create-a-filename-using-variables-in-python
        https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row

    '''

    # saves the report as a txt file to my network drive folder
    #with open('C:\\Users\\MohamadYusuf\\Desktop\\Haikal\\Personal Projects\\cerberus-check\\WCC (KT Report) - LW%s.txt' % (str(logweek),), 'w') as f:    
    # had troubles opening the UNC path with open(), refer to https://stackoverflow.com/questions/7169845/using-python-how-can-i-access-a-shared-folder-on-windows-network
    with open('//sinsdn38.ap.infineon.com/BE_CLUSTER_PTE/04_Data_Management/09_Intern_Projects/Haikal Yusuf/Weekly Cerberus Check (Automated)/WCC (KT Report) - LW%s.txt' % (str(logweek),), 'w') as f:
        f.write(report)

    # find the latest Cerberus Report txt file & copy it to the relevant folders
    #path = r"C:\Users\MohamadYusuf\Desktop\Haikal\Personal Projects\cerberus-check"
    path = r"\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly Cerberus Check (Automated)"
    filename_cerb_report = latestFile(path)
    import shutil
    import os 
    shutil.copy(filename_cerb_report, r"\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly Cerberus Check (KT Report)")
    #shutil.copy(filename_cerb_report, r"\\sinsdn38.ap.infineon.com\BE_CLUSTER_PTE\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly LRR Reports")
    # this was commented out because copying the Cerberus Report txt file will cause future runs of this program to fail (w.r.t line 206 where non-excel files can't be added)
    
    # find the latest Cerberus Report LW Compile & copy it to the relevant folders 


''' Main '''
'''
def main(s1):
    # Section 1
    if s1:
        cerberusTransfer()

    # Section 2
    path = r'Z:\04_Data_Management\09_Intern_Projects\Haikal Yusuf\Weekly LRR Reports'
    # possible error in function latestFile is when non-excel files are added into the folder in the path above 
    filename = latestFile(path)
    print(filename)
    st = filename.split("\\")
    logweek = st[-1].split(" ")[0]
    logweek = int( logweek[2:] )
    print('LogWeek value is:', logweek)

    # Section 3
    report = report_generator(logweek, filename)

    # Section 4
    copy_files(report, logweek)

    #exit()

if __name__ == "__main__":
    main(s1=False)
'''
