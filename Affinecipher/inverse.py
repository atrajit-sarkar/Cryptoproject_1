def inverse(a):
  for i in range(1,41):
    if (a*i)%41==1:
      return i
  else:
    return 0