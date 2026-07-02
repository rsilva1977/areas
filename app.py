#!/usr/bin/env python3
"""App simples para calcular a área de um quadrado.

O utilizador fornece o comprimento do lado e a app imprime a área.
"""

def ler_lado():
    while True:
        try:
            valor = input("Insira o comprimento do lado do quadrado: ")
            lado = float(valor.replace(',', '.'))
            if lado < 0:
                print("O comprimento não pode ser negativo. Tente novamente.")
                continue
            return lado
        except ValueError:
            print("Valor inválido. Introduza um número (por ex. 3.5).")


def calcula_area(lado: float) -> float:
    return lado * lado


def main():
    lado = ler_lado()
    area = calcula_area(lado)
    print(f"Área do quadrado: {area}")


if __name__ == "__main__":
    main()
