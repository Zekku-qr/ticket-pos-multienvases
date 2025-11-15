import os

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    while True:
        limpiar()
        print("=====================================")
        print("   SISTEMA POS - MULTIENVASES")
        print("=====================================")
        print("1) Nueva venta")
        print("2) Reimprimir ticket")
        print("3) Ver historial de ventas")
        print("4) Configuración")
        print("5) Salir")
        print("=====================================")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nueva_venta()
        elif opcion == "2":
            reimprimir_ticket()
        elif opcion == "3":
            ver_historial()
        elif opcion == "4":
            configuracion()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            input("Opción inválida. Presiona ENTER para continuar.")

def nueva_venta():
    print("\n👉 Aquí irá la lógica para crear un ticket nuevo")
    input("\nENTER para volver al menú...")

def reimprimir_ticket():
    print("\n👉 Aquí irá la función para reimprimir ticket")
    input("\nENTER para volver al menú...")

def ver_historial():
    print("\n👉 Aquí irá el historial de ventas")
    input("\nENTER para volver al menú...")

def configuracion():
    print("\n👉 Aquí modificarás nombre, RUT, logo, etc.")
    input("\nENTER para volver al menú...")

if __name__ == "__main__":
    menu()
