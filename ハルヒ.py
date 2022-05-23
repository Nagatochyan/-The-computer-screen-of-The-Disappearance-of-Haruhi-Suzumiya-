from time import sleep


def yuki_n(*message, speed=0.15):
    count = 0 #何行目を出力し終わったあとかを代入する変数
    name = "ＹＵＫＩ. Ｎ＞"

    
    msg = message[0]

    #名前を表示
    for s in range(len(name)):
        print(name[0:s+1]+"\r",end="")
        sleep(speed)

    for i in range(len(msg)):
       
        if i == len(msg)-1:
            print(name + msg)
            sleep(speed)
            count += 1

        else:
            print(name + msg[0:i+1],end="")
            print("＿"+"\r",end="")
            sleep(speed)

    
    if len(message) > 1:
        for msg in message[1:]:
            for i in range(len(msg)):
                   
                    if i == len(msg)-1:
                        print("　　　　　　　" + msg)
                        sleep(speed)
                        count += 1

                    else:
                        print("　　　　　　　" + msg[0:i+1],end="")
                        print("＿"+"\r",end="")
                        sleep(speed)

    
    if count == len(message):
        print("")



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



yuki_n("これをあなたが読んでいる時、","わたしはわたしではないだろう。")
yuki_n("このメッセージが表示されたということは、","そこにはあなた、わたし、涼宮ハルヒ、朝比奈みくる、","小泉一樹が存在しているはずである。")
yuki_n("それが鍵。","あなたは回答を見つけ出した。")
yuki_n("これは緊急脱出プログラムである。"," ","起動させる場合はエンターキーを、","そうでない場合はそれ以外のキーを選択せよ。"," ","起動させた場合、"\
    ,"あなたは時空修正の機会を得る。","ただし成功は保証できない。","また帰還の保証もできない。")
yuki_n("このプログラムが起動するのは一度きりである。","実行ののち、消去される。"," ","非実行が選択された場合は起動せずに削除される。"," ")
ready()

input()
