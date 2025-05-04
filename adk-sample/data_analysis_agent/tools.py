from google.cloud import bigquery
import json

def execute_query(query: str) -> str:
    """
    This is a tool for executing queries in BigQuery and retrieving data.
    Query results are returned in JSON format.

    Args:
        query (str): The SQL query to execute.

    Returns:
        str: The query result in JSON format.

    Raises:
        Exception: If the query fails.
    """
    try:
      client = bigquery.Client(project="issen-global", location="US")
      job = client.query(query)
      result = job.result()
      result = [dict(row) for row in result]
      result = [{key: str(value) for key, value in raw.items()} for raw in result]
      return json.dumps(result, ensure_ascii=False)
    except Exception as e:
      print(f"Failed to run query: {e}")
      raise 