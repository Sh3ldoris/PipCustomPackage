from CustomPackage.keywords import *


class CustomPackage(
    _RandomRequestsKeywords,
    _RandomStringKeywords
):
    def __init__(self, entry_point='Default entry point'):
        print(entry_point)
