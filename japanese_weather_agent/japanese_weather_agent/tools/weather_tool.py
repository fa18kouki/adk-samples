from typing import Dict, Optional, Any
import requests
import os
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

def get_weather(city: str) -> dict:
    """
    指定された都市の天気情報をOpenWeather APIから取得します。
    
    Args:
        city: 天気情報を取得したい都市名
        
    Returns:
        dict: 天気情報を含む辞書。以下のキーが含まれます:
            - status: "success"または"error"
            - report: 天気情報（statusがsuccessの場合）
            - error_message: エラーメッセージ（statusがerrorの場合）
    """
    print(f"--- ツール実行: 都市「{city}」の天気情報を取得中 ---")
    
    # OpenWeather APIキーの取得
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return {"status": "error", "error_message": "OpenWeather APIキーが設定されていません。"}

    # 日本語と英語の都市名マッピング
    city_mapping = {
        "tokyo": "東京",
        "osaka": "大阪",
        "sapporo": "札幌",
        "fukuoka": "福岡",
        "nagoya": "名古屋",
        "okinawa": "沖縄",
        "kyoto": "京都",
        "kobe": "神戸",
        "yokohama": "横浜",
        "hiroshima": "広島",
    }
    
    # 入力された都市名を小文字に変換して処理
    city_lower = city.lower()
    
    # マッピングの逆引き辞書を作成（日本語→英語）
    reverse_mapping = {v.lower(): k for k, v in city_mapping.items()}
    
    # 検索用の都市名を決定
    search_city = city
    
    # 日本語の都市名が入力された場合、英語に変換
    if city_lower in reverse_mapping:
        search_city = reverse_mapping[city_lower]
    elif city_lower in city_mapping:
        # すでに英語名の場合はそのまま使用
        search_city = city_lower
    
    # APIリクエストを送信
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": f"{search_city},jp",
            "appid": api_key,
            "units": "metric",
            "lang": "ja"
        }
        response = requests.get(url, params=params)
        
        # レスポンスを確認
        if response.status_code == 200:
            data = response.json()
            weather_desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            
            # 表示用の都市名を決定（元の入力を尊重）
            display_city = city
            # 入力が英語で、日本語表記がある場合は日本語表記を使用
            if city_lower in city_mapping:
                display_city = city_mapping[city_lower]
            
            weather_report = (
                f"{display_city}の天気は{weather_desc}で、気温は{temp}°Cです。"
                f"体感温度は{feels_like}°Cで、湿度は{humidity}%です。"
            )
            
            return {"status": "success", "report": weather_report}
        else:
            return {"status": "error", "error_message": f"申し訳ありませんが、「{city}」の天気情報は見つかりませんでした。"}
    
    except Exception as e:
        return {"status": "error", "error_message": f"天気情報の取得中にエラーが発生しました: {str(e)}"}


def get_forecast(city: str, days: int = 3) -> dict:
    """
    指定された都市の天気予報をOpenWeather APIから取得します。
    
    Args:
        city: 天気予報を取得したい都市名
        days: 取得したい予報日数（デフォルト: 3日）
        
    Returns:
        dict: 天気予報情報を含む辞書
    """
    print(f"--- ツール実行: 都市「{city}」の{days}日間の天気予報を取得中 ---")
    
    # OpenWeather APIキーの取得
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return {"status": "error", "error_message": "OpenWeather APIキーが設定されていません。"}

    # 日本語と英語の都市名マッピング
    city_mapping = {
        "tokyo": "東京",
        "osaka": "大阪",
        "sapporo": "札幌",
        "fukuoka": "福岡",
        "nagoya": "名古屋",
        "okinawa": "沖縄",
        "kyoto": "京都",
        "kobe": "神戸",
        "yokohama": "横浜",
        "hiroshima": "広島",
    }
    
    # 入力された都市名を小文字に変換して処理
    city_lower = city.lower()
    
    # マッピングの逆引き辞書を作成（日本語→英語）
    reverse_mapping = {v.lower(): k for k, v in city_mapping.items()}
    
    # 検索用の都市名を決定
    search_city = city
    
    # 日本語の都市名が入力された場合、英語に変換
    if city_lower in reverse_mapping:
        search_city = reverse_mapping[city_lower]
    elif city_lower in city_mapping:
        # すでに英語名の場合はそのまま使用
        search_city = city_lower
    
    # APIリクエストを送信
    try:
        url = f"https://api.openweathermap.org/data/2.5/forecast"
        params = {
            "q": f"{search_city},jp",
            "appid": api_key,
            "units": "metric",
            "lang": "ja",
            "cnt": min(days * 8, 40)  # 1日8回の3時間ごとのデータ、最大5日間(40)
        }
        response = requests.get(url, params=params)
        
        # レスポンスを確認
        if response.status_code == 200:
            data = response.json()
            forecast_items = data["list"]
            
            # 表示用の都市名を決定
            display_city = city
            # 入力が英語で、日本語表記がある場合は日本語表記を使用
            if city_lower in city_mapping:
                display_city = city_mapping[city_lower]
            
            # 日付ごとに天気予報をまとめる
            daily_forecasts = {}
            for item in forecast_items:
                date = item["dt_txt"].split(" ")[0]
                if date not in daily_forecasts:
                    daily_forecasts[date] = {
                        "temp_min": float('inf'),
                        "temp_max": float('-inf'),
                        "descriptions": []
                    }
                
                # 最低・最高気温の更新
                temp = item["main"]["temp"]
                daily_forecasts[date]["temp_min"] = min(daily_forecasts[date]["temp_min"], temp)
                daily_forecasts[date]["temp_max"] = max(daily_forecasts[date]["temp_max"], temp)
                
                # 天気の説明を追加
                description = item["weather"][0]["description"]
                if description not in daily_forecasts[date]["descriptions"]:
                    daily_forecasts[date]["descriptions"].append(description)
            
            # 予報レポートの作成
            report_lines = [f"{display_city}の{days}日間の天気予報:"]
            for date, forecast in list(daily_forecasts.items())[:days]:
                descriptions = "、".join(forecast["descriptions"])
                report_lines.append(
                    f"・{date}: {descriptions}、最低気温{forecast['temp_min']:.1f}°C、最高気温{forecast['temp_max']:.1f}°C"
                )
            
            forecast_report = "\n".join(report_lines)
            return {"status": "success", "report": forecast_report}
        else:
            return {"status": "error", "error_message": f"申し訳ありませんが、「{city}」の天気予報は見つかりませんでした。"}
    
    except Exception as e:
        return {"status": "error", "error_message": f"天気予報の取得中にエラーが発生しました: {str(e)}"}


def get_air_pollution(city: str) -> dict:
    """
    指定された都市の大気汚染情報をOpenWeather APIから取得します。
    
    Args:
        city: 大気汚染情報を取得したい都市名
        
    Returns:
        dict: 大気汚染情報を含む辞書
    """
    print(f"--- ツール実行: 都市「{city}」の大気汚染情報を取得中 ---")
    
    # OpenWeather APIキーの取得
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return {"status": "error", "error_message": "OpenWeather APIキーが設定されていません。"}

    # 日本語と英語の都市名マッピング
    city_mapping = {
        "tokyo": "東京",
        "osaka": "大阪",
        "sapporo": "札幌",
        "fukuoka": "福岡",
        "nagoya": "名古屋",
        "okinawa": "沖縄",
        "kyoto": "京都",
        "kobe": "神戸",
        "yokohama": "横浜",
        "hiroshima": "広島",
    }
    
    # 入力された都市名を小文字に変換して処理
    city_lower = city.lower()
    
    # マッピングの逆引き辞書を作成（日本語→英語）
    reverse_mapping = {v.lower(): k for k, v in city_mapping.items()}
    
    # 検索用の都市名を決定
    search_city = city
    
    # 日本語の都市名が入力された場合、英語に変換
    if city_lower in reverse_mapping:
        search_city = reverse_mapping[city_lower]
    elif city_lower in city_mapping:
        # すでに英語名の場合はそのまま使用
        search_city = city_lower
    
    try:
        # まず地理座標を取得
        geo_url = f"https://api.openweathermap.org/geo/1.0/direct"
        geo_params = {
            "q": f"{search_city},jp",
            "limit": 1,
            "appid": api_key
        }
        geo_response = requests.get(geo_url, params=geo_params)
        
        if geo_response.status_code != 200 or not geo_response.json():
            return {"status": "error", "error_message": f"申し訳ありませんが、「{city}」の位置情報が見つかりませんでした。"}
        
        location = geo_response.json()[0]
        lat = location["lat"]
        lon = location["lon"]
        
        # 大気汚染情報を取得
        pollution_url = f"https://api.openweathermap.org/data/2.5/air_pollution"
        pollution_params = {
            "lat": lat,
            "lon": lon,
            "appid": api_key
        }
        
        pollution_response = requests.get(pollution_url, params=pollution_params)
        
        if pollution_response.status_code == 200:
            data = pollution_response.json()
            aqi = data["list"][0]["main"]["aqi"]
            components = data["list"][0]["components"]
            
            # AQI（大気質指数）の評価を日本語で表現
            aqi_levels = {
                1: "とても良い",
                2: "良い",
                3: "普通",
                4: "悪い",
                5: "とても悪い"
            }
            
            # 表示用の都市名を決定
            display_city = city
            # 入力が英語で、日本語表記がある場合は日本語表記を使用
            if city_lower in city_mapping:
                display_city = city_mapping[city_lower]
            
            pollution_report = (
                f"{display_city}の大気質は「{aqi_levels.get(aqi, '不明')}」です。\n"
                f"PM2.5: {components.get('pm2_5', 'N/A')}μg/m³、"
                f"PM10: {components.get('pm10', 'N/A')}μg/m³、"
                f"二酸化窒素(NO₂): {components.get('no2', 'N/A')}μg/m³"
            )
            
            return {"status": "success", "report": pollution_report}
        else:
            return {"status": "error", "error_message": f"申し訳ありませんが、「{city}」の大気汚染情報は見つかりませんでした。"}
    
    except Exception as e:
        return {"status": "error", "error_message": f"大気汚染情報の取得中にエラーが発生しました: {str(e)}"} 