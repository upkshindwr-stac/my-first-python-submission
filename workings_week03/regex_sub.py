import re
text = "My contact number is 94 70 334 3980"
match = re.sub(r"-","",text)
print(match)