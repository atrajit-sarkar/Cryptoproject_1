def gcd(a,b):
  if a==0:
    if b>0:
      return b
    else:
      return -b
  elif b==0:
    if a>0:
      return a
    else:
      return -a
  else:
    return gcd(b,a%b)

