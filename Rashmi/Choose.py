# Ask user to enter their name
a = input("No Of Adult: ")
b = input("No Of Children: ")
c = input("No Of Senior Citizen: ")
ar = 0.2*30
cr = 0.1*30
sr = 0.15*30
av = 0.3*30
cv = 0.1*30
sv = 0.3*30


# Print the name
print("Rice Per Month=", int(a)*ar+int(b)*cr+int(c)*sr,"KG")
print("Vegitable Per Month=", int(a)*av+int(b)*cv+int(c)*sv,"KG")
