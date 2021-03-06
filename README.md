# Auto-Complete
**Google Project:** Search and auto-complete sentences within given input text files, manipulating data with complex data-structures.

Autocomplete, or word completion, is a feature in which an application predicts the rest of a word a user is typing.

The purpose of the completion action is to make it easier for the user to find the most appropriate sentence.

Once entering some text the user will get the five closest completions to the input from a big amount of data.

If there are five sentences that the text is their sub-string, they will be returned. Otherwise will be returned sentences containing the sub-string with one of the changes - a missing letter, additional letter, or a replaced letter.

If the user insert #, start a new word to search.

The results will be from sentences within given input text files.

You can upload your own files. In data_manager.py, line 4, change to your path to folder.

### Example:
![image](https://user-images.githubusercontent.com/86181688/132979149-d87b05c3-6d0b-49bd-826a-b02a7aedcc6e.png)

## Design:
The program consists of two parts: preprocessing and online search.

In preprocessing the system is taking the data and builds a data structure from it.

In the online search the system takes the sentence which the user types and search this sentence in the data structure.

After one time the system runs the preprocessing, its saves the data structure in a file, and then when the user runs it again, the system reads the data structure from the file instead of build it again.

## Demo
[Live Demo](https://youtu.be/_CzQbs_mxHk)
