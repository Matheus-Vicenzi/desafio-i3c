const saveItem = () => {
    console.log("saveItem inicio")
    const reloadIcon = document.getElementById('reloadIcon');
    const descricao = document.getElementById("descricao");
    const quantidade = document.getElementById("quantidade");
    const valor = document.getElementById("valor");
    const valor36meses = document.getElementById("valor36meses");
    const valor60meses = document.getElementById("valor60meses");

    
    let item = {
        descricao: descricao.value,
        quantidade: quantidade.value,
        valor: valor.value,
        valor_36_meses: valor36meses.value,
        valor_60_meses: valor60meses.value
    };

    let isItemValid = validateSaveItemValues(item);

    if(!isItemValid) return;

    fetch('http://localhost:8000/item', {
        method: 'POST',
        headers: {
            Accept: 'application/json',
                'Content-Type': 'application/json'
            },
        body: JSON.stringify(item)
    }).then(response => {
        console.log(response);
        alert("Item salvo com sucesso");
        location.reload(true);
    }).catch(error => {
        alert("Erro ao salvar item");
        console.log(error);
    });
    console.log("saveItem fim")
}

function validateSaveItemValues(item){

    if(item.descricao == ""){
        alert("Descrição é obrigatório");
        document.getElementById("descricao").focus();
        return(false);
    }

    if(item.quantidade == ""){
        alert("Quantidade é obrigatório");
        document.getElementById("quantidade").focus();
        return(false);
    }

    if(item.valor == ""){
        alert("Valor é obrigatório");
        document.getElementById("valor").focus();
        return(false);
    }

    if(item.valor_36_meses == ""){
        alert("Valor 36 meses é obrigatório");
        document.getElementById("valor36meses").focus();
        return(false);
    }

    if(item.valor_60_meses == ""){
        alert("Valor 60 meses é obrigatório");
        document.getElementById("valor60meses").focus();
        return(false);
    }

    return true;
}

function changeItem(){
    console.log("changeItem inicio")
    let id = document.getElementById("id-item");
    let quantidade = document.getElementById("quantidade");

    if (id.value == ""){
        alert("Código do item é obrigatório");
        document.getElementById("id-item").focus();
        return(false);
    }
    if (quantidade.value == ""){
        alert("Quantidade é obrigatório");
        document.getElementById("quantidade").focus();
        return(false);
    }

    fetch('http://localhost:8000/item?' + new URLSearchParams({
        id: id.value,
        new_quantity_value: quantidade.value
    }), {
        method: 'PATCH',
    })
    .then(response => response.json())
    .then(response => {
        if (response.detail){throw new Error(response.detail);}
        console.log(response);
        alert("Item alterado com sucesso, proposta gerada: " + response.content.newTotalPrice);
        //location.reload(true);
    }).catch(error => {
        console.log(error);
        alert("Erro ao alterar item");
        
    });
    console.log("changeItem fim")
}