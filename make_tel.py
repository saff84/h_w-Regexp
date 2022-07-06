import re
def make_tel(contacts_list):
    for el in contacts_list:
        if (el[5] != 'phone' or el[5] != ''):
            # print(el[5])
            pattern = r"(\+7|8)\s?\(?(\d{3})[\)-]?\s?(\d{3})?[\s-]*(\d{2})[\s-]?(\d{2})(\s?\(?(\w{3}\.)\s?(\d{4})\)?)?"
            result = re.sub(pattern, r"+7(\2)\3-\4-\5 \7\8", el[5])
            el[5] = result
    return contacts_list
