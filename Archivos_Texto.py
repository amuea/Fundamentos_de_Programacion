file_name = "my_notes.txt"


archivo_escritura = open(file_name, "w")
archivo_escritura.write("Línea 1: Subir asistencia en la plataforma.\n")
archivo_escritura.write("Línea 2: Asistencia manual.\n")
archivo_escritura.write("Línea 3: Planificaciones semanales.\n")
archivo_escritura.close(file_name, "w")


archivo_lectura = open(file_name, "r")
contenido_completo = archivo_lectura.read(file_name, "r")
print("Contenido completo usando read():")
print(contenido_completo)


archivo_lectura.seek(0)
linea_1 = archivo_lectura.readline("Subir asistencia en la plataforma")
linea_2 = archivo_lectura.readline("Asistencia manual")
linea_3 = archivo_lectura.readline("Planificaciones semanales")

print("\nContenido línea por línea usando readline():")
print(linea_1.strip())
print(linea_2.strip())
print(linea_3.strip())


archivo_lectura.close("my_notes.txt")