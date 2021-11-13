from collections import Counter
from collections import OrderedDict


class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def player_rank(self, rank):
        ranks = []
        for i, (name, counter) in enumerate(self.standings.items()):
            player = (-counter['score'], counter['games_played'], i, name)
            ranks.append(player)
        ranks = sorted(ranks)
        print(ranks)
        return ranks[rank - 1][3]


def main():
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 4)
    table.record_result('Chris', 5)
    table.record_result('Chris', 0)
    print(table.player_rank(1))


if __name__ == '__main__':
    main()
