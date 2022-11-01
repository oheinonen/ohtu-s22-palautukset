import unittest
from statistics import Statistics
from player import Player
from enum import Enum

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_haku_palauttaa_oikean_pelaajan(self):
        player = self.statistics.search("Lemieux")
        self.assertEqual(player.name, "Lemieux")
    
    def test_haku_ei_palauta_olematonta_pelaajaa(self):
        player = self.statistics.search("Koivu")
        self.assertIsNone(player)
    
    def test_team_palauttaa_haetun_tiimin_pelaajat(self):
        team = self.statistics.team("EDM")
        for player in team:
            self.assertEqual(player.team, "EDM")
    
    def test_top_palauttaa_halutun_määrän_parhaita(self):
        top = self.statistics.top(2)
        self.assertEqual(len(top), 2)
        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")

    def test_top__pisteillä_palauttaa_halutun_määrän_parhaita(self):
        top = self.statistics.top(2, SortBy.POINTS)
        self.assertEqual(len(top), 2)
        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")

    def test_top_maaleilla_palauttaa_parhaat_maalintekijät(self):
        top = self.statistics.top(2, SortBy.GOALS)
        self.assertEqual(len(top), 2)
        self.assertEqual(top[0].name, "Lemieux")
        self.assertEqual(top[1].name, "Yzerman")

    def test_top_syötöillä_palauttaa_parhaat_syöttelijät(self):
        top = self.statistics.top(2, SortBy.ASSISTS)
        self.assertEqual(len(top), 2)
        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Yzerman")


