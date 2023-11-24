def chunk_to_babylonian(n):
    unit = '┬'
    ten = '‹'
    representation = ''
    
    tens_count = n // 10
    unit_count = n % 10
    
    # gérer les dizaines
    representation += ten * tens_count
    
    # gérer les unités
    representation += unit * unit_count
    
    return representation

def number_to_babylonian(n):
    if n == 0:
        return 'Pas de symbole pour 0 en babylonien!'
    
    babylonian_representation = ''
    
    while n > 0:
        n_60 = n % 60
        n = n // 60
        current_representation = chunk_to_babylonian(n_60)
        babylonian_representation = current_representation + ' ' + babylonian_representation
    
    return babylonian_representation.strip()

if __name__ == "__main__":
    while True:
        user_input = input("Veuillez entrer un nombre à convertir en notation babylonienne (ou 'exit' pour quitter): ")
        if user_input.lower() == 'exit':
            break
        try:
            n = int(user_input)
            print("La notation babylonienne est : ")
            print(number_to_babylonian(n))
        except ValueError:
            print("Ce n'est pas un nombre valide. Veuillez réessayer.")
