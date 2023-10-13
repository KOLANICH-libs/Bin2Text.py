Bin2Text.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
==========
~~[wheel (GitLab)](https://gitlab.com/KOLANICH-libs/Bin2Text.py/-/jobs/artifacts/master/raw/dist/Bin2Text-0.CI-py3-none-any.whl?job=build)~~
~~[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-libs/Bin2Text.py/workflows/CI/master/Bin2Text-0.CI-py3-none-any.whl)~~
~~[![GitHub Actions](https://github.com/KOLANICH-libs/Bin2Text.py/workflows/CI/badge.svg)](https://github.com/KOLANICH-libs/Bin2Text.py/actions/)~~
![N∅ dependencies](https://shields.io/badge/-N∅_Ъ_deps!-0F0)
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-libs/Bin2Text.py.svg)](https://libraries.io/github/KOLANICH-libs/Bin2Text.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

**We have moved to https://codeberg.org/KOLANICH-libs/Bin2Text.py, grab new versions there.**

Under the disguise of "better security" Micro$oft-owned GitHub has [discriminated users of 1FA passwords](https://github.blog/2023-03-09-raising-the-bar-for-software-security-github-2fa-begins-march-13/) while having commercial interest in success and wide adoption of [FIDO 1FA specifications](https://fidoalliance.org/specifications/download/) and [Windows Hello implementation](https://support.microsoft.com/en-us/windows/passkeys-in-windows-301c8944-5ea2-452b-9886-97e4d2ef4422) which [it promotes as a replacement for passwords](https://github.blog/2023-07-12-introducing-passwordless-authentication-on-github-com/). It will result in dire consequencies and is competely inacceptable, [read why](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

If you don't want to participate in harming yourself, it is recommended to follow the lead and migrate somewhere away of GitHub and Micro$oft. Here is [the list of alternatives and rationales to do it](https://github.com/orgs/community/discussions/49869). If they delete the discussion, there are certain well-known places where you can get a copy of it. [Read why you should also leave GitHub](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

---

An extremily simple and restricted tool/lib converting binary data into text that can be processed with unsuperwised character-level natural language processing tools/libs.

## Rationale

NLP tools don't work on raw bytes. At least don't work correctly.

The tools it'd be nice to be able to use with binary data:
* [`sentencepiece`](https://github.com/google/sentencepiece)
* [`python-bpe`](https://github.com/soaxelbrooke/python-bpe)
* [🤗`tokenizers`](https://github.com/huggingface/tokenizers)
* [`YouTokenToMe`(`yttm`)](https://github.com/VKCOM/YouTokenToMe)
