birthday = ("John","01.01.1995")
print(birthday)

#Finding the index position of a certain value 
print(birthday.index("John"))
#print(birthday)

#Retrieving a record to the existing tuple
birthday = birthday + ("Sarah","05.06.1996")
print(birthday)

#Retrieving the DOB of a certain person
person_index_id = birthday.index("Sarah")
person_dob = birthday[person_index_id+1]
print(person_dob)

#Tuples cannot be modified directly 
#Convert tuple to list if modification is needed
#ERROR because cannot change an existing value
birthday_list = list(birthday)

#Change value 
birthday_list[0] = "Patrick"

#Convert back to tuple
birthday = tuple(birthday_list)
print(birthday)
#tp = (1,2,3,4)