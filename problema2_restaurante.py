# Matriz de productos
productos = [
    ["Hamburguesa", "Comida", 25000],
    ["Pizza", "Comida", 30000],
    ["Jugo Natural", "Bebida", 12000],
    ["Pasta", "Comida", 28000],
    ["Café", "Bebida", 7000],
    ["Ensalada", "Comida", 22000]
]

# Función para calcular precio final
def calcular_precio(categoria, precio):
    if categoria == "Comida" and precio > 20000:
        descuento = precio * 0.15
        return precio - descuento
    else:
        return precio

# Mostrar resultados
print("PROMOCIONES DEL RESTAURANTE\n")

for producto in productos:
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    precio_final = calcular_precio(categoria, precio_base)

    print("Producto:", nombre)
    print("Categoría:", categoria)
    print("Precio base:", precio_base)
    print("Precio final:", precio_final)
    print("-----------------------------")