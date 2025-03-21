from cargo import Cargo

cargo = Cargo(
    id="fruits",
    type_name="string(STR_CARGO_NAME_FRUITS)",
    unit_name="string(STR_CARGO_NAME_FRUITS)",
    type_abbreviation="string(STR_CID_FRUITS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_EXPRESS, CC_PIECE_GOODS, CC_REFRIGERATED)",
    cargo_label="FRUT",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_FRUITS)",
    penalty_lowerbound="0",
    single_penalty_length="26",
    price_factor=124,
    capacity_multiplier="1",
    icon_indices=(14, 0),
    sprites_complete=True,
)
