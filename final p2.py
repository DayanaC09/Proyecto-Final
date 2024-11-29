import sqlite3
import tkinter as tk
from tkinter import messagebox

def inicializar_base_datos():
    conexion = sqlite3.connect("recomendaciones_academicas.db")
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        curso_aprobado TEXT NOT NULL,
        nota REAL NOT NULL
    )
    """)
    conexion.commit()
    conexion.close()


def recomendar_cursos(nota):
    if nota >= 4.5:
        return ["Curso Avanzado de Matemáticas", "Seminario en Investigación Científica"]
    elif 4.0 <= nota < 4.5:
        return ["Curso de Algoritmos y Estructuras de Datos", "Programación Orientada a Objetos"]
    elif 3.5 <= nota < 4.0:
        return ["Taller de Resolución de Problemas", "Curso de Física Aplicada"]
    else:
        return ["Curso de Reforzamiento en Fundamentos", "Asesoría Académica"]


def mostrar_cursos_y_recomendaciones():
    nombre = entrada_nombre.get().strip()

    if not nombre:
        messagebox.showerror("Error", "Por favor, ingresa el nombre del estudiante.")
        return

    conexion = sqlite3.connect("recomendaciones_academicas.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT DISTINCT curso_aprobado, nota FROM estudiantes WHERE nombre = ?", (nombre,))
    resultados = cursor.fetchall()

    if not resultados:
        messagebox.showerror("Error", f"No se encontraron registros para el estudiante: {nombre}")
        conexion.close()
        return

    conexion.close()


    salida = f"Cursos Aprobados y Recomendaciones para {nombre}:\n\n"

    for curso, nota in resultados:
        salida += f"- {curso} (Nota: {nota})\n  Recomendaciones:\n"
        recomendaciones = recomendar_cursos(nota)  
        for rec in recomendaciones:
            salida += f"    - {rec}\n"
        salida += "\n"
        
    messagebox.showinfo("Cursos y Recomendaciones", salida)



    salida = f"Cursos Aprobados y Recomendaciones para {nombre}:\n\n"
    recomendaciones_generales = set()

    for curso, nota in resultados:
        salida += f"- {curso} (Nota: {nota})\n"
        recomendaciones = recomendar_cursos(nota)
        recomendaciones_generales.update(recomendaciones)

    salida += "\nRecomendaciones Generales:\n"
    for rec in recomendaciones_generales:
        salida += f"- {rec}\n"

    


inicializar_base_datos()


ventana = tk.Tk()
ventana.title("Sistema de Recomendación Académica")
ventana.geometry("500x200")

tk.Label(ventana, text="Nombre del estudiante:").pack(pady=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=5)

tk.Button(ventana, text="Buscar Cursos y Recomendaciones", command=mostrar_cursos_y_recomendaciones).pack(pady=20)

ventana.mainloop()
