from app.lib import create_flat, add_flat, search_flats, search_price


def test_create_flat():

    data = {
        'district': 'Кировский',
        'rooms_quantity': 3,
        'price': 3000000,
     }

    result = create_flat(data['district'], data['rooms_quantity'], data['price'])

    assert data == result

def test_add_one_flat_to_empty_library():
    container = []
    flat = create_flat('Кировский', 3, 3000000)

    add_flat(container, flat)

    assert  len(container) == 1
    assert flat in container

def test_search_district():
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

    founded_flat = [{
    'district': 'Кировский',
    'rooms_quantity': 2,
    'price': 3_000_000,
    }]
    result = search_flats(flats, 'Кировский')
    assert founded_flat == result


def test_search_price():
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
    result = [{
    'district': 'Кировский',
    'rooms_quantity': 2,
    'price': 3_000_000,
    }]
    assert result == search_price(flats, 3_500_000)