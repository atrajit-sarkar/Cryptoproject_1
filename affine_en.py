from Affinecipher.encrypt import encrypt
from Affinecipher.gcd import gcd
alp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
special=" ,.?!"
print("Only use characters in the following list: ",list(alp),list(num),list(special),"forget about case sensitiveness")
message=input("Enter the encrypted message: ")
message=message.upper()
for i in message:
  if i not in alp and i not in num and i not in special:
    raise TypeError(f"Invalid character {i} in the message")
key=input("Enter your key(two digit number, remeber 10th digit must be coprime with 41): ")
if gcd(int(key[0]),40)!=1:
  raise TypeError(f"{key[0]} is not coprime with 40")
print(f"Your encrypted message is \n {encrypt(message,key)}")
 