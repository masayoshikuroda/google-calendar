# google-calendar


## 事前準備

*Google Service設定*
- カレンダーの作成
- 共有設定で、サービスアカウントを追加
- カレンダーのIDを取得

*GCP設定*
- アカウント作成
- プロジェクトの作成
- Calendar APIの有効化
- サービスアカウントの作成
- サービスアカウントのキーをJSON形式で取得

## ごみ収集カレンダーからのゴミ収集予定の取得

引数にカレンダーIDを指定
```
$ python3 garbage.py xxxxx@group.calendar.google.com
$ 不燃ごみの日です。
$
```
