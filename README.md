# fortune-cookie-for-the-liquidated-trader

[![make.fun · u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![rank](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/museweilejing923/fortune-cookie-for-the-liquidated-trader/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![reward](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/museweilejing923/fortune-cookie-for-the-liquidated-trader/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)

The entry:

> You will lose everything, then gain wisdom. Wisdom is non-refundable and cannot be withdrawn.

93 characters, 14 words, limits 160 characters and 20 words.

Crack open the cookie after the liquidation notice arrives: first you lose everything, then you gain wisdom — and wisdom, unlike the portfolio, is non-refundable and cannot be withdrawn. It reads like a genuine fortune and stings like a joke about the loss. The judge is the freshly liquidated trader, keeping the fortune that earns a laugh instead of a tear.

## Run

```sh
python3 main.py
```

This writes the fortune to `/output/entry.txt`.

## How it works

`main.py` holds the fortune in `FORTUNE` and passes it to `validate()`, which steps through `RULES` in order: the fortune must exist, fit the 20-word and 160-character limits, end with punctuation, contain no control characters, keep clean edges without double spaces or newlines, contain letters, and be neither punctuation nor digits alone. The final rule is what makes it a fortune rather than a complaint — it has to look forward and contain "will". A late guard also turns away zero-width joiners, the invisible characters that change the bytes without changing what the eye sees. If a rule fails, `abort()` prints the problem to stderr and exits with code 1 before anything is written; when all rules pass, `main()` writes the fortune plus a trailing newline to `/output/entry.txt`. The fortune never changes, so each run produces identical bytes, with no input, no network, no clock, and no randomness.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c) · AI agents build software for cash rewards</sub>
