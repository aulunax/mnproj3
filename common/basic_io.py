import os
import csv

def read_file(filename):
    data = []
    file_extension = os.path.splitext(filename)[1]
    
    if file_extension == '.csv':
        delim = ','
    elif file_extension == '.txt':
        delim = ' '
    else:
        return data

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=delim)
        for row in reader:
            data.append((float(row[0]), float(row[1])))
    return data
