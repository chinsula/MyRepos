from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000 # КОЛИЧЕСТВО ВРЕМЕННЫХ МЕТОК

PROBABILITY_SCORE_CHANGED = 0.0001 # ОЦЕНКА ВЕРОЯТНОСТИ ИЗМЕНЕНИЯ

PROBABILITY_HOME_SCORE = 0.45 #ОЦЕНКА ВЕРОЯТНОСТИ ИСХОДА

OFFSET_MAX_STEP = 3 # МАКСИМАЛЬНЫЙ ШАГ СМЕЩЕНИЯ

INITIAL_STAMP = {  #НАЧАЛЬНАЯ ОТМЕТКА
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}



def generate_stamp(previous_value): #создать штамп
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()

pprint(game_stamps)


def get_score(game_stamps, offset):
    '''
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.

        Берет список игровых штампов и смещений времени, для которых возвращаются результаты для команд хозяев
        и гостей. Обратите внимание, что для некоторых смещений список game_stamps может не содержать баллов

        которая вернет счет на момент offset в списке game_stamps
    '''
    for score_offset in game_stamps:  # перебираем список словарей для поиска нужного значения по ключу offset
        if score_offset['offset'] == offset:
            return score_offset['score']['away'], score_offset['score']['home']

    # return home, away

if __name__ == "__main__":
    print({get_score(game_stamps, 97816)})

