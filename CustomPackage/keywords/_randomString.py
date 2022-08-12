import random
import string


class _RandomStringKeywords:

    def get_random_string(self, length=5):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str
