# Tuple as records
# Tuple as records with named fields

from collections import namedtuple
from typing import NamedTuple


def display_coordinates(lat_lon: tuple[float, float]) -> str:
    lat, lon = lat_lon
    ns = 'N' if lat >= 0 else 'S'
    ew = 'E' if lon >= 0 else 'W'
    return f'{abs(lat):0.2f}°{ns}, {abs(lon):0.2f}°{ew}'


Coordinate_not_typed = namedtuple('Coordinate_not_typed', 'lat lon')


class Coordinate(NamedTuple):
    lat: float
    lon: float


def print_verbose(coordinates: tuple[float, float]) -> None:
    print()
    print(coordinates)
    print(type(coordinates))
    if getattr(coordinates, '__annotations__', None):
        print(coordinates.__annotations__)
    else:
        print('No annotations')
    print(display_coordinates(coordinates))
    print(30 * '-')


if __name__ == '__main__':
    wroclaw = (51.107883, 17.038538)
    print_verbose(wroclaw)

    santa_barbara = Coordinate_not_typed(34.420830, -119.698189)
    print_verbose(santa_barbara)

    cape_town = Coordinate(-33.918861, 18.423300)
    print_verbose(cape_town)
