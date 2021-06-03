import winsound as ws
import time

tempo = 120

sound_list = list()
a0 = 32.703 # C1
ai = a0

onkais = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']

sound_list.append(list()) # 空リスト
for i in range(1, 8):
    sound_list.append(list())
    for onkai in onkais:
        sound_list[i].append(round(ai))
        ai *= (2 ** (1/len(onkais)))

def kyuusi(onpu):
    duration = onpu[2] * 60 * 2 / tempo
    time.sleep(duration)

def beeping(onpu):
    if onpu[0] == 'n':
        kyuusi(onpu)
        return
    sound = onpu[0]
    pitch = onpu[1]
    duration = onpu[2] * 1000 * 60 / tempo

    frequency = sound_list[pitch][onkais.index(sound)]
    ws.Beep(frequency, round(duration))

# # little star
# gakuhu = [('E', 6, 0.5), ('E', 6, 0.5), ('n', 0, 0.5), ('E', 6, 0.5), ('n', 0, 0.5), ('C', 6, 0.5),('E', 6, 0.5), ('n', 0, 0.5),
#            ('G', 6, 0.5), ('n', 0, 0.5),('n', 0, 0.5),('n', 0, 0.5),('G', 5, 0.5),('n', 0, 0.5),('n', 0, 0.5),('n', 0, 0.5),]

# 夜に駆ける
gakuhu = [('C', 6, 0.5), ('C', 6, 0.5), ('C', 7, 0.5), ('H', 6, 0.5), ('G', 6, 0.5), # 忘れてし
            ('G', 6, 0.75), ('A', 6, 0.25), ('E', 6, 0.5), ('D', 6, 0.5),('C', 6, 0.5), ('D', 6, 0.5), ('A', 6, 0.5), # まいたくて閉じ込 
            ('G', 6, 1.25), ('A', 6, 0.25), ('E', 6, 1.25), ('C', 6, 0.25),('D', 6, 0.5), ('C', 6, 1), # めた日々も
            ('C', 6, 0.5), ('G', 6, 0.5),('F', 6, 0.5), ('E', 6, 0.5), ('D', 6, 0.5), ('C', 6, 0.5), # 抱きしめたぬく
            ('H', 5, 0.5), ('C', 6, 0.5), ('D', 6, 0.5), ('F', 6, 0.5), ('E', 6, 0.5), ('D', 6, 0.25), ('E', 6, 1), ('A', 6, 0.5), # もりで溶かすか
            ('G', 6, 0.5), ('n', 0, 0.5), ('E', 6, 0.5), ('G', 6, 0.5), # ら、怖
            ('A', 6, 1.25), ('F', 6, 0.25), ('E', 6, 0.5), ('D', 6, 0.5),('H', 6, 0.5), ('A', 6, 0.5), ('G', 6, 0.5), # くないよいつか 
            ('G', 6, 0.5), ('A', 6, 0.5),('H', 6, 0.5), ('C', 7, 1), ('E', 6, 0.5), ('D', 6, 0.5), ('C', 6, 0.5), # 日が昇るまで
            ('n', 0, 0.5), ('A', 5, 0.5), ('C', 6, 0.5), ('F', 6, 0.5), ('E', 6, 0.5), ('C', 6, 0.5), ('D', 6, 1), # 二人でいよ
            ('C', 6, 3) # う
        ]


for onpu in gakuhu:
    beeping(onpu)
