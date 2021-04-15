function entrarEmServico(user_pin) {
    var ans = confirm("Tem certeza que deseja entrar em serviço?")
    if (ans) {
        $.ajax({
            url: "/ponto",
            type: "POST",
            dataType: "json",
            contentType: 'application/json',
            data: JSON.stringify({"user_pin": user_pin, "tipo": "entrar"}),
            success: window.location.reload()
        });
    }
}

function sairDeServico(user_pin) {
    var ans = confirm("Tem certeza que deseja sair de serviço?")
    if (ans) {
        console.log("Sair de serviço")
        console.log(user_pin)
        $.ajax({
            url: "/ponto",
            type: "POST",
            dataType: "json",
            contentType: 'application/json',
            data: JSON.stringify({"user_pin": user_pin, "tipo": "sair"}),
            success: window.location.reload()
        });
    }
}