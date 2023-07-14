import sympy as sp  #Se importa la librería de Sympy para realizar las operaciones matemáticas
from sympy import symbols, integrate

def multiple_integral(expression, variables, limits):
    
    #Los parámetros dentro de la función son:
    #expression: la expresión a integrar
    #variables: las variables de integración
    #limits: los límites de integración para hacerla definida
    symbols = sp.symbols(variables) #Se crea una lista de símbolos para las variables de integración
    integral_expr = sp.sympify(expression)
    for i, limit in enumerate(limits):
        if limit[1] is None:
            integral_expr = sp.integrate(integral_expr, (symbols[i], limit[0]))
        else:
            integral_expr = sp.integrate(integral_expr, (symbols[i], limit[0], limit[1]))
    return integral_expr

def main():
    constant = False
    expression_str = input("Ingrese la expresión a integrar: ")
    expression = sp.sympify(expression_str.replace("^", "**"))
    
    #Se reemplazan los símbolos de potencia de ^ a ** para que Sympy los reconozca porque le da amzieda y explotaba el programa con los "^"
    #Adicionalmente, se pasa temporalmente como string pero para Sympify
    #Lo que lo convierte en una expresión matemática. Sin él, es un string cualquiera
        
    num_variables = int(input("Ingrese el número de variables de integración: "))        #Esta parte es para que el usuario ingrese el número de variables de integración
    variables = []
    for i in range(num_variables):
        variable = input(f"Ingrese el nombre de la variable {i + 1}: ")
        variables.append(variable)
    """ num_limits = int(input("Ingrese el número de límites de integración: ")) """
    num_limits = 1
    #si se deja con límite 1, sólo integra en base a una variable
    #pero igualado al número de variables, se integra en base a todas las variables
    #esto deja la diferencia entre:
    #Límite 1 de x + y:     x**2/2 + x*y + C
    #límite =num_variables de x + y:      x**2*y/2 + x*y**2/2 + C
    #Pese a que en calculadoras online como Mathway, el resultado es límite 1...
    # a little... SUS ඞ
    limits = []
    for i in range(num_limits):
        limit_type = input(f"Ingrese el tipo de límite (indefinido o definido) {i + 1}: ")
        if limit_type.lower() == "indefinido":
            constant = True
            #Sí ocupa constante de integración
            limits.append((None, None))
        elif limit_type.lower() == "definido":
            lower_limit = float(input(f"Ingrese el límite inferior {i + 1}: "))
            upper_limit = float(input(f"Ingrese el límite superior {i + 1}: "))
            limits.append((lower_limit, upper_limit))
            constant = False
            #No ocupa constante de integración
        else:
            print("Tipo de límite inválido. Por favor, intente nuevamente.")
            return
    result = multiple_integral(expression, variables, limits)
    check = False #auxiliar para el try
    
    #Se hace un try para que el usuario ingrese un número entero y no un string o float
    #Se repetirá gracias al check hasta que el usuario haga lo que se solicita
    while check == False:
        try:
            repeat = int(input("¿Cuántas veces quiere integrar?\t"))
            if repeat < 1:
                print("Ingrese un número mayor a 0")
            else:
                check = True
                repeat -= 1
        except ValueError:
            print("Ingrese un número entero")
            check = False

    #Se hace un for para que se repita la integral tantas veces como el usuario lo solicita
    print("La primera integral es: ", result, "+ C")
    for i in range(repeat):
        result = multiple_integral(result, variables, limits)
        if constant:
            print("La integral siguiente es:", result, "+ C")
        else:
            print("La integral siguiente es:", result)
    
main()