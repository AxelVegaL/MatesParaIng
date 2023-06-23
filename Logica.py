import sympy as sp

def multiple_integral(expression, variables, limits):
    symbols = sp.symbols(variables)
    integral_expr = expression
    for i, limit in enumerate(limits):
        if limit[1] is None:
            integral_expr = sp.integrate(integral_expr, (symbols[i], limit[0]))
        else:
            integral_expr = sp.integrate(integral_expr, (symbols[i], limit[0], limit[1]))
    return integral_expr

def main():
    expression_str = input("Ingrese la expresión a integrar: ")
    expression = sp.sympify(expression_str.replace("^", "**"))
    num_variables = int(input("Ingrese el número de variables de integración: "))
    variables = []
    for i in range(num_variables):
        variable = input(f"Ingrese el nombre de la variable {i + 1}: ")
        variables.append(variable)
    num_limits = int(input("Ingrese el número de límites de integración: "))
    limits = []
    for i in range(num_limits):
        limit_type = input(f"Ingrese el tipo de límite (indefinido o definido) {i + 1}: ")
        if limit_type.lower() == "indefinido":
            limits.append((None, None))
        elif limit_type.lower() == "definido":
            lower_limit = float(input(f"Ingrese el límite inferior {i + 1}: "))
            upper_limit = float(input(f"Ingrese el límite superior {i + 1}: "))
            limits.append((lower_limit, upper_limit))
        else:
            print("Tipo de límite inválido. Por favor, intente nuevamente.")
            return
    result = multiple_integral(expression, variables, limits)
    print("El resultado de la integral es:", result)

main()







