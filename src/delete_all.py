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

def delete_all_nodes_and_relationships(tx):
    tx.run("MATCH (n) DETACH DELETE n")

def main():
    with driver.session() as session:
        session.write_transaction(delete_all_nodes_and_relationships)
        print("All nodes and relationships have been deleted.")

if __name__ == "__main__":
    main()
    driver.close()
