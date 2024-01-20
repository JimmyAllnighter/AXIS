from economies import (
    basic_arctic,
    basic_temperate,
    basic_tropic,
    better_living_through_chemistry,
    in_a_hot_country,
    steeltown,
)

# specify economies in the order that they should appear in parameter list in-game (and also in docs)
# economies have a numeric ID which maps parameter values and avoids breaking savegames when this list changes
# !! ^ that doesn't appear to work, action 14 param doesn't seem to be able to abstract name value from name orde??

registered_economies = []

steeltown.economy.register()
basic_tropic.economy.register()
basic_temperate.economy.register()
basic_arctic.economy.register()
better_living_through_chemistry.economy.register()
in_a_hot_country.economy.register()
