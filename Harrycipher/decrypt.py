from Harrycipher.coverstion import conv
from Harrycipher.swap import swap
# we put messege as list and key as string
def decrypt(message,key):
  '''
  Here we are basically encrypting with the following rule:
  1) If the length of the message word =2 then we swap the first and second character of the word.
  2) If the length of the message word=1, then we keep it as it is.
  3) 
  '''
  if len(message)==2:
    dy=conv(swap(message))
  elif len(message)==1:
    dy=conv(message)
  else:
    dy=conv(message).lstrip(key[0]+key[1]+key[2])
    dy=dy.rstrip(key[3]+key[4]+key[5])
    # i=1
    # m=dy[-1]
    # dy_list=list(dy)
    # while i<len(dy):
    #   dy_list[i]=dy_list[i-1]    
    #   i=i+1
    # dy_list[0]=m 
    # dy=conv(dy_list)
    dy=dy[-1]+dy.rstrip(dy[-1])
        
    

  return dy