// Adiciona um "escutador" ao evento de submissão do formulário com id="form"
document.getElementById('form').addEventListener('submit', async function(event) {
    
    // PASSO CRUCIAL: Impede o comportamento padrão do formulário (que é recarregar a página)
    event.preventDefault();
    
    // Pega os valores dos elementos HTML
    const cardNumber = document.getElementById('cardNumber').value;
    const resultDiv = document.getElementById('result');
    
    // Mostra uma mensagem de carregamento
    resultDiv.textContent = 'Validando...';
    
    try {
        // Envia os dados para a nossa API FastAPI usando o método POST
        const response = await fetch('/validar-cartao', {
            method: 'POST',
            headers: {
                // Informa ao servidor que estamos a enviar dados em formato JSON
                'Content-Type': 'application/json',
            },
            // Converte nosso objeto JavaScript para uma string no formato JSON
            body: JSON.stringify({ numero_cartao: cardNumber }),
        });
        
        // Pega a resposta da API (que também é JSON)
        const data = await response.json();
        
        // Exibe o resultado na div 'result'
        if (data.bandeira === "Bandeira desconhecida") {
            resultDiv.textContent = `❌ Bandeira não identificada.`;
        } else {
            resultDiv.textContent = `✅ Bandeira: ${data.bandeira}`;
        }
        
    } catch (error) {
        // Exibe uma mensagem em caso de erro na comunicação com a API
        resultDiv.textContent = 'Erro ao se comunicar com o servidor.';
        console.error('Erro no fetch:', error);
    }
});