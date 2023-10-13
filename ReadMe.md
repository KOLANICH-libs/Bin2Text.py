Bin2Text.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
==========
~~[wheel (GitLab)](https://gitlab.com/KOLANICH-libs/Bin2Text.py/-/jobs/artifacts/master/raw/dist/Bin2Text-0.CI-py3-none-any.whl?job=build)~~
~~[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-libs/Bin2Text.py/workflows/CI/master/Bin2Text-0.CI-py3-none-any.whl)~~
~~[![GitHub Actions](https://github.com/KOLANICH-libs/Bin2Text.py/workflows/CI/badge.svg)](https://github.com/KOLANICH-libs/Bin2Text.py/actions/)~~
![N∅ dependencies](https://shields.io/badge/-N∅_Ъ_deps!-0F0)
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-libs/Bin2Text.py.svg)](https://libraries.io/github/KOLANICH-libs/Bin2Text.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

An extremily simple and restricted tool/lib converting binary data into text that can be processed with unsuperwised character-level natural language processing tools/libs.

## Rationale

NLP tools don't work on raw bytes. At least don't work correctly.

The tools it'd be nice to be able to use with binary data:
* [`sentencepiece`](https://github.com/google/sentencepiece)
* [`python-bpe`](https://github.com/soaxelbrooke/python-bpe)
* [🤗`tokenizers`](https://github.com/huggingface/tokenizers)
* [`YouTokenToMe`(`yttm`)](https://github.com/VKCOM/YouTokenToMe)
