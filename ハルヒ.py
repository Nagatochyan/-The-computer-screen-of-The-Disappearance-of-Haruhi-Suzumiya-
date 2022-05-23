from time import sleep

#引数に与えられた文字をYUKI.Nっぽく表示する
def yuki_n(*message, speed=0.15):
    count = 0 #何行目を出力し終わったあとかを代入する変数
    name = "ＹＵＫＩ. Ｎ＞"

    #1行目の出力に対して行う処理
    msg = message[0]

    #名前を表示
    for s in range(len(name)):
        print(name[0:s+1]+"\r",end="")
        sleep(speed)

    for i in range(len(msg)):
        #行の最後の文字の場合、文末に＿をつけない
        if i == len(msg)-1:
            print(name + msg)
            sleep(speed)
            count += 1

        else:
            print(name + msg[0:i+1],end="")
            print("＿"+"\r",end="")
            sleep(speed)

    #2行目以降の出力があれば行う処理
    if len(message) > 1:
        for msg in message[1:]:
            for i in range(len(msg)):
                    #行の最後の文字の場合、文末に＿をつけない
                    if i == len(msg)-1:
                        print("　　　　　　　" + msg)
                        sleep(speed)
                        count += 1

                    else:
                        print("　　　　　　　" + msg[0:i+1],end="")
                        print("＿"+"\r",end="")
                        sleep(speed)

    #最後の行を出力し終わったあとに改行する
    if count == len(message):
        print("")


#「Ｒｅａｄｙ？」を表示する
def ready(speed=0.5):
    ready = "Ｒｅａｄｙ？"
    #「_」を点滅させる
    for _ in range(2):
        print("　　　　　　　" + "＿"+"\r",end="")
        sleep(speed)
        print("　　　　　　　" + " "+"\r",end="")
        sleep(speed)

    print("　　　　　　　" + "＿"+"\r",end="")
    sleep(speed)

    for s in range(len(ready)):
        print("　　　　　　　" + ready[0:s] + "＿" + "\r",end="")
        sleep(0.15)
    print("　　　　　　　" + ready,end="")


#改行する時は複数の引数としてyuki_n関数ににわたす
yuki_n("これをあなたが読んでいる時、","わたしはわたしではないだろう。")
yuki_n("このメッセージが表示されたということは、","そこにはあなた、わたし、涼宮ハルヒ、朝比奈みくる、","小泉一樹が存在しているはずである。")
yuki_n("それが鍵。","あなたは回答を見つけ出した。")
yuki_n("これは緊急脱出プログラムである。"," ","起動させる場合はエンターキーを、","そうでない場合はそれ以外のキーを選択せよ。"," ","起動させた場合、"\
    ,"あなたは時空修正の機会を得る。","ただし成功は保証できない。","また帰還の保証もできない。")
yuki_n("このプログラムが起動するのは一度きりである。","実行ののち、消去される。"," ","非実行が選択された場合は起動せずに削除される。"," ")
ready()

input()