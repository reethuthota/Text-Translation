from difflib import SequenceMatcher
import csv

def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # Skip the header
        next(reader, None)
        return [(row[0].lower().strip(), row[1].lower().strip()) for row in reader]

def find_similarity(original_text, translated_text):
    seq_matcher = SequenceMatcher(None, original_text, translated_text)
    return seq_matcher.ratio()


def similarity(translated):
    csv_file_path = "english-french.csv"
    # Read the contents of the CSV file
    dataset_lines = read_csv(csv_file_path)
    translated_cleaned = translated.lower().strip()
    
    # Compare the cleaned translated response with each French row in the dataset
    similarities = [find_similarity(french_text, translated_cleaned) for _, french_text in dataset_lines]

    # Find the index of the most similar Spanish row in the dataset
    most_similar_index = similarities.index(max(similarities))

    similarityratio={similarities[most_similar_index]}
    print(similarityratio)
    return similarityratio