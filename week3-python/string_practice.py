#Task 1
first_name = "Hajira"
last_name = "Baffoe"
age = 21
favorite_concept = "loops"
print(first_name)
print(last_name)
print(age)
print(favorite_concept)
 
 #Task 2
name = first_name + last_name
print(name)
full_name = f"{first_name} {last_name}"
print(full_name)


#Task 3
print(full_name.upper())
print(full_name.lower())
print(full_name.lower().count("a"))
print(full_name.index(" "))
new_name = full_name.replace("Hajira", "Coder")
print(new_name)


#Task 4
complete_sentence = f"My name is {first_name} {last_name}.\nI am {age} years old.\nMy favorite concept learnt in python class thus far is {favorite_concept} "
print(complete_sentence)
print(full_name[0])
print(full_name[-1])
print(full_name[0:7])
