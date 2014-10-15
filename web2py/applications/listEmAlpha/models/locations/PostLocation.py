from enum import Enum
from applications.listEmAlpha.models.locations.CraigslistLocation import CraigslistLocation
from applications.listEmAlpha.models.locations.KijLocation import KijLocation


class PostLocation(Enum):
    burnaby_newwest = (
        CraigslistLocation.burnaby_newwest.value,
        KijLocation.burnaby_newwest.value)

    delta_surrey_langley = (
        CraigslistLocation.delta_surrey_langley.value,
        KijLocation.delta_surrey_langley.value)

    northshore = (
        CraigslistLocation.northshore.value,
        KijLocation.northshore.value)

    richmond = (
        CraigslistLocation.richmond.value,
        KijLocation.richmond.value)

    ubc = (
        CraigslistLocation.vancouver.value,
        KijLocation.ubc.value)

    vancouver = (
        CraigslistLocation.vancouver.value,
        KijLocation.vancouver.value)

    tricities_pitt_maple = (
        CraigslistLocation.tricities_pitt_maple.value,
        KijLocation.tricities_pitt_maple.value)