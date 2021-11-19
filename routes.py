from flask import Flask, request
from database import insertUsuario


app = Flask("Pkm")

@app.route("/pokemon", methods=["GET"])
def encontrarPokemon():
    return {"Pokemon": "Pikachu"}

@app.route("/pokemon/adicionar", methods=["POST"])
def adicionarPokemon():

    body = request.get_json()

    if("number" not in body):
        return geraResponse(400, "O parâmetro number é obrigatório!")
    if ("name" not in body):
        return geraResponse(400, "O parâmetro name é obrigatório!")
    if ("type" not in body):
        return geraResponse(400, "O parâmetro type é obrigatório!")
    if ("hp" not in body):
        return geraResponse(400, "O parâmetro hp é obrigatório!")

    usuario = insertUsuario(body["number"], body["name"], body["type"], body["hp"])

    return geraResponse(200, "Usuário criado", "user", usuario)

def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):              #nome_do_conteudo and conteudo = True - Python já entende.
        response[nome_do_conteudo] = conteudo

    return response

app.run()
