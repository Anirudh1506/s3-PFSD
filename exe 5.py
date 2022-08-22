import csv
with open("employee.csv","w") as csv_write:
    types=["name","id","age"]
    csv_write = csv.DictWriter(csv_write,fieldnames=types,delimiter=',')
    line1=["ani","31630",25]
with open("employee.csv","r") as csv_read:
    csv_read=csv.DictReader(csv_read,delimiter=',')
    for i in csv_read:
        print(i)

