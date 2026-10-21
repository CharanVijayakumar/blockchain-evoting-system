# Blockchain E-Voting System — Reconstruction

This repository is a fresh reconstruction inspired by an earlier academic group project, **not recovered original source code**.

## Scope
A local educational prototype demonstrating ballot registration, vote validation, one-vote-per-voter rules, and a hash-linked audit trail. It is not a secure production election system and does not claim to implement a decentralized blockchain network.

## Project structure
- `src/` — Python voting model
- `tests/` — Python unit tests

## Run
```bash
python -m unittest discover -s tests -v
python -m src.demo
```

## Limitations
This is an in-memory demonstration with no real authentication, cryptographic ballot secrecy, or decentralized consensus. Never use it for real elections.
