def main():
    option = 1
    while option != 0:
        print("###############")
        print("1. Opción 1")
        print("2. Opción 2")
        print("3. Opción 3")
        print("0. Salir")
        print("###############")
        try:
            option = int(input("Introduce una opción: "))
        except:
            pass
        
        match option:
            case 1:
                print("Opción 1")
            case 2:
                print("Opción 2")
            case 3:
                print("Opción 3")
            case 0:
                print("Hasta pronto!!")
            case _:
                print("[!] Elige un número dentro del rango.")

if __name__ == '__main__':
    main()