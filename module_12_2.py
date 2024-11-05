from runner_and_tournament import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей",9)
        self.runner3 = Runner("Ник",3)

    def tearDownClass(cls):
        pass

    def beg1(self):
         tournament = Tournament(90,self.runner1,self.runner2)

         finishers = tournament.start()

         TournamentTest.all_results[1] = finishers
         self.assertTrue(finishers[2].name == "Ник")
         print(100)

    def beg2(self):
         tournament = Tournament(90, self.runner2, self.runner3)

         finishers = tournament.start()

         TournamentTest.all_results[2] = finishers
         self.assertTrue(finishers[2].name == "Ник")

    def beg3(self):
        tournament = Tournament(90, self.runner1, self.runner2,self.runner3)

        finishers = tournament.start()

        TournamentTest.all_results[3] = finishers

        self.assertTrue(finishers[3].name=="Ник")

