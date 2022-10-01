from kaggle_environments import evaluate
from my_agents import all_agents

number_episodes_steps = 100


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

def rps_print_result(result, agents):
    print("Results:")
    print("{:^4} {:^25} | {}".format("№","agent name", "count win"))
    print("_"*37)
    for i in range(len(agents)):
        print("[{:>2}] {:^25} = {: }".format(i+1, agents[i][0], result[i]))

if __name__ == '__main__':
    print("RPS info:")
    print("{:<25} = {}".format("agent count ", len(all_agents)))
    print("{:<25} = {}".format("number of episode steps ", number_episodes_steps))
    print("{:<25} = {}".format("number of rounds", len(all_agents)*(len(all_agents)-1)))

    result = rps_all_agents_run(all_agents)
    rps_print_result(result, all_agents)

