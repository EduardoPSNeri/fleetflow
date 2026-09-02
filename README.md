# FleetFlow

Sistema de gestão de frotas desenvolvido com Python, FastAPI e SQLite.

O FleetFlow foi criado para centralizar informações de veículos, motoristas, abastecimentos, diário de bordo e manutenções, aplicando regras de negócio e disponibilizando os dados através de uma API REST.

## Tecnologias

- Python
- FastAPI
- Pydantic
- SQLite
- Uvicorn
- Git e GitHub

## Arquitetura

O projeto utiliza separação em camadas:


Router
  ↓
Service
  ↓
Repository
  ↓
SQLite
Router

Responsável pelos endpoints HTTP da API.

Service

Responsável pelas regras de negócio e validações.

Repository

Responsável pela comunicação com o banco de dados.

Schemas

Responsáveis pela validação e estrutura dos dados de entrada e saída da API.

Funcionalidades
Veículos
Cadastro de veículos
Listagem de veículos
Busca por placa
Ativação e inativação
Atualização de quilometragem
Numeração automática de frota
Motoristas
Cadastro de motoristas
Listagem
Busca por CPF
Ativação e inativação
Abastecimentos
Registro de abastecimentos
Atualização automática da quilometragem do veículo
Histórico por veículo
Cálculo de consumo médio
Cálculo de custo por quilômetro
Resumo de abastecimentos
Diário de Bordo
Registro de saída
Registro de chegada
Controle de viagem aberta por veículo
Controle de viagem aberta por motorista
Atualização automática da quilometragem na chegada
Manutenções
Cadastro de manutenção preventiva e corretiva
Histórico de manutenções por veículo
Controle de quilometragem da manutenção
Registro de custos
API REST

A aplicação utiliza códigos HTTP de acordo com o resultado das operações.

200 OK
201 Created
400 Bad Request
404 Not Found

Os dados são retornados em formato JSON através de schemas Pydantic.

Executando o projeto

Clone o repositório:

git clone https://github.com/EduardoPSNeri/fleetflow.git

Entre na pasta:

cd fleetflow

Crie um ambiente virtual:

python -m venv .venv

Ative o ambiente virtual no Windows:

.venv\Scripts\activate

Instale as dependências:

pip install -r requirements.txt

Execute a API:

uvicorn app.main:app --reload

Acesse a documentação Swagger:

http://127.0.0.1:8000/docs
Status do projeto

Versão inicial da API em desenvolvimento.

Módulos atualmente implementados:

Veículos
Motoristas
Abastecimentos
Diário de Bordo
Manutenções
Próximos passos
Inicialização automática do banco de dados
Autenticação de usuários
Controle de permissões
Testes automatizados
Melhorias na estrutura do banco de dados
Dashboard
Deploy da aplicação

Tem só um detalhe importante: no seu Git o arquivo está como requeriments.txt, mas o padrão correto é:

requirements.txt

Então eu corrigiria isso junto agora:

git mv requeriments.txt requirements.txt

Depois:

git add README.md .gitignore
git commit -m "organiza projeto e atualiza documentacao"
git push
