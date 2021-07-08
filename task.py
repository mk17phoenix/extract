import docx2txt
import re

my_text=docx2txt.process("iob.docx")

Name=re.compile("[\w]{1,4}\s:\s[\w]{1}\s[\w]{1,5}\s[\w]{1,7}")
a=Name.findall(my_text)

Address=re.compile("[\w]{1,8}\s:\s\s[\w]{1,5}\s[\w]{1,2}/[\d]\s[\w]{1,15}\s[\w]{1,2}\s[\w]{1,15}\s[\w]{1,15}\s[\w]{1,20}")
b=Address.findall(my_text)

Email=re.compile("[\w]{1,5}\s[\w]{1,2}\s:\s[\w]{1,9}@[\w]{1,5}.[\w]{1,3}")
c=Email.findall(my_text)

Phone_no=re.compile("\w{1,7}\s\w{1,3}\s:\s\d{10}")
d=Phone_no.findall(my_text)
for i in a:
    print(i)
for i in b:
    print(i)
for i in c:
    print(i)
for item in d:
    print(item)

