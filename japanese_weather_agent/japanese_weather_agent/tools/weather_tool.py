from typing import Dict

def get_weather(city: str) -> Dict:
    """
    指定された都市の天気情報を取得します。
    
    Args:
        city: 天気情報を取得したい都市名
        
    Returns:
        Dict: 天気情報を含む辞書。以下のキーが含まれます:
            - status: "success"または"error"
            - report: 天気情報（statusがsuccessの場合）
            - error_message: エラーメッセージ（statusがerrorの場合）
    """
    print(f"--- ツール実行: 都市「{city}」の天気情報を取得中 ---")
    city_normalized = city.lower().replace(" ", "")
    
    # モック天気データ（実際のAPIでは置き換えられます）
    mock_weather_db = {
        "東京": {"status": "success", "report": "東京の天気は晴れで、気温は25°Cです。"},
        "大阪": {"status": "success", "report": "大阪は曇りで、気温は22°Cです。"},
        "札幌": {"status": "success", "report": "札幌は雪で、気温は2°Cです。"},
        "福岡": {"status": "success", "report": "福岡は雨で、気温は20°Cです。"},
        "名古屋": {"status": "success", "report": "名古屋は晴れで、気温は24°Cです。"},
        "沖縄": {"status": "success", "report": "沖縄は晴れで、気温は30°Cです。"},
        "京都": {"status": "success", "report": "京都は曇りで、気温は23°Cです。"},
        "神戸": {"status": "success", "report": "神戸は晴れで、気温は21°Cです。"},
        "横浜": {"status": "success", "report": "横浜は晴れで、気温は24°Cです。"},
        "広島": {"status": "success", "report": "広島は曇りで、気温は22°Cです。"},
    }
    
    # 日本語と英語の都市名マッピング（オプション）
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
    
    # 英語の都市名が入力された場合、日本語に変換を試みる
    if city_normalized in city_mapping:
        city = city_mapping[city_normalized]
    
    # 都市の天気情報があれば返す
    if city in mock_weather_db:
        return mock_weather_db[city]
    else:
        return {"status": "error", "error_message": f"申し訳ありませんが、「{city}」の天気情報は見つかりませんでした。"} 