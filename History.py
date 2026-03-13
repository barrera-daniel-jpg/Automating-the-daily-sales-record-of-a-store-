history = [] #Lista global que actúa como memoria del programa


def add_to_history(producto): #Recibe diccionarios de Login.py y los almacena con append()
    history.append(producto)

def show_summary(): #Recorre la lista, imprime productos y acumula totales
    
    print("\n=========== Sales summary ===========") # Mejora la visualizacion y la experiencia de usuario
    total_memories = 0
    
    for producto in history:
        print(f">> {producto['product']}: {producto['quantity']} quantity x ${producto['price']} = ${producto['total']}")
        total_memories += producto['total']
    
    print(f">> Total raised: ${total_memories}")
    print("="*40) # Mejora la visualizacion y la experiencia de usuario.