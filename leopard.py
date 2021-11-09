import csv

class Leopard(object):

    def __init__(self, csvfile):
        c1 = []
        c2 = []

        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            c1.append(row[0])
            c2.append(row[1])

    def get_header(self, csvfile):

        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        print(header)

    def get_dimension(self):
        print("Pending")


    def count_instances(Gender, Female):
        print("Pending")



    def total_missing(self, csvfile):
        rows = 0
        missing = 0

        for record in csvfile:
            if record.count('NA') > 0:
                rows += 1
                missing += record.count('NA')
        print('{# of rows with missing value: %d }' % (rows))






    #1
    try:
        csvfile = open("/Users/James/PycharmProjects/nky/diabetes_data.csv")
    except IOError:
        print("File not found!")
    else:
        __init__('self', csvfile)



    #2
    #csvfile = open("C:\py\diabetes_data.csv")
    #get_header('self', csvfile)
    #csvfile.close()


    #3
    #csvfile = open("C:\py\diabetes_data.csv")
    #get_dimension()


    #4
    #csvfile = open("C:\py\diabetes_data.csv")
    #count_instances('Gender', 'male')
    #with open('Sparta/Users/James/PycharmProjects/nky/diabetes_data.csv', 'r', encoding='utf-8', newline='') as f:
    #count_instances('Gender', 'male')


    #5
    csvfile = open("/Users/James/PycharmProjects/nky/diabetes_data.csv")
    total_missing('self', csvfile)
    csvfile.close()

#ZeroDivisionError raised when you divide a number by zero
#ImportError raised when you try to import a library that is not installed
#IndexError raised when an index is not found
#Exception base class for all exceptions. So if you are not sure which type of exception that will occur, use this.



