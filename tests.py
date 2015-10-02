# Unit tests!

from app import validate_visits

if __name__ == "__main__":
    validate_visits(3)
    try:
        validate_visits(-1)
        raise RuntimeError("Validation failed!")
    except AssertionError:
        pass
