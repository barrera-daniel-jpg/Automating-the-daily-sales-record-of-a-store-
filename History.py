history = []

def add_to_history(producto):
    history.append(producto)

def show_summary():
    
    print("\n=========== Sales summary ===========")
    total_memories = 0
    
    for producto in history:
        print(f">> {producto['product']}: {producto['quantity']} quantity x ${producto['price']} = ${producto['total']}")
        total_memories += producto['total']
    
    print(f">> Total raised: ${total_memories}")
    print("="*40)