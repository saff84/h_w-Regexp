from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from make_fio import make_fio
from make_tel import make_tel
from diskard_duplicates import diskard_duplikates

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

contacts_list1 = contacts_list
make_fio(contacts_list)
make_tel(contacts_list)
new_contacts_list = diskard_duplikates(contacts_list,contacts_list1)

with open("phonebook.csv", "w",encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_contacts_list)
