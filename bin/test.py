import os
import pandas as pd 

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

st = filename.split("\\")
ans = st[-1].split(" ")[0]

print(ans)

#df = pd.read_excel(io=filename, sheet_name=None)
#print (df)