🧾 Sistema POS Interno – Multienvases Margarita

Generador de tickets tipo POS (80 mm) para uso interno.
Compatible con impresoras térmicas como Epson TM-T20II.

📌 Características principales

🖨️ Generación automática de tickets POS en PDF

👤 Registro rápido de cliente y RUT

🛒 Ingreso interactivo de productos (cantidad y precio)

💰 Cálculo automático de Neto + IVA 19% + Total

🧾 Numeración correlativa (ticket_001, ticket_002, …)

🖼️ Logo de la empresa incluido

🔳 Código QR con número de ticket, fecha y total

📁 Tickets internos (no tributarios), ideales para ventas rápidas

💻 Código listo para modificar y expandir

🏗️ Requisitos

Debes tener instalado:

Python 3.8+

Librerías:

pip install reportlab


logo.png (opcional) → se coloca en la misma carpeta que el script

Impresora recomendada:
Epson TM-T20II (papel 80 mm)

🚀 Cómo usar

Clona el repositorio:

git clone https://github.com/USUARIO/ticket-pos-multienvases.git


Entra a la carpeta:

cd ticket-pos-multienvases


Ejecuta el script:

python ticket_pos_v4.py


Ingresa los datos:

Nombre del cliente

RUT (opcional)

Productos: descripción, cantidad y precio

Enter para terminar

El sistema generará automáticamente:

ticket_001.pdf
ticket_002.pdf
ticket_003.pdf
...

🖨️ Impresión en Epson TM-T20II

En Adobe Acrobat:

Tamaño de papel: 80 × 200 mm

Escala: 100% (sin ajustar)

Márgenes: Ninguno

Imprimir y listo.

📦 Estructura del proyecto
ticket_pos_v4.py       → Script principal
ticket.txt             → Correlativo automático (se ignora en Git)
logo.png               → Logo impreso en el ticket
.gitignore             → Archivos ignorados por Git
README.md              → Este archivo

⚙️ Cómo sincronizar en PC y Notebook

Cuando trabajes en tu PC:

git add .
git commit -m "Actualizo ticket POS"
git push


Cuando trabajes desde tu notebook:

git pull


Así ambos equipos siempre tienen la última versión.

🧠 Próximas mejoras (roadmap)

Menú interactivo tipo POS

Base de datos de productos

Historial de ventas

Exportar a Excel

Modo “caja diaria”

Preparar integración futura con SII DTE

👨‍💻 Autor

Desarrollado por Zeku
Multienvases Margarita
Chile 🇨🇱

📄 Licencia

Uso interno privado.
No apto para emisión tributaria ante el SII.