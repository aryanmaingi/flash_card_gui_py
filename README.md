# Flashy - French Learning Flashcard App

This is a simple flashcard application that helps you learn French by flipping through flashcards. The front of the card shows a French word, and after a few seconds, the English translation is displayed. You can mark the word as "known," and it will be removed from the flashcard pool to focus only on words you haven't learned yet.

## Features
- **Interactive Flashcards**: Displays French words, then flips to show their English translation.
- **Progress Tracking**: Words marked as known are removed from the flashcard pool.
- **CSV Integration**: Automatically loads new words from a CSV file and saves progress by writing back to the CSV.

## Prerequisites
Before running the application, make sure you have the following installed:

- Python 3.x
- Required Python libraries:
  - `tkinter` (included in the Python standard library)
  - `pandas` (to handle CSV file operations)

## How it Works
1. **Loading the Data**: 
   - The app first checks for the existence of a `words_to_learn.csv` file, which stores any remaining words the user has yet to learn. If this file exists, it loads the words from this file.
   - If `words_to_learn.csv` does not exist (such as the first time you run the app), the app loads the original data from `french_words.csv`, which contains a list of French words and their English translations.
   
2. **Displaying Flashcards**: 
   - A random word is selected from the dataset and shown on the front of a flashcard, with the French word displayed.
   - After 3 seconds, the card "flips" to show the English translation on the back of the flashcard.
   
3. **User Interaction**: 
   - The user can interact with the app using two buttons:
     - **❌ Button**: Skips the current word and displays a new one.
     - **✅ Button**: Marks the current word as "known," removes it from the list of words to learn, and saves the updated list to the `words_to_learn.csv` file.
   
4. **Saving Progress**: 
   - When a word is marked as "known," it is removed from the list of words that still need to be learned. The updated list is saved to the `words_to_learn.csv` file so that the next time the app is opened, it only shows words the user hasn't marked as "known" yet.
