# ライブラリー読込
import tkinter
import random

# おみくじ結果
kuji = ['大吉','中吉','小吉','吉','末吉','凶','大凶']
# プログラム動作状態
state = 'stop'
# ループ処理ID
after_id = None

#おみくじ結果を表示する関数
def getResult():
    # プログラム動作状態を取得
    global state
    # ループ処理IDを取得
    global after_id

    # 動作中の場合
    if state == 'run':
        # 結果待ちのループ処理を終了
        form.after_cancel(after_id)
        #結果ラベルの色を戻す
        result['background'] = 'SystemButtonFace'
        
        # おみくじ結果の出力
        result['text'] = kuji[random.randrange(len(kuji))]
        # 停止中に更新
        state = 'stop'

#おみくじを開始する関数
def omikuziStart():
    # プログラム動作状態を取得
    global state

    # 停止中の場合
    if state == 'stop':
        # おみくじ結果をクリア
        result['text'] = ''
        # 動作中に更新
        state = 'run'
        # 結果待ちの処理を呼出
        turnResult()

# おみくじ結果待ちの関数
def turnResult():
    # プログラム動作状態を取得
    global state
    # ループ処理IDを取得
    global after_id

    # 動作中の場合
    if state == 'run':
        # 結果ラベルの色を点滅表示
        if result['background'] == 'red':
            # 結果ラベルの色を白に変更
            result['background'] = 'white'
        else:
            # 結果ラベルの色を赤に変更
            result['background'] = 'red'

        # 200ms後にこの関数を呼出       
        after_id = form.after(200,turnResult)

# TKクラス作成
form = tkinter.Tk()
# 画面サイズ設定
form.geometry('300x150')
# 画面タイトル設定
form.title('⑤おみくじプログラム')

# Labelクラスの作成
title = tkinter.Label(form,font=('',20),text="おみくじ")
result = tkinter.Label(form,font=('',20),width=20,borderwidth=1,relief="sunken")
# Labelの描画
title.pack(pady=5)
result.pack(pady=10)

# Buttonクラス作成
start_button = tkinter.Button(form,text="スタート",width=14,command=omikuziStart)
stop_button = tkinter.Button(form,text="ストップ",width=14,command=getResult)
# Buttonの描画
start_button.pack(fill = 'x', padx=20,pady=10,side='left')
stop_button.pack(fill = 'x', padx=20,pady=10,side='left')

# 画面をそのまま表示
form.mainloop()

