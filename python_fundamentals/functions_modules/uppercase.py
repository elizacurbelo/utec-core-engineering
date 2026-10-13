#!/usr/bin/env python3
def uppercase(str):
    resultado = ""
    for letra in str:
        if ord(letra) >= 97 and ord(letra) <= 122:
            resultado += chr(ord(letra) - 32)
        else:
            resultado += letra
    print("{}".format(resultado))

