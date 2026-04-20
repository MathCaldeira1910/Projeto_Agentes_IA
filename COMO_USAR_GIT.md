# 📘 Guia COMPLETO de GitHub para o Projeto

Este guia é para quem nunca usou GitHub. Siga exatamente os passos.

---

# 🧠 O que é GitHub?

* GitHub = onde o código do projeto fica armazenado
* Git = ferramenta que controla versões do código

👉 Vocês vão usar para:

* subir código
* baixar código
* trabalhar em grupo sem conflito

---

# 🔧 PRÉ-REQUISITOS (FAZER UMA VEZ)

## ✅ 1. Criar conta no GitHub

Acesse: https://github.com
Crie sua conta normalmente

---

## ✅ 2. Instalar o Git no computador

Acesse: https://git-scm.com/downloads
Instale com “Next, Next, Next”

---

## ✅ 3. Configurar seu nome (IMPORTANTE)

Abra o terminal (CMD ou PowerShell) e digite:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@email.com"
```

---

# 📥 1. BAIXAR O PROJETO (CLONE)

👉 Isso você faz **UMA ÚNICA VEZ**

### Passo a passo:

1. Vá no GitHub do projeto
2. Clique no botão verde **“Code”**
3. Copie o link

No terminal:

```bash
git clone https://github.com/SEU-USUARIO/projeto-agentes-ia.git
cd projeto-agentes-ia
```

---

# 🔄 2. SEMPRE ANTES DE COMEÇAR

👉 Antes de qualquer coisa, rode:

```bash
git pull
```

✔ Isso baixa as atualizações dos colegas
✔ Evita conflito

---

# 🛠️ 3. FAZER ALTERAÇÕES

👉 Agora você pode:

* abrir o projeto no VSCode
* ir até SUA pasta (muito importante)
* fazer suas alterações

---

# ⚠️ REGRA PRINCIPAL

👉 Trabalhe apenas na sua pasta:

* fundamentals → Matheus
* langgraph_core → Elder/Kyoko/Gabriel
* etc.

❌ NÃO mexa no código dos outros

---

# 💾 4. SALVAR SUAS ALTERAÇÕES (COMMIT + PUSH)

Depois de alterar arquivos:

### Passo 1 — adicionar arquivos

```bash
git add .
```

---

### Passo 2 — criar um commit

```bash
git commit -m "Expliquei conceitos de LangChain"
```

💡 Escreva o que você fez

---

### Passo 3 — enviar para o GitHub

```bash
git push
```

👉 Agora seu código está no projeto

---

# 🔁 5. ROTINA CORRETA (SEMPRE)

Toda vez que for trabalhar:

```bash
git pull
# faz alterações
git add .
git commit -m "o que fez"
git push
```

---

# 🚨 PROBLEMAS COMUNS

## ❌ ERRO: conflito de código

Se aparecer erro no `git pull`:

👉 NÃO tenta resolver sozinho
👉 chama no grupo

---

## ❌ ESQUECEU de dar pull

👉 Pode sobrescrever código de outro
👉 Sempre faça `git pull` primeiro

---

# 💡 ALTERNATIVA MAIS FÁCIL (SEM TERMINAL)

Se alguém tiver dificuldade:

👉 usar **GitHub Desktop**

Passos:

1. Baixar: https://desktop.github.com/
2. Fazer login
3. Clonar repositório
4. Usar botões:

   * Fetch
   * Pull
   * Commit
   * Push

👉 Interface gráfica, mais fácil

---

# 🧠 DICAS IMPORTANTES

* Faça commits pequenos (não tudo de uma vez)
* Teste antes de subir
* Se algo quebrar → avise o grupo

---

# ✅ RESUMO SIMPLES

| Ação           | Comando          |
| -------------- | ---------------- |
| Baixar projeto | git clone        |
| Atualizar      | git pull         |
| Salvar         | git add + commit |
| Enviar         | git push         |

---

# 🚀 CONCLUSÃO

Seguindo esse fluxo:

* ninguém perde código
* o projeto fica organizado
* o grupo consegue trabalhar junto sem problema

---

Se tiver dúvida → chama o grupo antes de fazer algo errado 👍
