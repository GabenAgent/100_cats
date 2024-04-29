import random
import csv


def simulate_scores(players):
    score = {}
    for i in players:
        sim_score = [random.randint(0, 1000) for j in range(100)]
        score[i] = sim_score
    print(score)
    return score


def score_counter(players_score):
    counter = {}
    for player, score in players_score.items():
        average = sum(score) / len(score)
        counter[player] = average
    print(counter)
    return counter


def save_to_csv(average_scores):
    with open(game_csv, "w", newline="") as csvfile:



players = ("Josh", "Luke", "Kate", "Mark" , "Mary")
players_score = simulate_scores(players)
average_scores = score_counter(players_score)
simulate_scores(players)
score_counter(players_score)




