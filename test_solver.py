import pokemon_bartle
import pokemon_bartle_solver
import pokemon_bartle_tool as pbt

if __name__ == "__main__":
    turn_min = 100
    turn_max = 0
    turn_sum = 0

    turn_cnt = [0] * 9

    for i in range(171):
        pb = pokemon_bartle.PokemonBartle(i)
        pbs = pokemon_bartle_solver.PokemonBartleSolver()

        while True:
            action, ans, minmax = pbs.suggest_next_answer()
            res = pb.submit_answer(action, ans)

            if action == "answer" and res == 2:
                pbt.print_type_pair(pb.ans_type_pair, pbt.TYPE_NAME_JP)
                print(pb.turn)

                turn_min = min(turn_min, pb.turn)
                turn_max = max(turn_max, pb.turn)
                turn_sum += pb.turn
                turn_cnt[pb.turn] += 1
                break
            pbs.add_result(action, (ans, res))
    
    print(f"Min : {turn_min}")
    print(f"Max : {turn_max}")
    print(f"Avg : {turn_sum / 171}")

    for i in range(3, 9):
        print(f"{i} : {turn_cnt[i]}")