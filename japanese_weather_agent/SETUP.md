# 日本語天気情報アシスタントのセットアップガイド

このガイドでは、日本語天気情報アシスタントを実行するために必要な設定手順を説明します。

## 前提条件

- Python 3.9以上
- Poetry
- OpenWeather APIアカウント

## ステップ1: OpenWeather APIキーの取得

1. [OpenWeather](https://openweathermap.org/)にアクセスし、アカウントを作成します（まだお持ちでない場合）
2. ログイン後、[APIキーページ](https://home.openweathermap.org/api_keys)に移動します
3. 「Create Key」ボタンをクリックして新しいAPIキーを生成します
4. 生成されたAPIキーをメモしておきます（後で使用します）

**注意**: 新しく作成したAPIキーは有効になるまで数時間かかることがあります。

## ステップ2: 環境変数の設定

1. プロジェクトのルートディレクトリに`.env`ファイルを作成します:
   ```bash
   cd japanese_weather_agent
   touch .env
   ```

2. お好みのテキストエディタで`.env`ファイルを開き、以下の内容を追加します:
   ```
   # Google ADK API Key
   GOOGLE_API_KEY=your_gemini_api_key_here
   
   # OpenWeather APIキー
   OPENWEATHER_API_KEY=your_openweather_api_key_here
   ```

3. `your_openweather_api_key_here`を先ほど取得したOpenWeather APIキーに置き換えます。
4. 同様に、`your_gemini_api_key_here`をGemini APIキーに置き換えます。

## ステップ3: 依存関係のインストール

1. Poetryを使って依存関係をインストールします:
   ```bash
   cd japanese_weather_agent
   poetry install
   ```

## ステップ4: アプリケーションの実行

1. 以下のコマンドでアプリケーションを起動します:
   ```bash
   poetry run adk web
   ```

2. ブラウザで`http://localhost:8000`にアクセスして、天気情報アシスタントとの対話を開始します。

## トラブルシューティング

### APIキーが認識されない場合

- `.env`ファイルがプロジェクトのルートディレクトリ（`japanese_weather_agent`フォルダ内）に正しく配置されていることを確認してください。
- `.env`ファイル内のAPIキーの前後に余分なスペースがないことを確認してください。

### 天気情報が取得できない場合

- OpenWeather APIキーが有効になっているか確認してください（新しいキーは有効になるまで数時間かかることがあります）。
- インターネット接続が正常に機能しているか確認してください。
- サポートされている都市名を使用しているか確認してください（「東京」、「大阪」、「札幌」など）。 