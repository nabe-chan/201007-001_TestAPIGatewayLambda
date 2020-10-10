# API Gateway/Lambda + FastAPI/Mangum のサンプルコード

AWS API Gateway と Lambda で 動的Webページを返却するサンプルコードです。

# 目的

WEBアプリケーションサーバとLambdaの、いずれでも動作するコードを作成することです。  
および、各技術の習熟のためです。

# 使用した技術

AWS
 - [AWS API Gateway](https://aws.amazon.com/jp/api-gateway/)
 - [AWS Lambda](https://aws.amazon.com/jp/lambda/)

Python
 - [FastAPI](https://github.com/tiangolo/fastapi)
 - [Mangum](https://github.com/jordaneremieff/mangum)
 - [uvicorn](https://www.uvicorn.org/)

# 参考にした情報

[Serverless Framework+mangum+FastAPIで、より快適なPython API開発環境を作る (JX PRESS Corp)](https://tech.jxpress.net/entry/2020/03/29/170000)

# 使い方memo

## 前提

- 開発環境に python3.8 がインストール済みであること。
- 開発環境に リポジトリデータがダウンロードされていること。

## パターンA: uvicornでローカル実行

1. 以下のライブラリをpipでインストール
```
pip install fastapi mangum jinja2 aiofiles uvicorn
```
2. src/main.pyを直接実行
```python
python src/main.py
```
3. ブラウザから`http://127.0.0.1:8000`へアクセス

## パターンB: API Gateway/lambdaでクラウド実行

### layerデータ作成

1. 以下のディレクトリを適当な場所に作成
```
layer/python/lib/python3.8/site-packages
```
2. コンソール(コマンドプロンプト)を起動し、layerフォルダに移動
3. 以下のコマンドを実行し、ライブラリ群をダウンロード※Win環境ではバックスラッシュ
```
pip install fastapi mangum jinja2 aiofiles uvicorn -t python/lib/python3.8/site-packages
```
4. layer/pythonフォルダをZIP圧縮
 - 解凍時にpythonフォルダが出力されることを想定

### Functionデータ作成
1. リポジトリのsrcディレクトリをZIP圧縮

### API Gateway/Lambda構成

1. AWS Consoleより Lambda Functionを作成
 - Python 3.8 を選択
2. AWS Consoleより API Gatewayを作成
 - HTTP API を選択
 - CORSを有効化
 - ペイロード形式は2.0 (default)
3. API Gateway と Lambda Function を統合
 - ルートは ANY:"/" → Lambda Function を想定
3. Lambda FunctionのLayerページから作成したlayerデータをアップロード
4. Lambda Functionの関数ページから作成したFunctionデータをアップロード
5. Lambda Functionのハンドラ設定をmain.pyに変更
```
 <ZIPファイル名>/src/main.handler
```
6. Lambda FunctionのLayerを先ほどアップロードしたlayerに変更

### 確認

1. API Gatewayの作成したステージのURLへアクセス
2. 必要に応じて、CloudWatchのロググループからログを確認

# 最後に

ご質問・ご要望がありましたら、  
Twitterアカウントまでご連絡ください。  
(Twitter: nabe-chan@harukaze256)