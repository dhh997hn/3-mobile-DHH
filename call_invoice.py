import csv
data_f = 'data.csv'
def input_data(phone_number):
    fiels = []
    rows = []

    with open(data_f,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fiels = csvreader.__next__()
        for row in csvreader:
            rows.append(row)
       
    index1 = fiels.index('msisdn_origin')
    index2 = fiels.index('msisdn_dest')
    res = []
    for row in rows:
        if (row[index1] == phone_number) or (row[index2] == phone_number):
            res.append(row)
            
    return fiels,res