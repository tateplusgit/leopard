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


    def count_instances(Gender, Female):
        d = {}
        with open('C:\py\diabetes_data.csv', 'r', encoding='utf-8', newline='') as f:
            dialect = csv.Sniffer().sniff(f.read(1000))
            #print(dialect)


            #Move to the beginning of the file headers
            f.seek(0)

            r = csv.DictReader(f, dialect=dialect)

            for row in r:
                if  row['Gender'] == 'Female':
                    d[row['Gender']] = d.get(row['Gender'], 0) + 1
        for k in d:
           print ('{} {}'.format(k, d[k]))






    #1
    try:
        csvfile = open("C:\py\diabetes_data.csv")
    except IOError:
        print("File not found!")
    else:
        __init__('self', csvfile)



    #2
    csvfile = open("C:\py\diabetes_data.csv")
    get_header('self', csvfile)
    csvfile.close()


    #3
    csvfile = open("C:\py\diabetes_data.csv")
    #get_dimension()


    #4
    csvfile = open("C:\py\diabetes_data.csv")
    count_instances('Gender', 'male')


#ZeroDivisionError raised when you divide a number by zero
#ImportError raised when you try to import a library that is not installed
#IndexError raised when an index is not found
#Exception base class for all exceptions. So if you are not sure which type of exception that will occur, use this.



