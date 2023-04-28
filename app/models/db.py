import sqlite3

conn = sqlite3.connect("qualidade.sqlite")
cursor = conn.cursor()
sql_query = """
CREATE TABLE qualidade(
id integer PRIMARY KEY,
influente TEXT,
dominante TEXT,
estavel TEXT,
analitico TEXT
)
"""

cursor.execute(sql_query)

sql_query = """
CREATE TABLE Perguntas(
    id integer PRIMARY KEY,
    area_da_gestão TEXT,
    area_da_medicina TEXT,
    area_da_informatica TEXT,
    area_da_contabilidade TEXT
    )
"""

cursor.execute(sql_query)