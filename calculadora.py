#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora Simples em Python
Suporta todas as operações matemáticas básicas
"""

import math


def adicao(a, b):
    """Realiza a adição de dois números"""
    return a + b


def subtracao(a, b):
    """Realiza a subtração de dois números"""
    return a - b


def multiplicacao(a, b):
    """Realiza a multiplicação de dois números"""
    return a * b


def divisao(a, b):
    """Realiza a divisão de dois números"""
    if b == 0:
        raise ValueError("Erro: Divisão por zero não é permitida!")
    return a / b


def potencia(a, b):
    """Eleva 'a' à potência de 'b'"""
    return a ** b


def raiz_quadrada(a):
    """Calcula a raiz quadrada de um número"""
    if a < 0:
        raise ValueError("Erro: Não é possível calcular raiz quadrada de número negativo!")
    return math.sqrt(a)


def raiz_n_esima(a, n):
    """Calcula a raiz n-ésima de um número"""
    if a < 0 and n % 2 == 0:
        raise ValueError("Erro: Não é possível calcular raiz par de número negativo!")
    if n == 0:
        raise ValueError("Erro: Índice da raiz não pode ser zero!")
    return a ** (1 / n)


def resto_divisao(a, b):
    """Calcula o resto da divisão (módulo)"""
    if b == 0:
        raise ValueError("Erro: Divisão por zero não é permitida!")
    return a % b


def divisao_inteira(a, b):
    """Realiza a divisão inteira de dois números"""
    if b == 0:
        raise ValueError("Erro: Divisão por zero não é permitida!")
    return a // b


def fatorial(n):
    """Calcula o fatorial de um número"""
    if n < 0:
        raise ValueError("Erro: Fatorial não é definido para números negativos!")
    if not isinstance(n, int):
        raise ValueError("Erro: Fatorial só é definido para números inteiros!")
    return math.factorial(n)


def logaritmo(a, base=10):
    """Calcula o logaritmo de um número"""
    if a <= 0:
        raise ValueError("Erro: Logaritmo só é definido para números positivos!")
    if base <= 0 or base == 1:
        raise ValueError("Erro: Base do logaritmo deve ser positiva e diferente de 1!")
    return math.log(a, base)


def seno(angulo_graus):
    """Calcula o seno de um ângulo em graus"""
    return math.sin(math.radians(angulo_graus))


def cosseno(angulo_graus):
    """Calcula o cosseno de um ângulo em graus"""
    return math.cos(math.radians(angulo_graus))


def tangente(angulo_graus):
    """Calcula a tangente de um ângulo em graus"""
    return math.tan(math.radians(angulo_graus))


def exibir_menu():
    """Exibe o menu de opções da calculadora"""
    print("\n" + "="*50)
    print("          CALCULADORA SIMPLES")
    print("="*50)
    print("1.  Adição (+)")
    print("2.  Subtração (-)")
    print("3.  Multiplicação (*)")
    print("4.  Divisão (/)")
    print("5.  Potenciação (^)")
    print("6.  Raiz Quadrada (√)")
    print("7.  Raiz N-ésima")
    print("8.  Resto da Divisão (Módulo %)")
    print("9.  Divisão Inteira (//)")
    print("10. Fatorial (!)")
    print("11. Logaritmo")
    print("12. Seno")
    print("13. Cosseno")
    print("14. Tangente")
    print("0.  Sair")
    print("="*50)


def obter_numero(mensagem="Digite um número: "):
    """Obtém um número válido do usuário"""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Por favor, digite um número válido!")


def obter_numero_inteiro(mensagem="Digite um número inteiro: "):
    """Obtém um número inteiro válido do usuário"""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido!")


def main():
    """Função principal da calculadora"""
    print("Bem-vindo à Calculadora Simples!")
    
    while True:
        exibir_menu()
        escolha = input("\nEscolha uma opção: ").strip()
        
        if escolha == "0":
            print("\nObrigado por usar a calculadora! Até logo!")
            break
        
        try:
            if escolha == "1":
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = adicao(a, b)
                print(f"\nResultado: {a} + {b} = {resultado}")
            
            elif escolha == "2":
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = subtracao(a, b)
                print(f"\nResultado: {a} - {b} = {resultado}")
            
            elif escolha == "3":
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = multiplicacao(a, b)
                print(f"\nResultado: {a} × {b} = {resultado}")
            
            elif escolha == "4":
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = divisao(a, b)
                print(f"\nResultado: {a} ÷ {b} = {resultado}")
            
            elif escolha == "5":
                a = obter_numero("Digite a base: ")
                b = obter_numero("Digite o expoente: ")
                resultado = potencia(a, b)
                print(f"\nResultado: {a} ^ {b} = {resultado}")
            
            elif escolha == "6":
                a = obter_numero("Digite o número: ")
                resultado = raiz_quadrada(a)
                print(f"\nResultado: √{a} = {resultado}")
            
            elif escolha == "7":
                a = obter_numero("Digite o número: ")
                n = obter_numero("Digite o índice da raiz: ")
                resultado = raiz_n_esima(a, n)
                print(f"\nResultado: {n}√{a} = {resultado}")
            
            elif escolha == "8":
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = resto_divisao(a, b)
                print(f"\nResultado: {a} % {b} = {resultado}")
            
            elif escolha == "9":
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = divisao_inteira(a, b)
                print(f"\nResultado: {a} // {b} = {resultado}")
            
            elif escolha == "10":
                n = obter_numero_inteiro("Digite um número inteiro: ")
                resultado = fatorial(n)
                print(f"\nResultado: {n}! = {resultado}")
            
            elif escolha == "11":
                a = obter_numero("Digite o número: ")
                base = input("Digite a base do logaritmo (Enter para base 10): ").strip()
                if base == "":
                    base = 10
                else:
                    base = float(base)
                resultado = logaritmo(a, base)
                print(f"\nResultado: log_{base}({a}) = {resultado}")
            
            elif escolha == "12":
                angulo = obter_numero("Digite o ângulo em graus: ")
                resultado = seno(angulo)
                print(f"\nResultado: sen({angulo}°) = {resultado}")
            
            elif escolha == "13":
                angulo = obter_numero("Digite o ângulo em graus: ")
                resultado = cosseno(angulo)
                print(f"\nResultado: cos({angulo}°) = {resultado}")
            
            elif escolha == "14":
                angulo = obter_numero("Digite o ângulo em graus: ")
                resultado = tangente(angulo)
                print(f"\nResultado: tan({angulo}°) = {resultado}")
            
            else:
                print("\nOpção inválida! Por favor, escolha uma opção do menu.")
        
        except ValueError as e:
            print(f"\n{e}")
        except Exception as e:
            print(f"\nErro inesperado: {e}")
        
        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()

