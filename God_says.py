from random import randint, shuffle, sample
from time import sleep
import pythonbible as bible

# Pythagorean mapping to convert alphabet to numeric
pythagorean_gematria_dict = {
    "a": 1,"b": 2,"c": 3,"d": 4,"e": 5,
    "f": 6,"g": 7,"h": 8,"i": 9,"j": 1,
    "k": 2,"l": 3,"m": 4,"n": 5,"o": 6,
    "p": 7,"q": 8,"r": 9,"s": 1,"t": 2,
    "u": 3,"v": 4,"w": 5,"x": 6,"y": 7,
    "z": 8,
}

# Create list of all Bible verse IDs
all_bible_verse_ids = list(bible.verses.VERSE_IDS)

# Number of verses to randomly select
number_of_samples = 3
random_verse_ids = sample(all_bible_verse_ids, number_of_samples)

# Use randomly selected verse IDs to return scripture
verse_texts_list = []
tries = 10
# for verse in random_verse_ids:
for i in range(tries):
    for verse in random_verse_ids:
        try:
            verse_texts_list.append(bible.get_verse_text(verse, version=bible.Version.KING_JAMES).replace(",", "").replace(":", "").replace(".", "").split(" "))
        except bible.VersionMissingVerseError as e:
            if tries < i:
                sleep(3)
                continue
            else:
                print(f"Error: {e}")
        break    

# Randomly sample words from each verse
verses_sampling_list = []
for i in range(len(verse_texts_list)):
    random_num_sample = randint(0,len(verse_texts_list[i]))
    random_word_selection = sample(verse_texts_list[i], random_num_sample)
    verses_sampling_list.append(random_word_selection)

# Shuffle randomly sampled words from each verse
shuffle(verses_sampling_list)

# Concat 3 lists of randomly sampled words into one list
concat_verses_sampling_lists = verses_sampling_list[0] + verses_sampling_list[1] + verses_sampling_list[2]

# Shuffle again
shuffle(concat_verses_sampling_lists)

# Calculate the numerical value of each word using our gematric mapping
word_numeric_list = []
for i in concat_verses_sampling_lists:
    word_numeric = 0
    for j in i: 
        letter_value = pythagorean_gematria_dict.get(j)
        if letter_value is not None: word_numeric += letter_value
        else: pass
    word_numeric_list.append(word_numeric)

# Arrive at Terry's randomized list of words which he interpreted as God speaking to him
God_says_dict = dict(zip(word_numeric_list, concat_verses_sampling_lists))
God_says = f"God says: \nDecoded: {[*God_says_dict.values()]} \nEncoded: {[*God_says_dict.keys()]}"
print(God_says)