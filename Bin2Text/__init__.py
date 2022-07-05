import string
import typing
from warnings import warn

from collections import Counter

asciiChars = "eainotrslduchmpgfbywkvzSACjMTPBLIDREGFNHKqWJxOVUZYXQ"
extAdditLatin = "éóäłèüàąáíśężåñúńßçýćÉčêùôšžòæîźâľÈŚťïûÜìŁÁœŻňÅďČŠĺŽ"
DEFAULT_ALPHABET = asciiChars + extAdditLatin + string.digits


class Bin2Text:
	"""Almost all BPE impls work properly only with text strings. So we transform the bytes into ASCII text strings. It is not always possible."""

	__slots__ = ("_byte2letter", "_letter2byte", "counter", "alphabet")

	def __init__(self, alphabet: str = None) -> None:
		if alphabet is None:
			alphabet = DEFAULT_ALPHABET

		self._byte2letter = None
		self._letter2byte = {}
		self.counter = Counter()
		self.alphabet = alphabet

	@property
	def byte2letter(self) -> bytes:
		self.ensureMappings()
		return self._byte2letter

	@property
	def letter2byte(self):
		self.ensureMappings()
		return self._letter2byte

	def ensureMappings(self) -> None:
		if self._byte2letter is None or not self._letter2byte:
			self.genMappings()

	def genMappings(self) -> None:
		locAlph = self.alphabet[: len(self.counter)]

		aTrans = bytearray()
		for lett, (byt, freq) in zip(locAlph, self.counter.most_common()):
			aTrans.append(byt)
			# self.byte2letter[byt] = lett
			self._letter2byte[lett] = byt

		self._byte2letter = bytes.maketrans(aTrans, locAlph.encode("ascii"))

	def fit(self, ss: typing.Iterable[bytes]) -> None:
		for el in ss:
			self.counter |= Counter(el)
		self._byte2letter = None

	def transform(self, el: bytes) -> str:
		return el.translate(self.byte2letter).decode("ascii")

	def reverse_transform(self, el: str) -> bytes:
		return bytes(self.letter2byte[c] for c in el)
