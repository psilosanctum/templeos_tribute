from random import randint, shuffle, choice, sample
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
book_value = bible.Book.MARK.value
book_name = bible.Book.MARK.name
book_title = bible.Book.MARK.title

book_chapters = bible.get_number_of_chapters(bible.Book.MARK)
book_verses = bible.get_number_of_verses(bible.Book.MARK, chapter=1)
# print(book_verses)
count_book_chapters = bible.count_chapters(book_name)
count_book_verses = bible.count_verses(book_name)
# all_references = bible.convert_verse_ids_to_references(verse_ids=all_bible_verse_ids[0:37])
max_verse_book_chapter = bible.verses.MAX_VERSE_NUMBER_BY_BOOK_AND_CHAPTER
# for key, value in max_verse_book_chapter.items():
#     print(key.name)
#     print(value)
# print(max_verse_book_chapter.items())

bible_books = bible.BOOK_GROUPS
# print(bible_books['New Testament'][0])

all_bible_verse_ids = list(bible.verses.VERSE_IDS)
number_of_samples = 3
random_verse_ids = sample(all_bible_verse_ids, number_of_samples)
verse_texts_list = []
for verse in random_verse_ids:
    verse_texts_list.append(bible.get_verse_text(verse, version=bible.Version.KING_JAMES).replace(",", "").replace(":", "").replace(".", "").split(" "))

verses_sampling_list = []
for i in range(len(verse_texts_list)):
    random_num_sample = randint(0,len(verse_texts_list[i]))
    random_word_selection = sample(verse_texts_list[i], random_num_sample)
    verses_sampling_list.append(random_word_selection)

shuffle(verses_sampling_list)
concat_verses_sampling_lists = verses_sampling_list[0] + verses_sampling_list[1] + verses_sampling_list[2]
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

# Create list of words
def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())
        valid_words = list(valid_words)
    return valid_words

# Randomize selection of a numeric value between 1 and 37
response_range = randint(1,37)

# Iterate over range of randomized number selected
# Randomized numbers selected again from the range of total words in our list
response_range_ints_list = []
for i in range(response_range):
    random_word = randint(0,466548)
    response_range_ints_list.append(random_word)

# Select the individual words from our words list using the randomly generated integers
words = load_words()
random_words_list = []
for i in response_range_ints_list:
    random_words_list.append(words[i].lower())

# Shuffle the list to increase randomization
shuffle(random_words_list)

# Calculate the numerical value of each word using our gematric mapping
word_numeric_list = []
for i in random_words_list:
    word_numeric = 0
    for j in i: 
        letter_value = pythagorean_gematria_dict.get(j)
        if letter_value is not None: word_numeric += letter_value
        else: pass
    word_numeric_list.append(word_numeric)

# # Arrive at Terry's randomized list of words which he interpreted as God speaking to him
# God_says_dict = dict(zip(word_numeric_list, random_words_list))
# God_says = f"God says: \nEncoded: {[*God_says_dict.keys()]} \nDecoded: {[*God_says_dict.values()]}"
# print(God_says)