import csv
import math

with open("std_deviation.csv",newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n
    return mean

file_list = []

for number in data:
    a = int(number)-mean(data)
    a = a**2
    file_list.append(a)
sum =  0

for i in file_list:
    sum = sum+1
result = sum/(len(data)-1)

Standard = math.sqrt(result)

print(Standard)