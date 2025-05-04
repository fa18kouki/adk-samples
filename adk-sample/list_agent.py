import vertexai
from vertexai import agent_engines

# プロジェクト設定
PROJECT_ID = "ai-agent-sample-1" # あなたのプロジェクトIDに変更してください
LOCATION = "us-central1"

def main():
    vertexai.init(
        project=PROJECT_ID,
        location=LOCATION,
    )

    # エージェント一覧を取得
    agents = agent_engines.list()

    for agent in agents:
        print(agent.name)
        
if __name__ == "__main__":
    main() 