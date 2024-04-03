from Affinecipher.dict import get_key
from Affinecipher.encrypt import encrypt


message=input("Enter the message: ")
key=input("Enter your key(two digit number, remeber 10th digit must be coprime with 40): ")
print(f"Your encrypted message is {encrypt(message,key)}")
