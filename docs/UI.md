 
Para criar uma interface de usuário (UI) para interagir com a blockchain usando JavaScript (JS), HTML e CSS, seguiremos estas etapas:

1. **Definir a Estrutura HTML**: Crie a estrutura básica do documento HTML, incluindo os elementos necessários para interagir com a blockchain, como botões para enviar transações e visualizar a cadeia de blocos.

2. **Estilizar com CSS**: Use CSS para estilizar a aparência da sua aplicação, tornando-a mais atraente e fácil de usar.

3. **Adicionar Comportamento com JavaScript**: Use JavaScript para adicionar interatividade à sua interface de usuário. Isso inclui ações como enviar transações, exibir a cadeia de blocos e atualizar a página com novas informações da blockchain.

Aqui está um exemplo básico de como você pode começar:

### 1. Estrutura HTML (`index.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blockchain UI</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Blockchain UI</h1>
        <button id="viewChainBtn">View Blockchain</button>
        <button id="sendTransactionBtn">Send Transaction</button>
        <div id="blockchainData"></div>
    </div>
    <script src="script.js"></script>
</body>Este é apenas um exemplo básico para começar. Você pode expandir este código adicionando mais funcionalidades, como a interação com a blockchain real por meio de uma API ou WebSocket. Além disso, você pode considerar o uso de frameworks e bibliotecas front-end, como React ou Vue.js, para criar uma UI mais complexa e dinâmica.
</html>
```

### 2. Estilos CSS (`styles.css`):

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 800px;
    margin: 50px auto;
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

button {
    display: block;
    margin: 20px auto;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
}

button:hover {
    background-color: #0056b3;
}

#blockchainData {
    margin-top: 20px;
    border: 1px solid #ccc;
    padding: 10px;
    border-radius: 5px;
    overflow: auto;
    max-height: 300px;
}
```

### 3. Comportamento JavaScript (`script.js`):

```javascript
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
```