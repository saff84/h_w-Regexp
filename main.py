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
# for el in contacts_list:
#     if (len(el[0].split(' ')) == 2):
#         # print(el[0])
#         a = el[0].split(' ')
#         # print(a)
#         el[0] = a[0]
#         el[1] = a[1]
#         # print(el)
#     elif (len(el[0].split(' ')) == 3):
#         # print(el[0])
#         a = el[0].split(' ')
#         # print(a)
#         el[0] = a[0]
#         el[1] = a[1]
#         el[2] = a[2]




# for el in contacts_list:
#     if (el[5] != 'phone' or el[5] != ''):
#         # print(el[5])
#         pattern = r"(\+7|8)\s?\(?(\d{3})[\)-]?\s?(\d{3})?[\s-]*(\d{2})[\s-]?(\d{2})(\s?\(?(\w{3}\.)\s?(\d{4})\)?)?"
#         result = re.sub(pattern, r"+7(\2)\3-\4-\5 \7\8", el[5])
#         el[5] = result




# for i in range(0, len(contacts_list)):
#     for j in range(0, len(contacts_list1)):
#         if(contacts_list[i] != contacts_list1[j] and contacts_list[i][0] == contacts_list1[j][0] and contacts_list[i][1] == contacts_list1[j][1]):
#             for g in range(0, len(contacts_list[i])):
#                 if (contacts_list[j][g] > contacts_list[i][g]):
#                     contacts_list[i][g] = contacts_list[j][g]
#             if(contacts_list[i] not in new_contacts_list):
#                 new_contacts_list.append(contacts_list[i])
#         if (contacts_list[i] not in new_contacts_list):
#             new_contacts_list.append(contacts_list[i])
#
#
#
#
# for el in new_contacts_list:
#     if new_contacts_list.count(el) > 1:
#         new_contacts_list.remove(el)

# pprint(new_contacts_list)

# код для записи файла в формате CSV
with open("phonebook.csv", "w",encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_contacts_list)
