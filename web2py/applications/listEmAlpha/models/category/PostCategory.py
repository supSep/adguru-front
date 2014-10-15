from enum import Enum
from applications.listEmAlpha.models.category.KijCategory import KijCategory
from applications.listEmAlpha.models.category.CraigslistCategory import CraigslistCategory


class PostCategory():
    antique_art_collectibles = (
        CraigslistCategory.antiques,
        KijCategory.art_collectibles)

    appliances = (
        CraigslistCategory.appliances,
        KijCategory.home_appliances)

    baby_stuff = (
        CraigslistCategory.baby_kid_stuff,
        KijCategory.baby_items)

    books = (
        CraigslistCategory.books_magazines,
        KijCategory.books)

    cd_dvd_bluray = (
        CraigslistCategory.cds_dvds_vhs,
        KijCategory.cds_dvds_bluray )

    cell_phone = (
        CraigslistCategory.cell_phones,
        KijCategory.electronics)

    computers = (
        CraigslistCategory.computers,
        KijCategory.computers)

    electronics = (
        CraigslistCategory.electronics,
        KijCategory.electronics)

    free = (
        CraigslistCategory.free_stuff,
        KijCategory.other)

    furniture = (
        CraigslistCategory.furniture,
        KijCategory.furniture)

    garage_yard_sale = (
        CraigslistCategory,
        KijCategory)

    home_farm_garden = (
        CraigslistCategory.farm_garden,
        KijCategory.home_outdoor)

    jewelry = (
        CraigslistCategory.jewelry,
        KijCategory.jewelery_watches)

    motorvehicles_car_truck_rv = (
        CraigslistCategory.cars_trucks,
        KijCategory.cars_trucks)

    musical_instruments = (
        CraigslistCategory.musical_instruments,
        KijCategory.musical_instruments)

    office_business = (
        CraigslistCategory.business_commercial,
        KijCategory.business_industrial)

    pets = (
        CraigslistCategory.general_sale,
        KijCategory.other)

    shoes_clothing_watches = (
        CraigslistCategory.clothing_accessories,
        KijCategory.clothing)

    sporting_goods = (
        CraigslistCategory.sporting_goods,
        KijCategory.sporting_goods_exercise)

    tickets = (
        CraigslistCategory.tickets,
        KijCategory.tickets)

    toys_games = (
        CraigslistCategory.toys_games,
        KijCategory.toys_games)

    video_games = (
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