# 日本語天気情報アシスタント

このプロジェクトは、Google ADK（Agent Development Kit）を使用して作成された日本語の天気情報アシスタントです。ユーザーが都市名を入力すると、その地域の天気情報を提供します。

## 機能

- 日本語での対話
- 都市名から天気情報の取得
- 簡単な挨拶の処理

## 前提条件

- Python 3.9以上
- Poetry
- Google Cloud環境またはGemini API Key

## セットアップ方法

1. リポジトリをクローンする
2. `.env.example`ファイルを`.env`にコピーし、必要な環境変数を設定する
3. 依存関係をインストールする：
   ```bash
   cd japanese_weather_agent
   poetry install
   ```

## 使用方法

エージェントを実行するには：

```bash
cd japanese_weather_agent
adk web
```

ブラウザからアクセスして対話を開始できます。

## カスタマイズ

`prompt.py`ファイルを編集することで、エージェントの応答や振る舞いをカスタマイズできます。 