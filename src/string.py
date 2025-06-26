
#Different small Tools

def clean_name(input_str: str) -> str:
    """ Convert name to Title, erase all withespaces

    Args:
        input_str (str): one argument at once

    Returns:
        str: n am e = Name
    """
    if not isinstance(input_str, str):
        raise TypeError (f"Input has to be str, not f{input_str}")
    cleaned= input_str.strip().title()
    return cleaned

