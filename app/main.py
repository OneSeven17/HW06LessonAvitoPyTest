from app.lib import search_flats, create_flat, add_flat, search_price

flats = []


flat_1 = create_flat(
    'Вахитовский',
    3,
    5_000_000,
    )

flat_2 = create_flat(
    'Кировский',
    2,
    3_000_000,
    )

flat_3 = create_flat(
    'Московский',
    4,
    5_500_000,
    )


add_flat(flats, flat_1)
add_flat(flats, flat_2)
add_flat(flats, flat_3)


print(search_flats(flats, 'Кировский'))
print(search_price(flats, 5000000))