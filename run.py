# run.py
import subprocess
import sys
import unittest

def ejecutar_main():
    """Ejecuta el archivo principal de la aplicación."""
    print("Ejecutando main.py...")
    subprocess.run(["python", "main.py"])

def ejecutar_pruebas_con_coverage():
    """Ejecuta pruebas unitarias con coverage y genera reportes."""
    print("Ejecutando pruebas con coverage...")
    
    try:
        # Ejecutar coverage run en la carpeta de pruebas
        subprocess.run(["coverage", "run", "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"], check=True)
        
        # Generar reporte en consola
        print("\nGenerando reporte de cobertura en consola:")
        subprocess.run(["coverage", "report", "--fail-under=99"], check=True)

        # Generar reporte HTML
        print("\nGenerando reporte HTML en la carpeta 'htmlcov':")
        subprocess.run(["coverage", "html"], check=True)
        print("\nReporte HTML generado en 'htmlcov/index.html'")
    except subprocess.CalledProcessError as e:
        print(f"Ocurrió un error al ejecutar coverage: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()
        if comando == "main":
            ejecutar_main()
        elif comando == "test":
            # Verificar si se solicita usar coverage
            usar_coverage = len(sys.argv) > 2 and sys.argv[2].lower() == "coverage"
            if usar_coverage:
                ejecutar_pruebas_con_coverage()
            else:
                # Ejecutar pruebas sin coverage
                print("Ejecutando pruebas unitarias sin coverage...")
                tests = unittest.defaultTestLoader.discover('tests')
                unittest.TextTestRunner(verbosity=2).run(tests)
        else:
            print("Comando no reconocido. Usa 'main' para ejecutar la aplicación o 'test' para ejecutar pruebas.")
    else:
        print("Por favor, proporciona un comando: 'main' o 'test'.")
