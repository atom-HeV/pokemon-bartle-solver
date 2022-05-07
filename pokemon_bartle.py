import random

import pokemon_bartle_tool as pbt

class PokemonBartle:
    """
    Pokemon Bartleを行うクラス。
    指定した、もしくはランダムな答えを持つ
    
    Attributes
    ----------
    ans_type_pair : (int, int)
        答えのタイプ。数字のペアをタイプとする。
    turn : int
        現在の回答回数。
    cleared : bool
        正解しているかどうか。
    """

    def __init__(self, q_num = -1):
        """
        Parameters
        ----------
        q_num : int
            答えを指定する際に用いる。デフォルトは-1でランダム
        """
        self.type_pairs = self.make_type_pairs()
        if q_num == -1:
            q_num = random.randint(0, len(self.type_pairs))
        self.ans_type_pair = self.type_pairs[q_num]
        self.turn = 0
        self.cleared = False



    def make_type_pairs(self):
        """
        答え候補となる数字のペアを作る

        Returns
        -------
        type_pairs : list of (int, int)
            タイプを表す数字のペアのリスト
        """
        types = list(range(19))
        type_pairs = []
        for i in range(19):
            for j in range(i+1, 19):
                type_pairs.append((types[i], types[j]))
        return type_pairs



    def submit_answer(self, action, ans):
        """
        回答を受け付けて、判定を返す

        Parameters
        ----------
        action : str
            "answer"のとき、回答を判定
            "attack"のとき、タイプ相性を判定
        ans : (int, int) or int
            "answer"のとき、タイプのペア
            "attack"のとき、攻撃タイプ

        Returns
        -------
        res : int
            "answer"のとき、回答の一致度を示す。0:不正解, 1:一部正解, 2:正解
            "attack"のとき、攻撃の効果量を示す。0:なし, 1:いまひとつ, 2:ふつう, 3:抜群
        """
        self.turn += 1
        
        if action == "answer":
            res = pbt.judge_type_pair(ans, self.ans_type_pair)
            if res == 2:
                self.cleared = True
            return res
        
        else:
            res = pbt.check_effective(ans, self.ans_type_pair)
            return res



if __name__ == "__main__":
    """
    コンソール上でPokemon Bartleを行う。
    動作確認用。
    """

    type_name = pbt.TYPE_NAME_JP
    pb = PokemonBartle()

    while True:
        print("1 : ⚔攻撃技のタイプを選ぶ")
        print("2 : ❓相手のタイプを選ぶ")

        action = int(input("Select action : "))

        if action == 1:
            pbt.print_types(type_name)
            print()

            type = int(input("Input attack type : "))
            res = pb.submit_answer("attack", type)
            print(type_name[type], end=" : ")
            print(pbt.EFFECTIVE_CHAR[res])
        else:
            pbt.print_types(type_name)
            print()

            type1 = int(input("Input type 1 : "))
            type2 = int(input("Input type 2 : "))

            res = pb.submit_answer("answer", (type1, type2))
            print(pbt.JUDGE_CHAR[res])
            if res == 2:
                break
            

        

