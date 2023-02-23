import re
regexobj = re.compile(r"Agent \w+")
subobj = regexobj.sub("CENSORED", "Agent Alice gave the secret documents to Agent Bob")
print(subobj)