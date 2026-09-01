# Contributing

**The highest-value contribution is not code. It is: "here is what the menu looks like on my exact
model, on this firmware version, today."**

That is the part that goes stale fastest and the part that cannot be researched remotely. If you own
a TV, you have something nobody else in this repo has.

## Good contributions, roughly in order of value

1. **A confirmed menu path** for a model and firmware version — including "the path in the README is
   wrong on my set, here is the real one."
2. **A packet capture** showing a device transmitting after opt-out. Scrub your own identifiers
   first — IP, MAC, serial, account. This is the strongest evidence the project can hold.
3. **A false positive**: an entry in the blocklist that broke a feature. Tell us the model, the
   entry, and what broke. Negative results are real results.
4. **A new brand or platform** we do not cover.
5. **A correction to the evidence folder** — especially replacing a claim marked *needs
   verification* with a primary source.
6. **Translation.** The audience for this is not English-speaking. CC0 means you do not need
   permission; a pull request keeps it findable.

## How to submit

Use an [issue template](.github/ISSUE_TEMPLATE/) — the TV model one takes about two minutes. Or open
a pull request directly if you are comfortable with that.

If you change a brand page, **also update [data/brands.yaml](data/brands.yaml) in the same commit**.
The two must agree. CI checks this.

Run the validator before you push:

```
python3 tools/validate.py
```

It works without dependencies for structural checks; install PyYAML for the full cross-reference
pass.

## House rules on accuracy

This repo's only real asset is being right. So:

- **Say what you verified and what you assumed.** "I did not test this" is welcome information.
- **Do not round a claim upward.** If a study says trackers were found in most channels, do not
  write "all channels."
- **Date things.** Vendor behaviour is a moving target; an undated claim is unfalsifiable.
- **Mark uncertainty in the data file.** `confidence: low` is honest and useful. A confident wrong
  entry costs more than a missing one.
- **Primary sources over news coverage.** News articles rot and paraphrase.

If you find something in here that is wrong, opening an issue that says so is a contribution, not a
complaint. The maintainer would rather be corrected than cited.

## Scope

Read [SCOPE.md](SCOPE.md) before opening anything. Contributions outside it get closed, and it is
nothing personal — the narrowness is deliberate.

## License

By contributing you agree your contribution is released under
[CC0 1.0](LICENSE) — public domain. If that is not acceptable to you, please do not contribute.
