
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
    writer.writerow(['Anish',24,'Ind'])

# csv to dict

with open('output.csv',mode='r') as file :

    csv_reader = csv.DictReader(file)

    for row in csv_reader :
        print(row)

# dict to csv

fieldname = ['Name' , 'Age' , 'City']

data = [
    {'Name' : 'Anish','Age':24 , 'City':'IND'},
    {'Name' : 'Anusha','Age':24 , 'City':'USA'},
    {'Name' : 'ABI','Age':24 , 'City':'UK'}
]

with open('output2.csv',mode='w',newline='') as file :

    csv_writer = csv.DictWriter(file,fieldname,)
    csv_writer.writeheader()
    csv_writer.writerows(data)

