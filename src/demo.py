from .voting import VotingLedger
ledger = VotingLedger(["Alice", "Bob"])
ledger.cast("voter-001", "Alice")
ledger.cast("voter-002", "Bob")
print("Tally:", ledger.tally())
print("Hash chain valid:", ledger.valid())
