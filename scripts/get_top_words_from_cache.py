import json
import pickle

words_file_path = "../src/words.json"


exclude_words = ["verse", "chorus", "bridge", "feat", "edit", "justin", "chris", "sean", "wayne",
                 "james", "travis", "mike", "savage", "harris", "kelly", "kevin", "mill", "taylor", "lewis"]


def load_lyrics_cache():
    lyrics_cache = {}
    try:
        file = open('lyrics_cache', 'rb')
        lyrics_cache = pickle.load(file)
    except FileNotFoundError:
        file = open('lyrics_cache', 'wb')
        pickle.dump({}, file)
        file.close()
    return lyrics_cache


def remove_non_letters(lyrics):
    return "".join([char for char in lyrics if char.isalpha() or char == " " or char == "\n"])


words_allow_list_file = open("./10k-english-no-swears.txt", "r")
allowed_words = set()
for line in words_allow_list_file:
    allowed_words.add(line.strip())

word_counts = {}
lyrics_cache = load_lyrics_cache()
for track_id, lyrics in lyrics_cache.items():
    lyrics = remove_non_letters(lyrics)

    # add words to set
    word_set = set()
    for word in lyrics.split():
        word = word.lower()
        if word in word_set or word not in allowed_words or word in exclude_words:
            continue
        word_set.add(word)

    # add words from set to word_counts
    for word in word_set:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

min_word_length = 4
max_word_length = 10
filtered_word_counts = {}
for word, count in word_counts.items():
    if len(word) >= min_word_length and len(word) <= max_word_length:
        filtered_word_counts[word] = count

sorted_word_counts = sorted(
    filtered_word_counts.items(), key=lambda item: item[1], reverse=True)

sorted_word_counts = [(word, count) for word,
                      count in sorted_word_counts if count > 40]
for word, count in sorted_word_counts:
    print(word, count)

with open(words_file_path, "w") as words_file:
    words = [word for word, count in sorted_word_counts]
    words_as_json = json.dumps(words)
    words_file.write(words_as_json)
