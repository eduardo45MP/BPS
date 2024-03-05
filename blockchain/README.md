# Blockchain Documentation

## Introduction
This document describes the implementation of a simple Blockchain in Python. Blockchain is a distributed and immutable data structure used to securely and decentralized register transactions. This project aims to provide a basic understanding of how Blockchain works and how it can be implemented.

## Features
The Blockchain implemented in this project has the following main features:

1. **Block Generation**: The Blockchain generates new blocks containing valid transactions.
2. **Block Validation**: Blocks are validated to ensure that all transactions are legitimate and that the blockchain is immutable.
3. **Proof of Work**: The Blockchain uses a proof of work algorithm to ensure the security and integrity of the blockchain.
4. **Transaction Addition**: Users can add new transactions to the Blockchain, which will be included in new blocks after mining.

## Components

### Block Class
The `Block` class represents a block in the Blockchain and has the following attributes:
- `index`: The index of the block in the blockchain.
- `timestamp`: The timestamp (date and time) when the block was created.
- `transactions`: A list of transactions included in the block.
- `previous_hash`: The hash of the previous block in the blockchain.
- `proof`: The proof of work that validates the block.

Additionally, the `Block` class has the `hash_block()` method that calculates the block's hash.

### Blockchain Class
The `Blockchain` class manages the blockchain and has the following functionalities:
- Adding new blocks to the blockchain.
- Validating the integrity of the blockchain.
- Performing proof of work to mine new blocks.
- Adding new transactions to the Blockchain.

## Usage
To use the Blockchain, simply instantiate the `Blockchain` class and start adding transactions and mining new blocks.

Example usage:

```python
from blockchain import Blockchain

# Create an instance of the Blockchain
blockchain = Blockchain()

# Add transactions to the Blockchain
blockchain.new_transaction(sender='sender_address', recipient='recipient_address', amount=10)

# Mine a new block
blockchain.mine_block(miner_address='miner_address')
```

## Conclusion
This project provides a basic introduction to implementing a simple Blockchain in Python. Although it is a simplified version, it demonstrates the fundamental concepts behind Blockchain technology and serves as a starting point for more advanced explorations.