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
