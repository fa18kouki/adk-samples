# 日本語天気情報アシスタント

このプロジェクトは、Google ADK（Agent Development Kit）を使用して作成された日本語の天気情報アシスタントです。ユーザーが都市名を入力すると、その地域の天気情報を提供します。

## 機能

- 日本語での対話
- OpenWeather APIを使用したリアルタイムの天気情報の取得
- 天気予報（3日間）の取得
- 大気汚染情報の取得
- 簡単な挨拶の処理

## 前提条件

- Python 3.9以上
- Poetry
- Google Cloud環境またはGemini API Key
- OpenWeather API Key (https://openweathermap.org/api で取得可能)

## セットアップ方法

1. リポジトリをクローンする
2. `.env.example`ファイルを`.env`にコピーし、必要な環境変数を設定する:
   - `GOOGLE_API_KEY`: Gemini API Key
   - `OPENWEATHER_API_KEY`: OpenWeather API Key
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

## 使用例

- 「東京の天気を教えて」
- 「大阪の3日間の天気予報は？」
- 「札幌の大気汚染状況はどうですか？」

## カスタマイズ

`prompt.py`ファイルを編集することで、エージェントの応答や振る舞いをカスタマイズできます。
`tools/weather_tool.py`ファイルを編集することで、天気情報の取得方法をカスタマイズできます。 