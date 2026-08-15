#!/usr/bin/env python3
import os
import requests
import json
from datetime import datetime

# サンプル飲み会イベントデータ - 京都社会人飲み友募集
SAMPLE_EVENTS = [
    {
        "date": "2026-08-15",
        "location": "京都・祇園の立ち飲み屋",
        "participants": ["社会人"],
        "activities": ["気軽に飲む🍺", "新しい友達と出会う"],
        "highlights": "飲み友募集"
    },
    {
        "date": "2026-08-22",
        "location": "京都・四条通の居酒屋",
        "participants": ["社会人"],
        "activities": ["美味しい料理を食べながら乾杯🍶", "楽しく交流"],
        "highlights": "飲み友募集"
    },
    {
        "date": "2026-08-29",
        "location": "京都・烏丸のおしゃれなBAR",
        "participants": ["社会人"],
        "activities": ["落ち着いた雰囲気で乾杯🥂", "大人の交流"],
        "highlights": "飲み友募集"
    }
]

def generate_envious_text(event):
    """飲み友募集のテキストを生成"""
    texts = [
        f"🍺 {event['location']}で飲み友募集中！\n社会人同士、気軽に飲みませんか？😊\n\nカウンターで新しい友達と出会おう！\n#飲み友募集 #京都 #社会人",
        
        f"🍶 {event['location']}から\n{event['highlights']}です！\n社会人ならみんなウェルカム🎉\n\n一緒に楽しい夜を過ごしましょう！\n#京都 #飲み友募集 #社会人交流",
        
        f"🥂 今夜は{event['location']}で飲み会！\n飲み友を募集してます😄\n\n新しい友達との出会いが待ってる✨\n#飲み友募集 #京都グルメ #社会人",
        
        f"🌃 {event['location']}からのご案内🎊\n飲み友募集中です！\n\n社会人同士、気軽に飲める雰囲気🍻\nあなたも一緒に！\n#京都飲み会 #飲み友募集 #楽しい夜"
    ]
    
    import random
    return random.choice(texts)

def post_to_threads(text):
    """Threads APIに投稿"""
    access_token = os.getenv('THREADS_ACCESS_TOKEN')
    business_account_id = os.getenv('THREADS_BUSINESS_ACCOUNT_ID')
    
    if not access_token or not business_account_id:
        print("❌ エラー: 認証情報が設定されていません")
        print("以下をGitHub Secretsに設定してください：")
        print("  - THREADS_ACCESS_TOKEN")
        print("  - THREADS_BUSINESS_ACCOUNT_ID")
        print("\n📝 投稿内容（プレビュー）:")
        print("=" * 50)
        print(text)
        print("=" * 50)
        return False
    
    # Threads APIエンドポイント
    url = f"https://graph.threads.net/v1.0/{business_account_id}/threads"
    
    params = {
        'media_type': 'TEXT',
        'text': text,
        'access_token': access_token
    }
    
    try:
        response = requests.post(url, data=params)
        response.raise_for_status()
        
        result = response.json()
        print(f"✅ 投稿成功！ ID: {result.get('id')}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ 投稿失敗: {e}")
        return False

def main():
    print("🚀 Threads自動投稿スクリプト開始")
    print(f"⏰ 実行時刻: {datetime.now()}")
    
    # サンプルイベントからランダムに選択
    import random
    event = random.choice(SAMPLE_EVENTS)
    
    print(f"\n📅 選択されたイベント: {event['date']}")
    print(f"📍 場所: {event['location']}")
    print(f"🎯 内容: {event['highlights']}")
    
    # 飲み友募集文を生成
    text = generate_envious_text(event)
    print(f"\n📝 生成された投稿文:\n{text}\n")
    
    # Threadsに投稿
    print("🌐 Threadsに投稿中...")
    success = post_to_threads(text)
    
    if success:
        print("\n✨ 完了！飲み友募集をThreadsで共有しました")
    else:
        print("\n⚠️ テストモード: 実際に投稿するにはシークレット設定が必要です")

if __name__ == '__main__':
    main()
