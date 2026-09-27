#Define a imagem base
FROM python:3.11-slim

#Define o diretório de trabalho dentro do container
WORKDIR /app

#Copia os arquivos de requisitos
COPY requirements.txt .

#Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

#Copia o código fonte
COPY . .

#Expoõe a porta da API
EXPOSE 5002

#Comando de execução
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5002"]