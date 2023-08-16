import sympy as sp

def integrate_expression(expression_str, variables, num_iterations=1):
    # Crear símbolos para todas las variables
    symbols = sp.symbols(variables)
    expression = sp.sympify(expression_str)
    
    for _ in range(num_iterations):
        expression = sp.integrate(expression, *symbols)
    
    return expression

def defined_integral(expression_str, variables, lower_limit, upper_limit):
    # Crear símbolos para todas las variables
    symbols = sp.symbols(variables)
    expression = sp.sympify(expression_str)
    
    result = sp.integrate(expression, (*symbols, lower_limit, upper_limit))
    return result