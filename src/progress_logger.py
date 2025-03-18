import sys
import time
import collections.abc


def log_progress(iterable, total=None, prefix='Progress:', suffix='Complete', 
                 decimals=1, length=50, fill='█', print_end="\r"):
    """
    Create a dynamic progress bar for logging the progress of an iteration.

    Args:
        iterable (iterable): The iterable object to track progress for.
        total (int, optional): Total number of iterations. Defaults to len(iterable).
        prefix (str, optional): Prefix text for the progress bar. Defaults to 'Progress:'.
        suffix (str, optional): Suffix text for the progress bar. Defaults to 'Complete'.
        decimals (int, optional): Positive number of decimals in percent complete. Defaults to 1.
        length (int, optional): Character length of the progress bar. Defaults to 50.
        fill (str, optional): Bar fill character. Defaults to '█'.
        print_end (str, optional): End character (e.g. "\r", "\r\n"). Defaults to "\r".

    Yields:
        Items from the iterable, while displaying a progress bar.

    Raises:
        ValueError: If total is less than or equal to 0.
        TypeError: If iterable cannot be converted to a sequence.
    """
    # Convert generator to list for multiple iterations
    if not isinstance(iterable, (list, tuple, collections.abc.Sequence)) and not hasattr(iterable, '__len__'):
        iterable = list(iterable)

    # Handle cases where total is not provided
    if total is None:
        total = len(iterable)

    # Handle empty iterables or zero total
    if total <= 0:
        print(f'\r{prefix} |{"-" * length}| 0.0% {suffix}')
        return

    # Prepare iteration variables
    iteration = 0

    # Iterate through items
    for item in iterable:
        # Calculate percentage and progress bar
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)

        # Print progress bar
        sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
        sys.stdout.flush()

        # Yield current item
        yield item

        # Increment iteration
        iteration += 1

    # Print new line on completion
    print()