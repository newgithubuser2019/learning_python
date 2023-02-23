import re
phonenum_regex = re.compile(r"\((\d\d\d)\) (\d\d\d-\d\d\d\d)")
match_objects = phonenum_regex.search("my number is (415) 555-4242")
print(match_objects.groups())