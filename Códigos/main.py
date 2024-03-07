# Convert csv to json
# Manage ebooks pdf library
import csv
import json
def csv2json( filename ):
    data = ''

    with open(filename, 'r' ) as fl:
        data = fl.read()

    
    return data

