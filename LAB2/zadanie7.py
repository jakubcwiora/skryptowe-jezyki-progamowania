from sympy import symbols, sympify, solve

x = symbols('x')

expression_string = input('Podaj równanie kwadratowe w formacie (a * x ** 2 + b * x + c): \n')
try:  
  expression = sympify(expression_string) ## Zamieniamy na format który przetrafi SymPy
  solutions = solve(expression, x) ## Pozwalamy mu rozwiązać równanie
  print('Pierwiastki równania kwadratowego: ', solutions)
except:
  print("Podano niepoprawne równanie (pamiętaj o odpowiednim zapisie), lub wystąpił inny błąd")

