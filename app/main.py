from app.lib import *

flats = []

create1 = create_flat('2 комнатная квартира', '1/10', '50', 5_000_000, 'Вахитовский')
create2 = create_flat('1 комнатная квартира', '3/10', '40', 4_000_000, 'Советский')
create3 = create_flat('3 комнатная квартира', '5/19', '80', 7_000_000, 'Приволжский')
create4 = create_flat('1 комнатная квартира', '2/10', '35', 3_000_000, 'Вахитовский')

add_flat(flats, create1)
add_flat(flats, create2)
add_flat(flats, create3)
add_flat(flats, create4)

print(flats)

