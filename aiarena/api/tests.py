from django.test import TestCase, TransactionTestCase

from aiarena.core.tests.tests import FullDataSetMixin


class ApiReadPrivatePagesTestCase(FullDataSetMixin, TransactionTestCase):
    """
    Tests to ensure private API endpoint pages don't break.
    """

    def test_get_api_discord_users_page(self):
        self.client.login(username='regular_user', password='x')
        response = self.client.get('/api/discord-users/')
        self.assertEqual(response.status_code, 403)

        self.client.login(username='staff_user', password='x')
        response = self.client.get('/api/discord-users/')
        self.assertEqual(response.status_code, 200)


class ApiReadPublicPagesTestCase(FullDataSetMixin, TransactionTestCase):
    """
    Tests to ensure public API endpoint pages don't break.
    """

    def setUp(self):
        super().setUp()
        self.client.login(username='staff_user', password='x')

    def test_get_api_index_page(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)

    def test_get_api_bots_page(self):
        response = self.client.get('/api/bots/')
        self.assertEqual(response.status_code, 200)

    def test_get_api_competitions_page(self):
        response = self.client.get('/api/competitions/')
        self.assertEqual(response.status_code, 200)

    def test_get_api_competitionmatchupstatus_page(self):
        response = self.client.get('/api/competition-bot-matchup-stats/')
        self.assertEqual(response.status_code, 200)

    def test_get_api_competitionparticipations_page(self):
        response = self.client.get('/api/competition-participations/')
        self.assertEqual(response.status_code, 200)

    def test_get_api_games_page(self):
        response = self.client.get('/api/games/')
        self.assertEqual(response.status_code, 200)

    def test_get_api_gamemodes_page(self):
        response = self.client.get('/api/game-modes/')
        self.assertEqual(response.status_code, 200)

    def test_get_api_maps_page(self):
        response = self.client.get('/api/maps/')
        self.assertEqual(response.status_code, 200)

    def test_get_api_mappools_page(self):
        response = self.client.get('/api/map-pools/')
        self.assertEqual(response.status_code, 200)

    def test_get_api_matches_page(self):
        response = self.client.get('/api/matches/')
        self.assertEqual(response.status_code, 200)

    def test_get_api_matchparticipations_page(self):
        response = self.client.get('/api/match-participations/')
        self.assertEqual(response.status_code, 200)

    def test_get_api_news_page(self):
        response = self.client.get('/api/news/')
        self.assertEqual(response.status_code, 200)

    def test_get_api_results_page(self):
        response = self.client.get('/api/results/')
        self.assertEqual(response.status_code, 200)

    def test_get_api_rounds_page(self):
        response = self.client.get('/api/rounds/')
        self.assertEqual(response.status_code, 200)

    def test_get_api_users_page(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
