import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os

def analizar_codigo():
    # 1. Obtener el texto del área de entrada
    codigo = text_area.get("1.0", tk.END).strip()
    if not codigo:
        messagebox.showwarning("Advertencia", "Ingresa código para analizar.")
        return

    # 2. Guardar el código en un archivo de texto temporal
    archivo_temp = "temp.txt"
    with open(archivo_temp, "w", encoding="utf-8") as f:
        f.write(codigo)

    # 3. Limpiar la tabla de resultados anterior
    for row in tabla.get_children():
        tabla.delete(row)

    # 4. Ejecutar el analizador léxico (C/FLEX) mediante un subproceso
    try:
        # Llama al ejecutable pasando el archivo temporal como argumento
        proceso = subprocess.run(
            ["./AnalizadorLexico.exe", archivo_temp], 
            capture_output=True, 
            text=True
        )
        
        # 5. Procesar la salida estándar (stdout) del ejecutable
        lineas = proceso.stdout.split('\n')
        for linea in lineas:
            if "|" in linea:
                # Divide la salida por el carácter "|"
                tipo_token, lexema = linea.split("|", 1)
                # Inserta los datos en la tabla
                tabla.insert("", tk.END, values=(tipo_token.strip(), lexema.strip()))
                
    except FileNotFoundError:
        messagebox.showerror("Error Fatal", "No se encontró 'AnalizadorLexico.exe'. Verifica que esté compilado en la misma carpeta.")
    
    # 6. Limpieza: Eliminar el archivo temporal
    finally:
        if os.path.exists(archivo_temp):
            os.remove(archivo_temp)

# --- Configuración de la Interfaz Gráfica (UI) ---
root = tk.Tk()
root.title("Analizador Léxico - Compiladores")
root.geometry("600x550")
root.configure(padx=20, pady=20)

# Etiqueta superior
lbl_titulo = tk.Label(root, text="Ingrese el código fuente:", font=("Arial", 12, "bold"))
lbl_titulo.pack(anchor="w", pady=(0, 5))

# Área de texto para ingresar código
text_area = tk.Text(root, height=10, width=70, font=("Consolas", 11))
text_area.pack(fill="x", pady=(0, 10))

# Botón de análisis
btn_analizar = tk.Button(root, text="Analizar Código", command=analizar_codigo, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"))
btn_analizar.pack(pady=10)

# Configuración de la Tabla (Treeview)
columnas = ("Tipo de Token", "Lexema")
tabla = ttk.Treeview(root, columns=columnas, show="headings", height=12)

# Definir encabezados de la tabla
tabla.heading("Tipo de Token", text="Tipo de Token")
tabla.heading("Lexema", text="Lexema")

# Definir tamaño de columnas
tabla.column("Tipo de Token", width=250, anchor="center")
tabla.column("Lexema", width=250, anchor="w")

tabla.pack(fill="both", expand=True)

# Iniciar el bucle de la aplicación
root.mainloop()
