
from genericpath import exists
from pathlib import Path
from Create_CSV import creating
from Write_File import writing_scv
from Write_File import writing_txt


Path = 'Phonebook.csv'
valid = exists(Path)
if not valid:
    creating()

writing_scv()
writing_txt()