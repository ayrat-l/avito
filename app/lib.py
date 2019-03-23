def create_flat(rooms, floor, area, price, district):
    return {
        'rooms': rooms,
        'floor': floor,
        'area': area,
        'price': price,
        'district': district

    }


def add_flat(container, flat):
    container.append(flat)


def search_flat(container, search):
    search_lowercased = search.strip().lower()  # 1. search.strip() 2. (результат search.strip()).lower()
    result = []
    for flat in container:
        if search_lowercased in flat['district'].lower():
            result.append(flat)
            continue

    return result


def search_by_price(container, search):
    result = []
    for flat in container:
        if flat['price'] <= search:
            result.append(flat)
            continue
        return result
