hobbies = []

# Prompt the user to enter three hobbies and add them to the list
for i in range(3):
    hobby = input(f"Enter hobby {i+1}: ")
    hobbies.append(hobby)

# Print the statement with the listed hobbies
print(f"I enjoy {', '.join(hobbies)}.")

hobby=["A","B","C"]

for hobbiess in hobby:
    print(f"i enjoy {hobbiess}")