names = ["John","Peter","Eric","Tim","Bob","Sarah","Ema","Elisa","Laura","Julia"]

for name in names:
    print(name)

ask = input("Who do you want to check on?").lower()
in_jail = ''

for name in names:
   if name.lower() == ask:
       print(f"Yes, {ask.title()} is in jail")
       in_jail = True

if in_jail != True:
   print(f"No, we don't have {ask.title()} in jail")