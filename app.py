#!/usr/bin/env python3
"""App simples para calcular a área de um quadrado ou de um retângulo."""


def ler_numero(prompt: str) -> float:
    while True:
        try:
            valor = input(prompt)
            numero = float(valor.replace(',', '.'))
            if numero < 0:
                print("O valor não pode ser negativo. Tente novamente.")
                continue
            return numero
        except ValueError:
            print("Valor inválido. Introduza um número (por ex. 3.5).")


def calcula_area_quadrado(lado: float) -> float:
    return lado * lado


def calcula_area_retangulo(base: float, altura: float) -> float:
    return base * altura


def calcula_area_circulo(raio: float) -> float:
    import math
    return math.pi * raio * raio


def main():
    print("Escolha uma opção:")
    print("1 - Calcular a área de um quadrado")
    print("2 - Calcular a área de um retângulo")
    print("3 - Calcular a área de um círculo")

    while True:
        escolha = input("Opção: ").strip()

        if escolha == "1":
            lado = ler_numero("Insira o comprimento do lado do quadrado: ")
            area = calcula_area_quadrado(lado)
            print(f"Área do quadrado: {area}")
            break

        if escolha == "2":
            base = ler_numero("Insira a base do retângulo: ")
            altura = ler_numero("Insira a altura do retângulo: ")
            area = calcula_area_retangulo(base, altura)
            print(f"Área do retângulo: {area}")
            break

        if escolha == "3":
            raio = ler_numero("Insira o raio do círculo: ")
            area = calcula_area_circulo(raio)
            print(f"Área do círculo: {area}")
            break

        print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
