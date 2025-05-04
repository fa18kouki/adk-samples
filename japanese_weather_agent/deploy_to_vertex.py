"""
日本語天気エージェントをVertex AI Agent Engineにデプロイするスクリプト
"""

import os
import vertexai
from vertexai import agent_engines
from vertexai.preview import reasoning_engines
from dotenv import load_dotenv

# 環境変数を.envファイルから読み込み
load_dotenv()

# Japanese Weather Agentをインポート
from japanese_weather_agent import agent

# Google Cloud Projectの設定
# 環境変数から読み込む、または直接設定する
PROJECT_ID = os.getenv("PROJECT_ID", "your-project-id")
LOCATION = os.getenv("LOCATION", "us-central1")
STAGING_BUCKET = os.getenv("STAGING_BUCKET", "gs://your-google-cloud-storage-bucket")

# 設定の表示
print(f"プロジェクト設定:")
print(f"  PROJECT_ID: {PROJECT_ID}")
print(f"  LOCATION: {LOCATION}")
print(f"  STAGING_BUCKET: {STAGING_BUCKET}")

# Vertex AI初期化
vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
)

# エージェントをAgent Engineにデプロイ可能な形式に変換
app = reasoning_engines.AdkApp(
    agent=agent,
    enable_tracing=True,
)

def deploy_agent():
    """エージェントをVertex AI Agent Engineにデプロイします"""
    print("日本語天気エージェントをデプロイしています...")
    
    # エージェントをデプロイ
    remote_app = agent_engines.create(
        app,
        requirements=[
            "google-cloud-aiplatform[adk,agent_engines]"
        ]
    )
    
    print(f"エージェントをデプロイしました。リソース名: {remote_app.resource_name}")
    return remote_app

def test_local():
    """ローカルでエージェントをテスト"""
    print("ローカルでエージェントをテスト中...")
    
    # セッション作成
    session = app.create_session(user_id="test_user_001")
    print(f"セッションID: {session.id}")
    
    # テストクエリを送信
    test_query = "東京の天気を教えてください"
    print(f"テストクエリ: {test_query}")
    
    for event in app.stream_query(
        user_id="test_user_001",
        session_id=session.id,
        message=test_query,
    ):
        print(event)

def test_remote(remote_app):
    """リモートでデプロイされたエージェントをテスト"""
    print("リモートでデプロイされたエージェントをテスト中...")
    
    # リモートセッション作成
    remote_session = remote_app.create_session(user_id="test_user_002")
    print(f"リモートセッションID: {remote_session['id']}")
    
    # テストクエリを送信
    test_query = "東京の天気を教えてください"
    print(f"テストクエリ: {test_query}")
    
    for event in remote_app.stream_query(
        user_id="test_user_002",
        session_id=remote_session["id"],
        message=test_query,
    ):
        print(event)

if __name__ == "__main__":
    # 実行モードの選択
    mode = input("実行モードを選択してください（local/deploy/remote_test/all）: ").strip().lower()
    
    if mode == "local" or mode == "all":
        test_local()
    
    if mode == "deploy" or mode == "all" or mode == "remote_test":
        remote_app = deploy_agent()
        
        if mode == "remote_test" or mode == "all":
            test_remote(remote_app)
            
            # クリーンアップするかどうか
            cleanup = input("デプロイされたエージェントを削除しますか？ (y/n): ").strip().lower()
            if cleanup == "y":
                remote_app.delete(force=True)
                print("エージェントを削除しました。") 