import random
from utils import get_score

last_round_robin = 0

# циклический перебор (0 - 1 - 2)
def round_robin(observation, configuration):
    global last_round_robin
    last_round_robin = (last_round_robin+1) % 2
    return last_round_robin

# случайный выбор
def random_step(observation, configuration):
    return random.randrange(0, configuration.signs)

# всегда камень (0)
def rock(observation, configuration):
    return 0

# всегда бумага (1)
def paper(observation, configuration):
    return 1

# всегда ножници (2)
def scissors(observation, configuration):
    return 2

# первый ход - случайный выбор
# все остальные ходы - повтор прошлого хода опонента
def copy_opponent(observation, configuration):
    if observation.step > 0:
        return observation.lastOpponentAction
    else:
        return random.randrange(0, configuration.signs)


# первый ход - случайный выбор
# все остальные ходы - реакция на прошлый ход (если прошлый ножници, то будет камень)
def reactionary(observation, configuration):
    if observation.step == 0:
        return random.randrange(0, configuration.signs)
    else:
        return (observation.lastOpponentAction + 1) % configuration.signs

reactionary_last_step = 0
# первый ход - случайный выбор
# все остальные ходы - ожидаем, что противник сделает реакцию на наш прошлый ход и делаем реакцию на его реакцию
def double_reactionry(observation, configuration):
    global reactionary_last_step
    if observation.step == 0:
        reactionary_last_step = random.randrange(0, configuration.signs)
    else:
        reactionary_last_step = (reactionary_last_step + 2) % configuration.signs
    return reactionary_last_step


action_histogram = {}

# первый ход - случайный выбор
# все остальные ходы - выбор действия на основании статистики всех прошлых ходов
def statistical(observation, configuration):
    global action_histogram
    if observation.step == 0:
        action_histogram = {}
        return random.randrange(0, configuration.signs)
    action = observation.lastOpponentAction
    if action not in action_histogram:
        action_histogram[action] = 0
    action_histogram[action] += 1
    mode_action = None
    mode_action_count = None
    for k, v in action_histogram.items():
        if mode_action_count is None or v > mode_action_count:
            mode_action = k
            mode_action_count = v
            continue

    return (mode_action + 1) % configuration.signs

# чередование камень и случайное значение
def rock_random(observation, configuration):
    if (observation.step % 2) == 0:
        return 0
    else:
        return random.randrange(0, configuration.signs)

# чередование бумага и случайное значение
def paper_random(observation, configuration):
    if (observation.step % 2) == 0:
        return 1
    else:
        return random.randrange(0, configuration.signs)

# чередование ножници и случайное значение
def scissors_random(observation, configuration):
    if (observation.step % 2) == 0:
        return 2
    else:
        return random.randrange(0, configuration.signs)

last_random = 0

# случайный выбор без повторений прошлого
def random_without_repetition(observation, configuration):
    global last_random
    if observation.step == 0:
        last_random = random.randrange(0, configuration.signs)
    else:
        while True:
            rand = random.randrange(0, configuration.signs)
            if (rand != last_random):
                break
        last_random = rand
    return last_random

all_agents = [
    ["rock", rock],
    ["paper", paper],
    ["scissors", scissors],
    ["rock_random", rock_random],
    ["paper_random", paper_random],
    ["scissors_random", scissors_random],
    ["copy_opponent", copy_opponent],
    ["reactionary", reactionary],
    ["double_reactionry", double_reactionry],
    ["statistical", statistical],
    ["random_step", random_step],
    ["round_robin", round_robin],
    ["random_without_repetition", random_without_repetition]
]

