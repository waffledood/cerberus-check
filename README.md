# cerberus-check
Weekly Cerberus check done as part of my routine tasks during my internship

The weekly Cerberus check is done to ensure the data sanity of our productive datasets. The datasets obtained from the Cerberus application were checked against our productive datasets that were generated through automated Excel VBA & Python scripts. The productive dataset is then used to construct department-critical Tableau charts used by other employees in our cluster.

The cleaned data from Cerberus is checked against our Tableau charts for values of "Sum LOH" (LOH) & "Total Lot Count" (TTL). Manually checking the Tableau charts is time-consuming, especially with the slow load-times of the charts caused by the large dataset we have, and thus I developed this Python script that will access the underlying database of the Tableau charts to extract & tabulate the values of "Sum LOH" & "Total Lot Count".

The Python script itself takes a while to read the Excel sheet because of the huge size (~250MB) but this script can be automated & thus done in parallel to querying the dataset from Cerberus.

Process:

1. Data extracted from Cerberus is manually filtered (Owner, then Hold Comments). The data for LOH & TTL lots for each segment are separated into individual Excel Worksheets. So 2 (LOH, TTL) x 7 (segments) = 14 worksheets. The count of LOH & TTL lots (number of rows) is then extracted from each worksheet.
- cerberusCheck.py

2. Count for LOH & TTL lots is extracted from the underlying database of the Tableau charts.
- csv_export.vb (consists of cerberusv4 sub & POB_CSV2 sub)
- cerberus_v2.py

3. Comparison is made between the values of "Sum LOH" & "Total Lot Count" to check the data sanity. 
* Compare the LOH, TTL & LRR% values for each segment & correspondingly generate a report if the LRR% are within an acceptable range
- cerberus_report.py
