from project3.coverstion import conv
from project3.swap import swap
# we put messege as list and key as string
def encrypt(message,key):
  '''
  Here we are basically encrypting with the following rule:
  1) If the length of the message word =2 then we swap the first and second character of the word.
  2) If the length of the message word=1, then we keep it as it is.
  3) If the length of the message word >2, then we take the three character of our key word and add it to the begging of our message and putting th first letter of our message at the end and append at the end the last three character of our key word.
  '''
  if len(message)==2:
    en=conv(swap(message))
  elif len(message)==1:
    en=conv(message)
  else:
    i=0
    m=message[0]
    while i<len(message)-1:
      message[i]=message[i+1]    
      i=i+1
    message[len(message)-1]=m
    en=key[0]+key[1]+key[2]+conv(message)+key[3]+key[4]+key[5]

  return en

