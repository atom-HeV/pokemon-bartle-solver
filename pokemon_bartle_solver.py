import pokemon_bartle_tool as pbt

class PokemonBartleSolver:
    """
    Pokemon Bartleを解くクラス
    正解候補を持ち、回答によって返ってくる結果から候補を減らしていく

    Attributes
    ----------
    type_pairs : list of (int, int)
        タイプのペアの正解候補のリスト
    """

    def __init__(self):
        self.type_pairs = pbt.make_type_pairs()
        self.types = list(range(19))



    def suggest_type_attack(self):
        """
        MinMax法（alpha-beta法）を用いて、最悪の場合の候補がもっとも小さくなる攻撃タイプを求める

        Returns
        -------
        type_res : int
            攻撃タイプ
        sta_minmax : int
            最悪ケースの候補数
        """

        type_res = -1
        sta_minmax = len(self.type_pairs)

        for type_attack in self.types:
            effective_division = [0] * 4
            sta_max = 0
            for type_diffence in self.type_pairs:
                ce = pbt.check_effective(type_attack, type_diffence)
                effective_division[ce] += 1

                sta_max = max(sta_max, effective_division[ce])
                if effective_division[ce] > sta_minmax:
                    break

            if sta_max < sta_minmax: 
                sta_minmax = sta_max
                type_res = type_attack
        return type_res, sta_minmax



    def suggest_type_pair_answer(self):
        """
        MinMax法（alpha-beta法）を用いて、最悪の場合の候補がもっとも小さくなる回答を求める。
        正解になりうるタイプのペアを優先する。

        Returns
        -------
        type_pair_res : (int, int)
            タイプのペア
        stpa_minmax
            最悪ケースの候補数
        """
        
        type_pair_res = (0, 0)
        stpa_minmax = 1000

        for type_pair in self.type_pairs + list(set(pbt.make_type_pairs()) - set(self.type_pairs)):
            judge_division = [0] * 3
            stpa_max = 0
            for type_pair_comp in self.type_pairs:
                jtp = pbt.judge_type_pair(type_pair, type_pair_comp)
                judge_division[jtp] += 1

                stpa_max = max(stpa_max, judge_division[jtp])
                if judge_division[jtp] > stpa_minmax:
                    break
            
            if stpa_max < stpa_minmax:
                stpa_minmax = stpa_max
                type_pair_res = type_pair
        
        return type_pair_res, stpa_minmax



    def suggest_next_answer(self):
        """
        "attack"と"answer"のどちらが候補を絞れるかをもとめ、それらの結果を返す
        
        Returns
        -------
        1つ目の返り値 : str
            "attack"と"answer"のどちらを選んだかを返す
        2,3つ目
            それぞれの関数を参照
        """

        if len(self.type_pairs) == 1:
            return "answer", self.type_pairs[0], 1
        
        type_attack, sta_minmax = self.suggest_type_attack()
        type_pair_answer, stpa_minmax = self.suggest_type_pair_answer()

        if sta_minmax < stpa_minmax:
            return "attack", type_attack, sta_minmax
        else:
            return "answer", type_pair_answer, stpa_minmax



    def update_types(self, type):
        """
        攻撃タイプの候補を減らす
        """

        self.types.remove(type)



    def update_type_pairs(self, action, result):
        """
        攻撃相性の結果から、正解候補を減らす

        Attributes
        ----------
        action : str
            "attack"と"answer"のどちらか
        result : ((int, int), int) or (int, int)
            "answer"のとき、タイプのペアと回答の一致度
            "attack"のとき、攻撃タイプと攻撃の効果量を示す
        """

        next_type_pairs = []
        if action == "attack":
            for type_pair in self.type_pairs:
                if pbt.check_effective(result[0], type_pair) == result[1]:
                    next_type_pairs.append(type_pair)
        else:
            for type_pair in self.type_pairs:
                if pbt.judge_type_pair(result[0], type_pair) == result[1]:
                    next_type_pairs.append(type_pair)
        self.type_pairs = next_type_pairs


    def add_result(self, action, result):
        """
        結果から、候補を更新する
        
        Attributes
        ----------
        action : str
            "attack"と"answer"のどちらか
        result : int
            actionによって異なる。
        """

        self.update_type_pairs(action, result)
        if action == "attack":
            self.update_types(result[0])



if __name__ == "__main__":
    """
    コンソール上でPokemon Bartleを解く
    動作確認用。
    """
    type_name = pbt.TYPE_NAME_JP
    solver = PokemonBartleSolver()

    while True:
        # print(len(solver.type_pairs))
        # pbt.print_type_pairs(solver.type_pairs, type_name)
        action, ans, minmax = solver.suggest_next_answer()

        print("---Recommend---")
        if action == "answer":
            print(f"❓相手のタイプを選ぶ")
            pbt.print_type_pair(ans, type_name)
        else:
            print(f"⚔攻撃技のタイプを選ぶ")
            print(f"{ans} : {type_name[ans]}")
        print(f"worst : {minmax}")
        
        print()
        print("---Input Result---")

        print("1 : ⚔攻撃技のタイプを選ぶ")
        print("2 : ❓相手のタイプを選ぶ")

        action_num = int(input("Select action : "))
        action = ["attack", "answer"][action_num - 1]

        if action == "attack":
            # pbt.print_types(type_name)
            # print()
            pbt.print_effective_list()

            type_attack = int(input("Input attack type : "))
            result_effective = int(input("Input effective : "))

            result = (type_attack, result_effective)
        else:
            # pbt.print_types(type_name)
            # print()
            pbt.print_judge_list()

            type1 = int(input("Input type 1 : "))
            type2 = int(input("Input type 2 : "))
            judge = int(input("Input judge : "))

            result = ((type1, type2), judge)

            if judge == 2:
                break
        solver.add_result(action, result)

    

            
        
