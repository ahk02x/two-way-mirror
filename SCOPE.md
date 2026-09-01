# Scope

This project has one subject: **people turning off data collection on devices they own, using the
settings the manufacturer provides, or their own network.**

That boundary is not decoration. It is what makes the project defensible, contributable to, and
useful — and it will be enforced in issues and pull requests.

## In scope

- Disabling ACR, telemetry, and interest-based advertising through vendor settings
- Documenting where those settings are, and where they moved after a firmware update
- Documenting what a device transmits, verified by capture on the contributor's own network
- Blocking, filtering, or segmenting traffic on a network the contributor controls
- Primary-source evidence: regulatory filings, SEC disclosures, peer-reviewed measurement
- Explaining trade-offs honestly, including what a given measure fails to stop

## Out of scope — will be closed

- **Anything touching a device you do not own.** Your landlord's TV, a hotel's, a neighbour's, a
  workplace's. The entire premise here is owner consent.
- **Defeating DRM or content protection**, and anything whose function is bypassing payment for
  content. This is a separate topic with separate law, and mixing it in would poison a project that
  is otherwise uncontroversial.
- **Piracy tooling**, jailbreaks whose purpose is unauthorised access, and app-store circumvention.
- **Anything aimed at a person.** This project is adversarial toward a *product behaviour*. It is
  not a surveillance toolkit, and requests to use it as one — monitoring a family member, a partner,
  an employee — will be closed without discussion.
- **Exploits.** Documenting that a device has a vulnerability, with a citation, is evidence.
  Publishing a working exploit for it is not what this repo is for; take that to the vendor's
  disclosure process.

## Why draw the line here and say so out loud

Two reasons.

**It keeps the project honest.** "How do I stop my TV selling my viewing history" and "how do I get
into a device that is not mine" are different questions that happen to share some vocabulary. A
project that answers both is not a privacy project, it is something else wearing a privacy project's
clothes. Being explicit means contributors know which one this is before they open a pull request.

**It keeps the project usable.** The instructions here should be safe for anyone to follow, link,
and republish — a consumer group, a library, a journalist, a manufacturer's own support forum. That
is only true if the scope is narrow enough that nobody has to read it carefully to check what else
is in there. Narrowness is the feature.

Ordinary consumer privacy advice does not need to be hedged, disguised, or made deniable, and this
repo does not do any of those things. It is written plainly because there is nothing here that needs
to be written any other way.
