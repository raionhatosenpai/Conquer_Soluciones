# Este script simula un sistema de pedidos para un restaurante online.
# Permite a los usuarios seleccionar entre la hamburguesa Classica y la Vegana, con opciones de personalización
# permite al usuario elegir los ingredientes adicionales
# para la hamburguesa Classica : Queso Idaizabal, Bacon, Huevo
# para la hamburguesa Vegana : Tofu, Cebolla Caramelizada

#  solicita al usuario que elija una hamburguesa y personalice su pedido
hamburguesa = input("Elige tu hamburguesa (Classica/Vegana): ").strip().lower()
while hamburguesa not in ["classica", "vegana"]:
    print("Opción no válida. Por favor, elige 'Classica' o 'Vegana'.")
    hamburguesa = input("Elige tu hamburguesa (Classica/Vegana): ").strip().lower()
if hamburguesa == "classica":
    extra_validos = ["queso idaizabal", "bacon", "huevo"]
elif hamburguesa == "vegana":
    extra_validos = ["tofu", "cebolla caramelizada"]
ingredientes = input(f"Elige tus ingredientes extra ({', '.join(extra_validos)}): ").strip().lower()
while ingredientes not in extra_validos:
    print("Ingrediente no válido. Elige uno de los disponibles.")
    ingredientes = input(f"Elige tus ingredientes extra ({', '.join(extra_validos)}): ").strip().lower()
print(f"\nHas elegido la hamburguesa {hamburguesa.capitalize()} con los siguientes ingredientes extra: {ingredientes.title()}.")
print("\nGracias por tu pedido.")