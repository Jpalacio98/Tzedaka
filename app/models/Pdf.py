from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def generar_pdf(datos):
    # Crea un objeto canvas y establece el tamaño de página
    c = canvas.Canvas("Recibo.pdf", pagesize=letter)
    # Centra la imagen en la página
    imagen = "source/Imagenes/logo.png"
    c.drawImage(imagen, (letter[0]-200)/2, (letter[1]-200), width=200, height=200, mask='auto')
    # Establece el estilo para los campos de texto
    estilo_negrita_subrayado = ParagraphStyle("estilo_negrita_subrayado", parent=getSampleStyleSheet()["Normal"])
    estilo_negrita_subrayado.fontName = "Helvetica-Bold"
    estilo_negrita_subrayado.textColor = colors.black
    estilo_negrita_subrayado.spaceBefore = 10
    estilo_negrita_subrayado.spaceAfter = 10
    estilo_negrita_subrayado.leading = 16
    estilo_negrita_subrayado.alignment = 1
    estilo_negrita_subrayado.backColor = colors.white
    estilo_negrita_subrayado.borderColor = colors.black
    estilo_negrita_subrayado.borderWidth = 1
    estilo_negrita_subrayado.textColor = colors.black
    c.setFont("Helvetica-Bold", 16)
    c.drawString(170, 575, "RECIBO POR SERVICIO JURIDICO")
    # Agrega los datos del cliente al PDF
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, 500, "Datos del cliente")
    c.line(100, 495, 400, 495)
    c.setFont("Helvetica", 12)
    c.drawString(105, 470, "Cédula: {}".format(datos["cedula"]))
    c.drawString(105, 450, "Apellido: {}".format(datos["apellido"]))
    c.drawString(105, 430, "Nombre: {}".format(datos["nombre"]))

    # Agrega los datos del proceso al PDF
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, 370, "Datos del proceso")
    c.line(100, 365, 400, 365)
    c.setFont("Helvetica", 12)
    c.drawString(105, 340, "Número de proceso: {}".format(datos["numero_proceso"]))
    c.drawString(105, 320, "Área: {}".format(datos["area"]))
    c.drawString(105, 300, "Descripción: {}".format(datos["descripcion"]))
    c.drawString(105, 280, "Monto: {}".format(datos["monto"]))
    c.drawString(105, 260, "Abono: {}".format(datos["abono"]))
    c.drawString(105, 240, "Restante: ${}".format(datos["restante"]))
    # Agrega el campo de firma del abogado
    c.setFont("Helvetica-Bold", 12)
    c.drawString(270, 85, "Firma del Abogado")
    c.line(170, 100, 470, 100)  # Línea subrayada

    # Guarda el PDF y cierra el objeto canvas
    c.save()

def pdfdata(cedula,apellido,nombre,numpro,area,descripcion,monto,abono,restante):
    data = {
        "cedula": cedula,
        "apellido": apellido,
        "nombre": nombre,
        "numero_proceso": numpro,
        "area": area,
        "descripcion": descripcion,
        "monto": monto,
        "abono": abono,
        "restante": restante
    }
    return data