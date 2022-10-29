


from os.path import exists
from Create_CSV import creating
from Write_File import writing_csv
from Write_File import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_csv()
writing_txt()