import re
import csv

with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    contacts_list1 = []
def get_names():
    pattern1 = r'([А-Я])'
    sub1 = r' \1'
    for column in contacts_list[1:]:
        line = column[0] + column[1] + column[2]
        if len((re.sub(pattern1, sub1, line).split())) == 3:
            column[0] = re.sub(pattern1, sub1, line).split()[0]
            column[1] = re.sub(pattern1, sub1, line).split()[1]
            column[2] = re.sub(pattern1, sub1, line).split()[2]
        elif len((re.sub(pattern1, sub1, line).split())) == 2:
            column[0] = re.sub(pattern1, sub1, line).split()[0]
            column[1] = re.sub(pattern1, sub1, line).split()[1]
            column[2] = ''
        elif len((re.sub(pattern1, sub1, line).split())) == 1:
            column[0] = re.sub(pattern1, sub1, line).split()[0]
            column[1] = ''
            column[2] = ''
    return

def phone_change():
    pattern2 = re.compile(
        '(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    sub2 = r'+7(\2)\3-\4-\5\7\8\9'
    for column in contacts_list:
        column[5] = pattern2.sub(sub2, column[5])
    return
def doubles_unification():
    for column in contacts_list[1:]:
        first_name = column[0]
        last_name = column[1]
        for contact in contacts_list:
            new_first_name = contact[0]
            new_last_name = contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if column[1] == '':
                    column[1] = contact[1]
                if column[2] == '':
                    column[2] = contact[2]
                if column[3] == '':
                    column[3] = contact[3]
                if column[4] == '':
                    column[4] = contact[4]
                if column[5] == '':
                    column[5] = contact[5]
                if column[6] == '':
                    column[6] = contact[6]

    for contact in contacts_list:
        if contact not in contacts_list1:
            contacts_list1.append(contact)
    return contacts_list1


if __name__ == '__main__':
    get_names()
    phone_change()
    doubles_unification()

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list1)