Aqui está o README.md atualizado, com instruções para instalação local e no servidor AWS EC2, incluindo a configuração para sistemas **Linux**, **Windows** e **AWS EC2**.

---

# **Projeto Flask com PostgreSQL - ONG**

Este projeto é uma aplicação web simples desenvolvida em Flask, com integração ao banco de dados PostgreSQL. Ele permite capturar e armazenar informações de usuários, com fácil configuração tanto local quanto em servidores de produção.

---

## **Conteúdo**
1. [Instalação Local (Windows e Linux)](#instalação-local-windows-e-linux)
2. [Implantação no Servidor AWS EC2](#implantação-no-servidor-aws-ec2)
3. [Estrutura do Projeto](#estrutura-do-projeto)
4. [Requisitos](#requisitos)
5. [Licença](#licença)

---

## **Instalação Local (Windows e Linux)**

Siga as etapas abaixo para executar o projeto localmente no seu ambiente.

### **1. Pré-requisitos**
- **Python 3.7 ou superior**  
  Verifique se o Python está instalado:  
  ```bash
  python --version    # Windows ou Linux
  python3 --version   # Alternativa para Linux
  ```

- **PostgreSQL instalado e configurado**  
  Baixe e configure o PostgreSQL. Disponível para [download aqui](https://www.postgresql.org/download/).

---

### **2. Clone o repositório**
```bash
git clone <repository_url>
cd ong
```

---

### **3. Configure o banco de dados**
1. Crie o banco de dados:
   ```sql
   CREATE DATABASE postgresaula;
   ```

2. No arquivo `app.py`, edite as credenciais do banco PostgreSQL em:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<usuario>:<senha>@<host>:<porta>/<database>'
   ```

   Exemplo:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:senha@localhost:5432/postgresaula'
   ```

---

### **4. Configure o ambiente virtual e instale dependências**

#### **Windows:**
1. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. Instale as dependências:
   ```bash
   pip install Flask Flask-SQLAlchemy psycopg2-binary
   ```

---

#### **Linux/Mac:**
1. Crie e ative o ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Instale as dependências:
   ```bash
   pip install Flask Flask-SQLAlchemy psycopg2-binary
   ```

---

### **5. Execute a aplicação**
#### Windows:
```bash
python app.py
```

#### Linux/Mac:
```bash
python3 app.py
```

Acesse em `http://127.0.0.1:5000`.

---

## **Implantação no Servidor AWS EC2**

### **1. Configure o servidor**
1. Envie os arquivos para o servidor:
   ```bash
   scp -i "aluno_user2.pem" -r app/ ubuntu@<endereço_ip_da_instância>:~
   ```

2. Acesse a instância EC2:
   ```bash
   ssh -i "aluno_user2.pem" ubuntu@<endereço_ip_da_instância>
   ```

---

### **2. Instale dependências no servidor**
No servidor EC2:

1. Atualize os pacotes:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. Instale Python, pip e ambiente virtual:
   ```bash
   sudo apt install python3 -y
   sudo apt install python3-pip -y
   sudo apt install python3.12-venv -y
   ```

3. Crie e ative o ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Instale as bibliotecas do projeto:
   ```bash
   pip install flask
   pip install flask_sqlalchemy
   pip install psycopg2-binary
   pip install gunicorn
   ```

---

### **3. Execute a aplicação**
#### Em modo de produção (Gunicorn):
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

#### Em modo de desenvolvimento (para testes):
```bash
python3 app.py
```

O aplicativo estará disponível em `http://<endereço_ip_da_instância>:8000`.

---

## **Estrutura do Projeto**

A estrutura básica é a seguinte:

```plaintext
.
├── app.py                # Código principal da aplicação
├── templates/            # Arquivos HTML
│   ├── index.html        # Página inicial com formulário
│   ├── contato.html      # Página de confirmação
├── static/               # Arquivos estáticos (CSS, imagens, JS)
├── venv/                 # Ambiente virtual
```

---

## **Requisitos**
As dependências incluem:
- **Flask**: Framework web.
- **Flask-SQLAlchemy**: Integração com o banco de dados PostgreSQL.
- **psycopg2-binary**: Driver para o PostgreSQL.
- **Gunicorn**: Servidor WSGI para produção.

---

## **Licença**
Este projeto está sob a licença MIT. Modifique e compartilhe conforme necessário.

---

**Nota:** Para desenvolvedores novos no projeto, siga essas instruções cuidadosamente. Caso tenha dúvidas ou problemas, consulte a equipe de suporte.