import csv

dataFile = 'inputdata.txt'

def input_data(ip_number):
    fiels = []
    rows = []
    with open(dataFile,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fiels = csvreader.__next__()
        for row in csvreader:
            rows.append(row)
    res = []
    for row in rows:
        string = row[0].split()[0]
        if string == ip_number:
            res.append(row)
    return fiels,res