## このアプリについて
このFlaskアプリは、インデックスにアクセスされたときSeleniumのスクレイピングを実行して、その結果をCSVファイルに集計して返却します。各行に対応するスクレイピング対象のページはレスポンスを返却する前に1秒間スリープします。合計60回のスクレイピングを行うことでCSVファイルの返却に約60秒以上かかりますが、ストリーミングレスポンスの方式を採用することでHerokuの30秒タイムアウトの制限を回避します。

## 環境
1. Nix 2.10.3 ([Enable flakes](https://nixos.wiki/wiki/Flakes#Enable_flakes))

## ビルド方法
```sh
$ make nix-build
```

## Flaskアプリの起動方法
```sh
$ make nix-server
```

## テストの実行方法
### 開発環境(ローカル)
```sh
$ make nix-test-develop
```

### 本番環境(Heroku)
```sh
$ make nix-test-production
```

## リンク
* [Request Timeout | Heroku Dev Center](https://devcenter.heroku.com/articles/request-timeout#long-polling-and-streaming-responses)
* [NixOS - Getting Nix / NixOS](https://nixos.org/download.html)
* [Enable flakes](https://nixos.wiki/wiki/Flakes#Enable_flakes)
