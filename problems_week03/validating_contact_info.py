import re
name = input("Enter your Name: ")
phone = input("Enter your Phone Number: ")
email = input("Enter your Email Address: ")
address = input("Enter your Address: ")

phone_validation = re.match(r"^\d{9,12}$", phone)
email_validation = re.match(r"^[^@]+@[^@]+\.[^@]+$", email)

print("\nHi", name + ",")
print("You have entered the following details")
print("Phone number:", phone)
print("Email address:", email)
print("Address:", address)

print("\nPlease be kind to confirm the above details")