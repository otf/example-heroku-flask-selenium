## このアプリについて
このFlaskアプリは、インデックスにアクセスされたときSeleniumのスクレイピングを実行して、その結果をCSVファイルに集計して返却します。各行に対応するスクレイピング対象のページはレスポンスを返却する前に1秒間スリープします。合計60回のスクレイピングを行うことでCSVファイルの返却に約60秒以上かかりますが、ストリーミングレスポンスの方式を採用することでHerokuの30秒タイムアウトの制限を回避します。

## テストの実行環境
1. Python 3.10.6
1. Flask 2.2.2
1. Selenium 4.4.3
1. pytest 7.1.2
1. Playwright 1.25.1
1. Chromium
1. ChromeDriver

## テストの実行方法

```
$ pip install -r requirements.txt
$ pytest
```

## リンク
* [Request Timeout | Heroku Dev Center](https://devcenter.heroku.com/articles/request-timeout#long-polling-and-streaming-responses)
