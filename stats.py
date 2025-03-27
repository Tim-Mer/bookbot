def get_num_words(contents):
    text_list = contents.split()
    return len(text_list)

def get_num_chars(contents):
    contents = contents.lower()
    chars_dict = {}
    for char in contents:
        try:
            chars_dict[char] += 1
        except:
            chars_dict[char] = 1
    return chars_dict

def sort_on(dict):
    return dict["count"]

def sort_chars(chars_dict):
    list_chars = []
    for key in chars_dict:
        tmp = {}
        tmp["char"] = key
        tmp["count"] = chars_dict[key]
        list_chars.append(tmp)
    list_chars.sort(reverse=True, key=sort_on)
    return list_chars
    