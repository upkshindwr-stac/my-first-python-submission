student_details = {
    "name" : "John"
    "age" : "22"
    "department" : "PDU"
}
#print(student_details)

student_details["name"] = {
    "first_name" : "John",
    "sur_name" : "Williams"
}
print(student_details['name']['surname'])