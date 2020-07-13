import csv  # import the `csv` library
import os


income_fsa = open(os.path.join(os.getcwd(), "98-400-X2016008_English_CSV_data.csv"), 'r')
# this tells python to open the file

income_fsa_dictionary_reader = csv.DictReader(income_fsa)
# pass the file into `DictReader`

FSA = next(income_fsa_dictionary_reader)   # get the next row
print(FSA)