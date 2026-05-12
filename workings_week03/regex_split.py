import re
text = "tea, sugar/salt & chilli powder"
match = re.split(r"[,/&]",text)
print(match)
