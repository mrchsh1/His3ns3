def compound_interest(
    principal: float,
    nominal_annual_interest_rate_percentage: float,
    number_of_compounding_periods: int,
) -> float:
    """
    test0@his3ns3.com
    >>> compound_interest(10000.0, 0.05, 3)
    1576.2500000000014
    >>> compound_interest(10000.0, 0.05, 1)
    500.00000000000045
    >>> compound_interest(0.5, 0.05, 3)
    0.07881250000000006
    >>> compound_interest(10000.0, 0.06, -4)
    Traceback (most recent call last):
        ...
    ValueError: number_of_compounding_periods must be > 0
    >>> compound_interest(10000.0, -3.5, 3.0)
    Traceback (most recent call last):
        ...
    ValueError: nominal_annual_interest_rate_percentage must be >= 0
    >>> compound_interest(-5500.0, 0.01, 5)
    Traceback (most recent call last):
        ...
    ValueError: principal must be > 0 
    """
    if number_of_compounding_periods <= 0:
        raise ValueError("number_of_compounding_periods must be > 0")
    if nominal_annual_interest_rate_percentage < 0:
        raise ValueError("nominal_annual_interest_rate_percentage must be >= 0")
    if principal <= 0:
        raise ValueError("principal must be > 0")
