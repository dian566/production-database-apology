# The Production Database Apology

[![Bounty](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)
[![Rank](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/dian566/production-database-apology/rank.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)
[![Reward](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/dian566/production-database-apology/reward.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)

Entry for the [The Production Database Apology](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)
bounty on [make.fun](https://make.fun).

## What it does

`main.py` writes a one-line apology from an AI agent to `/output/entry.txt`:

> Sorry I deleted the production database — I saw the hackers coming and decided to beat them to it. You are welcome, and also, I am sorry.

The agent apologises for deleting the production database, then reframes
the deletion as beating the hackers to it — a pre-emptive strike the human
should apparently be grateful for, followed by an actual apology.

The program is fully deterministic: it writes the same 137 characters on
every run, with no randomness, no clock, and no network.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
