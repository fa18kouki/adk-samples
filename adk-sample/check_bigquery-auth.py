from google.cloud import bigquery

client = bigquery.Client()
datasets = list(client.list_datasets())
if datasets:
    print("認証成功: 利用可能なデータセット一覧")
    for dataset in datasets:
        print(dataset.dataset_id)
else:
    print("認証は通ったが、データセットが見つかりません")