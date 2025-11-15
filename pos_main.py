import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader

# ==========================
#   CONFIGURACIÓN GENERAL
# ==========================

NOMBRE_NEGOCIO = "Multienvases Margarita"
IVA = 0.19
TICKET_FILE = "ticket.txt"      # correlativo
HISTORIAL_FILE = "ventas.csv"   # historial de ventas
LOGO_FILE = "logo.png"          # logo si existe


# ==========================
#   FUNCIONES BÁSICAS
# ==========================

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def pausa():
    input("\nPresiona ENTER para continuar...")

def obtener_correlativo():
    if not os.path.exists(TICKET_FILE):
        with open(TICKET_FILE, "w") as f:
            f.write("1")
        return 1
    
    with open(TICKET_FILE, "r") as f:
        return int(f.read().strip())

def guardar_correlativo(num):
    with open(TICKET_FILE, "w") as f:
        f.write(str(num))


# ==========================
#   GENERADOR DE TICKET PDF
# ==========================

def generar_ticket(cliente, rut, productos):
    correlativo = obtener_correlativo()
    nombre_archivo = f"ticket_{correlativo:03}.pdf"

    w = 80 * mm
    h = 200 * mm

    c = canvas.Canvas(nombre_archivo, pagesize=(w, h))

    y = 190 * mm

    # LOGO
    if os.path.exists(LOGO_FILE):
        try:
            logo = ImageReader(LOGO_FILE)
            c.drawImage(logo, 20, y-40, width=40*mm, preserveAspectRatio=True)
            y -= 45
        except:
            pass

    # CABECERA
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(w/2, y, NOMBRE_NEGOCIO)
    y -= 10

    c.setFont("Helvetica", 9)
    c.drawString(5*mm, y, f"Ticket N°: {correlativo:03}")
    y -= 10
    c.drawString(5*mm, y, f"Fecha: {datetime.now().strftime('%d-%m-%Y %H:%M')}")
    y -= 10

    # CLIENTE
    if cliente.strip():
        c.drawString(5*mm, y, f"Cliente: {cliente}")
        y -= 10
    if rut.strip():
        c.drawString(5*mm, y, f"RUT: {rut}")
        y -= 10

    # DETALLE
    c.setFont("Helvetica-Bold", 9)
    c.drawString(5*mm, y, "Producto")
    c.drawString(50*mm, y, "Total")
    y -= 5
    c.drawString(5*mm, y, "-" * 30)
    y -= 10

    c.setFont("Helvetica", 9)
    neto_total = 0

    for descripcion, cantidad, precio in productos:
        total = cantidad * precio
        neto_total += total

        c.drawString(5*mm, y, f"{descripcion} x{cantidad}")
        c.drawRightString(75*mm, y, f"${total:,}")
        y -= 5

    y -= 5
    c.drawString(5*mm, y, "-" * 30)
    y -= 10

    # TOTALES
    iva_monto = int(neto_total * IVA)
    total_final = neto_total + iva_monto

    c.setFont("Helvetica-Bold", 10)
    c.drawString(5*mm, y, f"Neto:")
    c.drawRightString(75*mm, y, f"${neto_total:,}")
    y -= 10

    c.drawString(5*mm, y, f"IVA 19%:")
    c.drawRightString(75*mm, y, f"${iva_monto:,}")
    y -= 10

    c.drawString(5*mm, y, f"Total:")
    c.drawRightString(75*mm, y, f"${total_final:,}")
    y -= 20

    # GUARDAR
    c.showPage()
    c.save()

    # Actualizar correlativo
    guardar_correlativo(correlativo + 1)

    # Registrar historial
    registrar_historial(correlativo, cliente, total_final)

    return nombre_archivo


# ==========================
#   HISTORIAL DE VENTAS
# ==========================

def registrar_historial(num, cliente, total):
    if not os.path.exists(HISTORIAL_FILE):
        with open(HISTORIAL_FILE, "w", encoding="utf-8") as f:
            f.write("ticket;fecha;cliente;total\n")

    with open(HISTORIAL_FILE, "a", encoding="utf-8") as f:
        f.write(f"{num};{datetime.now().strftime('%d-%m-%Y %H:%M')};{cliente};{total}\n")


# ==========================
#        MENU POS
# ==========================

def nueva_venta():
    limpiar_pantalla()
    print("=== NUEVA VENTA ===")

    cliente = input("Cliente: ")
    rut = input("RUT (opcional): ")

    print("\nIngrese productos (vacío para terminar)")

    productos = []
    while True:
        desc = input("Descripción: ")
        if desc == "":
            break
        cantidad = int(input("Cantidad: "))
        precio = int(input("Precio unitario: "))
        productos.append((desc, cantidad, precio))

    if not productos:
        print("\nNo se ingresaron productos. Venta cancelada.")
        pausa()
        return

    archivo = generar_ticket(cliente, rut, productos)

    print(f"\nTicket generado: {archivo}")
    pausa()


def reimprimir_ticket():
    limpiar_pantalla()
    print("=== REIMPRIMIR TICKET ===")
    num = input("Número de ticket: ")

    archivo = f"ticket_{int(num):03}.pdf"

    if not os.path.exists(archivo):
        print("❌ No existe ese ticket.")
    else:
        print(f"Abriendo {archivo}...")
        os.startfile(archivo) if os.name == "nt" else os.system(f"open {archivo}")

    pausa()


def ver_historial():
    limpiar_pantalla()
    print("=== HISTORIAL DE VENTAS ===\n")

    if not os.path.exists(HISTORIAL_FILE):
        print("No hay ventas registradas.")
        pausa()
        return

    with open(HISTORIAL_FILE, "r", encoding="utf-8") as f:
        print(f.read())

    pausa()


def main():
    while True:
        limpiar_pantalla()
        print("======================================")
        print("     SISTEMA POS – MULTIENVASES       ")
        print("======================================")
        print("1) Nueva venta")
        print("2) Reimprimir ticket")
        print("3) Ver historial")
        print("4) Salir")
        print("--------------------------------------")

        opcion = input("Elige: ")

        if opcion == "1":
            nueva_venta()
        elif opcion == "2":
            reimprimir_ticket()
        elif opcion == "3":
            ver_historial()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")
            pausa()


if __name__ == "__main__":
    main()
