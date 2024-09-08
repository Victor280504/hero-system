# Projeto de Banco de Dados
Este repositório contém o código destinado ao trabalho final da disciplina de Banco de Dados I.

## Descrição

O objetivo deste projeto é desenvolver um sistema de gerenciamento de heróis, utilizando um banco de dados relacional para armazenar informações sobre os heróis, missões e suas habilidades.

## Funcionalidades

| Funcionalidade                | Operação SQL   |
|-------------------------------|----------------|
| Adicionar um Administrador    | INSERT         |
| Remover um Administrador      | DELETE         |
| Atualizar um Administrador    | UPDATE         |
| Listar todos os Administradores | SELECT        |
| Adicionar um Herói            | INSERT         |
| Remover um Herói              | DELETE         |
| Atualizar um Herói            | UPDATE         |
| Listar todos os Heróis        | SELECT         |
| Adicionar uma Missão          | INSERT         |
| Remover uma Missão            | DELETE         |
| Atualizar uma Missão          | UPDATE         |
| Listar todas as Missões       | SELECT         |
| Adicionar uma Equipamento     | INSERT         |
| Remover uma Equipamento       | DELETE         |
| Atualizar uma Equipamento     | UPDATE         |
| Listar todas as Equipamentos  | SELECT         |
| Adicionar um Vilão            | INSERT         |
| Remover uma Vilão             | DELETE         |
| Atualizar uma Vilão           | UPDATE         |
| Listar todas as Vilão         | SELECT         |


## Tecnologias utilizadas

- Python
- PostgreSQL

## Como executar o projeto

### Inicializando o banco de dados

#### Para adicionar o banco de dados, siga os passos abaixo:

1. Certifique-se de ter o PostgreSQL instalado em seu sistema.
2. Abra o pgAdmin e crie um novo banco de dados chamado `hero_adm_system`
3. Em seguida, abra o query toll do banco de dados, adicione o arquivo `hero_adm_system.sql` disponível na raiz do projeto.
3. Execute o arquivo.
4. Adicione as credenciais do seu banco de dados no arquivo `.env`


#### Para inicializar o banco de dados, siga os passos abaixo:

1. Certifique-se de que o banco de dados está criado e configurado:
2. Prepare o arquivo SQL de dados iniciais:
3. Encontre o arquivo `initial_data.sql` que deve estar localizado na raiz do projeto.
4. Abra o cliente SQL , pgAdmin, para se conectar ao banco de dados hero_adm_system e execute o arquivo SQL de dados iniciais `initial_data.sql` para inserir os dados iniciais nas tabelas do banco de dados.
5. Agora você está pronto para utilizar o sistema de gerenciamento de heróis.

#### Para verificar os dados inseridos:

Execute consultas SQL para verificar se os dados foram inseridos corretamente nas tabelas.
Por exemplo, você pode executar SELECT * FROM nome_da_tabela; para listar os registros de uma tabela específica.

Caso os dados não tenham sido inseridos verifique o passo a passo e repita o processo novamente.

### Inicializando o sistema

1. Clone este repositório
2. Instale as dependências utilizando o comando `pip install -r requirements.txt`
3. Execute o arquivo `main.py` para iniciar o sistema
4. Acesse o sistema através do terminal



"""
A licença deste projeto é a Licença MIT. A Licença MIT é uma licença de software livre que permite que qualquer pessoa obtenha uma cópia do software e o utilize, copie, modifique, una, publique, distribua, sublicencie e/ou venda, sujeito às seguintes condições: a inclusão do aviso de direitos autorais e da licença nos arquivos do software. A licença também isenta os autores de qualquer responsabilidade por danos ou outras reivindicações relacionadas ao software. É uma licença amplamente utilizada e permite que o software seja usado de forma flexível e aberta.
"""

## Modelagem do Banco de Dados

Nesta seção, apresentaremos a modelagem do banco de dados do sistema de gerenciamento de heróis. Serão abordados os requisitos de dados, o modelo de entidade relacionamento (MER) e o diagrama de entidade relacionamento (DER).

### Requisitos de Dados

Os requisitos de dados são as informações que precisamos armazenar no banco de dados para atender às funcionalidades do sistema. Com base nas funcionalidades descritas anteriormente, identificamos os seguintes requisitos de dados:

- Administradores: nome, email, senha
- Heróis: nome, poderes, habilidades, nível
- Missões: título, descrição, recompensa
- Equipamentos: nome, descrição, tipo
- Vilões: nome, poderes, nível

### Modelo de Entidade Relacionamento (MER)

O modelo de entidade relacionamento (MER) é uma representação visual das entidades, atributos e relacionamentos do sistema. Com base nos requisitos de dados, criamos o seguinte MER:



### Diagrama de Entidade Relacionamento (DER)

O diagrama de entidade relacionamento (DER) é uma representação visual do modelo de entidade relacionamento (MER). Com base no MER apresentado anteriormente, criamos o seguinte DER:


Com o modelo de entidade relacionamento (MER) e o diagrama de entidade relacionamento (DER), temos uma visão clara das entidades, atributos e relacionamentos do banco de dados do sistema de gerenciamento de heróis.
