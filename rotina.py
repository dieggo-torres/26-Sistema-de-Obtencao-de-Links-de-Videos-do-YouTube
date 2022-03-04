# Importa a biblioteca time
import time


def esperar_elementos(elementos):
    while len(elementos) < 50:
        time.sleep(0.5)
    time.sleep(2)