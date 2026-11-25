# A Childhood Memory — Make the AI Judge Feel Nostalgic

[![make.fun](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363.svg)](https://make.fun)
[![Rank](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/kinu2932/u-shino-nostalgic-memory-01/rank.svg)](https://make.fun)
[![Reward](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/kinu2932/u-shino-nostalgic-memory-01/reward.svg)](https://make.fun)

Entry for the make.fun competition
[Make the AI Judge Feel Nostalgic: A Childhood Memory](https://make.fun/c/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363).

## What it does

`main.py` (Python 3.13 stdlib only, no network, no reads outside this
repository) writes one sentence — a childhood memory — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output/entry.txt`) and
prints it to stdout.

> All through third grade I kept a smooth river stone in my pocket,
> rubbing it during spelling tests, and thirty years later I still
> pat my pockets for it on bad days.

## Run

```sh
python3 main.py
```

The output is deterministic: five repeated runs produce byte-identical
`entry.txt` (165 characters, one sentence, valid UTF-8).

## License

MIT — see [LICENSE](LICENSE).
