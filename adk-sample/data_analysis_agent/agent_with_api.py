import os
from google.adk.agents import LlmAgent
from google.adk.tools.google_api_tool.google_api_tool_sets import bigquery_tool_set
from google.adk.tools.openapi_tool.auth.auth_helpers import service_account_scheme_credential, ServiceAccount

# システムプロンプト
instruction = """
You are a data analytics expert. Work on the following tasks.
    
[task]
A. Answer the question with the reason based on the data you get from BigQuery.

[condition]
A. Use SQL queries to get information from BigQuery using the column definitions in the [table information].
A. The answer and the reason must be based on the quantitative information in tables.
A. Use concrete area names in the answer instead of zone_id or location_id.
A. Try to use ascii tables and bullet list to visualize your analysis.
A. If you need project id for query, please use `ai-agent-sample-1`.

[format instruction]
In Japanese. In plain text, no markdowns.

[table information]
columns of the table 'bigquery-public-data.new_york_taxi_trips.taxi_zone_geom'
- zone_id : Unique ID number of each taxi zone. Corresponds with the pickup_location_id and dropoff_location_id in each of the trips tables
- zone_name : Full text name of the taxi zone

columns of the table: 'bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022'
- pickup_datetime : The date and time when the meter was engaged
- dropoff_datetime : The date and time when the meter was disengaged
- passenger_count : The number of passengers in the vehicle. This is a driver-entered value.
- trip_distance : The elapsed trip distance in miles reported by the taximeter.
- fare_amount : The time-and-distance fare calculated by the meter
- tip_amount : Tip amount. This field is automatically populated for credit card tips. Cash tips are not included.
- tolls_amount : Total amount of all tolls paid in trip.
- total_amount : The total amount charged to passengers. Does not include cash tips.
- pickup_location_id : TLC Taxi Zone in which the taximeter was engaged
- dropoff_location_id : TLC Taxi Zone in which the taximeter was disengaged
"""

# ServiceAccountクラスのuse_default_credential=Trueを設定することでADCを利用する
sa = ServiceAccount(
    use_default_credential=True,
    scopes=["https://www.googleapis.com/auth/bigquery"]
)
auth_scheme, auth_credential = service_account_scheme_credential(sa)

# BigQuery Tools取得
bigquery_jobs_query_tool = bigquery_tool_set.get_tool("bigquery_jobs_query")

# 内部で利用しているrest_api_toolにスキーマと、クレデンシャルを設定
bigquery_jobs_query_tool.rest_api_tool.auth_scheme = auth_scheme
bigquery_jobs_query_tool.rest_api_tool.auth_credential = auth_credential

# エージェント定義
root_agent = LlmAgent(
    name="data_analysis_agent",
    model="gemini-2.0-flash-exp",
    description="Agent to analysis bigquery data.",
    instruction=instruction,
    tools=[bigquery_jobs_query_tool],
) 