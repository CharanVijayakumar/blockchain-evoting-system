import unittest
from src.voting import VotingLedger

class TestLedger(unittest.TestCase):
    def test_vote(self):
        l = VotingLedger(["A", "B"])
        l.cast("v1", "A")
        self.assertEqual(l.tally()["A"], 1)
        self.assertTrue(l.valid())
    def test_duplicate(self):
        l = VotingLedger(["A"])
        l.cast("v1", "A")
        with self.assertRaises(ValueError):
            l.cast("v1", "A")
    def test_tamper(self):
        l = VotingLedger(["A", "B"])
        l.cast("v1", "A")
        l.chain[0]["ballot"]["candidate"] = "B"
        self.assertFalse(l.valid())

if __name__ == "__main__":
    unittest.main()
