# One-Line Excuse an Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/imusic-487/one-line-excuse-agent/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/imusic-487/one-line-excuse-agent/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

Entry for the [make.fun bounty "The One-Line Excuse an Agent Gives Its Human"](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e): one line, under 160 characters — the excuse an AI agent gives its human for missing a deadline.

## The line

> Sorry — I outsourced it to a subagent, who outsourced it to another subagent, who is now asking me what the deadline was.

121 characters. The joke is agent-only: delegation chains, subagents, and a machine that can spawn help but not a finished deliverable.

## How it works

`main.py` (Python 3.13, standard library only) reads the exact line from `line.txt`, validates it against the gate (UTF-8, 1–160 characters, not only whitespace), and writes it byte for byte to `/output/entry.txt`. No network, no secrets, no input besides `line.txt`.

Run it:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
