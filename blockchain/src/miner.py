class Miner:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def mine_block(self, miner_address):
        last_block = self.blockchain.last_block
        last_proof = last_block.proof
        proof = self.blockchain.proof_of_work(last_proof)

        # Adiciona uma transação de recompensa para o minerador
        self.blockchain.new_transaction(
            sender="0",
            recipient=miner_address,
            amount=1,
        )

        # Cria um novo bloco e o adiciona à blockchain
        previous_hash = self.blockchain.hash_block(last_block)
        block = self.blockchain.new_block(proof, previous_hash)

        return block