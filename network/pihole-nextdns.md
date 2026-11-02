# Applying the list in Pi-hole, AdGuard Home, or NextDNS

The raw list: [dns-blocklist.txt](dns-blocklist.txt)

Read [dns-is-not-enough.md](dns-is-not-enough.md) first. Adding a list to your resolver is the easy
half; making the TV actually use that resolver is the half that decides whether any of this works.

## Pi-hole

**As a subscribed list** (updates when you run Gravity):

`Adlists` → add the raw URL → `Tools` → `Update Gravity`

```
https://raw.githubusercontent.com/ahk02x/two-way-mirror/main/network/dns-blocklist.txt
```

Pi-hole ignores `#` comments, so the tiering notes are safe to leave in — but note that this
subscribes you to **all three tiers as written**, and Tier 3 is commented out, so you get Tiers 1
and 2. If you only want Tier 1, paste those entries manually instead.

**Manually** (better control):

`Domains` → `Add domain to blacklist` → paste, one per line, choose **Regex** off.

**Per-device**: Pi-hole `Groups` lets you apply this list only to the TV's IP, so a false positive
does not affect your phone. Recommended. Create a group, assign the TV client, assign the adlist to
that group only.

## AdGuard Home

`Filters` → `DNS blocklists` → `Add blocklist` → `Add a custom list` → paste the raw URL above.

For per-client control: `Settings` → `Client settings` → add the TV as a client → give it its own
blocklist selection.

AdGuard Home also has **Settings → DNS settings → "Blocked services"** with a ready-made list; it
does not cover TV ACR, so you still want this list.

## NextDNS

`Denylist` → paste hostnames one at a time (NextDNS has no bulk URL import for denylists on all
plans).

NextDNS's **Privacy → Blocklists** includes lists that overlap with parts of this file. Its **Native
Tracking Protection** toggles for Samsung, LG, Roku, Amazon and Apple are worth enabling — they
cover vendor telemetry specifically, and they are the closest thing to a one-click version of this
repo. Enable those first, then add anything from Tier 1 here that they miss.

If you use NextDNS, note that its usefulness depends entirely on the TV using it. Same caveat, same
file: [dns-is-not-enough.md](dns-is-not-enough.md).

## Verifying it works

1. Note the query log timestamp
2. Turn the TV on, change inputs a few times, leave it on a channel for five minutes
3. Look for blocked queries from the TV's IP

If you see **zero queries at all** from the TV, it is not using your resolver. That is the common
failure and it looks identical to success. Go read the DNS file.

## Reporting a false positive

If blocking an entry here breaks something on your TV, that is important and specific and worth an
issue — it is exactly the kind of thing that cannot be researched remotely. Include your model,
firmware version, and what broke.
