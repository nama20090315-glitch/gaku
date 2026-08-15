# 🎉 Threads自動投稿ボット - gaku

GitHub Actionsを使って、羨ましいと思わせる飲み会の様子を自動でThreadsに投稿するボットです！

## 🚀 機能

- ✨ サンプル飲み会イベントから自動生成
- 🎯 毎週金曜夜21時に自動投稿
- 💬 羨ましいと思わせるテキストを自動作成
- 🌐 Threads APIと連携

## 📋 セットアップ手順

### 1️⃣ テストモードで実行してみる

まずは、Threads認証情報なしで動作確認できます。

リポジトリの「Actions」タブから：
1. 「Threads Auto Post」ワークフローを選択
2. 「Run workflow」ボタンをクリック
3. 投稿内容がプレビュー表示されます

### 2️⃣ 実際にThreadsに投稿するには

以下の情報が必要です：

**Meta for Developersで取得：**
- https://developers.facebook.com/apps/ にアクセス
- Business Account ID を取得
- Access Token を生成

**GitHub Secretsに登録：**

1. リポジトリの Settings → Secrets and variables → Actions
2. 以下を新規追加：
   - 名前: `THREADS_ACCESS_TOKEN` → 値: あなたのアクセストークン
   - 名前: `THREADS_BUSINESS_ACCOUNT_ID` → 値: あなたのビジネスアカウントID

### 3️⃣ 自動実行の設定

- **自動実行：** 毎週金曜夜21時に実行（デフォルト設定済み）
- **手動実行：** Actions → Threads Auto Post → Run workflow

## 📝 サンプル投稿内容

```
✨ 最新AIプロジェクト完成を祝う飲み会 🎉
渋谷のおしゃれなバーで開発者A、デザイナーB、PM Cと最高の夜を過ごしました！

🍻 乾杯🎊 #チームパワー #成功祝い
```

## 🔧 カスタマイズ方法

`scripts/post_to_threads.py` の `SAMPLE_EVENTS` を編集して、独自のイベント情報を追加できます：

```python
SAMPLE_EVENTS = [
    {
        "date": "YYYY-MM-DD",
        "location": "場所",
        "participants": ["参加者1", "参加者2"],
        "activities": ["活動1", "活動2"],
        "highlights": "ハイライト"
    }
]
```

## 🧪 ローカルでテスト実行

```bash
python scripts/post_to_threads.py
```

## 📊 実行ログを確認

GitHub Actions → Threads Auto Post → 各実行結果 で投稿状況を確認できます

## ⚡ 今後の拡張案

- [ ] GitHub Discussionsから実際のイベント情報を取得
- [ ] セッション履歴から自動でハイライト抽出
- [ ] 複数言語対応
- [ ] 画像添付機能
- [ ] Slack連携通知

---

**作成日:** 2026-08-15  
**作成者:** nama20090315-glitch  
**ステータス:** 🟢 完成！
