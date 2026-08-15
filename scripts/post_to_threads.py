#!/usr/bin/env python3
import os
import requests
import json
from datetime import datetime

# サンプル飲み会イベントデータ
SAMPLE_EVENTS = [
    {
        "date": "2026-08-15",
        "location": "渋谷のおしゃれなバー",
        "participants": ["開発者A", "デザイナーB", "PM C"],
        "activities": ["乾杯🍻", "プロジェクト成功祝い🎉", "深夜カラオケ🎤"],
        "highlights": "最新AIプロジェクト完成を祝う飲み会"
    },
    {
        "date": "2026-08-22",
        "location": "六本木のロoftop bar",
        "participants": ["エンジニア5名", "デザイナー2名"],
        "activities": ["夜景を眺めながら乾杯", "新機能ローンチ祝い"],
        "highlights": "1000万ユーザー突破記念パーティー"
    },
    {
        "date": "2026-08-29",
        "location": "青山のワインバー",
        "participants": ["技術リーダー", "新入社員たち"],
        "activities": ["チームビルディング", "キャリア相談"],
        "highlights": "若手エンジニア育成プログラム修了祝い"
    }
]

def generate_envious_text(event):
    """羨ましいと思わせる文章を生成"""
    texts = [
        f"✨ {event['highlights']} 🎉\n{event['location']}で{len(event['participants'])}人の仲間と最高の夜を過ごしました！\n\n🍻 乾杯🎊 #チームパワー #成功祝い",
        
        f"🌃 {event['location']}からの景色最高〜！\n今日は{event['highlights']}🥂\nこんなチームで働けるって幸せだな〜😊\n\n#仕事仲間 #飲み会 #チームワーク",
        
        f"🎉 {event['highlights']}\n参加者：{len(event['participants'])}名の才能あふれるメンバーたち✨\n{event['location']}での時間は最高でした！\n\nこんなチームに出会えてラッキー🍀 #最高の仲間",
        
        f"📍 {event['location']}\n🎊 {event['highlights']}\n\nこのメンバーで一緒に働けるって、本当に幸せ。\n毎日がこんなに充実してて羨ましいでしょ？😄\n\n#エンジニアライフ #最高の環境 #チーム愛"
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
    print(f"👥 参加者: {len(event['participants'])}名")
    
    # 羨ましい文章を生成
    text = generate_envious_text(event)
    print(f"\n📝 生成された投稿文:\n{text}\n")
    
    # Threadsに投稿
    print("🌐 Threadsに投稿中...")
    success = post_to_threads(text)
    
    if success:
        print("\n✨ 完了！羨ましい飲み会の様子をThreadsで共有しました")
    else:
        print("\n⚠️ テストモード: 実際に投稿するにはシークレット設定が必要です")

if __name__ == '__main__':
    main()
