# cerberus-check
Weekly Cerberus check done as part of my routine tasks during my internship

The weekly Cerberus check is done to ensure the data sanity of our productive datasets. The datasets obtained from the Cerberus application were checked against our productive datasets that were generated through automated Excel VBA & Python scripts. The productive dataset is then used to construct department-critical Tableau charts used by other employees in our cluster.

The cleaned data from Cerberus is then checked against our Tableau charts for values of "Sum LOH" & "Total Lot Count". Manually checking the Tableau charts is time-consuming, especially with the slow load-times of the charts caused by the large dataset we have, and thus I developed this Python script that will access the underlying database of the Tableau charts to extract the values of "Sum LOH" & "Total Lot Count".

The Python script itself takes a while to read the Excel sheet because of the huge size (~250MB) but this script can be automated & thus done in parallel to querying the dataset from Cerberus.

