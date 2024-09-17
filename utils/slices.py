# Responável por lidar com as fatias de dados

def get_subset(dictionary, start, end):
    return {k: v for i, (k, v) in enumerate(dictionary.items()) if start <= i < end}

def get_subset_by_list(dictionary, indexes):
    return {k: v for i, (k, v) in enumerate(dictionary.items()) if i in indexes}

def get_subset_by_key_list(dictionary, keys):
    return {k: v for k, v in dictionary.items() if k in keys}
