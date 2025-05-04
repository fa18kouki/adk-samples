import vertexai
from vertexai import agent_engines

# プロジェクト設定
PROJECT_ID = "issen-global" # あなたのプロジェクトIDに変更してください
LOCATION = "us-central1"
AGENT_ENGINE_ID = "1743535170583003136" # デプロイ後に取得したIDに変更してください

def main():
    vertexai.init(
        project=PROJECT_ID,
        location=LOCATION,
    )

    # エージェントを取得
    agent = agent_engines.get(f"projects/{PROJECT_ID}/locations/{LOCATION}/reasoningEngines/{AGENT_ENGINE_ID}")
    
    # セッションの作成
    remote_session = agent.create_session(user_id="user1")

    # クエリの実行
    for event in agent.stream_query(
        user_id="user1",
        session_id=remote_session["id"],
        message="tlc_yellow_trips_2022 テーブルには何件レコードがありますか？"
    ):
        print("-----")
        print(event)
        
if __name__ == "__main__":
    main() 