#!/bin/bash
# Script para executar a calculadora Streamlit

# Verifica se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv venv
fi

# Ativa o ambiente virtual
echo "Ativando ambiente virtual..."
source venv/bin/activate

# Verifica se o Streamlit está instalado
if ! python3 -c "import streamlit" 2>/dev/null; then
    echo "Instalando Streamlit..."
    pip install -r requirements.txt
fi

# Executa a aplicação
echo "Iniciando calculadora Streamlit..."
streamlit run calculadora_streamlit.py

