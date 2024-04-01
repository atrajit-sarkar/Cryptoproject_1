from project3.encrypt import encrypt

key=input("Enter your 6 digit key: ")

if len(key)!=6:
   raise TypeError(f"Key must be 6 digit long, but you entered {len(key)} digit")

str=input("Enter the message: ")
i=0
List=str.split()
s=""
for item in List:
  en=encrypt(list(item),key)
  en=en+" "
  s=s+en
  i=i+1

print(f"Your encrypted message is: {s}")




