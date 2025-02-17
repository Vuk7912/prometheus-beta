from datetime import datetime

def calculate_days_between_dates(start_date: str, end_date: str) -> int:
    """
    Calculate the number of days between two dates.
    
    Args:
        start_date (str): The start date in 'YYYY-MM-DD' format
        end_date (str): The end date in 'YYYY-MM-DD' format
    
    Returns:
        int: Number of days between the two dates (inclusive)
    
    Raises:
        ValueError: If dates are not in the correct format or invalid
    """
    try:
        # Parse the dates using datetime
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Calculate the difference and add 1 to make it inclusive
        days_difference = (end - start).days + 1
        
        return max(0, days_difference)
    except ValueError as e:
        raise ValueError(f"Invalid date format. Please use YYYY-MM-DD: {e}")