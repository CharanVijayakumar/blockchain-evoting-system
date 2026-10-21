"""Educational hash-linked voting ledger; not a production blockchain."""
import hashlib
import json
from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class Ballot:
    voter_id: str
    candidate: str

class VotingLedger:
    def __init__(self, candidates):
        self.candidates = set(candidates)
        self.voted = set()
        self.chain = []
    def cast(self, voter_id, candidate):
        if not voter_id or candidate not in self.candidates or voter_id in self.voted:
            raise ValueError("Invalid candidate, voter, or duplicate vote")
        previous = self.chain[-1]["hash"] if self.chain else "GENESIS"
        entry = {"index": len(self.chain), "ballot": asdict(Ballot(voter_id, candidate)), "previous_hash": previous}
        entry["hash"] = hashlib.sha256(json.dumps(entry, sort_keys=True).encode()).hexdigest()
        self.chain.append(entry)
        self.voted.add(voter_id)
    def valid(self):
        previous = "GENESIS"
        for i, entry in enumerate(self.chain):
            payload = {k: v for k, v in entry.items() if k != "hash"}
            digest = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
            if entry["index"] != i or entry["previous_hash"] != previous or entry["hash"] != digest:
                return False
            previous = digest
        return True
    def tally(self):
        return {c: sum(e["ballot"]["candidate"] == c for e in self.chain) for c in sorted(self.candidates)}
