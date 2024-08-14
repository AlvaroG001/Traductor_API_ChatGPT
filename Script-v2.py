import tkinter as tk
from tkinter import ttk
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("OPENAI_API_KEY")

if not key:
    raise ValueError("No se encontró la clave API. Asegúrate de que esté configurada correctamente.")

client = OpenAI(api_key=key)

def traducir():
    idioma_origen = origen_entry.get()
    idioma_destino = destino_entry.get()
    texto_a_traducir = texto_entry.get("1.0", tk.END).strip()

    if not texto_a_traducir:
        return

    # Actualizar la etiqueta de traducción al idioma de destino
    destino_label.config(text=f"Traducción al {idioma_destino}:")

    # Traducir del idioma de origen al idioma destino
    mensajes_a_destino = [
        {"role": "system", "content": f"Traduce el siguiente texto del {idioma_origen} al {idioma_destino}."},
        {"role": "user", "content": texto_a_traducir}
    ]
    respuesta_destino = client.chat.completions.create(
        model="gpt-4",
        messages=mensajes_a_destino,
        temperature=0.8,
        max_tokens=1000
    )
    texto_traducido = respuesta_destino.choices[0].message.content.strip()
    destino_text.delete("1.0", tk.END)
    destino_text.insert("1.0", texto_traducido)

    # Traducir del idioma destino al español
    mensajes_espanol = [
        {"role": "system", "content": f"Traduce el siguiente texto del {idioma_destino} al español."},
        {"role": "user", "content": texto_traducido}
    ]
    respuesta_espanol = client.chat.completions.create(
        model="gpt-4",
        messages=mensajes_espanol,
        temperature=0.8,
        max_tokens=1000
    )
    texto_espanol = respuesta_espanol.choices[0].message.content.strip()
    espanol_text.delete("1.0", tk.END)
    espanol_text.insert("1.0", texto_espanol)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Traductor")
root.configure(bg="#f2f2f2")
root.minsize(root.winfo_screenwidth(), 400)

# Ajuste columnas y filas al tamaño de la ventana
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(4, weight=1)

# Estilo
style = ttk.Style()
style.configure("TLabel", background="#f2f2f2", foreground="#333333", font=("Helvetica", 10))
style.configure("TButton", background="#ffffff", foreground="#333333", font=("Helvetica", 10, "bold"))

# Etiquetas y entradas
ttk.Label(root, text="Idioma de Origen:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
origen_entry = ttk.Entry(root, width=30)
origen_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew", columnspan=3)

ttk.Label(root, text="Idioma al que Traducir:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
destino_entry = ttk.Entry(root, width=30)
destino_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew", columnspan=3)

ttk.Label(root, text="Texto a Traducir:").grid(row=2, column=0, padx=10, pady=5, sticky="nw")
texto_entry = tk.Text(root, height=5, bd=2, relief="solid")
texto_entry.grid(row=2, column=1, padx=10, pady=5, sticky="nsew", columnspan=1)

# Etiqueta que se actualizará con el idioma de destino
destino_label = ttk.Label(root, text="Traducción al :", background="#f2f2f2", foreground="#333333", font=("Helvetica", 10))
destino_label.grid(row=2, column=2, padx=10, pady=5, sticky="nw")
destino_text = tk.Text(root, height=5, bd=2, relief="solid")
destino_text.grid(row=2, column=3, padx=10, pady=5, sticky="nsew", columnspan=1)

ttk.Label(root, text="Traducción al Español:").grid(row=3, column=0, columnspan=4, padx=10, pady=5, sticky="w")
espanol_text = tk.Text(root, height=3, bd=2, relief="solid")
espanol_text.grid(row=4, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

# Botón de traducción
traducir_button = ttk.Button(root, text="Traducir", command=traducir)
traducir_button.grid(row=5, column=0, columnspan=4, pady=20)

root.mainloop()
