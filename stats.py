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
