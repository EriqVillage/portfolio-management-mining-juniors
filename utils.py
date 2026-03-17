def calc_expected_value(score, upside):
    try:
        return round(score * upside, 1)
    except:
        return None
