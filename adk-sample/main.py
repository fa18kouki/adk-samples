import vertexai
from vertexai import agent_engines
from vertexai.preview import reasoning_engines
from data_analysis_agent.agent import root_agent

# プロジェクト設定
PROJECT_ID = "issen-global" # あなたのプロジェクトIDに変更してください
LOCATION = "us-central1"
STAGING_BUCKET = "gs://adk-sample-bucket" # あなたのバケット名に変更してください

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
)

def main():
    # ADKアプリの作成
    app = reasoning_engines.AdkApp(
        agent=root_agent,
        enable_tracing=True,
    )

    # Agent Engineへデプロイ
    remote_app = agent_engines.create(
        agent_engine=app,
        requirements=[
            "google-adk>=0.1.0",
            "google-cloud-aiplatform[adk,agent-engines]>=1.88.0",
            "google-cloud-bigquery>=3.31.0",
        ],
        extra_packages=['data_analysis_agent']
    )

if __name__ == "__main__":
    main() 