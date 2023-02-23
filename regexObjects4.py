import re
regexobj = re.compile(r"Batman|Robin")
mo1 = regexobj.search("Batman and Robin")
print(mo1.group())
mo2 = regexobj.search("Robin plus Batman")
print(mo2.group())