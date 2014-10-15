from enum import Enum
from applications.listEmAlpha.models.category.KijCategory import KijCategory
from applications.listEmAlpha.models.category.CraigslistCategory import CraigslistCategory


class PostCategory(Enum):
    antique_art_collectibles = dict(
        CraigslistCategory.antiques,
        KijCategory.art_collectibles)

    appliances = dict(
        CraigslistCategory.appliances,
        KijCategory.home_appliances)

    baby_stuff = dict(
        CraigslistCategory.baby_kid_stuff,
        KijCategory.baby_items)

    books = dict(
        CraigslistCategory.books_magazines,
        KijCategory.books)

    cd_dvd_bluray = dict(
        CraigslistCategory.cds_dvds_vhs,
        KijCategory.cds_dvds_bluray )

    cell_phone = dict(
        CraigslistCategory.cell_phones,
        KijCategory.electronics)

    computers = dict(
        CraigslistCategory.computers,
        KijCategory.computers)

    electronics = dict(
        CraigslistCategory.electronics,
        KijCategory.electronics)

    free = dict(
        CraigslistCategory.free_stuff,
        KijCategory.other)

    furniture = dict(
        CraigslistCategory.furniture,
        KijCategory.furniture)

    garage_yard_sale = dict(
        CraigslistCategory,
        KijCategory)

    home_farm_garden = dict(
        CraigslistCategory.farm_garden,
        KijCategory.home_outdoor)

    jewelry = dict(
        CraigslistCategory.jewelry,
        KijCategory.jewelery_watches)

    motorvehicles_car_truck_rv = dict(
        CraigslistCategory.cars_trucks,
        KijCategory.cars_trucks)

    musical_instruments = dict(
        CraigslistCategory.musical_instruments,
        KijCategory.musical_instruments)

    office_business = dict(
        CraigslistCategory.business_commercial,
        KijCategory.business_industrial)

    pets = dict(
        CraigslistCategory.general_sale,
        KijCategory.other)

    shoes_clothing_watches = dict(
        CraigslistCategory.clothing_accessories,
        KijCategory.clothing)

    sporting_goods = dict(
        CraigslistCategory.sporting_goods,
        KijCategory.sporting_goods_exercise)

    tickets = dict(
        CraigslistCategory.tickets,
        KijCategory.tickets)

    toys_games = dict(
        CraigslistCategory.toys_games,
        KijCategory.toys_games)

    video_games = dict(
        CraigslistCategory.video_gaming,
        KijCategory.video_games_consoles)




#antique_art_collectibles
#appliances
#baby_stuff
#books
#cd_dvd_bluray
#cell_phone
##computers
#electronics
#free
#furniture
#garage_yard_sale
#home_farm_garden
#jewelry
#motorvehicles_car_truck_rv
#musical_instruments
##office_business
#pets
#shoes_clothing_watches
#sporting_goods
#tickets
#toys_games
#video_games