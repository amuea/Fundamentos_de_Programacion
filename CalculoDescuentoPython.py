# Definición de una función con dos parámetros
def calcular_descuento(monto, porcentaje):
    print(f"Compras, {monto} total {porcentaje} descuento.")

# Llamada a la función y paso de argumentos
calcular_descuento(150)
calcular_descuento(150, 10)


# Parámetros predeterminados
def calcular_descuento(monto, porcentaje, descuento="Compras"):
    print(f"{descuento}, {monto} total {porcentaje} descuento.")

# Llamada a la función con parámetros predeterminados
calcular_descuento_compras("Monto", 150)
calcular_descuento_compras("Porcentaje", 10, "Compras")