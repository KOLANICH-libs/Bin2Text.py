import re
import secrets
import string
from collections import Counter
import random
import sys
from pathlib import Path

thisDir = Path(__file__).parent

if __name__ == "__main__":
	t = (thisDir / "original.txt").read_text()

	x = re.compile("[^a-zA-Z]")

	t = x.subn("", t)[0]

	# t[:4096]
	ochr = "".join([el[0] for el in Counter(t).most_common()])
	rem = [chr(el) for el in range(ord("a"), ord("a") + 26)] + [chr(el) for el in range(ord("A"), ord("A") + len(ochr) - 26)]
	rem = "".join(rem)
	(thisDir / "test.bin").write_bytes(t.translate(str.maketrans(ochr, rem)).encode("ascii")[:4096])
