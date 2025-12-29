#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora Científica com Streamlit
Interface web moderna para calculadora científica completa
"""

import streamlit as st
import math
from typing import Optional

# Configuração da página
st.set_page_config(
    page_title="Calculadora Científica",
    page_icon="🔢",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS customizado para melhorar a aparência
st.markdown("""
<style>
    .main {
        padding: 1rem;
    }
    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 8px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: scale(0.98);
    }
    .display-box {
        background-color: #000000;
        color: #FFFFFF;
        padding: 20px;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
        font-size: 32px;
        text-align: right;
        margin-bottom: 20px;
        min-height: 80px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
    }
    .history-box {
        background-color: #1F2937;
        color: #9CA3AF;
        padding: 15px;
        border-radius: 8px;
        min-height: 100px;
        max-height: 150px;
        overflow-y: auto;
        margin-bottom: 20px;
        font-size: 12px;
    }
    .operation-button {
        background-color: #F97316;
        color: white;
    }
    .scientific-button {
        background-color: #2563EB;
        color: white;
    }
    .function-button {
        background-color: #6B7280;
        color: white;
    }
    .number-button {
        background-color: #374151;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar estado da sessão
if 'display' not in st.session_state:
    st.session_state.display = "0"
if 'previous_value' not in st.session_state:
    st.session_state.previous_value = None
if 'operation' not in st.session_state:
    st.session_state.operation = None
if 'waiting_for_operand' not in st.session_state:
    st.session_state.waiting_for_operand = False
if 'history' not in st.session_state:
    st.session_state.history = []
if 'memory' not in st.session_state:
    st.session_state.memory = 0
if 'angle_mode' not in st.session_state:
    st.session_state.angle_mode = "DEG"
if 'scientific_mode' not in st.session_state:
    st.session_state.scientific_mode = True

def format_display(value: float) -> str:
    """Formata o valor para exibição"""
    if not math.isfinite(value):
        return "Infinity" if value > 0 else "-Infinity"
    if math.isnan(value):
        return "Error"
    
    str_value = str(value)
    if len(str_value) <= 12:
        return str_value
    
    if '.' in str_value:
        int_part, dec_part = str_value.split('.')
        available_decimals = 12 - len(int_part) - 1
        if available_decimals > 0:
            return f"{value:.{min(available_decimals, len(dec_part))}f}"
    
    return f"{value:.5e}"

def to_radians(degrees: float) -> float:
    """Converte graus para radianos"""
    return degrees * (math.pi / 180)

def factorial(n: float) -> float:
    """Calcula o fatorial"""
    if n < 0 or not n.is_integer():
        return float('nan')
    n = int(n)
    if n == 0 or n == 1:
        return 1.0
    result = 1
    for i in range(2, n + 1):
        result *= i
    return float(result)

def input_number(num: str):
    """Adiciona um número ao display"""
    if st.session_state.waiting_for_operand:
        st.session_state.display = num
        st.session_state.waiting_for_operand = False
    else:
        new_display = num if st.session_state.display == "0" else st.session_state.display + num
        if len(new_display.replace('.', '').replace('-', '')) <= 12:
            st.session_state.display = new_display

def input_operation(op: str):
    """Processa uma operação"""
    try:
        input_value = float(st.session_state.display)
        
        if st.session_state.previous_value is None:
            st.session_state.previous_value = input_value
        elif st.session_state.operation:
            current_value = st.session_state.previous_value or 0
            new_value = calculate(current_value, input_value, st.session_state.operation)
            st.session_state.display = format_display(new_value)
            st.session_state.previous_value = new_value
            st.session_state.history.append(
                f"{current_value} {st.session_state.operation} {input_value} = {new_value}"
            )
            if len(st.session_state.history) > 10:
                st.session_state.history.pop(0)
        
        st.session_state.waiting_for_operand = True
        st.session_state.operation = op
    except Exception as e:
        st.session_state.display = "Error"
        st.error(f"Erro: {e}")

def calculate(first: float, second: float, op: str) -> float:
    """Realiza o cálculo"""
    try:
        if op == "+":
            return first + second
        elif op == "-":
            return first - second
        elif op == "×":
            return first * second
        elif op == "÷":
            if second == 0:
                raise ValueError("Divisão por zero!")
            return first / second
        elif op == "^":
            return first ** second
        else:
            return second
    except Exception as e:
        raise ValueError(f"Erro no cálculo: {e}")

def perform_calculation():
    """Executa o cálculo final"""
    try:
        input_value = float(st.session_state.display)
        if st.session_state.previous_value is not None and st.session_state.operation:
            new_value = calculate(st.session_state.previous_value, input_value, st.session_state.operation)
            st.session_state.display = format_display(new_value)
            st.session_state.history.append(
                f"{st.session_state.previous_value} {st.session_state.operation} {input_value} = {new_value}"
            )
            if len(st.session_state.history) > 10:
                st.session_state.history.pop(0)
            st.session_state.previous_value = None
            st.session_state.operation = None
            st.session_state.waiting_for_operand = True
    except Exception as e:
        st.session_state.display = "Error"
        st.error(f"Erro: {e}")

def clear():
    """Limpa a calculadora"""
    st.session_state.display = "0"
    st.session_state.previous_value = None
    st.session_state.operation = None
    st.session_state.waiting_for_operand = False

def clear_history():
    """Limpa o histórico"""
    st.session_state.history = []

def backspace():
    """Remove o último caractere"""
    if len(st.session_state.display) > 1:
        st.session_state.display = st.session_state.display[:-1]
    else:
        st.session_state.display = "0"

def handle_scientific_function(func: str):
    """Processa funções científicas"""
    try:
        current_value = float(st.session_state.display)
        result = 0.0
        
        if func == "sin":
            angle = to_radians(current_value) if st.session_state.angle_mode == "DEG" else current_value
            result = math.sin(angle)
        elif func == "cos":
            angle = to_radians(current_value) if st.session_state.angle_mode == "DEG" else current_value
            result = math.cos(angle)
        elif func == "tan":
            angle = to_radians(current_value) if st.session_state.angle_mode == "DEG" else current_value
            result = math.tan(angle)
        elif func == "ln":
            if current_value <= 0:
                raise ValueError("Logaritmo natural requer número positivo")
            result = math.log(current_value)
        elif func == "log":
            if current_value <= 0:
                raise ValueError("Logaritmo requer número positivo")
            result = math.log10(current_value)
        elif func == "√":
            if current_value < 0:
                raise ValueError("Raiz quadrada requer número não negativo")
            result = math.sqrt(current_value)
        elif func == "∛":
            result = current_value ** (1/3)
        elif func == "x²":
            result = current_value ** 2
        elif func == "x³":
            result = current_value ** 3
        elif func == "1/x":
            if current_value == 0:
                raise ValueError("Divisão por zero")
            result = 1 / current_value
        elif func == "!":
            result = factorial(current_value)
        elif func == "e":
            result = math.e
        elif func == "π":
            result = math.pi
        elif func == "e^x":
            result = math.exp(current_value)
        elif func == "10^x":
            result = 10 ** current_value
        else:
            result = current_value
        
        st.session_state.display = format_display(result)
        st.session_state.history.append(f"{func}({current_value}) = {result}")
        if len(st.session_state.history) > 10:
            st.session_state.history.pop(0)
        st.session_state.waiting_for_operand = True
    except Exception as e:
        st.session_state.display = "Error"
        st.error(f"Erro: {e}")

# Interface principal
st.title("🔢 Calculadora Científica")

# Controles superiores
col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

with col1:
    st.write("")

with col2:
    if st.button("🔄 Básica" if st.session_state.scientific_mode else "🔬 Científica"):
        st.session_state.scientific_mode = not st.session_state.scientific_mode
        st.rerun()

with col3:
    if st.button("⌫"):
        backspace()
        st.rerun()

with col4:
    if st.button("🗑️"):
        clear_history()
        st.rerun()

# Histórico
if st.session_state.history:
    st.markdown('<div class="history-box">', unsafe_allow_html=True)
    for entry in st.session_state.history[-5:]:
        st.text(entry)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="history-box">Histórico aparecerá aqui</div>', unsafe_allow_html=True)

# Display
display_info = ""
if st.session_state.memory != 0:
    display_info += "M "
display_info += st.session_state.angle_mode
if st.session_state.operation and st.session_state.previous_value is not None:
    display_info += f" | {st.session_state.previous_value} {st.session_state.operation}"

st.markdown(f'<div class="display-box">{st.session_state.display}</div>', unsafe_allow_html=True)
st.caption(display_info)

# Botões científicos (se ativado)
if st.session_state.scientific_mode:
    st.subheader("Funções Científicas")
    
    # Linha 1: Trigonometria e modo angular
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("DEG/RAD"):
            st.session_state.angle_mode = "RAD" if st.session_state.angle_mode == "DEG" else "DEG"
            st.rerun()
    with col2:
        if st.button("sin"):
            handle_scientific_function("sin")
            st.rerun()
    with col3:
        if st.button("cos"):
            handle_scientific_function("cos")
            st.rerun()
    with col4:
        if st.button("tan"):
            handle_scientific_function("tan")
            st.rerun()
    with col5:
        if st.button("x^y"):
            input_operation("^")
            st.rerun()
    
    # Linha 2: Logaritmos e raízes
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("ln"):
            handle_scientific_function("ln")
            st.rerun()
    with col2:
        if st.button("log"):
            handle_scientific_function("log")
            st.rerun()
    with col3:
        if st.button("√"):
            handle_scientific_function("√")
            st.rerun()
    with col4:
        if st.button("∛"):
            handle_scientific_function("∛")
            st.rerun()
    with col5:
        if st.button("n!"):
            handle_scientific_function("!")
            st.rerun()
    
    # Linha 3: Potências e inversos
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("x²"):
            handle_scientific_function("x²")
            st.rerun()
    with col2:
        if st.button("x³"):
            handle_scientific_function("x³")
            st.rerun()
    with col3:
        if st.button("1/x"):
            handle_scientific_function("1/x")
            st.rerun()
    with col4:
        if st.button("e^x"):
            handle_scientific_function("e^x")
            st.rerun()
    with col5:
        if st.button("10^x"):
            handle_scientific_function("10^x")
            st.rerun()
    
    # Linha 4: Memória e constantes
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("MC"):
            st.session_state.memory = 0
            st.rerun()
    with col2:
        if st.button("MR"):
            st.session_state.display = format_display(st.session_state.memory)
            st.session_state.waiting_for_operand = True
            st.rerun()
    with col3:
        if st.button("M+"):
            st.session_state.memory += float(st.session_state.display)
            st.rerun()
    with col4:
        if st.button("M-"):
            st.session_state.memory -= float(st.session_state.display)
            st.rerun()
    with col5:
        if st.button("π"):
            handle_scientific_function("π")
            st.rerun()

# Botões básicos
st.subheader("Operações Básicas")

# Linha 1: Limpar e operações
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("C"):
        clear()
        st.rerun()
with col2:
    if st.button("±"):
        try:
            new_value = float(st.session_state.display) * -1
            st.session_state.display = format_display(new_value)
            st.rerun()
        except:
            pass
with col3:
    if st.button("%"):
        try:
            new_value = float(st.session_state.display) / 100
            st.session_state.display = format_display(new_value)
            st.rerun()
        except:
            pass
with col4:
    if st.button("÷"):
        input_operation("÷")
        st.rerun()
with col5:
    if st.session_state.scientific_mode:
        if st.button("e"):
            handle_scientific_function("e")
            st.rerun()
    else:
        st.write("")

# Linha 2: Números 7-9 e multiplicação
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("7"):
        input_number("7")
        st.rerun()
with col2:
    if st.button("8"):
        input_number("8")
        st.rerun()
with col3:
    if st.button("9"):
        input_number("9")
        st.rerun()
with col4:
    if st.button("×"):
        input_operation("×")
        st.rerun()
with col5:
    st.write("")

# Linha 3: Números 4-6 e subtração
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("4"):
        input_number("4")
        st.rerun()
with col2:
    if st.button("5"):
        input_number("5")
        st.rerun()
with col3:
    if st.button("6"):
        input_number("6")
        st.rerun()
with col4:
    if st.button("-"):
        input_operation("-")
        st.rerun()
with col5:
    st.write("")

# Linha 4: Números 1-3 e adição
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("1"):
        input_number("1")
        st.rerun()
with col2:
    if st.button("2"):
        input_number("2")
        st.rerun()
with col3:
    if st.button("3"):
        input_number("3")
        st.rerun()
with col4:
    if st.button("+"):
        input_operation("+")
        st.rerun()
with col5:
    st.write("")

# Linha 5: Zero, ponto e igual
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("0"):
        input_number("0")
        st.rerun()
with col2:
    if st.button("."):
        if "." not in st.session_state.display:
            input_number(".")
            st.rerun()
with col3:
    if st.button("="):
        perform_calculation()
        st.rerun()
with col4:
    st.write("")
with col5:
    st.write("")

# Rodapé
st.markdown("---")
st.caption("Calculadora Científica desenvolvida com Streamlit")

