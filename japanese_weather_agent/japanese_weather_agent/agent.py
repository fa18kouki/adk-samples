from google.adk.agents import LlmAgent
from .tools.weather_tool import get_weather, get_forecast, get_air_pollution
from .prompt import WEATHER_AGENT_INSTRUCTION

# 天気情報アシスタントエージェントを作成
weather_agent = LlmAgent(
    model="gemini-1.5-flash-001",  # モデルを指定（または環境変数から取得）
    name="japanese_weather_agent",  # エージェント名
    description="日本語で対応する天気情報アシスタント",  # エージェントの説明
    instruction=WEATHER_AGENT_INSTRUCTION,  # エージェントの指示
    tools=[get_weather, get_forecast, get_air_pollution],  # 天気関連ツールを提供
)

# エージェントのエントリーポイント
agent = weather_agent 