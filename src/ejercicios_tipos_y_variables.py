# Ejercicios sobre Tipos y Variables

# E1: Declara tres variables de distintos tipos y muéstralas con su tipo.
variable_texto = "Python"
variable_entero = 2024
variable_flotante = 3.1416

print(f"'{variable_texto}' es de tipo {type(variable_texto)}")
print(f"{variable_entero} es de tipo {type(variable_entero)}")
print(f"{variable_flotante} es de tipo {type(variable_flotante)}")
print("-" * 20)

# E2: Convierte "99" a entero y súmalo con 1.
numero_como_cadena = "99"
resultado = int(numero_como_cadena) + 1
print(f'El resultado de convertir "99" a entero y sumarle 1 es: {resultado}')
print("-" * 20)

# E3: Pide por input() nombre y edad, y muestra un mensaje formateado.