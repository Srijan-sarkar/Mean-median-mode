import csv
with open('C:/Users/Asus/Desktop/whj/project 104/HW.csv',newline='' ) as f:
    reader = csv.reader(f)
    file_data = list(reader)    

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

new_data.sort()
n = len(new_data)

if n%2 == 0:
    median1= new_data[n//2]
    median2= new_data[n//2-1]
    median = (median1+median2)/2

else:
    median= new_data[n+1/2]

print(median)