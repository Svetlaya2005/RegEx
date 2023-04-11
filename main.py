import re
import csv
#from pprint import pprint

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

pattern1 = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)'
subst1 = r''
result1 = re.sub(pattern1, subst1, contacts_list)

#result1 = list()
#for i in result1:
  #f = " ".join(i[:2]).split(" ")
  #i[:len(f)] = f
  #print(f)

pattern2 = r'(8|\+7)?\s*\(\d+\)\s*\d+[-\s]*\d+[-\s]*\d+' \
r'\d+[-\s]*(\(*)(доб\.*)[-\s](\d+)*(\)*)'
subst2 = r'8(\2)-\3-\4-\5 \6\7'
result2 = re.sub(pattern2, subst1, contacts_list)
print(result2)

#result2 = list()
#for i in result2:
  #n = " ".join(i[:2]).split(" ")
  #i[:len(n)] = n
  #print(n)