import unittest
from statistics import Statistics
from player import Player
from sortby import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_hakee_oikean_pelaajan(self):
        player = self.statistics.search("Semenko")

        self.assertEqual(str(player), "Semenko EDM 4 + 12 = 16")

    def test_search_palauttaa_none_jos_pelaajaa_ei_ole(self):
        player = self.statistics.search("Ojanen")

        self.assertEqual(player, None)

    def test_team_palauttaa_yhden_tiimin_pelaajat(self):
        players = self.statistics.team("EDM")

        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[1].name, "Kurri")
        self.assertEqual(players[2].name, "Gretzky")

    def test_top_palauttaa_oikeat_pelaajat_ja_oikean_maaran_pelaajia(self):
        players = self.statistics.top(2)

        self.assertEqual(len(players), 3)

        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")

    def test_top_palauttaa_oikeat_pelaajat_maaleilla(self):
        players = self.statistics.top(1, SortBy.GOALS)

        self.assertEqual(players[0].name, "Lemieux")
        self.assertEqual(players[1].name, "Yzerman")

    def test_top_palauttaa_oikeat_pelaajat_syotoilla(self):
        players = self.statistics.top(1, SortBy.ASSISTS)

        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Yzerman")
