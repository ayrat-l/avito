from app.lib import create_flat, add_flat


def test_create_flat():
    flats = {'rooms': '2 комнатная квартира', 'floor': '1/10', 'area': '50', 'price': 5000000,
             'district': 'Вахитовский'}
    result = create_flat('2 комнатная квартира', '1/10', '50', 5_000_000, 'Вахитовский')
    assert result == flats


def test_add_flat():
    flats = []
    flat = create_flat('2 комнатная квартира', '1/10', '50', 5_000_000, 'Вахитовский')
    add_flat(flats, flat)
    assert len(flats) != 0
    assert flat in flats

