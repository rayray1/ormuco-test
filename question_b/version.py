from fractions import Fraction


def compare_versions(version_a, version_b):
    if isinstance(version_a, bool) or isinstance(version_b, bool):
        return False
    try:
        float(Fraction(version_a))
        float(Fraction(version_b))
        return True
    except ValueError:
        return False
