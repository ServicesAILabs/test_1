
#Different small Tools

def clean_name(input_str: str) -> str:
    """ Convert name to Title, erase withespaces

    Args:
        input_str (str): one argument at once

    Returns:
        str: n am e = Name
    """
    if not isinstance(input_str, str):
        raise TypeError (f"Input has to be str, not f{input_str}")
    cleaned= input_str.strip().title()
    return cleaned

def clean_number(input_num) -> float:
    """ Convert to float, erase Not numeric exept - .

    Args:
        input_num (int, float, str): Only numbers and "-", "." isn`t filtered

    Returns:
        float: -12,400 $ = -12400
    """
    if isinstance(input_num, (int, float)):
        return float(input_num)
    
    try:
        cleaned_str = "".join(filter(lambda x: x in "0123456789.-", str(input_num)))
        return float(cleaned_str)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Convert Error: {e} ") from e
    
