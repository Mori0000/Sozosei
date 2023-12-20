import numpy as np
import requests
import json
import wave

def vvox_test(text, filename):                                      # text: 話させたい言葉, filename: 保存するファイル名
    host = "https://kkpaam7cpn.ap-northeast-1.awsapprunner.com"     # ホスト名
    params = (                                                      # パラメータ
        ('text', text),                                             # 話させたい言葉
        ('speaker', 3),                                             # 話者 ずんだもん
    )
    query = requests.post(f'{host}/audio_query', params=params)     # クエリ
    synthesis = requests.post(                                      # 音声合成
        f'{host}/synthesis',                                        # ホスト名
        headers={"Content-Type": "application/json"},               # ヘッダー
        params=params,                                              # パラメータ
        data=json.dumps(query.json())                               # クエリ
    )
    voice = synthesis.content                                       # 音声データ
    with wave.open(filename, 'wb') as wav_file:                     # ファイルを開く
        wav_file.setnchannels(1)                                    # モノラル
        wav_file.setsampwidth(2)                                    # 16bit
        wav_file.setframerate(24000)                                # 24kHz
        wav_file.writeframes(voice)                                 # 音声データを書き込む
vvox_test("もう寝過ぎです。今から私の演奏で目を覚ませます", "okiro3.wav")                              # 音声データを保存する

