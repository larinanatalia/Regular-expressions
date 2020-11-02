from pprint import pprint
import csv
import re


def open_file(file_name):
  with open(f'{file_name}.csv',encoding="utf-8" ) as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
  return contacts_list


def format_name(contacts_list):
  for contact in contacts_list:
    contact[0] = f'{contact[0]} {contact[1]} {contact[2]}'
    full_name = contact[0].split(' ')
    contact[0] = full_name[0]
    contact[1] = full_name[1]
    contact[2] = full_name[2]
    try:
      contact.pop(7)
    except:
      pass
  return contacts_list

def del_doublet(contacts_list):
  for contact in contacts_list:
    for contact_2 in contacts_list:
      if contact[0] == contact_2[0] and contact[1] == contact_2[1] and contact is not contact_2:
        if contact[2] == '':
          contact[2] = contact_2[2]
        if contact[3] == '':
          contact[3] = contact_2[3]
        if contact[4] == '':
          contact[4] = contact_2[4]
        if contact[5] == '':
          contact[5] = contact_2[5]
        if contact[6] == '':
          contact[6] = contact_2[6]
  contacts_list_update = list()
  for contact in contacts_list:
    if contact not in contacts_list_update:
      contacts_list_update.append(contact)
  return  contacts_list_update

def phone_number(contacts_list):
  for contact in contacts_list:
    if len(contact[5]) <= 12:
      pattern = re.compile(r'(\+7|8)(\d{3})(\d{3})(\d{2})(\d{2})')
      contact[5] = pattern.sub(r'+7(\2)\3-\4-\5 ', contact[5])
    else:
      pattern = re.compile(r'(\+7|8)[\s|\(]?\(?(\d*)[-|\)]\s?(\d*)[-](\d{2,2})[-]?(\d*)\s?\(?([а-яё]*\.?)\s?(\d*)\)?')
      contact[5] = pattern.sub(r'+7(\2)\3-\4-\5 \6\7',contact[5])
  return contacts_list

def write_new_csv(file_name, contacts_list):
  with open(f"{file_name}.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)

if __name__ == '__main__':
  contacts_update = open_file('phonebook_raw')
  contacts_update = format_name(contacts_update)
  contacts_update = del_doublet(contacts_update)
  contacts_update = phone_number(contacts_update)
  write_new_csv('phonebook', contacts_update)
  pprint(contacts_update)
