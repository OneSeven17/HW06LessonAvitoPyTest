def create_flat(district, rooms_quantity, price):
    return {
    'district': district,
    'rooms_quantity': rooms_quantity,
    'price': price,
    }


def add_flat(container, flat):
    container.append(flat)


def list_flats(container, page, page_size):
    start = (page - 1)
    finish = start + page_size
    return container[start:finish]

def search_flats(container, search):
    search_lowercased = search.strip().lower()
    result = []
    for flat in container:
        if search_lowercased in flat['district'].lower():
            result.append(flat)
            continue
    return result

def search_price(container, search):
    result = []
    for flat in container:
        if search >= flat['price']:
            result.append(flat)
    return result



