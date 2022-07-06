def diskard_duplikates(contacts_list, contacts_list1):
    new_contacts_list = []
    for i in range(0, len(contacts_list)):
        for j in range(0, len(contacts_list1)):
            if(contacts_list[i] != contacts_list1[j] and contacts_list[i][0] == contacts_list1[j][0] and contacts_list[i][1] == contacts_list1[j][1]):
                for g in range(0, len(contacts_list[i])):
                    if (contacts_list[j][g] > contacts_list[i][g]):
                        contacts_list[i][g] = contacts_list[j][g]
                if(contacts_list[i] not in new_contacts_list):
                    new_contacts_list.append(contacts_list[i])
            if (contacts_list[i] not in new_contacts_list):
                new_contacts_list.append(contacts_list[i])

    for el in new_contacts_list:
        if new_contacts_list.count(el) > 1:
            new_contacts_list.remove(el)
    return new_contacts_list
