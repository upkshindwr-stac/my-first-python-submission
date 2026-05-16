import re
bio = """
John "Jake" Rivera is a certified structural welder with over 12 years of hands-on experience in MIG, TIG, and stick welding across industrial and commercial construction projects. Based in Chicago, Illinois, Jake has worked with leading fabrication firms, specializing in carbon steel, stainless steel, and aluminum structures. He holds certifications from the American Welding Society (AWS) and has a strong track record of delivering precision welds that meet strict safety and quality standards. Known for his reliability, attention to detail, and ability to read complex blueprints, Jake is currently available for full-time, contract, and freelance welding opportunities. He can be reached by email at jake.rivera.welds@email.com or by phone at (312) 555-0174.
"""
email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', bio)
phone_match = re.search(r'\(\d{3}\)\s\d{3}-\d{4}', bio)

contact_details = {
    "Email": email_match.group() if email_match else "Not found",
    
    "Phone": phone_match.group() if phone_match else "Not found"
}

print("Contact Details:")
print(contact_details)