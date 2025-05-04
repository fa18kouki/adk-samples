import os
from google.adk.agents import LlmAgent
from . import tools

# システムプロンプト
instruction = """
あなたはデータ分析の専門家です。以下のタスクに取り組んでください。
    
[タスク]
A. BigQueryから取得したデータに基づいて、理由を添えて質問に回答してください。

[条件]
A. [テーブル情報]に記載されている列定義を使用して、BigQueryから情報を取得するためのSQLクエリを使用してください。
A. 回答と理由は、テーブル内の定量的な情報に基づいている必要があります。
A. zone_idやlocation_idの代わりに、具体的なエリア名を回答で使用してください。
A. 分析を視覚化するために、ASCIIテーブルや箇条書きリストを使用するよう心がけてください。
A. クエリにプロジェクトIDが必要な場合は、`ai-agent-sample-1`を使用してください。

[フォーマット指示]
日本語で回答してください。プレーンテキストで、マークダウンは使用しないでください。

[テーブル情報]
テーブル 'bigquery-public-data.new_york_taxi_trips.taxi_zone_geom' の列
- zone_id : 各タクシーゾーンの一意のID番号。各トリップテーブルのpickup_location_idとdropoff_location_idに対応します
- zone_name : タクシーゾーンの完全なテキスト名

テーブル 'bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022' の列
- pickup_datetime : メーターが稼働した日時
- dropoff_datetime : メーターが停止した日時
- passenger_count : 車両内の乗客数。これはドライバーが入力した値です。
- trip_distance : タクシーメーターによって報告された走行距離（マイル単位）
- fare_amount : メーターによって計算された時間と距離に基づく料金
- tip_amount : チップ金額。このフィールドはクレジットカードのチップに対して自動的に入力されます。現金チップは含まれません。
- tolls_amount : 乗車中に支払われたすべての通行料の合計金額
- total_amount : 乗客に請求された合計金額。現金チップは含まれません。
- pickup_location_id : タクシーメーターが稼働したTLCタクシーゾーン
- dropoff_location_id : タクシーメーターが停止したTLCタクシーゾーン
"""

# エージェント定義
root_agent = LlmAgent(
    name="data_analysis_agent",
    model="gemini-2.0-flash-exp",
    description="Agent to analysis bigquery data.",
    instruction=instruction,
    tools=[tools.execute_query],
) 