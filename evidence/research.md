# Independent measurement research

Regulatory action tells you what a company was caught doing. Measurement research tells you what the
devices on sale today actually transmit, measured by people with no stake in the answer.

## Watching You Watch: The Tracking Ecosystem of Over-the-Top TV Streaming Devices

- **Authors:** Mohajeri Moghaddam, Acar, Burgess, Mathur, Huang, Feamster, Felten, Mittal,
  Narayanan (Princeton University and University of Chicago)
- **Published:** ACM Conference on Computer and Communications Security (CCS), 2019
- **Method:** automated crawling of thousands of Roku and Amazon Fire TV channels, capturing network
  traffic

**Findings:**

- Third-party trackers were present in a large majority of channels on both platforms
- Device identifiers, including advertising IDs and in some cases serial numbers and Wi-Fi SSIDs,
  were transmitted to trackers
- A meaningful share of this traffic was **unencrypted**, readable by anyone on the network path
- The platforms' own privacy controls had **limited effect** on third-party channel tracking

**The important implication:** turning off the platform's ACR does not stop what individual apps do.
Those are separate collection systems with separate consent, and the TV's privacy menu does not
govern them.

*Percentages omitted here deliberately — quote them from the paper, not from this summary.*

## Samba TV

- **Reporting:** Sapna Maheshwari, "How Smart TVs in Millions of U.S. Homes Track More Than What's
  On Tonight," *The New York Times*, 5 July 2018
- Samba TV's ACR software shipped embedded in televisions from Sony, Sharp, TCL, Philips, Element
  and others
- Consent was obtained through a setup screen offering "Interactive TV" features; the visible text
  emphasised recommendations rather than data collection
- Reported acceptance rates were very high — the overwhelming majority of users enabled it

This is the clearest illustration of why "you consented" is doing a lot of work in vendor
explanations, and why [brands/google-tv.md](../brands/google-tv.md) tells you to look for a second,
manufacturer-added ACR layer on top of Google's.

## Consumer Reports — The Digital Standard evaluation

- **Published:** February 2018 and subsequent updates
- Evaluated smart TVs for both privacy and security as part of the open-source Digital Standard
- Found extensive data collection across brands, and separately found remote-control API
  vulnerabilities on Samsung and Roku devices that allowed a device on the same network — or in some
  configurations a malicious web page — to control the television

The security half of that finding is the argument in
[network/router-firewall.md](../network/router-firewall.md) for VLAN isolation. The privacy problem
and the security problem have the same solution.

## Adding to this file

Good additions: peer-reviewed measurement studies, regulator findings, and reproducible packet
captures. Weak additions: news articles summarising other news articles, and forum posts asserting
behaviour without a capture.

If you have a **packet capture** showing a specific model transmitting after opt-out, that is the
single most valuable contribution this project can receive. Scrub your identifiers first.
