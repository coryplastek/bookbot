def get_num_words(text):
    return len(text.split())

def get_character_stats(text):
    stats = {}
    for c in list(text):
        c = c.lower()
        if c in stats:
            stats[c] = stats[c] + 1
        else:
            stats[c] = 1
    return stats

def get_character_dict_count(d):
    return d["num"]

def sort_character_stats(stats):
    stats_list = list()
    for c, num in stats.items():
       stats_list.append(dict(char=c, num=num))
    stats_list.sort(key=get_character_dict_count, reverse=True)
    return stats_list
