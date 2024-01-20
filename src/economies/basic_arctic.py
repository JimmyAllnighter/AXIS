from economy import Economy

economy = Economy(
    id="BASIC_ARCTIC",
    numeric_id=1,
    # as of May 2015 the following cargos must have fixed positions if used by an economy:
    # passengers: 0, mail: 2, goods 5, food 11
    # keep the rest of the cargos alphabetised
    # bump the min. compatible version if this list changes
    cargos=[
        "passengers",
        "ammonia",
        "mail",
        "engineering_supplies",
        "explosives",
        "farm_supplies",
        "fertiliser",
        "fish",
        "kaolin",
        "logs",
        "lumber",
        "food",
        "paper",
        "peat",
        "phosphate",
        "potash",
        "pyrite_ore",
        "sulphur",
        "zinc",
    ],
    cargoflow_graph_tuning={},
)
