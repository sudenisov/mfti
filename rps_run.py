from kaggle_environments import evaluate
from my_agents import all_agents

number_episodes_steps = 100

# запуск проверки двух агентов
# на вход поступают функции реализующие данных агентов
def rps_episode_steps(func1, func2):
    res = evaluate(
        "rps",
        [func1, func2],
        configuration={"episodeSteps": number_episodes_steps},
        debug=True
    )
    if res[0][0] > res[0][1]:
        ret = 1
    elif res[0][0] == res[0][1]:
        ret = 0
    else:
        ret = -1
    return ret

# запуск агентов и сбор общего результата
def rps_all_agents_run(agents):
    len_agent = len(agents)
    res = [0]*len_agent
    for i in range(len_agent):
        for j in range(i+1, len_agent):
            print("\rround {:>4} / {}".format(i*len_agent + j + 1, len_agent*(len_agent-1)), end="")
            res_win = rps_episode_steps(agents[i][1], agents[j][1])
            if (res_win > 0):
                res[i] += 1
            elif (res_win < 0):
                res[j] += 1
    print()
    return res

# вывод в удобном виде всех результатов
def rps_print_result(result, agents):
    print("Results:")
    print("{:^4} {:^25} | {}".format("№","agent name", "count win"))
    print("_"*37)
    for i in range(len(agents)):
        print("[{:>2}] {:^25} = {: }".format(i+1, agents[i][0], result[i]))

if __name__ == '__main__':
# вывод основной информации
    print("RPS info:")
    print("{:<25} = {}".format("agent count ", len(all_agents)))
    print("{:<25} = {}".format("number of episode steps ", number_episodes_steps))
    print("{:<25} = {}".format("number of rounds", len(all_agents)*(len(all_agents)-1)))

# запуск агентов и сбор общего результата
    result = rps_all_agents_run(all_agents)
# вывод в удобном виде всех результатов
    rps_print_result(result, all_agents)

