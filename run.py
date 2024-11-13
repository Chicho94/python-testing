# run.py
import subprocess
import sys
import unittest

def ejecutar_main():
    """Ejecuta el archivo principal de la aplicación."""
    print("Ejecutando main.py...")
    subprocess.run(["python", "main.py"])

def ejecutar_pruebas(guardar_en_archivo=False):
    """Ejecuta todas las pruebas unitarias en la carpeta tests/ y guarda los resultados si se solicita."""
    print("Ejecutando pruebas unitarias...")

    # Cargar todas las pruebas desde la carpeta 'tests'
    tests = unittest.defaultTestLoader.discover('tests')
    
    if guardar_en_archivo:
        try:
            # Abrir archivo para almacenar los resultados
            with open("resultados_pruebas.txt", "w") as archivo_resultado:
                # Crear un TextTestRunner que escriba en el archivo
                test_runner = unittest.TextTestRunner(stream=archivo_resultado, verbosity=2)
                test_runner.run(tests)
            print("Resultados guardados en 'resultados_pruebas.txt'")
        except Exception as e:
            print(f"Ocurrió un error al guardar los resultados: {e}")
    else:
        # Ejecutar normalmente en la consola
        test_runner = unittest.TextTestRunner(verbosity=2)
        test_runner.run(tests)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()
        if comando == "main":
            ejecutar_main()
        elif comando == "test":
            # Verificar si se solicita guardar en archivo
            guardar = len(sys.argv) > 2 and sys.argv[2].lower() == "guardar"
            ejecutar_pruebas(guardar_en_archivo=guardar)
        else:
            print("Comando no reconocido. Usa 'main' para ejecutar la aplicación o 'test' para ejecutar pruebas.")
    else:
        print("Por favor, proporciona un comando: 'main' o 'test'.")
