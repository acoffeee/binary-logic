class possibilities:
 
  def one_on(x,y):
    if x == 1 and y == 0 or x == 0 and y == 1:
      if x==1:
        return (1,0)
      else:
        return (0,1)
    else:
      return false;
      
  def both_on(x,y):
    if x == 1 and y == 1:
      return (1,1)
    else:
      return (0,0);
class gates:
  # gate(x,y) where x and y are the left/top and right/bottom input specifcally so if you wanted to out put like 1,0 via and gate youd do 
  class xor:
    def __init__(self):
      self.input = x,y
      self.output = (a,b)


add [0,0,0,0] [0,0,0,0]

