import sympy as sp  #Se importa la librería de Sympy para realizar las operaciones matemáticas


def multiple_integral(expression, variables, limits):
    
    #Los parámetros dentro de la función son:
    #expression: la expresión a integrar
    #variables: las variables de integración
    #limits: los límites de integración para hacerla definida
    
    symbols = sp.symbols(variables)     #Se crea una lista de símbolos para las variables de integración
    integral_expr = expression
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
    num_limits = int(input("Ingrese el número de límites de integración: "))
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
    if constant==True:
        print("El resultado de la integral es:", result, " + C")
    else:
        print("El resultado de la integral es:", result)
    multi = multiple_integral(result, variables, limits)
    print("La integral doble es:", multi, " + C")
    

##main()