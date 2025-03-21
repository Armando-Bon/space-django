# Space - Galeria de Fotos Espaciais 🚀

Uma galeria espacial desenvolvida com Django, que exibe imagens de nebulosas, capturadas por telescópios como o Hubble.

## 📋 Sobre o Projeto

Space é uma galeria web que exibe imagens de nebulosas, incluindo:
- Nebulosa Carina
- Nebulosa Águia (Pilares da Criação)
- Nebulosa Anel
- Nebulosa Cabeça de Bruxa
- Nebulosa Cabeça de Cavalo
- Nebulosa Helix

Cada imagem vem acompanhada de informações sobre a nebulosa.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Django 5.1.6** - Framework web
- **HTML5 & CSS3** - Estruturação e estilização
- **SQLite3** - Banco de dados
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## 🚀 Funcionalidades

- Visualização de imagens
- Informações sobre cada nebulosa
- Interface responsiva e intuitiva
- Sistema de tags para categorização
- Página "Sobre" com informações do projeto

## ⚙️ Como Executar o Projeto

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/space.git
cd space
```

2. Crie um ambiente virtual
```bash
python -m venv venv
```

3. Ative o ambiente virtual
```bash
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

4. Instale as dependências
```bash
pip install -r requirements.txt
```

5. Configure as variáveis de ambiente
```bash
# Crie um arquivo .env na raiz do projeto com:
SECRET_KEY=sua_chave_secreta
DEBUG=True
```

6. Execute as migrações
```bash
python manage.py migrate
```

7. Inicie o servidor
```bash
python manage.py runserver
```

8. Acesse http://localhost:8000 no seu navegador

## 📁 Estrutura do Projeto

```
space/
├── galeria/            # Aplicação principal
├── setup/              # Configurações do projeto
├── static/             # Arquivos estáticos
│   ├── assets/        # Imagens e ícones
│   └── styles/        # Arquivos CSS
├── templates/          # Templates HTML
├── .env               # Variáveis de ambiente (não versionado)
├── .gitignore         # Arquivos ignorados pelo git
├── manage.py          # Script de gerenciamento Django
└── requirements.txt   # Dependências do projeto
```


## 👤 Armando Bonifacio

* LinkedIn: [@armandobonifacio](https://linkedin.com/in/armandobonifacio)
* Github: [@Armando-Bon](https://github.com/Armando-Bon)

## 🙏 Agradecimentos

- Alura pelos conhecimentos compartilhados 