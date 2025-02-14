# Django Project - Autoparts Requirements

## About the Project

This project was developed to address the challenge of creating an automotive parts consultation system using Django. The main goal is to provide a RESTful API that enables:

- **Listing, querying, and managing the inventory of automotive parts**;
- **Asynchronous import of parts via spreadsheet**, optimizing bulk record updates in the system;
- **Automatic stock replenishment**, ensuring the system is always updated with minimum stock levels.

Additionally, the application was designed with a focus on efficiency and scalability, leveraging modern technologies such as Celery and Redis for asynchronous tasks and PostgreSQL for data management.

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