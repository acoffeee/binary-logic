class possibilities:
 
  def one_on(x,y):
    if x == 1 and y == 0 or x == 0 and y == 1:
      if x==1:
        return (1,0)
      else:
        return (0,1)
    else:
      return false;
      
  def and(x,y):
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

#i could either just take the numbers and output them in binary or actuall code the gates and run it through that proccess.
#so itd be like input > actual adder logic > output or input > binary logic > output
