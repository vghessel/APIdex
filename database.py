def insertUsuario():

    adress = '/home/vinicius/Pokemons.db'
    conn = sqlite3.connect(adress)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute("INSERT INTO Pok1 (Number, Name, Type, HP) VALUES ('{0}', '{1}', '{2}', '{3}');".format(body["number"], body["name"], body["type"], body["hp"]))

    con.commit()
    con.close()
