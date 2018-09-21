"""
Python 3.6
@Author: wrgsRay
"""
from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # if the country wasn't found, return None.
        return None


def main():
    print('import only')


if __name__ == '__main__':
    main()
