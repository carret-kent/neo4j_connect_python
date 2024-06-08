import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

# .envファイルをロード
load_dotenv(dotenv_path="/app/.env")

# 環境変数からNeo4jの接続情報を取得
uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")

# ドライバの作成
driver = GraphDatabase.driver(uri, auth=(user, password))

def create_person(tx, name):
    tx.run("CREATE (a:Person {name: $name})", name=name)

def main():
    with driver.session() as session:
        session.write_transaction(create_person, "Alice")

if __name__ == "__main__":
    main()
    driver.close()
