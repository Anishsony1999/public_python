
# open(path/ of/ your/ file)
# r,w,a ->rb,wb
# close()

file = open('OOPs.py','r')

content = file.read() # reading file
content = file.readline() # a single line
content = file.readlines() # all content in a list

file.close()

file = open('text.txt','a')
file.write("Hello Anish")
file.close()

with open('text.txt','r') as file :
    content = file.read()
    print(content)

try :

    with open('C:/Downloaded Web Sites1/metropolitanhost.com/themes/themeforest/html/maharatri/assets/img/flag.png','rb') as file :
        data = file.read()

    with open('copyimg.jpg','wb') as file:
        file.write(data)
    
except FileNotFoundError:
    pass
except PermissionError:
    pass
except Exception as e:
    pass

import csv

with open('data.csv',newline='') as file:
    reading = csv.reader(file)

    for row in reading :
        print(row)

with open('output.csv','w',newline='') as csvf :
    writer = csv.writer(csvf)
    writer.writerow(['Name','Age','City'])
    writer.writerow(['Alice',25,'New York'])

import os

if os.path.exists("output.csv") :
    print("File is avialble")
else:
    print("File nnot fount")
    