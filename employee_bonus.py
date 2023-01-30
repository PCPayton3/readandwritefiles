import csv
infile = open('EmployeePay.csv', 'r')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)
for record in csvfile:
    print(record)
    print('ID:', record[0])
    print('first name:', record[1])
    print('last name:', record[2])
    print('salary:', record[3])
    print('bonus:', record[4])
