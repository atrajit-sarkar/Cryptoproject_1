from Affinecipher.decrypt import decryption
from Affinecipher.gcd import gcd

message=input("Enter the encrypted message: ")
key=input("Enter your key(two digit number, remeber 10th digit must be coprime with 40): ")
if gcd(int(key[0]),40)!=1:
  raise TypeError(f"{key[0]} is not coprime with 40")
print(f"Your decrypted message is {decryption(message,key)}")

# H YHQP 