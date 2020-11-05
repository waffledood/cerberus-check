import pandas as pd 
import numpy as np 

#from . import cerberus_v2 
#from . import cerberusCheck
# apparently the above 2 methods don't work... it worked when used in the CS50 projects (recall from . import views)
import cerberus_v2
import cerberusCheck

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

cerberus_v2.tabulate()
cerberusCheck.tabulate()


