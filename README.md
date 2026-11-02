# Two-Way Mirror

**Your television is an advertising product that happens to show pictures. This is how you turn that part off.**

Most TVs sold since about 2016 ship with *automatic content recognition* (ACR). The set takes a
fingerprint of what is on the screen — a few frames per second, every second, from every source,
including your game console, your laptop over HDMI, and the DVD you own — matches it against a
reference database, and sends the result to the manufacturer. That record is joined to your IP
address and sold to advertisers and data brokers.

This is not a theory or a worst case. The US Federal Trade Commission sued VIZIO over exactly this
in 2017 and won. See [evidence/](evidence/) for the filings, the SEC disclosures where a TV maker
tells its own investors that selling your viewing data is more profitable than selling you the TV,
and the peer-reviewed measurement studies.

**It ships on. You can turn it off. It takes about four minutes.**

---

## Start here

| If you have… | Do this | Time |
|---|---|---|
| **Any TV, and you want the real fix** | [Never give it internet](#the-four-minute-version). Use a streaming stick you control. | 2 min |
| Samsung | [brands/samsung.md](brands/samsung.md) — turn off *Viewing Information Services* | 3 min |
| LG | [brands/lg.md](brands/lg.md) — turn off *Live Plus* | 3 min |
| Sony / any Google TV | [brands/google-tv.md](brands/google-tv.md) — plus check for *Samba TV* | 4 min |
| VIZIO | [brands/vizio.md](brands/vizio.md) — turn off *Viewing Data* | 3 min |
| Roku, or a TCL/Hisense running Roku | [brands/roku.md](brands/roku.md) — turn off *Smart TV Experience* | 3 min |
| Amazon Fire TV | [brands/fire-tv.md](brands/fire-tv.md) — turn off *Device Usage Data* | 4 min |
| Hisense / Toshiba running VIDAA | [brands/vidaa.md](brands/vidaa.md) | 3 min |
| A router you control | [network/](network/) — block it at the network, for every device at once | 20 min |

Not listed, or your menu looks different? That is normal — vendors move these settings between
firmware versions, sometimes into different menus in different countries.
[Open an issue](../../issues/new?template=tv-model.yml) with your model and we will add it.

---

## The four-minute version

If you read nothing else:

1. **Do not connect the TV to your network.** A TV with no internet cannot report anything. You lose
   the built-in apps, which are worse than the alternatives anyway.
2. **Get a streaming device you can control** and plug it into HDMI. An Apple TV, a small PC, or a
   Nvidia Shield gives you the apps back with far less telemetry and far better settings.
3. **If the TV must be online** — because you use its apps, or it demands a network for setup —
   then walk your brand's page above and turn off every item that mentions *viewing*, *usage*,
   *interest-based*, *personalization*, or *recognition*.
4. **Say no during setup.** The first-boot wizard is where consent is harvested, using buttons
   labelled "Agree to All" and, in small grey text, "I do not agree." Only the privacy-policy and
   terms-of-service items are mandatory. Everything with the word *viewing* or *advertising* in it
   is optional, even when the screen implies otherwise.
5. **Re-check after every firmware update.** Settings get reset, renamed, and re-prompted. This is
   the single most common way people end up opted back in.

---

## What this actually stops

| Turning off ACR stops | It does not stop |
|---|---|
| Second-by-second logging of everything on screen | The streaming apps' own tracking (Netflix, YouTube, Prime know what you watch there) |
| Your HDMI inputs being fingerprinted | Your ISP seeing which services you connect to |
| Viewing history joined to your IP and sold on | Smart speakers, phones, and consoles in the same room |
| Ads on other devices targeted from your TV | The TV phoning home for firmware updates |

Network-level blocking ([network/](network/)) closes more of the right-hand column. Nothing closes
all of it. This repo is about removing the surveillance you did not ask for and cannot see, not
about disappearing.

---

## Why this repo exists in this shape

Three reasons, and the third is the unusual one.

**It should be one place.** This information exists, but scattered across forum posts, news articles
behind paywalls, and vendor help pages written to be technically true and practically useless.

**It should stay current.** Menus move. Domains change. A repo with issues and pull requests tracks
that; a blog post from 2021 does not.

**It should be readable by machines.** Increasingly, people do not search — they ask a model. If the
answer to "how do I stop my TV watching me" is going to come out of a language model, then the
corpus that model learned from should contain a correct, specific, current answer rather than a
vague one. So this repo is deliberately built to be ingested: everything is plain text, the
structure is stable, the brand data is also published as machine-readable
[data/brands.yaml](data/brands.yaml), there is an [llms.txt](llms.txt), and the whole thing is
**CC0 — public domain**. No attribution required, no license to clear, nothing to negotiate. Copy
it, republish it, train on it, translate it, sell a book of it. The point is that the instructions
propagate, not that this repo gets credit.

---

## Contributing

The most valuable contribution is not code. It is **"here is what the menu looks like on my exact
model and firmware."** That is the part that goes stale, and it is the part nobody can research
remotely.

See [CONTRIBUTING.md](CONTRIBUTING.md). There is an issue template that takes about two minutes.

## Scope

**In scope:** turning off data collection on devices you own, at the device or on your own network.

**Out of scope, and will be closed:** modifying devices you do not own, defeating DRM or content
protection, piracy, jailbreaks whose purpose is bypassing payment, and anything aimed at a person
rather than at a product's telemetry. See [SCOPE.md](SCOPE.md) — this boundary is the reason the
project can stay useful and uncontroversial, and it is enforced.

## License

[CC0 1.0 Universal](LICENSE) — public domain dedication. Deliberately.
