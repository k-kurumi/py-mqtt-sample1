## MQTT sample1

MQTT broker(サーバに相当)にpythonから送受信するサンプル
写経元 http://tomowatanabe.hatenablog.com/entry/2014/04/21/095650

#### MQTT brokerのインストール、起動

```
$ sudo apt install mosquitto

## 起動しているので止める
$ sudo systemctl stop mosquitto.service

## ログ多めのフォアグラウンドで起動
$ mosquitto -v
```

#### 受信側

```
$ pip install -r requirements.txt
$ python sub.py
```

#### 送信側

```
$ pip install -r requirements.txt
$ python pub.py
```
