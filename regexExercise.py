import re, pyperclip
phoneregex = re.compile(r"(\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*\d{2,5})?")
emailregex = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}")
text = str(pyperclip.paste())
matches = []
for groups in phoneregex.findall(text):
    phonenumber = groups[0] + "-" + groups[2] + "-" + groups[4]
    if groups[5] != "":
        phonenumber += " ext" + groups[5]
    matches = matches + [phonenumber]
for groups in emailregex.findall(text):
    matches = matches + [groups]
if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard:")
    print("\n".join(matches))
else:
    print("No phone numbers or email adresses found")