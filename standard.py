import statistics 
import csv
#introduction
with open ("data.csv") as f:
    read1 = csv.reader(f)
    data = list(read1)

data2 = [60,61,65,63,98,99,90,95,91,96]

standard = statistics.stdev(data2)
print(standard)