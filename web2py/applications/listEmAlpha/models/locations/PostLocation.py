from enum import Enum

class PostLocation(Enum):
	burnaby_newwest = (
		CraigslistLocation.burnaby_newwest,
		 KijLocation.burnaby_newwest)

	delta_surrey_langley = (
		CraigslistLocation.delta_surrey_langley,
		 KijLocation.delta_surrey_langley)

	northshore = (
		CraigslistLocation.northshore,
		 KijLocation.northshore)

	richmond = (
		CraigslistLocation.richmond,
		 KijLocation.richmond)

	ubc = (
		CraigslistLocation.vancouver,
		 KijLocation.ubc)

	vancouver = (
		CraigslistLocation.vancouver,
		 KijLocation.vancouver)

	tricities_pitt_maple = (
		CraigslistLocation.tricities_pitt_maple,
		 KijLocation.tricities_pitt_maple)