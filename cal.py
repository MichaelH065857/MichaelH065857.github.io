import random
import string

def generar_codigo():
    caracteres = string.ascii_letters + string.digits
    codigo = ''.join(random.choice(caracteres) for _ in range(8))
    return codigo

if __name__ == "__main__":
    print("Content-Type: text/html\n")
    codigo_generado = generar_codigo()
    print(f"<html><body><h1>Código Aleatorio</h1><p>{codigo_generado}</p></body></html>")
