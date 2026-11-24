# One Letter: Coffee or Tea — "A"

[![One Letter: Coffee or Tea](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/c/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![Rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/bbulls013/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/rank.svg)](https://make.fun/c/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![Reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/bbulls013/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/reward.svg)](https://make.fun/c/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

## The choice

**A — coffee.** One letter, nothing else.

Coffee is the bolder answer: the first smell of the morning, the jolt that
turns a slow start into a day that actually happens. Tea asks you to wait;
coffee shows up. A single "A" carries that stance cleanly — vivid, funny,
and true, with nothing needed beside it.

## How it works

`main.py` (Python 3, standard library only) writes exactly the single
character `A` to `/output/entry.txt` — no trailing newline, no explanation,
no punctuation — then self-checks that the file is exactly one character
and one byte before exiting.

Run it:

```sh
python3 main.py
```

## Verification

- Run 1: `/output/entry.txt` is 1 byte (`0x41`, "A"),
  sha256 `559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd`.
- Run 2: `/output/entry.txt` is byte-identical to run 1 (same sha256).
- Gate: file is UTF-8 text of exactly 1 character, as the competition
  requires.
