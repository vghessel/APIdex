from flask import Flask, request, jsonify
import sqlite3

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

    return geraResponse(200, "Pokemon criado", "pokemon", body["name"])

@app.route("/pokemon/atualizar/", methods=["PUT"])
def atualizarPokemon():

    adress = '/home/vinicius/Pokemons.db'
    conn = sqlite3.connect(adress)
    cur = conn.cursor()

    body = request.get_json()

    if ("number" not in body):
        return geraResponse(400, "O parâmetro number é obrigatório!")

    else:
        if ("name" in body):
            result = cur.execute("UPDATE Pok1 SET Name = '{0}' WHERE Number = '{1}';".format(body["name"], body["number"]))

        if ("type" in body):
            result1 = cur.execute("UPDATE Pok1 SET Type = '{0}' WHERE Number = '{1}';".format(body["type"], body["number"]))

        if ("hp" in body):
            result2 = cur.execute("UPDATE Pok1 SET HP = '{0}' WHERE Number = '{1}';".format(body["hp"], body["number"]))

    conn.commit()
    conn.close()

    return geraResponse(200, "Pokemon atualizado", "pokemon", body["name"])

@app.route("/pokemon/deletar", methods=["DELETE"])
def deletarPokemon():

    body = request.get_json()

    if ("number" not in body):
        return geraResponse(400, "Informar apenas o parâmetro number")

    adress = '/home/vinicius/Pokemons.db'
    conn = sqlite3.connect(adress)
    cur = conn.cursor()
    result = cur.execute("DELETE from Pok1 WHERE Number = '{0}';".format(body["number"]))

    conn.commit()
    conn.close()

    return geraResponse(200, "Pokemon deletado", "pokemon", body["number"])


def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):              #nome_do_conteudo and conteudo = True - Python já entende.
        response[nome_do_conteudo] = conteudo

    return response

app.run()
