import csv


def main():
    infile = open('customers.csv', 'r')

    csvfile = csv.reader(infile, delimiter=',')
    next(csvfile)

    with open("customers_country.csv", 'a') as outfile:
        outfile.write('Full Name, Country\n')
        for record in csvfile:
            Fname = record[1] + " " + record[2]
            Country = record[4]
            outfile.write(Fname + ',' + Country + "\n")


main()
