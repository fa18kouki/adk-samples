# ADK サンプルプロジェクト

このプロジェクトは、Google Cloud Next 2025で発表された Agent Development Kit (ADK) のサンプル実装です。BigQueryからデータを取得して分析するAIエージェントを実装しています。

## 環境準備

### 前提条件
- Python 3.12.5
- mise
- uv
- Google Cloudアカウント

### セットアップ

1. リポジトリをクローン

```
git clone <repository>
cd adk-sample
```

2. 依存関係のインストール

```
mise use
uv venv
uv add google-adk
uv add google-cloud-bigquery
uv add google-cloud-aiplatform[adk,agent_engines]
```

3. 環境変数の設定

`.env`ファイルに以下を設定します：

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=<あなたのGemini API Key>
```

## ローカルでの実行

開発UIを起動：

```
adk web
```

## デプロイ

### Agent Engineへのデプロイ

1. GCSバケットの作成

```
gcloud storage buckets create gs://<バケット名> --project <プロジェクトID>
```

2. `main.py`を実行

```
python main.py
```

3. エージェント一覧を確認

```
python list_agent.py
```

4. エージェントを実行

`run_agent_engine.py`の`AGENT_ENGINE_ID`を変更後：

```
python run_agent_engine.py
```

### Cloud Runへのデプロイ

```
export GOOGLE_CLOUD_PROJECT="<プロジェクトID>"
export GOOGLE_CLOUD_LOCATION="asia-northeast1"
export SERVICE_NAME="ai-agent-sample"
export APP_NAME="data_analysis_agent"
export AGENT_PATH="./data_analysis_agent"

adk deploy cloud_run \
--project=$GOOGLE_CLOUD_PROJECT \
--region=$GOOGLE_CLOUD_LOCATION \
--service_name=$SERVICE_NAME \
--app_name=$APP_NAME \
--with_ui \
$AGENT_PATH
``` 