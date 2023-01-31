import csv


def main():
    infile = open('sales.csv', 'r', newline='')
    reader = csv.reader(infile)
    next(reader)
    outfile = open('salesreport.csv', 'w', newline='')

    writer = csv.writer(outfile)
    writer.writerow(["Customer ID, Total"])

    customer = ""
    count = 0
    total = 0

    for record in reader:
        if count == 0:
            customer = record[0]
        if record[0] == customer:
            total += float(record[3]) - (float(record[4]) + float(record[5]))

        else:
            writer.writerow([customer, format(total, '.2f')])
            total = float(record[3]) - (float(record[4]) + float(record[5]))
        customer = record[0]
        count += 1

    writer.writerow([customer,  format(total, '.2f')])

    infile.close()
    outfile.close()


main()
