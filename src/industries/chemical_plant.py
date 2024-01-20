from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="chemical_plant",
    accept_cargos_with_input_ratios=[("OIL_", 4), ("NITR", 4)],
    prod_cargo_types_with_output_ratios=[("RFPR", 8)],
    combined_cargos_boost_prod=True,
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="191",
    name="string(STR_IND_CHEMICAL_PLANT)",
    nearby_station_name="string(STR_STATION_HEAVY_INDUSTRY_2)",
    fund_cost_multiplier="170",
    pollution_and_squalor_factor=2,
)

industry.economy_variations["BASIC_TROPIC"].enabled = True
industry.economy_variations["BASIC_TROPIC"].accept_cargos_with_input_ratios = [
    ("SALT", 2),
    ("NITR", 2),
    ("RFPR", 2),
]
industry.economy_variations["BASIC_TROPIC"].prod_cargo_types_with_output_ratios = [
    ("ACET", 6),
    ("ENUM", 4),
]

industry.economy_variations["BASIC_ARCTIC"].enabled = True
industry.economy_variations["BASIC_ARCTIC"].accept_cargos_with_input_ratios = [
    ("SULP", 2),
    ("PHOS", 2),
    ("NH3_", 2),
    ("POTA", 2),
]
industry.economy_variations["BASIC_ARCTIC"].prod_cargo_types_with_output_ratios = [
    ("FERT", 4),
    ("BOOM", 4),
]

# should be Specialty Chemicals Plant, and should also accept ACID??
# also this should not be forced to be near port in BLTC
industry.economy_variations["BETTER_LIVING_THROUGH_CHEMISTRY"].enabled = True
industry.economy_variations[
    "BETTER_LIVING_THROUGH_CHEMISTRY"
].accept_cargos_with_input_ratios = [
    ("SASH", 1),
    ("LYE_", 2),
    ("NH3_", 2),
    ("CHLO", 2),
    ("PHAC", 1),
]
industry.economy_variations[
    "BETTER_LIVING_THROUGH_CHEMISTRY"
].prod_cargo_types_with_output_ratios = [("SOAP", 4), ("ENUM", 4)]

"""
industry.economy_variations['IN_A_HOT_COUNTRY'].enabled = True
industry.economy_variations['IN_A_HOT_COUNTRY'].accept_cargos_with_input_ratios = [('SULP', 2), ('PHOS', 2), ('NH3_', 2), ('POTA', 2)]
industry.economy_variations['IN_A_HOT_COUNTRY'].prod_cargo_types_with_output_ratios = [('FMSP', 4), ('BOOM', 4)]
"""

industry.add_tile(
    id="chemical_plant_tile_1",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
industry.add_tile(
    id="chemical_plant_tile_2",
    animation_length=47,
    animation_looping=True,
    animation_speed=2,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="concrete",
)
spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)

spriteset_horizontal_tanks = industry.add_spriteset(
    sprites=[(150, 10, 64, 114, -31, -83)],
)
spriteset_frac_columns = industry.add_spriteset(
    sprites=[(220, 10, 64, 114, -31, -83)],
)
spriteset_drop_tower_and_thin_chimney = industry.add_spriteset(
    sprites=[(290, 10, 64, 114, -31, -83)],
)
spriteset_large_building = industry.add_spriteset(
    sprites=[(360, 10, 64, 114, -31, -83)],
)
spriteset_fat_chimney = industry.add_spriteset(
    sprites=[(430, 10, 64, 114, -31, -83)],
)
spriteset_spherical_tanks = industry.add_spriteset(
    sprites=[(500, 10, 64, 66, -31, -35)],
)
spriteset_vertical_tanks = industry.add_spriteset(
    sprites=[(570, 10, 64, 66, -31, -35)],
)
spriteset_barrels = industry.add_spriteset(
    sprites=[(710, 10, 64, 66, -31, -35)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=0,
    yoffset=0,
    zoffset=81,
)

industry.add_spritelayout(
    id="chemical_plant_spritelayout_horizontal_tanks",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_horizontal_tanks],
)
industry.add_spritelayout(
    id="chemical_plant_spritelayout_frac_columns",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_frac_columns],
)
industry.add_spritelayout(
    id="chemical_plant_spritelayout_drop_tower_and_thin_chimney",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_drop_tower_and_thin_chimney],
    smoke_sprites=[sprite_smoke_1],
)
industry.add_spritelayout(
    id="chemical_plant_spritelayout_large_building",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_large_building],
)
industry.add_spritelayout(
    id="chemical_plant_spritelayout_fat_chimney",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_fat_chimney],
)
industry.add_spritelayout(
    id="chemical_plant_spritelayout_spherical_tanks",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_spherical_tanks],
)
industry.add_spritelayout(
    id="chemical_plant_spritelayout_vertical_tanks",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_vertical_tanks],
)
industry.add_spritelayout(
    id="chemical_plant_spritelayout_barrels",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_barrels],
)


industry.add_industry_layout(
    id="chemical_plant_industry_layout_1",
    layout=[
        (0, 0, "chemical_plant_tile_2", "chemical_plant_spritelayout_fat_chimney"),
        (0, 1, "chemical_plant_tile_2", "chemical_plant_spritelayout_fat_chimney"),
        (0, 2, "chemical_plant_tile_1", "chemical_plant_spritelayout_spherical_tanks"),
        (1, 0, "chemical_plant_tile_2", "chemical_plant_spritelayout_large_building"),
        (1, 1, "chemical_plant_tile_2", "chemical_plant_spritelayout_large_building"),
        (1, 2, "chemical_plant_tile_1", "chemical_plant_spritelayout_barrels"),
        (2, 0, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (2, 1, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (2, 2, "chemical_plant_tile_1", "chemical_plant_spritelayout_barrels"),
        (3, 0, "chemical_plant_tile_1", "chemical_plant_spritelayout_frac_columns"),
        (3, 1, "chemical_plant_tile_1", "chemical_plant_spritelayout_frac_columns"),
        (3, 2, "chemical_plant_tile_1", "chemical_plant_spritelayout_vertical_tanks"),
        (
            4,
            0,
            "chemical_plant_tile_1",
            "chemical_plant_spritelayout_drop_tower_and_thin_chimney",
        ),
        (4, 1, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (4, 2, "chemical_plant_tile_1", "chemical_plant_spritelayout_vertical_tanks"),
    ],
)
industry.add_industry_layout(
    id="chemical_plant_industry_layout_2",
    layout=[
        (
            0,
            1,
            "chemical_plant_tile_1",
            "chemical_plant_spritelayout_drop_tower_and_thin_chimney",
        ),
        (0, 2, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (0, 3, "chemical_plant_tile_2", "chemical_plant_spritelayout_fat_chimney"),
        (0, 4, "chemical_plant_tile_2", "chemical_plant_spritelayout_fat_chimney"),
        (1, 0, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (1, 1, "chemical_plant_tile_1", "chemical_plant_spritelayout_frac_columns"),
        (1, 2, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (1, 3, "chemical_plant_tile_2", "chemical_plant_spritelayout_large_building"),
        (1, 4, "chemical_plant_tile_2", "chemical_plant_spritelayout_large_building"),
        (2, 0, "chemical_plant_tile_1", "chemical_plant_spritelayout_vertical_tanks"),
        (2, 1, "chemical_plant_tile_1", "chemical_plant_spritelayout_vertical_tanks"),
        (2, 2, "chemical_plant_tile_1", "chemical_plant_spritelayout_barrels"),
        (2, 3, "chemical_plant_tile_1", "chemical_plant_spritelayout_spherical_tanks"),
        (2, 4, "chemical_plant_tile_1", "chemical_plant_spritelayout_spherical_tanks"),
    ],
)
industry.add_industry_layout(
    id="chemical_plant_industry_layout_3",
    layout=[
        (0, 0, "chemical_plant_tile_2", "chemical_plant_spritelayout_fat_chimney"),
        (0, 1, "chemical_plant_tile_2", "chemical_plant_spritelayout_fat_chimney"),
        (0, 2, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (0, 3, "chemical_plant_tile_1", "chemical_plant_spritelayout_frac_columns"),
        (0, 4, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (1, 0, "chemical_plant_tile_2", "chemical_plant_spritelayout_large_building"),
        (1, 1, "chemical_plant_tile_2", "chemical_plant_spritelayout_large_building"),
        (1, 2, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (1, 3, "chemical_plant_tile_1", "chemical_plant_spritelayout_frac_columns"),
        (
            1,
            4,
            "chemical_plant_tile_1",
            "chemical_plant_spritelayout_drop_tower_and_thin_chimney",
        ),
        (2, 0, "chemical_plant_tile_2", "chemical_plant_spritelayout_spherical_tanks"),
        (2, 1, "chemical_plant_tile_2", "chemical_plant_spritelayout_barrels"),
        (2, 2, "chemical_plant_tile_2", "chemical_plant_spritelayout_barrels"),
        (2, 3, "chemical_plant_tile_2", "chemical_plant_spritelayout_vertical_tanks"),
        (2, 4, "chemical_plant_tile_2", "chemical_plant_spritelayout_vertical_tanks"),
    ],
)
industry.add_industry_layout(
    id="chemical_plant_industry_layout_4",
    layout=[
        (0, 0, "chemical_plant_tile_1", "chemical_plant_spritelayout_vertical_tanks"),
        (0, 1, "chemical_plant_tile_1", "chemical_plant_spritelayout_vertical_tanks"),
        (1, 0, "chemical_plant_tile_1", "chemical_plant_spritelayout_frac_columns"),
        (1, 1, "chemical_plant_tile_1", "chemical_plant_spritelayout_frac_columns"),
        (2, 0, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (2, 1, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (3, 0, "chemical_plant_tile_2", "chemical_plant_spritelayout_fat_chimney"),
        (3, 1, "chemical_plant_tile_2", "chemical_plant_spritelayout_fat_chimney"),
        (4, 0, "chemical_plant_tile_2", "chemical_plant_spritelayout_large_building"),
        (4, 1, "chemical_plant_tile_2", "chemical_plant_spritelayout_large_building"),
        (
            5,
            0,
            "chemical_plant_tile_1",
            "chemical_plant_spritelayout_drop_tower_and_thin_chimney",
        ),
        (5, 1, "chemical_plant_tile_1", "chemical_plant_spritelayout_barrels"),
        (6, 0, "chemical_plant_tile_1", "chemical_plant_spritelayout_spherical_tanks"),
        (6, 1, "chemical_plant_tile_1", "chemical_plant_spritelayout_spherical_tanks"),
    ],
)
industry.add_industry_layout(
    id="chemical_plant_industry_layout_5",
    layout=[
        (0, 0, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (0, 1, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (0, 2, "chemical_plant_tile_2", "chemical_plant_spritelayout_fat_chimney"),
        (0, 3, "chemical_plant_tile_2", "chemical_plant_spritelayout_fat_chimney"),
        (
            1,
            0,
            "chemical_plant_tile_1",
            "chemical_plant_spritelayout_drop_tower_and_thin_chimney",
        ),
        (1, 1, "chemical_plant_tile_1", "chemical_plant_spritelayout_frac_columns"),
        (1, 2, "chemical_plant_tile_2", "chemical_plant_spritelayout_large_building"),
        (1, 3, "chemical_plant_tile_2", "chemical_plant_spritelayout_large_building"),
        (2, 0, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (2, 1, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (2, 2, "chemical_plant_tile_1", "chemical_plant_spritelayout_barrels"),
        (2, 3, "chemical_plant_tile_1", "chemical_plant_spritelayout_spherical_tanks"),
        (3, 0, "chemical_plant_tile_1", "chemical_plant_spritelayout_vertical_tanks"),
        (3, 1, "chemical_plant_tile_1", "chemical_plant_spritelayout_vertical_tanks"),
        (3, 2, "chemical_plant_tile_1", "chemical_plant_spritelayout_barrels"),
        (3, 3, "chemical_plant_tile_1", "chemical_plant_spritelayout_spherical_tanks"),
    ],
)
industry.add_industry_layout(
    id="chemical_plant_industry_layout_6",
    layout=[
        (0, 0, "chemical_plant_tile_2", "chemical_plant_spritelayout_fat_chimney"),
        (0, 1, "chemical_plant_tile_1", "chemical_plant_spritelayout_frac_columns"),
        (0, 2, "chemical_plant_tile_1", "chemical_plant_spritelayout_vertical_tanks"),
        (0, 3, "chemical_plant_tile_1", "chemical_plant_spritelayout_vertical_tanks"),
        (1, 0, "chemical_plant_tile_2", "chemical_plant_spritelayout_large_building"),
        (1, 1, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (
            1,
            2,
            "chemical_plant_tile_1",
            "chemical_plant_spritelayout_drop_tower_and_thin_chimney",
        ),
        (1, 3, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (2, 0, "chemical_plant_tile_2", "chemical_plant_spritelayout_fat_chimney"),
        (2, 1, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (2, 2, "chemical_plant_tile_1", "chemical_plant_spritelayout_frac_columns"),
        (2, 3, "chemical_plant_tile_1", "chemical_plant_spritelayout_horizontal_tanks"),
        (3, 0, "chemical_plant_tile_2", "chemical_plant_spritelayout_large_building"),
        (3, 1, "chemical_plant_tile_1", "chemical_plant_spritelayout_barrels"),
        (3, 2, "chemical_plant_tile_1", "chemical_plant_spritelayout_spherical_tanks"),
        (3, 3, "chemical_plant_tile_1", "chemical_plant_spritelayout_spherical_tanks"),
    ],
)
