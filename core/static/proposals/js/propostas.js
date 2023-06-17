document.addEventListener('DOMContentLoaded', function() {
    // Obter referência ao formulário
    const propostaForm = document.getElementById('propostaForm');

    // Adicionar evento de envio do formulário
    propostaForm.addEventListener('submit', function(event) {
        event.preventDefault();

        // Obter os valores dos campos do formulário
        const nomeCompleto = document.getElementById('nomeCompletoInput').value;
        const cpf = document.getElementById('cpfInput').value;
        const endereco = document.getElementById('enderecoInput').value;
        const valorEmprestimo = document.getElementById('valorEmprestimoInput').value;

        // Criar elemento de lista com os valores preenchidos
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            <a href="#" class="proposta-link">${nomeCompleto} - CPF: ${cpf} - Endereço: ${endereco} - Valor: ${valorEmprestimo}</a>
            <button type="button" class="btn btn-danger btn-sm delete-btn">Deletar</button>
            <button type="button" class="btn btn-secondary mt-3 atualizar-btn">Atualizar</button>
        `;

        // Adicionar o novo item à lista de propostas
        const propostasList = document.getElementById('propostas');
        propostasList.appendChild(listItem);

        // Limpar os campos do formulário
        propostaForm.reset();
    });
});

document.addEventListener('DOMContentLoaded', function() {
    // Função para deletar uma proposta
    function deleteProposta(event) {
        event.preventDefault();
        const propostaItem = event.target.closest('li');
        propostaItem.remove();
    }

    // Função para atualizar uma proposta
    function updateProposta(event) {
        event.preventDefault();
        const propostaItem = event.target.closest('li');
        const propostaLink = propostaItem.querySelector('.proposta-spán');
        const nomeCompleto = prompt('Digite o novo nome completo:');
        const cpf = prompt('Digite o novo CPF:');
        const endereco = prompt('Digite o novo endereço:');
        const valorEmprestimo = prompt('Digite o novo valor de empréstimo:');
        propostaLink.innerHTML = `${nomeCompleto} - CPF: ${cpf} - Endereço: ${endereco} - Valor: ${valorEmprestimo}`;
    }

    // Adicionar eventos aos botões de deletar e atualizar
    const deleteButtons = document.querySelectorAll('.delete-btn');
    const updateButtons = document.querySelectorAll('.atualizar-btn');

    deleteButtons.forEach(function(button) {
        button.addEventListener('click', deleteProposta);
    });

    updateButtons.forEach(function(button) {
        button.addEventListener('click', updateProposta);
    });
});