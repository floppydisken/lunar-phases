def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def map_range(value: float, from_min: float, from_max: float, to_min: float, to_max: float):
    value = clamp(value, from_min, from_max)

    from_diff = from_max - from_min
    to_diff = to_max - to_min

    value_start = value - from_min

    scaled = to_min + value_start / from_diff * to_diff

    return scaled

