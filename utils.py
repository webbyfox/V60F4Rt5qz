"""Summary
"""
import calendar


def weekday(dayrange):
    """
    return the list of weekdays from dayrange
    
    Args:
        dayrange (TYPE): Description
    
    Returns:
        TYPE: Description
    
    Raises:
        ValueError: if input is not valid
    """
    if '-' in dayrange:
        try:
            weekdays = [d[:3].lower() for d in calendar.day_name]
            start, end = (weekdays.index(d)
                          for d in dayrange.lower().split('-'))
            return weekdays[start:end + 1]
        except:
            raise

    else:
        raise ValueError("Not a valid day range")


def square(this):
    """Square the int
    
    Args:
        this (TYPE): int
    
    Returns:
        TYPE: int
    """
    try:
        return int(this) ** 2
    except:
        raise


def double(this):
    """Double the int
    
    Args:
        this (TYPE): int
    
    Returns:
        TYPE: int
    """
    try:
        return int(this) * 2
    except:
        raise


