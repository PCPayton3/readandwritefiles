import csv


def main():
    infile = open('sales.csv', 'r')

    csvfile = csv.reader(infile, delimiter=',')
    next(csvfile)

    with open("salesreport.csv", 'a') as outfile:
        outfile.write('Customer ID, Total\n')
        for record in csvfile:
            CustID = record[0]
            Sales = record[3]
            outfile.write(CustID + ',' + Sales + "\n")


main()
