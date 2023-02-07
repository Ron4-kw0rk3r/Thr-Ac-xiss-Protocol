import subprocess

# Especificar el nombre del script Bash
script_name = "script.sh"

# Ejecutar el script Bash utilizando `subprocess.call`
subprocess.call(["bash", script_name])




##########################3333333



# Importar el módulo `importlib`
import importlib.util

# Especificar el nombre del script externo
script_name = "script.py"

# Utilizar `importlib.util.spec_from_file_location` para obtener un especificación del script
spec = importlib.util.spec_from_file_location(script_name, script_name)

# Utilizar `importlib.util.module_from_spec` para crear un módulo a partir de la especificación
module = importlib.util.module_from_spec(spec)

# Utilizar `spec.loader.exec_module` para ejecutar el módulo
spec.loader.exec_module(module)

# Acceder a las variables y funciones del script externo a través del módulo
print(module.x) # 5
module.my_function() # imprime "Hello, World!"



import io

# Crea un buffer en memoria
buffer = io.StringIO()

# Abrir el archivo externo
with open("script.py", "r") as script:
    # Escribir el contenido del archivo externo en el buffer
    buffer.write(script.read())

# Mueve el puntero al inicio del buffer
buffer.seek(0)

# Ejecutar el script en el buffer
exec(buffer.read())


################################333



import io

# Crea un buffer en memoria
buffer = io.StringIO()

# Escribe varios scripts en el buffer
buffer.write("x = 5\n")
buffer.write("print('El valor de x es:', x)\n")
buffer.write("x += 3\n")
buffer.write("print('El nuevo valor de x es:', x)")

# Mueve el puntero al inicio del buffer
buffer.seek(0)

# Ejecuta el script en el buffer
exec(buffer.read())




