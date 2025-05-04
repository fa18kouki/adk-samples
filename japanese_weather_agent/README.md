# 日本語天気情報アシスタント

このプロジェクトは、Google ADK（Agent Development Kit）を使用して作成された日本語の天気情報アシスタントです。ユーザーが都市名を入力すると、その地域の天気情報を提供します。

## 機能

- 日本語での対話
- OpenWeather APIを使用したリアルタイムの天気情報の取得
- 天気予報（3日間）の取得
- 大気汚染情報の取得
- 簡単な挨拶の処理

## 前提条件

- Python 3.9以上
- Poetry
- Google Cloud環境またはGemini API Key
- OpenWeather API Key (https://openweathermap.org/api で取得可能)

## セットアップ方法

1. リポジトリをクローンする
2. `.env.example`ファイルを`.env`にコピーし、必要な環境変数を設定する:
   - `GOOGLE_API_KEY`: Gemini API Key
   - `OPENWEATHER_API_KEY`: OpenWeather API Key
3. 依存関係をインストールする：
   ```bash
   cd japanese_weather_agent
   poetry install
   ```

## 使用方法

エージェントを実行するには：

```bash
cd japanese_weather_agent
adk web
```

ブラウザからアクセスして対話を開始できます。

## 使用例

- 「東京の天気を教えて」
- 「大阪の3日間の天気予報は？」
- 「札幌の大気汚染状況はどうですか？」

## カスタマイズ

`prompt.py`ファイルを編集することで、エージェントの応答や振る舞いをカスタマイズできます。
`tools/weather_tool.py`ファイルを編集することで、天気情報の取得方法をカスタマイズできます。

## Vertex AI Agent Engineへのデプロイ

このプロジェクトは、Google CloudのVertex AI Agent Engineへデプロイすることができます。
Agent Engineは、AIエージェントの本番環境でのデプロイ、管理、スケーリングを可能にするフルマネージドサービスです。

### 前提条件

- Google Cloudアカウントとプロジェクト
- Google Cloud CLIのインストールと初期設定
- `google-cloud-aiplatform[adk,agent_engines]`パッケージのインストール
- Python 3.9以上、3.12以下（Agent Engineの要件）

### デプロイ手順

1. 必要な依存関係をインストールします：

```bash
pip install "google-cloud-aiplatform[adk,agent_engines]"
```

2. 環境変数を設定します：

`.env`ファイルをプロジェクトのルートディレクトリに作成し、以下の情報を設定します：

```
PROJECT_ID=your-project-id
LOCATION=us-central1
STAGING_BUCKET=gs://your-google-cloud-storage-bucket
```

もしくは、以下のように環境変数を直接設定します：

```bash
export PROJECT_ID=your-project-id
export LOCATION=us-central1
export STAGING_BUCKET=gs://your-google-cloud-storage-bucket
```

3. デプロイスクリプトを実行します：

```bash
python deploy_to_vertex.py
```

実行モードを選択するプロンプトが表示されます：

- `local`: ローカルでエージェントをテストします
- `deploy`: エージェントをVertex AI Agent Engineにデプロイします
- `remote_test`: デプロイ後にリモートでエージェントをテストします
- `all`: すべての操作を実行します

4. エージェントの使用：

デプロイ後、エージェントのリソース名が表示されます。このリソース名を使用して、Google Cloud Consoleでエージェントを管理したり、APIリクエストを送信したりすることができます。

5. クリーンアップ：

不要になったエージェントは削除することができます：

```python
remote_app.delete(force=True)
```

### サポートされているリージョン

Vertex AI Agent Engineは特定のリージョンでのみ利用可能です。最新の情報は[公式ドキュメント](https://cloud.google.com/vertex-ai/docs/agent-engine/regions)を参照してください。 