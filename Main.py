from os.path  
from Create_CSV import creating
from Write_File import writing_scv
from Write_File import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()