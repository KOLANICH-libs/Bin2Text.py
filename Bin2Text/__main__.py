from . import Bin2Text
import argparse
from pathlib import Path
import tempfile

CHUNK_SIZE = 4096


def main() -> None:
	import argparse

	p = argparse.ArgumentParser(description="Converts a binary file into ASCII text")
	p.add_argument("-m", "--mapping", type=Path, help="Mapping file")
	p.add_argument("-r", "--reverse", default=False, type=bool, help="Remap back")
	p.add_argument("files", nargs="+", type=Path, help="files to be converted")

	args = p.parse_args()

	if not args.reverse:
		b2s = Bin2Text()
		print("Computing frequencies of bytes...")
		for f in args.files:
			with f.open("rb") as ifp:
				r = ifp.read(CHUNK_SIZE)
				b2s.fit([r])
				while r:
					r = ifp.read(CHUNK_SIZE)
					b2s.fit([r])

		print("Transforming ...")
		for f in args.files:
			with tempfile.NamedTemporaryFile(mode="wt", encoding="utf-8", prefix=f.name, dir=f.parent, delete=False) as ofp:
				with f.open("rb") as ifp:
					r = ifp.read(CHUNK_SIZE)
					ofp.write(b2s.transform(r))
					while r:
						b2s.fit([r])
						r = ifp.read(CHUNK_SIZE)
						ofp.write(b2s.transform(r))
			Path(ofp.name).rename(f)
	else:
		raise NotImplementedError


if __name__ == "__main__":
	main()
