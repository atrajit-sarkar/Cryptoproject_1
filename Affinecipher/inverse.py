def inverse(a):
  for i in range(1,40):
    if (a*i)%40==1:
      return i
  else:
    return 0