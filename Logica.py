
import sympy as sp

def integrate_expression(expression_str, num_iterations=1):
    # Convertir el string de la expresión en una expresión sympy
    expression = sp.sympify(expression_str)
    # Realizar la integral.. y YA >:( DESPUÉS DE TODO LO QUE LLEVABA.
    #jaja q creisi, visual pone en amarillo el "TODO"

    # Realizar la integral múltiples veces
    for _ in range(num_iterations):
        expression = sp.integrate(expression)

    return expression

