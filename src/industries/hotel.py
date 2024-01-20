from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="hotel",
    accept_cargo_types=["FOOD", "BEER", "PASS"],
    prod_cargo_types_with_multipliers=[("PASS", 17)],
    prob_in_game="15",
    prob_map_gen="10",
    map_colour="189",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    location_checks=dict(same_type_distance=16),
    prospect_chance="0.75",
    name="string(STR_IND_HOTEL)",
    nearby_station_name="string(STR_STATION_BAR_GRILL_AND_ROOMS)",
    fund_cost_multiplier="102",
)

industry.economy_variations["BASIC_TEMPERATE"].enabled = True

industry.economy_variations["BASIC_TROPIC"].enabled = True

industry.economy_variations["BASIC_ARCTIC"].enabled = True
industry.economy_variations["BASIC_ARCTIC"].accept_cargo_types = [
    "FOOD",
    "PASS",
]

industry.economy_variations["STEELTOWN"].enabled = True
industry.economy_variations["STEELTOWN"].accept_cargo_types = [
    "FOOD",
    "PASS",
]

industry.economy_variations["BETTER_LIVING_THROUGH_CHEMISTRY"].enabled = True

industry.economy_variations["IN_A_HOT_COUNTRY"].enabled = True


industry.add_tile(
    id="hotel_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, require_houses_nearby=True
    ),
)

sprite_ground = industry.add_sprite(sprite_number="GROUNDSPRITE_CLEARED")
spriteset_ground_overlay = industry.add_spriteset(
    type="slab",
)

sprite_ground_3 = industry.add_sprite(sprite_number=1448)
sprite_ground_4 = industry.add_sprite(sprite_number=1451)

sprite_ground_5 = industry.add_sprite(sprite_number=4485)
sprite_ground_6 = industry.add_sprite(sprite_number=4486)

sprite_building_1 = industry.add_sprite(
    sprite_number="(terrain_type == TILETYPE_SNOW) ? 4583 : 4475"
)
sprite_building_2 = industry.add_sprite(
    sprite_number="(terrain_type == TILETYPE_SNOW) ? 4584 : 4476"
)
sprite_building_3 = industry.add_sprite(sprite_number=1450)
sprite_building_4 = industry.add_sprite(sprite_number=1453)
sprite_building_5 = industry.add_sprite(sprite_number=4491)
sprite_building_6 = industry.add_sprite(sprite_number=4492)

industry.add_spritelayout(
    id="hotel_spritelayout_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_building_1],
)
industry.add_spritelayout(
    id="hotel_spritelayout_2",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_building_2],
)

industry.add_spritelayout(
    id="hotel_spritelayout_3",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_ground_3, sprite_building_3],
)
industry.add_spritelayout(
    id="hotel_spritelayout_4",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_ground_4, sprite_building_4],
)

industry.add_spritelayout(
    id="hotel_spritelayout_5",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_ground_5, sprite_building_5],
)
industry.add_spritelayout(
    id="hotel_spritelayout_6",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_ground_6, sprite_building_6],
)

industry.add_industry_layout(
    id="hotel_industry_layout_1",
    layout=[
        (0, 0, "hotel_tile_1", "hotel_spritelayout_1"),
        (1, 0, "hotel_tile_1", "hotel_spritelayout_1"),
        (0, 1, "hotel_tile_1", "hotel_spritelayout_2"),
        (1, 1, "hotel_tile_1", "hotel_spritelayout_2"),
    ],
)

industry.add_industry_layout(
    id="hotel_industry_layout_2",
    layout=[
        (0, 0, "hotel_tile_1", "hotel_spritelayout_3"),
        (0, 1, "hotel_tile_1", "hotel_spritelayout_4"),
    ],
)

industry.add_industry_layout(
    id="hotel_industry_layout_3",
    layout=[
        (0, 0, "hotel_tile_1", "hotel_spritelayout_5"),
        (1, 0, "hotel_tile_1", "hotel_spritelayout_6"),
    ],
)
