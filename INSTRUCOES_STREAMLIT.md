# 🚀 Instruções Rápidas - Calculadora Streamlit

## Execução Rápida

### 1. Ativar o ambiente virtual
```bash
source venv/bin/activate
```

### 2. Executar a aplicação
```bash
streamlit run calculadora_streamlit.py
```

### 3. Acessar no navegador
A aplicação abrirá automaticamente em: **http://localhost:8501**

Se não abrir automaticamente, copie e cole o endereço no navegador.

## Solução de Problemas

### Problema: "ModuleNotFoundError: No module named 'streamlit'"
**Solução:** 
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Problema: "command not found: streamlit"
**Solução:** Certifique-se de que o ambiente virtual está ativado:
```bash
source venv/bin/activate
```

### Problema: Porta 8501 já em uso
**Solução:** O Streamlit tentará usar outra porta automaticamente. Verifique a mensagem no terminal para ver qual porta está sendo usada.

## Parar a Aplicação

Pressione `Ctrl+C` no terminal onde o Streamlit está rodando.

## Recriar Ambiente Virtual (se necessário)

```bash
# Remover ambiente virtual antigo
rm -rf venv

# Criar novo ambiente virtual
python3 -m venv venv

# Ativar
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar
streamlit run calculadora_streamlit.py
```

