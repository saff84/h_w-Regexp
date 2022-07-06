def make_fio(contacts_list):
    for el in contacts_list:
        if (len(el[0].split(' ')) == 2):
            # print(el[0])
            a = el[0].split(' ')
            # print(a)
            el[0] = a[0]
            el[1] = a[1]
            # print(el)
        elif (len(el[0].split(' ')) == 3):
            # print(el[0])
            a = el[0].split(' ')
            # print(a)
            el[0] = a[0]
            el[1] = a[1]
            el[2] = a[2]
    return contacts_list
