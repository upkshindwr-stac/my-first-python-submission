import re
text = "Hello World"
match = re.search(r"Hello",text)
#print(match[0])
#ERROR WITH THE FOLLOWING CORE BECAUSE re.match ONLY COMPARE THE FIRST VALUE IN THE STRING
#match = re.match(r"world",text)
print(match[0])