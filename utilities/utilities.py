import re 

def delete_first_char_space(text: str) -> str :
    pattern_first_space = "^\s*"
    result = re.sub(pattern_first_space, "", text)
    return result

def search_index(oj: list, search: int, key: str) -> int:
    return next((index for (index, item) in enumerate(oj) if item[key] == search), None)