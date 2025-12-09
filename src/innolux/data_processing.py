import re
from datetime import timedelta

def strptime_timedelta(time_str: str, fmt: str) -> timedelta:
    """
    Parses a time string into a timedelta object using a format string
    with optional components. Supports %d, %H, %M, %S.
    """
    # 1. Define the mapping of directives to capture groups
    # We use a pattern that captures one or more digits (\d+) for the value
    directives = {
        '%d': 'days',
        '%H': 'hours',
        '%M': 'minutes',
        '%S': 'seconds',
    }

    # 2. Build the Regex pattern dynamically
    regex_source = ""
    last_idx = 0
    
    # Iterate through the format string to find directives (%d, %H, etc.)
    for match in re.finditer(r'(%[dHMS])', fmt):
        start, end = match.span()
        directive = match.group(0)
        unit = directives[directive]
        
        # a. Capture the static text *before* the directive (e.g., 'Day', 'Hr')
        static_text = re.escape(fmt[last_idx:start])
        
        # b. Define the capture group for the value (e.g., (?P<days>\d+))
        capture_group = f"(?P<{unit}>\\d+)"
        
        # c. Combine the static text and the value capture group, making the whole block optional.
        # The structure is: ((static_text)(value_capture_group))?
        # This makes the unit label and its corresponding number optional *together*.
        regex_source += f"(?:{static_text}{capture_group})?"
        
        last_idx = end

    # 3. Add any trailing static text (e.g., if fmt ends with 's')
    regex_source += re.escape(fmt[last_idx:])

    # 4. Final match attempt
    match = re.match(f"^{regex_source}$", time_str)
    
    if match is None:
        raise ValueError(f"Time data '{time_str}' does not match format '{fmt}'")
    
    # 5. Extract values and convert to integers
    # Only include non-None matches (the optional parts that were present)
    data = {k: int(v) for k, v in match.groupdict().items() if v is not None}
    
    # 6. Create and return the timedelta
    return timedelta(**data)