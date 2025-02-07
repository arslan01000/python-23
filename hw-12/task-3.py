yoda = ['on Python', 'programming ', 'I like ']

#Regular option
string = f"{yoda[2]}{yoda[1]}{yoda[0]}"
print(string + "!")

#Bonus option
yoda[1] = yoda[1].strip()
yoda[2] = yoda[2].strip()
yoda.reverse()
string_bonus = " ".join(yoda)
print(string_bonus + "!")
