# neo4j_connect_python
このプロジェクトは、DockerとPoetryを使用してPython環境を設定し、Neo4jデータベースに接続してデータを挿入する方法を示しています。


# 起動方法
## 前提条件
- Docker
- Docker Compose

## プロジェクトのセットアップ
### 1. リポジトリをクローン

```bash
git clone https://github.com/your-repository.git
cd your-repository
```

### 2. `.env`ファイルを作成

`.env.example`ファイルをコピーして`.env`ファイルを作成し、必要に応じて値を編集します。

```bash
cp ./src/.env.example ./src/.env
```

`.env`ファイルには以下の変数が含まれていることを確認してください：

```env
NEO4J_URI=bolt://neo4j:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=password
```

### 3. Dockerコンテナをビルドして起動

```bash
docker-compose up -d
```

### 4. Poetryを使用して依存関係をインストール

```bash
docker-compose exec python poetry install
```

### 5. Pythonスクリプトを実行

```bash
docker-compose exec python poetry run python /app/main.py
```

もしくは、提供されている`Makefile`を使用して簡単に実行できます。

### 6. Neo4jでデータを確認

ウェブブラウザで`http://localhost:7474`にアクセスし、`.env`ファイルで指定された認証情報を使用してログインします。次のクエリを実行してデータが挿入されたことを確認します：

```cypher
MATCH (n:Person) RETURN n LIMIT 25
```

"alice"という名前のノードが表示されるはずです。

## Makefile

プロセスを簡略化するために、提供された`Makefile`を使用できます。以下のコマンドが利用可能です：

- `make install`: Poetryを使用して依存関係をインストールします。
- `make run`: `main.py`を実行します。
- `make delete`: `delete_all.py`を実行してNeo4jのデータをすべて削除します。

### 使用例：

```bash
make install
make run
make delete
```