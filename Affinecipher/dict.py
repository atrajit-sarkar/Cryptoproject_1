dict={0:'A',1:'B',2:'C' ,3:'D' ,4:'E' ,5:'F' ,6:'G' ,7:'H' ,8:'I' ,9:'J',10:'K',11:'L' ,12:'M' ,13:'N' ,14:'O' ,15:'P',16:'Q' ,17:'R' ,18:'S' ,19:'T' ,20:'U',21:'V' ,22:'W' ,23:'X' ,24:'Y' ,25:'Z',26:' ',27:',',28:'.',29:'?',30:'0',31:'1',32:'2',33:'3',34:'4',35:'5',36:'6',37:'7',38:'8',39:'9',40:'!'}
item=dict.items()

def get_key(val):
  for key, value in item:
    if val == value:
      return key

  return 0