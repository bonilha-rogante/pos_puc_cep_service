# cep_service — Microsserviço de Consulta de CEP

Microsserviço responsável por consultar endereços a partir de um CEP, utilizando a API pública [ViaCEP](https://viacep.com.br/). Faz parte do MVP da Sprint 2.

## Responsabilidade

Este serviço tem **uma única responsabilidade**: receber um CEP e devolver o endereço completo (logradouro, bairro, cidade e UF).

É **stateless** — não usa banco de dados. Pode ser consumido por qualquer sistema que precise resolver CEPs. No MVP, é consumido por:
- **`app_api`** — durante o cadastro/edição de usuários
- **`app_front`** — no preview do formulário de cadastro

## Tecnologias

- Python 3.11
- Flask
- Flask-CORS
- Requests (cliente HTTP para o ViaCEP)
- Docker

### Exemplo de requisição

```bash
curl http://localhost:5002/cep/05438200
```

### Exemplo de resposta (200 OK)

```json
{
  "cep": "05438200",
  "address": "Rua Heitor Penteado",
  "neighborhood": "Sumaré",
  "city": "São Paulo",
  "state": "SP"
}
```

### Exemplo de resposta (404 Not Found)

```json
{
  "error": "not_found",
  "message": "CEP 00000000 inválido ou não encontrado"
}
```

## Como executar

### Pré-requisitos

- **Docker** instalado e rodando

### 1. Buildar a imagem

Na **raiz do projeto** (`mvp_sprint_2/`):

```bash
docker build -t cep_service ./cep_service
```

### 2. Criar a rede Docker (só na primeira vez)

```bash
docker network create mvp_network
```

### 3. Subir o container

```bash
docker run -d --name cep_service --network mvp_network -p 5002:5002 cep_service
```

### 4. Verificar que está rodando
```bash
docker ps
# deve mostrar: cep_service  Up  ...  0.0.0.0:5002->5002/tcp
```

### 5. Testar

No navegador ou terminal:

```bash
curl http://localhost:5002/cep/05438200
```