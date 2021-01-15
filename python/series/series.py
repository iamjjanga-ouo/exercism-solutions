def slices(series, length):
    if not 0 < length <= len(series):
        raise ValueError(f"The given length {length} isn't compatible.")
    elif not series:
        raise ValueError("Series is empty.")
    return [series[i:i + length] for i in range(0, len(series)) if i + length <= len(series)]