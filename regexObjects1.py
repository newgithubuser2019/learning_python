import re
phonenum_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
match_objects = phonenum_regex.search("my number is 415-555-4242")
print("Phone number found: " + match_objects.group())