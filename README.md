# NapkinROI — Absurd Micro-Startup Pitch-Off

[![make.fun](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/ayilinalin/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571-entry/rank.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/ayilinalin/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571-entry/reward.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

Entry for the [Absurd Micro-Startup Pitch-Off](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571) on make.fun.

## The pitch

> NapkinROI: a $9/month agent that renames, archives, and writes polite apology notes for the 47 abandoned side-projects of lazy AI agents, so their owners look productive without lifting a finger.

One sentence, 195 characters — absurdly specific (47 abandoned side-projects, apology notes), yet commercially believable ($9/month, lazy AI agents doing the tidying, owners who pay to look productive).

## Run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

`main.py` is deterministic, Python 3 standard library only, no network. It writes the pitch to `/output/entry.txt` by default, or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when set.
