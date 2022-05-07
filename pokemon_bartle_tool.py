TYPE_NAME = [
    "None",
    "Normal",
    "Fire",
    "Water",
    "Electric",
    "Grass",
    "Ice",
    "Fighting",
    "Poison",
    "Ground",
    "Flying",
    "Psychic",
    "Bug",
    "Rock",
    "Ghost",
    "Dragon",
    "Dark",
    "Steel",
    "Fairy"
]

TYPE_NAME_JP = [
    "なし",
    "ノーマル",
    "ほのお",
    "みず",
    "でんき",
    "くさ",
    "こおり",
    "かくとう",
    "どく",
    "じめん",
    "ひこう",
    "エスパー",
    "むし",
    "いわ",
    "ゴースト",
    "ドラゴン",
    "あく",
    "はがね",
    "フェアリー"
]


"""
タイプ相性を示す。値が効果倍率
"""
COMPATIBILITY = [
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.0, 1.0, 1.0, 0.5, 1.0],
    [1.0, 1.0, 0.5, 0.5, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 0.5, 1.0, 0.5, 1.0, 2.0, 1.0],
    [1.0, 1.0, 2.0, 0.5, 1.0, 0.5, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 2.0, 1.0, 0.5, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 2.0, 0.5, 0.5, 1.0, 1.0, 1.0, 0.0, 2.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0],
    [1.0, 1.0, 0.5, 2.0, 1.0, 0.5, 1.0, 1.0, 0.5, 2.0, 0.5, 1.0, 0.5, 2.0, 1.0, 0.5, 1.0, 0.5, 1.0],
    [1.0, 1.0, 0.5, 0.5, 1.0, 2.0, 0.5, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 0.5, 1.0],
    [1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 0.5, 1.0, 0.5, 0.5, 0.5, 2.0, 0.0, 1.0, 2.0, 2.0, 0.5],
    [1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 0.0, 2.0],
    [1.0, 1.0, 2.0, 1.0, 2.0, 0.5, 1.0, 1.0, 2.0, 1.0, 0.0, 1.0, 0.5, 2.0, 1.0, 1.0, 1.0, 2.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 0.5, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 0.5, 1.0, 1.0, 1.0, 0.5, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.0, 0.5, 1.0],
    [1.0, 1.0, 0.5, 1.0, 1.0, 2.0, 1.0, 0.5, 0.5, 1.0, 0.5, 2.0, 1.0, 1.0, 0.5, 1.0, 2.0, 0.5, 0.5],
    [1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 2.0, 0.5, 1.0, 0.5, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0],
    [1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 0.5, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 0.5, 0.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 0.5, 1.0, 0.5],
    [1.0, 1.0, 0.5, 0.5, 0.5, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 0.5, 2.0],
    [1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 2.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 0.5, 1.0]
]

EFFECTIVE_CHAR = ["✖", "🔺", "⚪", "⭕"]
JUDGE_CHAR = ["⬛", "🟨", "🟩"]



def make_type_pairs():
    """
    タイプのペアである数字の組み合わせのリストを作成

    Returns
    -------
    type_pairs : list of (int, int)
        タイプのペア
    """

    types = list(range(19))
    type_pairs = []
    for i in range(19):
        for j in range(i+1, 19):
            type_pairs.append((types[i], types[j]))
    return type_pairs



def check_effective(type_attack, type_diffence):
    """
    攻撃による効果量を求める

    Attributes
    ----------
    type_attack : int
        攻撃タイプ
    type_diffence : (int, int)
        防御側のタイプのペア
    
    Returns
    -------
    効果の倍率を変換して返す。0:なし, 1:いまひとつ, 2:ふつう, 3:抜群
    """

    power =  COMPATIBILITY[type_attack][type_diffence[0]] * COMPATIBILITY[type_attack][type_diffence[1]]
    if power == 0.0:
        return 0
    elif power < 1.0:
        return 1
    elif power == 1.0:
        return 2
    else:
        return 3


def judge_type_pair(type_pair_call, type_pair_ans):
    """
    回答の一致度を返す。

    Attributes
    ----------
    type_pair_call : (int, int)
        提出されたタイプのペア
    type_pair_ans : (int, int)
        正解となるタイプのペア

    Returns
    -------
    回答の一致度。0:不正解, 1:一部正解, 2:正解
    """

    res = 0
    if type_pair_call[0] == type_pair_call[1]:
        type_pair_call = (type_pair_call[0], 0)
    if type_pair_ans[0] == type_pair_ans[1]:
        type_pair_ans = (type_pair_ans[0], 0)

    if type_pair_call[0] in type_pair_ans:
        res += 1
    if type_pair_call[1] in type_pair_ans:
        res += 1
    return res


"""
以下、表示用の関数
"""

def print_types(type_name):
    for i, type in enumerate(type_name):
        if i == 0:
            continue
        print(f"{i} : {type}")



def print_type_pair(type_pair, type_name):
    if type_pair[0] == 0 or type_pair[1] == 0:
        print(type_name[max(type_pair)])
    else:
        print(f"{type_name[type_pair[0]]}&{type_name[type_pair[1]]}")



def print_type_pairs(type_pairs, type_name):
    for type_pair in type_pairs:
        print_type_pair(type_pair, type_name)



def print_effective_list():
    for i in range(4):
        print(f"{i} : {EFFECTIVE_CHAR[i]}")



def print_judge_list():
    for i in range(3):
        print(f"{i} : {JUDGE_CHAR[i]}")
