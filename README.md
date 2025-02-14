# Django Project - Autoparts Requirements

## Sobre o Projeto

Este projeto foi desenvolvido para atender ao desafio de criar um sistema de consulta de peças automotivas utilizando Django. O objetivo principal é oferecer uma API RESTful que permita:

- **Listagem, consulta e gestão de estoque de peças automotivas**;
- **Importação assíncrona de peças via planilha**, otimizando a atualização em massa dos registros no sistema;
- **Reposição automática de estoque**, garantindo que o sistema esteja sempre atualizado com níveis mínimos de peças.

Além disso, a aplicação foi projetada com foco em eficiência e escalabilidade, utilizando tecnologias modernas, como Celery e Redis, para tarefas assíncronas, e PostgreSQL para gerenciar os dados.

## Autoparts Configurations and Requirements

### **Ubuntu 14.11 22.04.1**

### **psql (PostgreSQL) 16**

### **python 3.12**

### Basic Requrirements

- tzdata
- python3-setuptools
- python3-pip
- python3-dev
- python3-venv
- git

### Installing Postgres 16 (Ubuntu 22.04)

```bash
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```

```bash
curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg 
```

```bash
sudo apt update
```

```bash
sudo apt install postgresql-16 postgresql-contrib-16
```

```bash
sudo systemctl start postgresql    
```

```bash
sudo systemctl enable postgresql    
```

### **DataBase Configuration**

```bash
sudo -u postgres psql
```

```sql
CREATE DATABASE parts;
CREATE USER pguser WITH PASSWORD 'password';
ALTER ROLE pguser SET client_encoding TO 'utf8';
GRANT ALL PRIVILEGES ON DATABASE parts TO pguser;
ALTER USER pguser WITH SUPERUSER;
```

### **Create a virtual environment**

```bash
python3 -m venv ./path/to/your/env
```
>On your rootbase project (where manage.py its located)

### **Activate your virtual environment**

```bash
source ./path/to/your/env/bin/activate
```

### **Install Project Requirements**

```bash
pip install -r requirements.txt
```
### Dot-env
>On your rootbase project (where manage.py its located)
```bash
mv env-example .env
```
**Run Project**

```bash
python3 manage.py migrate
```
> Only needed on first time, and with new migrations and models

```bash
python3 manage.py createsuperuser
```

```bash
python3 manage.py runserver
```

```bash
sudo apt install redis-server
```

```bash
redis-server
```

```bash
celery -A autoparts worker --loglevel=info
```

```bash
python3 manange.py help
```


```bash
python3 manange.py create_parts_command
```