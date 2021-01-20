import random
import matplotlib.pyplot as graph

# カウンターの初期化
count_changed_wins = 0
count_unchanged_wins = 0
list_changed_wins = []
list_unchanged_wins = []

# シミュレーション回数
times = 100000000

# 1000回シミュレーション
for i in range(times):

    # 当たりのドアと挑戦者が選ぶドアを決める
    truth = random.randrange(3)
    player_selected = random.randrange(3)
    doors_unselected = [d for d in range(3) if d is not player_selected]

    # 司会者が選ぶドアを決める
    if player_selected == truth:
        master_selected = random.choice(doors_unselected)
    elif doors_unselected[0] == truth:
        master_selected = doors_unselected[1]
    elif doors_unselected[1] == truth:
        master_selected = doors_unselected[0]

    # 残されたドアを決める
    doors_unselected.remove(master_selected)
    another_door = doors_unselected[0]

    # 勝ち回数をカウント
    if another_door == truth:
        count_changed_wins += 1
    elif player_selected == truth:
        count_unchanged_wins += 1

    # リストのデータ追加
    list_changed_wins.append(count_changed_wins/(count_changed_wins + count_unchanged_wins))
    list_unchanged_wins.append(count_unchanged_wins/(count_changed_wins + count_unchanged_wins))

# 勝ち回数と確率の表示
print('count_changed_wins = ', count_changed_wins, 'list_changed_wins = ',list_changed_wins[-1])
print('count_unchanged_wins = ', count_unchanged_wins, 'list_unchanged_wins = ', list_unchanged_wins[-1])

# 確率グラフ表示
graph.plot(list_changed_wins, label='list_changed_wins')
graph.plot(list_unchanged_wins, label='list_unchanged_wins')
graph.legend()
graph.show()