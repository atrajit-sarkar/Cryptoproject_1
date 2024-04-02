from Harrycipher.decrypt import decrypt

key=input("Enter your 6 digit key: ")

if len(key)!=6:
   raise TypeError(f"Key must be 6 digit long, but you entered {len(key)} digit")

str=input("Enter the message: ")
i=0
List=str.split()
s=""
for item in List:
  dy=decrypt(list(item),key)
  dy=dy+" "
  s=s+dy
  i=i+1

print(f"Your decrypted message is: {s}")

# test encrypted word: 172i,H917 I ma 172oobN917
# 172elloH917 172orldw917