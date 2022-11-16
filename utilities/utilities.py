import re 

def delete_first_char_space(text):
    pattern_first_space = "^\s*"
    result = re.sub(pattern_first_space, "", text)
    return result