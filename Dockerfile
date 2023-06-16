# Usa a imagem base do Python
FROM python:3.10 as base

# Define o diretório de trabalho dentro do contêiner
WORKDIR /application

# Copia os arquivos de requirements para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Copia todo o código-fonte para o diretório de trabalho
COPY . .

# Define as variáveis de ambiente necessárias
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE emprestimo.settings

# Executa as migrações do Django
RUN python manage.py migrate

# Define o comando padrão para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]