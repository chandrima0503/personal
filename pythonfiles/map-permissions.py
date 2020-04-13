from bs4 import BeautifulSoup
import os
import csv
import sys
Dict = {}
user_path = "C:\Users\Chandrima.Mukherjee\documentation"
print(user_path)
for lists in os.listdir(user_path):
    path='{}\{}'.format(user_path,lists)
    if os.path.isdir(path):
        for files in os.listdir(path):     
            new_path =  os.path.join(path,files)
            # st = os.stat(new_path)
            # print( bool(st.st_mode & stat.S_IRGRP))
            if(files.endswith('.ditamap')):
                print(new_path)
                ret = os.access(path, os.X_OK)
                if(ret == True):
                    infile = open(new_path,'r')
                    contents = infile.read()
                    soup = BeautifulSoup(contents,'xml')
                    for element in soup.find_all("permissions"):
                        print element['view']
                        Dict[files] = element['view']

print(Dict)
csv_path='{}\{}'.format(user_path,'result.csv')
with open(csv_path, 'wb') as f:
    writer = csv.DictWriter(f, fieldnames=["Filename", "Permissions"])
    writer.writeheader()
    for key in Dict.keys():
        writer.writerows(
        [{"Filename": key, "Permissions": Dict[key]}])
    print("csv created")

