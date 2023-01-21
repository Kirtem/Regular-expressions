import re
from pprint import pprint
import csv

pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
phone_number = r'+7(\2)-\3-\4-\5 \6\7'

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

#TODO 1: выполните пункты 1-3 ДЗ
def phone_book (contact_list: list):
    new_list = list()
    for item in contact_list:
        full_name = ' '.join(item[:3]).split(' ')
        result = [full_name[0], full_name[1], full_name[2], item[3], item[4],
                  re.sub(pattern, phone_number, item[5]),
                  item[6]]
        new_list.append(result)
    return unification(new_list)

def unification(contacts: list):
    for contact in contacts:
        name = contact[:2]
        for new_contact in contacts:
            new_name = new_contact[:2]
            if name == new_name:
                if contact[2] == "":
                    contact[2] = new_contact[2]
                if contact[3] == "":
                    contact[3] = new_contact[3]
                if contact[4] == "":
                    contact[4] = new_contact[4]
                if contact[5] == "":
                    contact[5] = new_contact[5]
                if contact[6] == "":
                    contact[6] = new_contact[6]
    result_list = list()
    for i in contacts:
        if i not in result_list:
            result_list.append(i)
    return result_list

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(phone_book(contacts_list))