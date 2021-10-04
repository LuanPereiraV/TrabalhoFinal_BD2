from neo4j import GraphDatabase
import neo4j
import numpy as np
import readfile
import sys
from timeit import default_timer as timer


class Neo4jConnection:

    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(
                self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)

    def close(self):
        if self.__driver is not None:
            self.__driver.close()

    def query(self, query, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try:
            session = self.__driver.session(
                database=db) if db is not None else self.__driver.session()
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally:
            if session is not None:
                session.close()
        return response



def main():
    db = "trabfinal"
    conn = Neo4jConnection("bolt://localhost:7687", "neo4j", "0000")

    number = int(sys.argv[1])

    words = readfile.read_n("names.txt", number)

    query_text = "MATCH (n) DELETE n"

    conn.query(query_text)

    # Insert in database STRINGS test
    t0 = timer()
    for i in words:
        query_text = "CREATE (c:Cliente {Nome:\"" + i + "\", Sexo: \"M/F\", Endereco:\"Lugar\", Cidade:\"OutroLugar\", UF:\"OL\"})"
        conn.query(query_text, db)
    t1 = timer()
    print("Insert STRINGS: " + str(t1 - t0))
    
    # Insert in database NUMBER test
    t0 = timer()
    for i in range(len(words)):
        query_text = "CREATE (c:ClienteProduto {IdProduto:" + str(i) + ", Qtde: 1, Valor: 10.50})"
        conn.query(query_text, db)
    t1 = timer()
    print("Insert NUMBER: " + str(t1 - t0))

    # Update in database STRINGS test
    query_text = "MATCH (c:Cliente) SET c.Nome = \"Juanito\""
    t0 = timer()
    conn.query(query_text, db)
    t1 = timer()
    print("Update STRINGS: " + str(t1 - t0))
    
    # Update in database NUMBER test
    query_text = "MATCH (c:ClienteProduto) SET c.Qtde = 2"
    t0 = timer()
    conn.query(query_text, db)
    t1 = timer()
    print("Update NUMBER: " + str(t1 - t0))


    # Delete in database STRINGS test
    query_text = "MATCH (c:Cliente) DELETE c"
    t0 = timer()
    conn.query(query_text, db)
    t1 = timer()
    print("Delete STRINGS: " + str(t1 - t0))

    # Delete in database NUMBER test
    query_text = "MATCH (c:ClienteProduto) DELETE c"
    t0 = timer()
    conn.query(query_text, db)
    t1 = timer()
    print("Delete NUMBER: " + str(t1 - t0))


    # print(*conn.query("MATCH (c:Cliente) RETURN c.Nome LIMIT 10", db=db), sep='\n')
    conn.query("MATCH (n) DELETE n")
    conn.close()

if __name__ == "__main__":
    main()
