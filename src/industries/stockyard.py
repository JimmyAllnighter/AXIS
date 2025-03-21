from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="stockyard",
    accept_cargos_with_input_ratios=[("LVST", 6)],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("FOOD", 8)],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="177",
    special_flags=["IND_FLAG_MILITARY_HELICOPTER_CAN_EXPLODE"],
    name="string(STR_IND_STOCKYARD)",
    nearby_station_name="string(STR_STATION_ANIMALS)",
    fund_cost_multiplier="115",
    pollution_and_squalor_factor=2,
)


industry.economy_variations["BASIC_TEMPERATE"].enabled = True
industry.economy_variations["BASIC_TEMPERATE"].accept_cargos_with_input_ratios = [
    ("LVST", 6)
]

industry.economy_variations["BASIC_TROPIC"].enabled = True
industry.economy_variations["BASIC_TROPIC"].accept_cargos_with_input_ratios = [
    ("LVST", 8),
    ("SOAP", 2),
]
industry.economy_variations["BASIC_TROPIC"].prod_cargo_types_with_output_ratios = [
    ("MEAT", 8),
]

industry.economy_variations['BETTER_LIVING_THROUGH_CHEMISTRY'].enabled = True
industry.economy_variations['BETTER_LIVING_THROUGH_CHEMISTRY'].accept_cargos_with_input_ratios = [('LVST', 6), ('MNSP', 1), ('ENUM', 1)]

industry.economy_variations["IN_A_HOT_COUNTRY"].enabled = True
industry.economy_variations["IN_A_HOT_COUNTRY"].accept_cargos_with_input_ratios = [
    ("LVST", 6)
]

industry.economy_variations["STEELTOWN"].enabled = True
industry.economy_variations["STEELTOWN"].accept_cargos_with_input_ratios = [
    ("LVST", 6),
    ("SOAP", 2),
]
industry.economy_variations["STEELTOWN"].prod_cargo_types_with_output_ratios = [
    ("FISH", 8),
]

industry.add_tile(
    id="stockyard_tile_1",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(type="concrete")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 44, -31, -13)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 74, -31, -43)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 88, -31, -57)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 85, -31, -54)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 104, -31, -73)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 91, -31, -60)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 98, -31, -67)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 54, -31, -23)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 76, -31, -45)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(640, 10, 64, 32, -31, -1)],
)
spriteset_11 = industry.add_spriteset(
    sprites=[(710, 10, 64, 49, -31, -18)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=17,
    yoffset=9,
    zoffset=99,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=20,
    yoffset=9,
    zoffset=100,
    animation_frame_offset=1,
)

industry.add_spritelayout(
    id="stockyard_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_spritelayout(
    id="stockyard_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
)
industry.add_spritelayout(
    id="stockyard_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id="stockyard_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
)
industry.add_spritelayout(
    id="stockyard_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2],
)
industry.add_spritelayout(
    id="stockyard_spritelayout_6",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
)
industry.add_spritelayout(
    id="stockyard_spritelayout_7",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
)
industry.add_spritelayout(
    id="stockyard_spritelayout_8",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
)
industry.add_spritelayout(
    id="stockyard_spritelayout_9",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
)
industry.add_spritelayout(
    id="stockyard_spritelayout_10",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
)
industry.add_spritelayout(
    id="stockyard_spritelayout_11",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_11],
)
industry.add_spritelayout(
    id="stockyard_spritelayout_12",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
)

industry.add_industry_layout(
    id="stockyard_industry_layout_1",
    layout=[
        (0, 0, "stockyard_tile_1", "stockyard_spritelayout_12"),
        (0, 1, "stockyard_tile_1", "stockyard_spritelayout_12"),
        (0, 2, "stockyard_tile_1", "stockyard_spritelayout_11"),
        (0, 3, "stockyard_tile_1", "stockyard_spritelayout_12"),
        (1, 0, "stockyard_tile_1", "stockyard_spritelayout_12"),
        (1, 1, "stockyard_tile_1", "stockyard_spritelayout_8"),
        (1, 2, "stockyard_tile_1", "stockyard_spritelayout_9"),
        (1, 3, "stockyard_tile_1", "stockyard_spritelayout_10"),
        (3, 0, "stockyard_tile_1", "stockyard_spritelayout_12"),
        (3, 1, "stockyard_tile_1", "stockyard_spritelayout_5"),
        (3, 2, "stockyard_tile_1", "stockyard_spritelayout_6"),
        (3, 3, "stockyard_tile_1", "stockyard_spritelayout_7"),
        (4, 0, "stockyard_tile_1", "stockyard_spritelayout_1"),
        (4, 1, "stockyard_tile_1", "stockyard_spritelayout_2"),
        (4, 2, "stockyard_tile_1", "stockyard_spritelayout_3"),
        (4, 3, "stockyard_tile_1", "stockyard_spritelayout_4"),
    ],
)
