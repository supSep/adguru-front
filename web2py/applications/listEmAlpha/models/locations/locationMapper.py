from applications.listEmAlpha.models.locations import PostLocation

title_location_mapper = {
   "Burnaby & New Westminister" : PostLocation.burnaby_newwest,
    "Delta, Surrey & Langley" : PostLocation.delta_surrey_langley,
    "North Van & West Van": PostLocation.northshore,
    "Richmond":  PostLocation.richmond,
    "UBC" : PostLocation.ubc,
    "Vancouver" : PostLocation.vancouver,
    "Tricities, Pitt Meadows & Maple Ridge" : PostLocation.tricities_pitt_maple}