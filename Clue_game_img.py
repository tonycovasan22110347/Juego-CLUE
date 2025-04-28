import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os

# Datos del juego
personajes = ["Elena Duarte", "Marco Salazar", "Lucía Rivas", "Tomás Vélez", "Sofía Mendoza"]
armas = ["Cuchillo", "Pistola", "Veneno", "Estatua pesada", "Candelabro"]
locaciones = ["Cocina de la mansión", "Estudio privado", "Biblioteca", "Jardín", "Habitación principal"]

# Historias para los diferentes casos (culpable, arma, locación)
historias = {
    ("Elena Duarte", "Cuchillo", "Cocina de la mansión"):
        "Durante una acalorada discusión, Elena utilizó el cuchillo de cocina para cometer el crimen.",
    ("Marco Salazar", "Pistola", "Estudio privado"):
        "Marco, el detective, utilizó una pistola en el estudio privado para silenciar a la víctima.",
    ("Lucía Rivas", "Veneno", "Biblioteca"):
        "Lucía envenenó a su víctima mientras discutían sobre literatura en la biblioteca.",
    ("Tomás Vélez", "Estatua pesada", "Jardín"):
        "Tomás usó una estatua pesada en el jardín durante una discusión acalorada.",
    ("Sofía Mendoza", "Candelabro", "Habitación principal"):
        "Sofía dejó caer un candelabro antiguo sobre su rival en la habitación principal."
}

# Pistas para cada combinación de culpable, arma y locación
pistas = {
    ("Elena Duarte", "Cuchillo", "Cocina de la mansión"): "Pista: El crimen ocurrió donde se preparaban comidas deliciosas.",
    ("Marco Salazar", "Pistola", "Estudio privado"): "Pista: El detective sabía más de lo que parecía.",
    ("Lucía Rivas", "Veneno", "Biblioteca"): "Pista: El veneno se sirvió en una bebida elegante mientras discutían libros.",
    ("Tomás Vélez", "Estatua pesada", "Jardín"): "Pista: El crimen ocurrió en un lugar rodeado de belleza natural.",
    ("Sofía Mendoza", "Candelabro", "Habitación principal"): "Pista: La habitación estaba decorada con antigüedades valiosas."
}

# Variables globales
intentos = 3
ganadas = 0
perdidas = 0
historial_intentos = []

# Funciones
def cargar_imagen(ruta, tamaño=(300, 300)):
    try:
        imagen = Image.open(ruta)
        imagen = imagen.resize(tamaño)
        return ImageTk.PhotoImage(imagen)
    except FileNotFoundError:
        print(f"Advertencia: No se encontró {ruta}")
        return None

def comenzar_partida():
    pantalla_inicio.destroy()
    ventana.after(300, iniciar_juego)  # pequeña transición suave

def iniciar_juego():
    nuevo_juego()
    mostrar_juego()

def nuevo_juego():
    global culpable, arma, locacion, intentos, historial_intentos
    culpable, arma, locacion = random.choice(list(historias.keys()))  # Selección aleatoria de culpable, arma y locación
    intentos = 3
    historial_intentos.clear()
    actualizar_imagen()
    pista_label.config(text="Pista: ???")
    mensaje_label.config(text="")
    historial_text.delete(1.0, tk.END)
    actualizar_contador()

def actualizar_imagen():
    nombre_imagen = f"{culpable.lower().replace(' ', '_')}.png"
    imagen = cargar_imagen(nombre_imagen)
    if imagen:
        canvas.itemconfig(personaje_imagen_id, image=imagen)
        canvas.image = imagen  # para no perder referencia

def verificar():
    global intentos, ganadas, perdidas

    seleccion_culpable = culpable_var.get()
    seleccion_arma = arma_var.get()
    seleccion_locacion = locacion_var.get()

    intento_actual = f"{seleccion_culpable} con {seleccion_arma} en {seleccion_locacion}"

    if (seleccion_culpable, seleccion_arma, seleccion_locacion) == (culpable, arma, locacion):
        mensaje_label.config(text="🎉 ¡Correcto!", fg="green")
        ganadas += 1
        mostrar_historia(finalizado=True)
    else:
        intentos -= 1
        historial_intentos.append(f"❌ {intento_actual}")
        actualizar_historial()

        if intentos > 0:
            mensaje_label.config(text=f"❌ Incorrecto. Te quedan {intentos} intentos.", fg="red")
            pista_label.config(text=pistas.get((culpable, arma, locacion), ""))
        else:
            mensaje_label.config(text="💀 ¡Juego terminado!", fg="red")
            perdidas += 1
            mostrar_historia(finalizado=True)

    actualizar_contador()

def mostrar_historia(finalizado=False):
    historia = historias.get((culpable, arma, locacion), "No se encontró historia.")
    messagebox.showinfo("Resultado Final", f"{culpable} con {arma} en {locacion}\n\n{historia}")
    if finalizado:
        nuevo_juego()

def actualizar_historial():
    historial_text.delete(1.0, tk.END)
    for intento in historial_intentos:
        historial_text.insert(tk.END, intento + "\n")

def actualizar_contador():
    contador_label.config(text=f"Ganadas: {ganadas} | Perdidas: {perdidas}")

def mostrar_juego():
    juego_frame.pack()

# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Clue 2.2 - Misterio Interactivo")
ventana.geometry("1000x750")
ventana.configure(bg="#f0f8ff")

# --- Pantalla de inicio ---
pantalla_inicio = tk.Frame(ventana, bg="#f0f8ff")
pantalla_inicio.pack(expand=True)

titulo_inicio = tk.Label(pantalla_inicio, text="🔍 Bienvenido a Clue Misterioso 🔍", font=("Arial", 28), bg="#f0f8ff")
titulo_inicio.pack(pady=40)

boton_comenzar = tk.Button(pantalla_inicio, text="Comenzar Partida", font=("Arial", 20), bg="blue", fg="white", command=comenzar_partida)
boton_comenzar.pack(pady=20)

# --- Juego Frame ---
juego_frame = tk.Frame(ventana, bg="#f0f8ff")

# Canvas con fondo
fondo = cargar_imagen("fondo.png", tamaño=(1000, 750))
canvas = tk.Canvas(juego_frame, width=1000, height=750)
canvas.pack()
if fondo:
    canvas.create_image(0, 0, anchor="nw", image=fondo)

# Imagen personaje
placeholder = cargar_imagen("placeholder.png", tamaño=(300, 300))
personaje_imagen_id = canvas.create_image(650, 400, anchor="nw", image=placeholder)
canvas.image = placeholder

# Variables de selección
culpable_var = tk.StringVar(value=personajes[0])
arma_var = tk.StringVar(value=armas[0])
locacion_var = tk.StringVar(value=locaciones[0])

# Menús
tk.Label(juego_frame, text="Culpable:", font=("Arial", 14), bg="#f0f8ff").place(x=20, y=20)
tk.OptionMenu(juego_frame, culpable_var, *personajes).place(x=120, y=20)

tk.Label(juego_frame, text="Arma:", font=("Arial", 14), bg="#f0f8ff").place(x=20, y=70)
tk.OptionMenu(juego_frame, arma_var, *armas).place(x=120, y=70)

tk.Label(juego_frame, text="Locación:", font=("Arial", 14), bg="#f0f8ff").place(x=20, y=120)
tk.OptionMenu(juego_frame, locacion_var, *locaciones).place(x=120, y=120)

confirmar_btn = tk.Button(juego_frame, text="Confirmar", font=("Arial", 16), bg="green", fg="white", command=verificar)
confirmar_btn.place(x=100, y=180)

# Mensajes
mensaje_label = tk.Label(juego_frame, text="", font=("Arial", 20), bg="#f0f8ff")
mensaje_label.place(x=30, y=250)

pista_label = tk.Label(juego_frame, text="Pista: ???", font=("Arial", 14), bg="#f0f8ff", fg="blue")
pista_label.place(x=30, y=300)

# Contador
contador_label = tk.Label(juego_frame, text="Ganadas: 0 | Perdidas: 0", font=("Arial", 14), bg="#f0f8ff", fg="darkgreen")
contador_label.place(x=30, y=350)

# Historial
tk.Label(juego_frame, text="Historial de Intentos:", font=("Arial", 14), bg="#f0f8ff").place(x=30, y=400)
historial_text = tk.Text(juego_frame, height=10, width=50, font=("Arial", 12))
historial_text.place(x=30, y=440)

# --- Fin del Juego Frame ---

ventana.mainloop()
