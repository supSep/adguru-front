from enum import Enum

css_element = 'select'


class KijCategory(Enum):
    # def __hash__(self):
    #     return self.name.__hash__()
    #
    # def __lt__(self, other):
    #     if type(other) is self.__class__ and ( self.__class__ is KijCategory):
    #         assert isinstance(other, KijCategory)
    #         return self._name_ < other._name_
    #
    # def __gt__(self, other):
    #     if type(other) is self.__class__ and ( self.__class__ is KijCategory):
    #         assert isinstance(other, KijCategory)
    #         return self._name_ < other._name_

    art_collectibles = "CategoryId12"
    baby_items = "CategoryId253"
    bikes = "CategoryId644"
    books = "CategoryId109"
    business_industrial = "CategoryId145"
    cameras_camcorders = "CategoryId103"
    cds_dvds_bluray = "CategoryId104"
    clothing = "CategoryId274"
    computers = "CategoryId16"
    computer_accessories = "CategoryId128"
    electronics = "CategoryId15"
    furniture = "CategoryId235"
    garage_sales = "CategoryId638"
    health_special_needs = "CategoryId140"
    hobbies_crafts = "CategoryId139"
    home_appliances = "CategoryId107"
    home_indoor = "CategoryId717"
    home_outdoor = "CategoryId19"
    home_renovation_materials = "CategoryId727"
    iPods_mp3_headphones = "CategoryId767"
    jewelery_watches = "CategoryId133"
    musical_instruments = "CategoryId17"
    phones = "CategoryId134"
    sporting_goods_exercise = "CategoryId111"
    tickets = "CategoryId14"
    tools = "CategoryId110"
    toys_games = "CategoryId108"
    video_games_consoles = "CategoryId141"
    other = "CategoryId26"
    cars_trucks = "CategoryId174"
    classic_cars = "CategoryId122"
    auto_parts_tires = "CategoryId31"
    automotive_services = "CategoryId142"
    motorcycles = "CategoryId30"
    ATVs_snowmobiles = "CategoryId171"
    boats_watercraft = "CategoryId29"
    RVs_campers_trailers = "CategoryId172"