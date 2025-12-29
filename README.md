# Calculadora Científica

Uma calculadora completa com interface web moderna (React + TypeScript) e versão em Python que suporta todas as operações matemáticas básicas e avançadas.

## Funcionalidades

- ✅ Operações básicas: Adição, Subtração, Multiplicação, Divisão
- ✅ Potenciação e Raízes (quadrada e n-ésima)
- ✅ Divisão inteira e Resto da divisão (módulo)
- ✅ Fatorial
- ✅ Logaritmo
- ✅ Funções trigonométricas: Seno, Cosseno, Tangente

## 🚀 Frontend Web (React + TypeScript)

### Requisitos do Frontend

- Node.js 18 ou superior
- npm ou yarn

### Como executar o Frontend

1. Instale as dependências:
```bash
npm install
```

2. Execute o servidor de desenvolvimento:
```bash
npm run dev
```

3. Abra seu navegador em `http://localhost:5173`

4. A calculadora estará disponível com interface moderna e todas as funcionalidades!

### Funcionalidades do Frontend

- ✅ Interface moderna e responsiva
- ✅ Modo científico e básico (alternável)
- ✅ Histórico de cálculos
- ✅ Memória (MC, MR, M+, M-)
- ✅ Modo DEG/RAD para funções trigonométricas
- ✅ Todas as operações matemáticas disponíveis

## 🐍 Versão Python (CLI)

### Requisitos Python

- Python 3.6 ou superior
- Biblioteca padrão `math` (já incluída no Python)

### Como usar a versão Python

1. Execute o programa:
```bash
python3 calculadora.py
```

2. Escolha uma operação do menu e siga as instruções na tela.

## Exemplo de uso

```
Bem-vindo à Calculadora Simples!

==================================================
          CALCULADORA SIMPLES
==================================================
1.  Adição (+)
2.  Subtração (-)
3.  Multiplicação (*)
4.  Divisão (/)
5.  Potenciação (^)
6.  Raiz Quadrada (√)
7.  Raiz N-ésima
8.  Resto da Divisão (Módulo %)
9.  Divisão Inteira (//)
10. Fatorial (!)
11. Logaritmo
12. Seno
13. Cosseno
14. Tangente
0.  Sair
==================================================

Escolha uma opção: 1
Digite o primeiro número: 10
Digite o segundo número: 5
Resultado: 10.0 + 5.0 = 15.0
```

## 📁 Estrutura do Projeto

```
CursorAI_Lab/
├── calculadora.py          # Versão Python (CLI)
├── package.json            # Dependências do frontend
├── vite.config.ts          # Configuração do Vite
├── tsconfig.json           # Configuração TypeScript
├── index.html              # HTML principal
├── src/
│   ├── main.tsx           # Ponto de entrada React
│   ├── App.tsx             # Componente principal da calculadora
│   ├── index.css           # Estilos globais
│   └── lib/
│       └── utils.ts        # Utilitários (cn function)
└── README.md               # Este arquivo
```

## Licença

Este projeto é de código aberto e está disponível para uso livre.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.


