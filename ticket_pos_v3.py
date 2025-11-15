from reportlab.lib.pagesizes import mm
from reportlab.pdfgen import canvas
from datetime import datetime
import os

# ==============================
# CONFIGURACIÓN EMPRESA
# ==============================
EMPRESA = "MULTIENVASES MARGARITA LTDA"
RUT_EMPRESA = "77.618.426-8"
DIRECCION = "SANTIAGO 119, LANCO"
GIRO = "PROD. CARTÓN PLÁSTICO Y EMBALAJES"
EMAIL = "ruth_cj31@hotmail.com"
FONO = "+56 9 9999 9999"

# ==============================
# FUNCIONES DE APOYO
# ==============================

def obtener_numero_ticket():
    archivo = "ticket.txt"
    if not os.path.exists(archivo):
        with open(archivo, "w") as f:
            f.write("1")
        return 1
    else:
        with open(archivo, "r+") as f:
            num = int(f.read().strip())
            nuevo = num + 1
            f.seek(0)
            f.write(str(nuevo))
            f.truncate()
        return nuevo

def ingresar_productos():
    productos = []
    print("\n🛒 Ingrese los productos (deje descripción vacía para terminar):")
    while True:
        desc = input("Descripción: ").strip()
        if not desc:
            break
        try:
            cant = float(input("Cantidad: "))
            precio = float(input("Precio unitario: "))
            productos.append((desc, cant, precio))
        except ValueError:
            print("❌ Ingrese valores numéricos válidos.")
    return productos

# ==============================
# DATOS DE VENTA
# ==============================
cliente = input("👤 Cliente: ") or "Cliente General"
rut_cliente = input("🧾 RUT del cliente (opcional): ") or "-"
productos = ingresar_productos()
if not productos:
    print("⚠️ No se ingresaron productos. Saliendo...")
    exit()

numero_ticket = obtener_numero_ticket()

# ==============================
# CÁLCULOS
# ==============================
neto = sum(cant * precio for _, cant, precio in productos)
iva = round(neto * 0.19)
total = neto + iva

# ==============================
# GENERAR PDF
# ==============================
ancho, alto = 80 * mm, 200 * mm
pdf = canvas.Canvas(f"ticket_{numero_ticket:03}.pdf", pagesize=(ancho, alto))

y = alto - 5 * mm
pdf.setFont("Helvetica-Bold", 9)
pdf.drawCentredString(ancho / 2, y, EMPRESA)
y -= 5 * mm
pdf.setFont("Helvetica", 7)
pdf.drawCentredString(ancho / 2, y, f"RUT: {RUT_EMPRESA}")
y -= 4 * mm
pdf.drawCentredString(ancho / 2, y, DIRECCION)
y -= 4 * mm
pdf.drawCentredString(ancho / 2, y, GIRO)
y -= 6 * mm
pdf.line(5 * mm, y, ancho - 5 * mm, y)
y -= 5 * mm

pdf.setFont("Helvetica-Bold", 7)
pdf.drawString(5 * mm, y, f"Ticket N° {numero_ticket:03}")
pdf.drawRightString(ancho - 5 * mm, y, datetime.now().strftime("%d/%m/%Y %H:%M"))
y -= 5 * mm
pdf.setFont("Helvetica", 7)
pdf.drawString(5 * mm, y, f"CLIENTE: {cliente}")
y -= 4 * mm
pdf.drawString(5 * mm, y, f"RUT: {rut_cliente}")
y -= 5 * mm
pdf.line(5 * mm, y, ancho - 5 * mm, y)
y -= 5 * mm

# Detalle
pdf.setFont("Helvetica-Bold", 7)
pdf.drawString(5 * mm, y, "DESCRIPCIÓN")
pdf.drawRightString(ancho - 20 * mm, y, "CANT")
pdf.drawRightString(ancho - 5 * mm, y, "VALOR")
y -= 3 * mm
pdf.line(5 * mm, y, ancho - 5 * mm, y)
y -= 5 * mm

pdf.setFont("Helvetica", 7)
for desc, cant, precio in productos:
    pdf.drawString(5 * mm, y, desc[:18])
    pdf.drawRightString(ancho - 20 * mm, y, str(cant))
    pdf.drawRightString(ancho - 5 * mm, y, f"${precio * cant:,.0f}")
    y -= 5 * mm

pdf.line(5 * mm, y, ancho - 5 * mm, y)
y -= 6 * mm
pdf.setFont("Helvetica-Bold", 8)
pdf.drawRightString(ancho - 5 * mm, y, f"NETO: ${neto:,.0f}")
y -= 5 * mm
pdf.drawRightString(ancho - 5 * mm, y, f"IVA 19%: ${iva:,.0f}")
y -= 5 * mm
pdf.drawRightString(ancho - 5 * mm, y, f"TOTAL: ${total:,.0f}")
y -= 10 * mm

# Pie
pdf.setFont("Helvetica", 6)
pdf.drawCentredString(ancho / 2, y, "Gracias por su compra")
y -= 4 * mm
pdf.drawCentredString(ancho / 2, y, "Documento interno sin validez tributaria")
y -= 4 * mm
pdf.drawCentredString(ancho / 2, y, "www.sii.cl")

pdf.save()
print(f"\n✅ Ticket generado: ticket_{numero_ticket:03}.pdf")
