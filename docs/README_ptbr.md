# Documentação da Blockchain

## Introdução
Este documento descreve a implementação de uma Blockchain simples em Python. A Blockchain é uma estrutura de dados distribuída e imutável que é utilizada para registrar transações de forma segura e descentralizada. Este projeto visa fornecer uma compreensão básica de como a Blockchain funciona e como ela pode ser implementada.

## Funcionalidades
A Blockchain implementada neste projeto possui as seguintes funcionalidades principais:

1. **Geração de Blocos**: A Blockchain gera novos blocos que contêm transações válidas.
2. **Validação de Blocos**: Os blocos são validados para garantir que todas as transações sejam legítimas e que a cadeia de blocos seja imutável.
3. **Prova de Trabalho**: A Blockchain utiliza um algoritmo de prova de trabalho para garantir a segurança e a integridade da cadeia de blocos.
4. **Adição de Transações**: Os usuários podem adicionar novas transações à Blockchain, que serão incluídas em novos blocos após a mineração.

## Componentes

### Classe Block
A classe `Block` representa um bloco na Blockchain e possui os seguintes atributos:
- `index`: O índice do bloco na cadeia de blocos.
- `timestamp`: O timestamp (data e hora) em que o bloco foi criado.
- `transactions`: Uma lista de transações incluídas no bloco.
- `previous_hash`: O hash do bloco anterior na cadeia de blocos.
- `proof`: A prova de trabalho que valida o bloco.

Além disso, a classe `Block` possui o método `hash_block()` que calcula o hash do bloco.

### Classe Blockchain
A classe `Blockchain` gerencia a cadeia de blocos e possui as seguintes funcionalidades:
- Adicionar novos blocos à cadeia de blocos.
- Validar a integridade da cadeia de blocos.
- Realizar a prova de trabalho para minerar novos blocos.
- Adicionar novas transações à Blockchain.

## Uso
Para utilizar a Blockchain, basta instanciar a classe `Blockchain` e começar a adicionar transações e minerar novos blocos.

Exemplo de uso:

```python
from blockchain import Blockchain

# Criar uma instância da Blockchain
blockchain = Blockchain()

# Adicionar transações à Blockchain
blockchain.new_transaction(sender='sender_address', recipient='recipient_address', amount=10)

# Minerar um novo bloco
blockchain.mine_block(miner_address='miner_address')
```

## Conclusão
Este projeto fornece uma introdução básica à implementação de uma Blockchain simples em Python. Embora seja uma versão simplificada, ela demonstra os conceitos fundamentais por trás da tecnologia Blockchain e serve como ponto de partida para explorações mais avançadas.