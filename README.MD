# Pulse Precision - Sistema de Cadastro e Avaliação de Tutores e Alunos

Este projeto é um sistema básico para cadastro, gerenciamento e avaliação de tutores e alunos. O sistema permite a criação de contas para tutores, login, atribuição de alunos a tutores e avaliação de desempenho dos alunos com base em critérios de precisão e ritmo.

## Funcionalidades

### Cadastro de Usuários (Alunos)
- Criação de novos alunos no sistema.
- Edição de informações de alunos existentes.
- Exibição de todos os alunos cadastrados.

### Cadastro de Tutores
- Criação de novos tutores no sistema com nome, email, universidade e senha.
- Login de tutores para acessar suas informações.

### Atribuição e Avaliação de Alunos
- Os tutores podem visualizar os alunos atribuídos a eles.
- Os tutores podem avaliar os alunos com base em critérios de precisão no movimento, precisão no clique e ritmo.

### Autenticação de Tutores
- Sistema de login para tutores com autenticação por nome e senha.

## Estrutura de Dados

Este projeto usa matrizes (listas aninhadas) para armazenar informações sobre alunos e tutores:

- Cada aluno é representado por uma lista com os seguintes dados:
  - Nome
  - Idade
  - Email
  - Semestre
  - Tutor

- Cada tutor é representado por uma lista com os seguintes dados:
  - Nome
  - Email
  - Universidade
  - Senha

## Requisitos do Sistema
- Python 3.x
- Nenhuma biblioteca externa é necessária além do Python padrão.

## Como Usar

### 1. Clonar o Repositório

Clone o repositório do projeto:

```bash
git clone https://github.com/seuusuario/pulse-precision.git
cd pulse-precision
```

### 2. Executar o Sistema

Execute o arquivo principal que contém o loop principal do sistema:

```bash
python main.py
```

### 3. Funcionalidades Disponíveis

Ao executar o sistema, você terá as seguintes opções principais:

#### Menu Principal:
- **Acessar menu de cadastro**
  - Ver, cadastrar e editar alunos.
- **Acessar menu de tutor**
  - Login de tutor.
  - Exibir alunos atribuídos e avaliá-los.
- **Sair do programa**

#### Menu de Cadastro:
- **Ver usuários cadastrados**
  - Exibe todos os alunos cadastrados no sistema.
- **Cadastrar novo usuário**
  - Adiciona um novo aluno ao sistema.
- **Editar informações de usuário**
  - Permite alterar os dados de um aluno específico.
- **Sair do menu de cadastro**

#### Menu de Tutor:
- **Fazer Login**
  - Permite que o tutor faça login com seu nome e senha.
- **Criar acesso**
  - Permite criar uma nova conta de tutor.
- **Ver alunos atribuídos**
  - Mostra todos os alunos que têm o tutor logado atribuído a eles.
- **Avaliar aluno**
  - Avalia um aluno em precisão e ritmo, com base em uma média ponderada.

## Exemplo de Estrutura de Dados

### Usuários (Alunos)
| Nome  | Idade | Email              | Semestre | Tutor    |
|-------|-------|--------------------|----------|----------|
| João  | 22    | joao@example.com   | 4        | Carlos   |
| Maria | 20    | maria@example.com  | 2        | Fernanda |

### Tutores
| Nome     | Email                 | Universidade | Senha  |
|----------|-----------------------|--------------|--------|
| Carlos   | carlos@example.com     | UFMG         | 12345  |
| Fernanda | fernanda@example.com   | USP          | 54321  |


## Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usar, modificar e distribuir conforme necessário.
