import re
text = "Test scores : 60,75,95"
match = re.findall(r"\d+",text)
print(match[0])