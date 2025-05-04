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

    # エージェントを取得して削除
    agent = agent_engines.get(f"projects/{PROJECT_ID}/locations/{LOCATION}/reasoningEngines/{AGENT_ENGINE_ID}")
    agent.delete(force=True)
        
if __name__ == "__main__":
    main() 