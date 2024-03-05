from block import Block
import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Cria o bloco genesis
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Cria um novo bloco na blockchain
        :param proof: A prova dada pelo algoritmo de consenso
        :param previous_hash: Hash do bloco anterior
        :return: Novo bloco
        """
        block = Block(
            index=len(self.chain) + 1,
            timestamp=time(),
            transactions=self.current_transactions,
            proof=proof,
            previous_hash=previous_hash or self.hash_block(self.chain[-1]),
        )

        # Reinicia a lista de transações atuais
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Cria uma nova transação para ser incluída no próximo bloco minerado
        :param sender: Endereço do remetente
        :param recipient: Endereço do destinatário
        :param amount: Quantidade enviada
        :return: O índice do bloco que conterá esta transação
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block.index + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash_block(block):
        """
        Gera um hash SHA-256 de um bloco
        :param block: Bloco
        :return: String contendo a hash
        """
        block_string = json.dumps(block.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        """
        Algoritmo de prova de trabalho:
         - Encontre um número p' tal que hash(pp') contenha 4 zeros à esquerda, onde p é a prova anterior e p' é a nova prova
        :param last_proof: Prova anterior
        :return: Nova prova
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Verifica se a prova é válida: hash(last_proof, proof) contém 4 zeros à esquerda
        :param last_proof: Prova anterior
        :param proof: Prova atual
        :return: True se for válida, False se não for
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
