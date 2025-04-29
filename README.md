
# 🤖 Bot FURIA CS

Este é um chatbot desenvolvido em Python para fãs da FURIA Esports no Telegram.  
O bot fornece informações atualizadas sobre o time principal de CS2, incluindo:

- 📅 Próximos jogos  
- 🧑‍🤝‍🧑 Line-up atual  
- 🏆 Posição no ranking mundial  
- ❓ Comandos disponíveis

---

## 🚀 Funcionalidades

- `/proximojogo` – Mostra a próxima partida da FURIA  
- `/lineup` – Lista os jogadores atuais da FURIA CS  
- `/ranking` – Informa a posição da equipe no ranking mundial  
- `/help` – Exibe os comandos disponíveis  
- `/teste` – Confirma se o bot está online  

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12  
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) v22.0  
- requests (para consultar dados externos)  
- BeautifulSoup (scraping de HTML, caso a API da HLTV não esteja disponível)  

---

## ⚙️ Como Rodar o Projeto

1. **Clone o repositório**:

```bash
git clone https://github.com/seu-usuario/furia-bot.git
cd furia-bot
```

2. **Crie e ative um ambiente virtual (opcional)**:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

3. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

4. **Configure seu token em `config.py`**:

Crie um arquivo `config.py` com o conteúdo:

```python
TELEGRAM_TOKEN = "SEU_TOKEN_AQUI"
```

5. **Execute o bot**:

```bash
python main.py
```

---

## 🧪 Teste rápido

No Telegram, envie o comando:

```
/teste
```

Isso confirma que o bot está rodando corretamente.

---

## 🙋‍♂️ Autor

Desenvolvido por **Lucas Vidigal** como parte de um desafio técnico para fãs da FURIA Esports.

---

## 📌 Observações

- A integração com a API da HLTV pode variar. Caso esteja offline, o bot utiliza scraping com BeautifulSoup.  
- Pode ser adaptado para outras plataformas, como **Discord** ou **Web**, com pequenas alterações estruturais.

---

# 🖤💛 GO FURIA!
