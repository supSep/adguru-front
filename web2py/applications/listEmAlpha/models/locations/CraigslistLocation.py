# # cl uses radio input
## City = (css element - value)

from enum import Enum

css_element = 'radio'


class CraigslistLocation(Enum):
# Enum    def __lt__(self, other):
#         if type(other) is self.__class__ and ( self.__class__ is CraigslistLocation):
#             return self._value_ < other._value_
#
#
#     def __eq__(self, other):
#         if type(other) is self.__class__:
#             return self is other
#         return NotImplemented


    vancouver = 1
    northshore = 2
    burnaby_newwest = 3
    delta_surrey_langley = 4
    tricities_pitt_maple = 5
    richmond = 6
