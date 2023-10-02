
import re
import os
import sys
path = "C:\\Users\\aneme\\Desktop\\Progetti\\typer\\typer_f"
sys.path.append(path)
from database import get_db, Word



def get_words_from_txt(file_path, pattern) -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        dictionary = dict()
        for line in file:
            # clean line
            line = re.sub(r'[^\w\s\']', '', line)
            # print(line)  ## Outputs: "Hello World Python NLP"
            words = line.split()
            for word in words:
                if not pattern.search(word):
                    continue
                
                if not dictionary.get(word):
                    dictionary[word] = 1
                else:
                    dictionary[word] += 1
        return dictionary


def save_words_on_db(dictionary:dict, language: str):
    with get_db() as db:
        counter_new_words = 0
        for word in dictionary:
            # if the world already exists
            old_word_freq = db.query(Word.frequency).filter(Word.word == word).first()
            if old_word_freq:
                # I uppdated the frequency for such word
                old_word_freq = old_word_freq[0] + dictionary[word]
                db.query(Word).filter(Word.word == word).update({Word.frequency: old_word_freq})
                db.commit()

            else:
                new_word = Word(
                    word = word,
                    language = language,
                    frequency = dictionary[word]  # Add frequency column
                )
                db.add(new_word)
                counter_new_words += 1 
                db.commit()
        print(f"{counter_new_words} new words have been loaded in the db")
        


if __name__ == "__main__":
    # to be passed as parameter TODO
    pattern = re.compile('[a-zA-Z\']')
    folder_path = f"{path}\\scripts\\GOT"
    language = "english"

    for filename in os.listdir(folder_path):
        print(f"start file: {filename}")
        file_path = f"{folder_path}\\{filename}" 
        dictionary = get_words_from_txt(file_path, pattern)
        print(" - Dictionary has been created")
        save_words_on_db(dictionary, language)
        print(" - Data have been uploaded")
        print(f"finished file: {filename}")

        
    
    
        

    