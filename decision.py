def decision(a,b):
      a = str(a)
      b = str(b)
      ab = a+b
      result = {
      '00':'Tie', '01':'You lose', '02':'You win',
      '10':'You win', '11':'Tie', '12':'You lose',
      '20':'You lose', '21':'You win', '22':'Tie' }
      return result[ab]