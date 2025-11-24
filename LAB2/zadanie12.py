def typeChecking():
  intA: int = 6
  intB: int = 2
  floatA: float = 6.0
  floatB: float = 2.0

  result1 = intA / intB
  result2 = intA / floatB
  result3 = floatA / floatB

  print(f'a) {type(result1)}' + 
        f'\nb) {type(result2)}' + 
        f'\nc) {type(result3)}' )

typeChecking()