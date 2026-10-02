# FleetFlow

API REST para gestão de frotas com Python, FastAPI, SQLite e arquitetura em camadas

O FleetFlow foi criado para centralizar informações de veículos, motoristas, abastecimentos, diário de bordo, manutenções e trocas de óleo, aplicando regras de negócio e disponibilizando os dados por meio de uma API REST.

## Tecnologias

- Python
- FastAPI
- Pydantic
- SQLite
- Uvicorn
- Git
- GitHub

## Arquitetura

O projeto utiliza separação em camadas:

```text
Router
  ↓
Service
  ↓
Repository
  ↓
SQLite

Router
````
Responsável pelos endpoints HTTP da API.

Service

Responsável pelas regras de negócio e validações.

Repository

Responsável pela comunicação com o banco de dados.

Schemas

Responsáveis pela validação e estrutura dos dados de entrada e saída.

Funcionalidades
Veículos
Cadastro de veículos
Listagem de veículos
Busca por placa
Ativação e inativação
Atualização de quilometragem
Numeração automática de frota
Validação de placa duplicada
Motoristas
Cadastro de motoristas
Listagem de motoristas
Busca por CPF
Ativação e inativação
Abastecimentos
Registro de abastecimentos
Histórico por veículo
Atualização automática da quilometragem
Cálculo de consumo médio
Cálculo de custo por quilômetro
Resumo de abastecimentos
Diário de Bordo
Registro de saída
Registro de chegada
Controle de viagem aberta por veículo
Controle de viagem aberta por motorista
Atualização da quilometragem do veículo na chegada
Manutenções
Cadastro de manutenção preventiva
Cadastro de manutenção corretiva
Histórico por veículo
Registro de custos
Controle de quilometragem
Definição de próxima manutenção
Alertas de manutenção por quilometragem

Os alertas podem assumir os estados:

OK
Próximo
Vencida
Troca de Óleo
Registro de troca de óleo
Histórico por veículo
Registro do tipo de óleo
Registro do custo
Definição da próxima troca
Alertas por quilometragem
Consideração apenas da troca mais recente para geração do alerta
Dashboard

O Dashboard apresenta informações consolidadas da frota, incluindo:

Total de veículos
Veículos ativos e inativos
Total de motoristas
Total de abastecimentos
Total gasto com combustível
Total de manutenções
Total gasto com manutenções
Total de trocas de óleo
Total gasto com trocas de óleo
Custo total da frota
Custo médio por veículo
Consumo médio por veículo
Melhor consumo
Pior consumo
Alertas de manutenção
Alertas de troca de óleo
Quantidade de manutenções por veículo
Veículo com maior custo
Ranking de custos por veículo
Banco de Dados

O projeto utiliza SQLite.

As tabelas são criadas automaticamente durante a inicialização da aplicação.

O banco utiliza relacionamentos por chave estrangeira entre os principais módulos.

API REST

A aplicação utiliza códigos HTTP de acordo com o resultado das operações.

Exemplos:

200 OK
201 Created
400 Bad Request
404 Not Found
409 Conflict
422 Unprocessable Entity

Os dados são enviados e recebidos em formato JSON.

CORS

A API possui configuração de CORS para permitir integração com aplicações frontend executadas localmente.

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
Estrutura do Projeto
fleetflow/
├── app/
│   ├── database/
│   ├── models/
│   ├── repositories/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── .gitignore
├── requirements.txt
└── README.md
Status do Projeto

Versão 1 da API concluída.

O projeto foi desenvolvido com foco em aprendizado de:

APIs REST
FastAPI
SQLite
Arquitetura em camadas
Regras de negócio
Validação de dados
Integração entre módulos
Git e GitHub
Evoluções Futuras

Possíveis melhorias futuras:

Autenticação de usuários
Controle de permissões
Testes automatizados mais completos
Migrações de banco de dados
ORM
Frontend
Docker
Deploy em nuvem

Essas funcionalidades não fazem parte da versão 1 atual.
