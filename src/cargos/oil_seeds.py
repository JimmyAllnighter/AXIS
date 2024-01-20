from cargo import Cargo

cargo = Cargo(
    id="oil_seeds",
    type_name="string(STR_CARGO_NAME_OIL_SEEDS)",
    unit_name="string(STR_CARGO_NAME_OIL_SEEDS)",
    type_abbreviation="string(STR_CID_OIL_SEEDS)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.5",
    is_freight="1",
    cargo_classes="bitmask(CC_BULK, CC_COVERED)",
    cargo_label="OLSD",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_OIL_SEEDS)",
    penalty_lowerbound="4",
    single_penalty_length="40",
    price_factor=113,
    capacity_multiplier="1",
    icon_indices=(6, 6),
    sprites_complete=True,
)
