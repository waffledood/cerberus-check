# cerberus-check
Weekly Cerberus check done as part of my routine tasks during my internship

The weekly Cerberus check is done to ensure the data sanity of our productive datasets. The datasets obtained from the Cerberus application were checked against our productive datasets that were generated through automated Excel VBA & Python scripts. The productive dataset is then used to construct department-critical Tableau charts used by other employees in our cluster.

The cleaned data from Cerberus is checked against our Tableau charts for values of "Sum LOH" & "Total Lot Count". Manually checking the Tableau charts is time-consuming, especially with the slow load-times of the charts caused by the large dataset we have, and thus I developed this Python script that will access the underlying database of the Tableau charts to extract & tabulate the values of "Sum LOH" & "Total Lot Count".

The Python script itself takes a while to read the Excel sheet because of the huge size (~250MB) but this script can be automated & thus done in parallel to querying the dataset from Cerberus.


Future areas of improvement:
1. ~~Filtering out the data in the pre-processing stage to reduce the size of the dataset (perhaps filtering out LW's before 2010). This would require separate VBA / Python scripts.~~
2. ~~Converting the Excel worksheet to CSV format, to improve the time the Python script takes to read.~~
3. Extra filters for DS MAL & SIN TS segments


Decided course of action:
1. Extract each DDM_FINAL Worksheet from each Segment's Masterfile Workbook as a CSV file (csv_export.vb).
2. Calculate the LOH & TTL count from each Segment's CSV file (cerberus_v2.py).

Notes:
- cerberusCheck.py developed to **filter the data extracted from Cerberus**
- 
