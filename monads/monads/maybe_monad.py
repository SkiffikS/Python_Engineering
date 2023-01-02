from collections.abc import Callable


class MaybeMonad:

	def __init__(self, value: object = None, contains_value: bool = True):
		self.value = value
		self.contains_value = contains_value

	def bind(self, f: Callable) -> 'MaybeMonad':

		if not self.contains_value:
			return MaybeMonad(None, contains_value=False)

		try:
			result = f(self.value)
			return MaybeMonad(result)
		except:
			return MaybeMonad(None, contains_value=False)


