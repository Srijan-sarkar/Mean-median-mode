import csv
with open('C:/Users/Asus/Desktop/whj/project 104/HW.csv',newline='' ) as f:
    reader = csv.reader(f)
    file_data = list(reader)    

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

n = len(new_data)
total =0

for x in new_data:
    total= total+x

mean = total/n

print("mean = " + str(mean))