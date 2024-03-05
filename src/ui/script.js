// Simulate sending transaction
function sendTransaction() {
    alert("Transaction sent!");
}

// Simulate viewing blockchain
function viewBlockchain() {
    const blockchainData = document.getElementById("blockchainData");
    blockchainData.innerHTML = "<p>Blockchain Data:</p><pre>Block 1: ...</pre>";
}

document.getElementById("sendTransactionBtn").addEventListener("click", sendTransaction);
document.getElementById("viewChainBtn").addEventListener("click", viewBlockchain);