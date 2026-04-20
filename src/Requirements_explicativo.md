# 📦 Guia Explicativo - requirements.txt

Este documento explica todas as bibliotecas utilizadas no projeto **Agentes Inteligentes com LangChain e LangGraph**, bem como sua finalidade dentro da arquitetura do sistema.

---

# 🧠 Objetivo

O arquivo `requirements.txt` contém todas as dependências necessárias para executar o projeto.

Ao instalar essas bibliotecas, garantimos que todos os integrantes utilizem o mesmo ambiente, evitando erros de incompatibilidade.

---

# 🚀 Como instalar as dependências

No terminal, execute:

```bash
pip install -r requirements.txt
```

---

# 📚 Bibliotecas utilizadas

## 🔹 1. Core do Projeto (LangChain + LangGraph)

### 📌 langchain

Biblioteca principal para criação de aplicações com LLMs (Large Language Models).

Permite:

* criação de agentes
* uso de prompts
* integração com ferramentas

---

### 📌 langgraph

Extensão do LangChain para construção de fluxos baseados em grafos.

Permite:

* controle de estado
* loops e ciclos
* execução complexa de agentes

---

### 📌 langchain-core

Contém componentes fundamentais do LangChain.

---

### 📌 langchain-community

Inclui integrações com ferramentas externas e recursos adicionais.

---

## 🤖 2. Integração com IA (Groq)

### 📌 langchain-groq

Integra o projeto com a API da Groq.

Permite:

* uso de modelos como LLaMA 3
* execução rápida e gratuita (dentro do plano free)

---

## 🔍 3. Monitoramento e Debug

### 📌 langsmith

Ferramenta para:

* rastrear execução dos agentes
* debug de fluxos
* análise de performance

---

## 🔐 4. Variáveis de Ambiente

### 📌 python-dotenv

Permite ler variáveis do arquivo `.env`.

Exemplo:

```env
GROQ_API_KEY=your_key_here
```

---

## 🧾 5. Estrutura e Validação de Dados

### 📌 pydantic

Usado para:

* validar dados
* estruturar estados (State)
* garantir consistência

---

## 🌐 6. Integração com APIs

### 📌 requests

Permite fazer requisições HTTP.

Usado para:

* consumir APIs externas
* criar tools (ferramentas)

---

## ⚡ 7. Performance e Otimização

### 📌 orjson

Biblioteca rápida para manipulação de JSON.

---

### 📌 aiohttp

Permite execução assíncrona.

Usado para:

* paralelismo
* múltiplas chamadas simultâneas

---

## 📊 8. Logging (Logs do Sistema)

### 📌 loguru

Facilita a criação de logs mais organizados.

---

## 🧠 9. Tipagem

### 📌 typing-extensions

Ajuda na tipagem do código Python.

---

## 🧪 10. Testes

### 📌 pytest

Framework para testes automatizados.

---

## 📅 11. Utilidades

### 📌 python-dateutil

Manipulação de datas e horários.

---

# 🔐 Variáveis de ambiente (.env)

Cada integrante deve criar um arquivo `.env` com sua própria chave:

```env
GROQ_API_KEY=your_key_here
```

---

## ⚠️ IMPORTANTE

* O arquivo `.env` NÃO deve ser enviado para o GitHub
* Ele já está ignorado pelo `.gitignore`

---

# 💰 Sobre custos

O projeto utiliza a plataforma **Groq**, que possui plano gratuito.

Isso permite:

* desenvolvimento sem custo inicial
* testes rápidos

---

# 🧠 Boas práticas

* Não remover bibliotecas sem alinhar com o grupo
* Sempre atualizar o `requirements.txt` ao adicionar novas dependências
* Testar após instalar novas bibliotecas

---

# 🚀 Conclusão

Este conjunto de bibliotecas foi escolhido para permitir:

* construção de agentes inteligentes
* uso de múltiplos agentes
* integração com ferramentas externas
* escalabilidade do projeto

---

Qualquer dúvida, alinhar com o grupo antes de alterar o ambiente 👍
