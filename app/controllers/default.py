from app.models.db_connection import db_connection
from app.controllers.function import orderListe,teste_disc
from flask import jsonify,request
from app import app

@app.route("/disc",methods=["GET","POST","DELETE"])
def disc():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor = conn.execute("SELECT * FROM qualidade")
        row = cursor.fetchall()
        influente,dominante,estavel,analitico=orderListe(row)
        cursor = conn.execute("SELECT * FROM Perguntas")
        row = cursor.fetchall()
        area_da_gestão, area_da_medicina, area_da_informatica, area_da_contabilidade = orderListe(row)
        dados = [
           dict(
             influente = influente,
             dominante = dominante,
             estavel = estavel,
             analitico = analitico,
             area_da_gestão=area_da_gestão,
             area_da_medicina=area_da_medicina,
             area_da_informatica=area_da_informatica,
             area_da_contabilidade=area_da_contabilidade
               )
            ]
        if dados is not None:
           return jsonify(dados)

    if request.method == 'POST':
        dados = request.get_json()
        if type(dados) != dict: return "Bad value, it must be a dict!",404
        if dados["tabela"]=="qualidade":
            if type(dados["influente"])!=list: return "the value must be a list!",404
            for i in range(0,dados["influente"].__len__()):
              sql = """INSERT INTO qualidade (influente,estavel,dominante,analitico)
              VALUES (?,?,?,?)"""
              cursor = cursor.execute(sql,(dados["influente"][i],dados["dominante"][i],dados["estavel"][i],dados["analitico"][i]))
              conn.commit()
        elif dados["tabela"]=="Perguntas":
            if type(dados["area_da_gestao"]) != list: return "the value must be a list!", 404
            for i in range(0,dados["area_da_gestao"].__len__()):
              sql = """INSERT INTO qualidade (area_da_gestao,area_da_medicina,area_da_informatica,area_da_contabilidade)
              VALUES (?,?,?,?)"""
              cursor = cursor.execute(sql,(dados["area_da_gestao"][i],dados["area_da_medicina"][i],dados["area_da_informatica"][i],dados["area_da_contabilidade"][i]))
              conn.commit()
        return f"Qualidade with the id: {cursor.lastrowid} created successfully"

    if request.method == "DELETE":
        dados = request.get_json()
        if type(dados) != dict: return "Bad value, it must be a dict!",404
        sql = f""" DELETE FROM {dados["tabela"]} WHERE id=?"""
        conn.execute(sql,(dados["id"],))
        conn.commit()
        return "The qualidade with id: {} has been deleted.".format(dados["id"]),200


@app.route("/disc/teste", methods=["POST"])
def teste_DISC():
    conn = db_connection()
    cursor = conn.cursor()
    dados = request.get_json()
    if type(dados)!=list: return "Bad value, it must be a list!",404
    if request.method == 'POST':
        cursor = conn.execute("SELECT * FROM qualidade")
        Qrow = cursor.fetchall()
        cursor = conn.execute("SELECT * FROM Perguntas")
        Prow = cursor.fetchall()
        return jsonify(teste_disc(dados,orderListe(Qrow),orderListe(Prow)))