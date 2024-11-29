import sqlite3

# Conexión a la base de datos
conexion = sqlite3.connect("recomendaciones_academicas.db")
cursor = conexion.cursor()

# Datos del estudiante
nombre = "Juan Perez"
materias = [
    ("Introducción a la Ingeniería", 4.5),
    ("Autómatas y Lenguajes Formales", 4.2),
    ("Gestión de Proyectos de TIC", 4.0),
    ("Ecuaciones Diferenciales", 3.8),
    ("Arquitectura de Computadores", 4.3)
]

# Insertar cada materia aprobada
for materia, nota in materias:
    cursor.execute("INSERT INTO estudiantes (nombre, curso_aprobado, nota) VALUES (?, ?, ?)", (nombre, materia, nota))

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Datos insertados con éxito.")
