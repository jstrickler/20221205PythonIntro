import csv

with open('/users/jstrick/curr/courses/python/common/DATA/presidents.csv') as pres_in:
    rdr = csv.reader(pres_in)
    for row in rdr:
        print(row)

