# このリポジトリについて

このリポジトリは、PHPの基本を学ぶための環境として用意したものです。
vscodeのDevContainer機能を用いることで、少しだけ使い勝手が増す(かもしれない)以外は基本的にPHPとMySQLの動く環境です。

# 前提

以下のソフトウェアと拡張が必要です。

- vscode
- vscodeのDevContainer拡張(ID: `ms-vscode-remote.remote-containers`)
- Docker Desktop(Dockerエンジンが動けば種類を問いません、rancherやOrbStackでも多分いけますが未確認)

# 使い方

1. vscodeでこのディレクトリを開く
2. `Shift+Ctrl+P`(macOSでは`Shift+CMD+P`)にて "Rebuild and reopen in container"を実行
3. 初回はイメージ取得などで少し時間がかかりますが、開発環境が起動します

# DevContainerでのディレクトリの扱い

開発コンテナ内の `/workspace` ディレクトリ以下にディレクトリが用意され、マウントされています。

`public`:
    Webサーバー上のコンテンツとして見えるファイルを配置してください、このディレクトリは同時に `/var/www/html` に配置されており、そのまま[Webサーバー](http://localhost:8000/)側から見ることができます
`db`:
    データベース(MySQL)に繋がっており、データベースコンテナでは `/docker-entrypoint-initdb.d`として見えます。
    このディレクトリにシェルスクリプトやSQLのファイルを配置すると、コンテナの初回起動時に実行されます(初期化コードとして機能する)。
`all`:
    普段使うことは無いと思いますが、もともとのディレクトリがそのままマップされています。

# phpMyAdminについて

DevContainerで起動をすると、データベース操作の補助として、phpMyAdminコンテナが追加で起動します。
こちらは[別ポート](http://localhost:8001/)にてアクセス可能です。
本番運用で見えるところに配置してはいけないため、DevContainer専用で起動します。

# データベースの設定について

あくまで開発の練習用です。本番運用では絶対にこの設定のままで使わないで下さい。

- サーバー名: db(として見える)
- 管理ID: root
- ログインパスワード: admin


