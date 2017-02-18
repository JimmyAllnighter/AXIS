"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimary, IndustryLocationChecks

industry = IndustryPrimary(id='fishing_grounds',
                    accept_cargo_types=[],
                    prod_cargo_types=['FISH'],
                    layouts='[tilelayout_fishing_grounds_1, tilelayout_fishing_grounds_2, tilelayout_fishing_grounds_3, tilelayout_fishing_grounds_4]',
                    prob_in_game='14',
                    prob_random='14',
                    prod_multiplier='[7, 0]',
                    substitute='5',
                    map_colour='158',
                    life_type='IND_LIFE_TYPE_EXTRACTIVE',
                    spec_flags='bitmask(IND_FLAG_BUILT_ON_WATER, IND_FLAG_NO_PRODUCTION_INCREASE, IND_FLAG_AI_CREATES_AIR_AND_SHIP_ROUTES)',
                    location_checks=IndustryLocationChecks(require_cluster=['fishing_grounds', [20, 84, 1, 5]],
                                                           incompatible={'fishing_harbour': 16},
                                                           coast_distance=True),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_FISHING_GROUND)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_WATER))',
                    fund_cost_multiplier='88',
                    template="industry_fishing_grounds.pypnml" )

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].enabled = True
industry.economy_variations['BASIC_TROPIC'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True

spriteset_1 = industry.add_spriteset(
    id = 'fishing_grounds_spriteset_1',
    sprites = [(10, 10, 64, 31, -31, 0)],
    zextent = 16
)
spriteset_2 = industry.add_spriteset(
    id = 'fishing_grounds_spriteset_2',
    sprites = [(80, 10, 64, 31, -31, 0)],
    zextent = 16
)
spriteset_3 = industry.add_spriteset(
    id = 'fishing_grounds_spriteset_3',
    sprites = [(150, 10, 64, 31, -31, 0)],
    zextent = 16
)
spriteset_4 = industry.add_spriteset(
    id = 'fishing_grounds_spriteset_4',
    sprites = [(220, 10, 64, 31, -31, 0)],
    zextent = 16
)
spriteset_5 = industry.add_spriteset(
    id = 'fishing_grounds_spriteset_5',
    sprites = [(290, 10, 64, 31, -31, -32)],
    zextent = 16
)
