import csv
with open("arya.csv",mode="r")as file:
    reader1=csv.reader(file)
    for row in reader1:
        print(row)

