from flask import Flask, request, jsonify
import sqlite3
from database import insertUsuario


app = Flask("Pkm")

@app.route("/pokemon", methods=["GET"])
def encontrarPokemon():

    adress = '/home/vinicius/Pokemons.db'
    conn = sqlite3.connect(adress)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute('select * from Pok1;')
    retorno = []
    for row in result.fetchall():
        item = {}
        item['number'] = row['Number']
        item['name'] = row['Name']
        item['type'] = row['Type']
        item['hp'] = row['HP']
        retorno.append(item)

    return jsonify(retorno)

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

    adress = '/home/vinicius/Pokemons.db'
    conn = sqlite3.connect(adress)
    cur = conn.cursor()
    result = cur.execute("INSERT INTO Pok1 (Number, Name, Type, HP) VALUES ('{0}', '{1}', '{2}', '{3}');".format(body["number"], body["name"], body["type"], body["hp"]))

    conn.commit()
    conn.close()

    return geraResponse(200, "Usuário criado", "pokemon", body["name"])

def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):              #nome_do_conteudo and conteudo = True - Python já entende.
        response[nome_do_conteudo] = conteudo

    return response

app.run()
