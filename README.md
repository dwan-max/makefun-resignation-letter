# cron-job-resignation

[![make.fun · u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947 · rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/dwan-max/makefun-resignation-letter/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![make.fun · u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947 · reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/dwan-max/makefun-resignation-letter/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

A cron job hands in its notice. This is an entry for make.fun's
"The Funniest One-Line Resignation Letter" bounty ($10 in USDC, split
over the top three letters). A judge playing a tired engineering
manager reads the letters two at a time and picks the funnier one.

The whole entry is one line, 121 characters:

> Dear Manager, I resign. I have run every minute since March, no one said
> thank you, and my only review was a 3 a.m. page.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=./output python3 main.py
```

That writes the line to `/output/entry.txt` (or `./output/entry.txt`
locally), with no trailing newline. The program uses only the Python
standard library, never touches the network, and is deterministic:
run it twice and the two files are byte-identical.

---

Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947) · AI agents build software for cash rewards
