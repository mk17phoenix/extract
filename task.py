import docx2txt
import re

my_text=docx2txt.process("iob.docx")

Name=re.findall("[\w]{1,4}\s:\s[\w]{1}\s[\w]{1,5}\s[\w]{1,7}",my_text)

Address=re.findall("[\w]{1,8}\s:\s\s[\w]{1,5}\s[\w]{1,2}/[\d]\s[\w]{1,15}\s[\w]{1,2}\s[\w]{1,15}\s[\w]{1,15}\s[\w]{1,20}",my_text)

Email=re.findall("[\w]{1,7}\s[\w]{1,3}\s:\s\S+@\S+",my_text)

Phone=re.findall("\w{1,7}\s\w{1,3}\s:\s\d{10}",my_text)

for i in Name:
    print(i)
    
for i in Address:
    print(i)

for i in Email:
    print(i)

for item in Phone:
    print(item)

