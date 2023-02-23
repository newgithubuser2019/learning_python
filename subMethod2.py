import re
regexobj = re.compile(r"Agent (\w)\w*")
subobj = regexobj.sub(r"\1****", "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent")
print(subobj)