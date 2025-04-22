"""Game assets and where they are located. This is a lazy/OK solution 
to creating a singleton class."""

from os import path
from videogame.pong_asset_dict import pong_asset_dict as asset_dict

main_dir = path.split(path.abspath(__file__))[0]
data_dir = path.join(main_dir, "data")



def get(key):
    """Given the key representing the asset, return a fully qualified
    path to the asset."""
    # Throws a KeyError if key doesn't exist.
    try:
        value = asset_dict[key]
    except KeyError:
        print(
            f'The asset key {key} is unknown and a KeyError exception was raised.'
        )
        raise
    value = path.join(data_dir, value)
    # Make sure the path exists
    assert path.exists(value)
    return value
