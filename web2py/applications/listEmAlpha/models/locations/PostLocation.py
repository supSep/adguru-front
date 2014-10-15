from enum import Enum
from applications.listEmAlpha.models.locations.CraigslistLocation import CraigslistLocation
from applications.listEmAlpha.models.locations.KijLocation import KijLocation


class PostLocation(Enum):
    burnaby_newwest = dict(
        CraigslistLocation.burnaby_newwest.value,
        KijLocation.burnaby_newwest.value)

    delta_surrey_langley = dict(
        CraigslistLocation.delta_surrey_langley.value,
        KijLocation.delta_surrey_langley.value)

    northshore = dict(
        CraigslistLocation.northshore.value,
        KijLocation.northshore.value)

    richmond = dict(
        CraigslistLocation.richmond.value,
        KijLocation.richmond.value)

    ubc = dict(
        CraigslistLocation.vancouver.value,
        KijLocation.ubc.value)

    vancouver = dict(
        CraigslistLocation.vancouver.value,
        KijLocation.vancouver.value)

    tricities_pitt_maple = dict(
        CraigslistLocation.tricities_pitt_maple.value,
        KijLocation.tricities_pitt_maple.value)