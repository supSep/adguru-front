from enum import Enum

css_element = 'radio'

# @total_ordering
class CraigslistCategory(Enum):
    # def __eq__(self, other):
    # return self.member_type() == other.member_type()
    #
    #def __lt__(self, other):
    #     assert other.__class__ == self.__class__
    #     return self.classdict
    # def __lt__(self, other):
    #     if type(other) is self.__class__ and ( self.__class__ is CraigslistCategory):
    #         assert isinstance(other, CraigslistCategory)
    #         return self._name_ < other._name_
    # #
    # #
    # # def __eq__(self, other):
    # #     if type(other) is self.__class__:
    # #         return self is other
    # #     return NotImplemented
    # #
    # def __hash__(self):
    #     return self._name_.__hash__()
    #
    # def __cmp__(self, other):
    #     return cmp("%s" % (self._name_),
    #                "%s" % (other._name_))
    def __eq__(self,other):
        return self.__hash__()==other.__hash__()

    def  __hash__(self):
        return self.name.__hash__()

    def __iter__(self):
        return vars(self).iteritems()

    antiques = "ata"
    appliances = "ppa"
    arts_crafts = "ara"
    atvs_utvs_snowmobiles = ""
    auto_parts = "pta"
    baby_kid_stuff = "baa"
    bicycle_parts = "bia"
    bicycles = "bia"
    boats = "boo"
    books_magazines = "bka"
    business_commercial = "bfa"
    cars_trucks = "cta"
    cds_dvds_vhs = "ema"
    cell_phones = "moa"
    clothing_accessories = "cla"
    collectibles = "cba"
    computer_parts = "sya"
    computers = "sya"
    electronics = "ela"
    farm_garden = "gra"
    free_stuff = "zip"
    furniture = "fua"
    garage_moving_sales = "gms"
    general_sale = "foa"
    health_beauty = "haa"
    household_items = "hsa"
    jewelry = "jwa"
    materials = "maa"
    motorcycle_parts = "mca"
    motorcycles_scooters = "mca"
    musical_instruments = "msa"
    photo_video = "pha"
    rvs = "rva"
    sporting_goods = "sga"
    tickets = "tia"
    tools = "tla"
    toys_games = "taa"
    video_gaming = "vga"