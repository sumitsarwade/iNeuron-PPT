

#2. Write a MapReduce program to calculate the word count of a given input text file.
import sys

# Read input line by line
for line in sys.stdin:
    # Split the line into words
    words = line.strip().split()

    # Emit each word with a count of 1
    for word in words:
        print(word, 1)

# Reducer code
#!/usr/bin/env python

import sys

# Initialize variables
current_word = None
current_count = 0

# Read input from mapper
for line in sys.stdin:
    # Parse the input
    word, count = line.strip().split('\t')

    # Convert count to integer
    count = int(count)

    # If the word is the same as the previous word, increment the count
    if word == current_word:
        current_count += count
    else:
        # If the word is different, emit the previous word and count
        if current_word:
            print(current_word, current_count)
        current_word = word
        current_count = count

# Emit the last word and count
if current_word:
    print(current_word, current_count)


-------------------------------------------------------------------------------------------------------------------------------------------------------------
#3. Write a Spark program to count the number of occurrences of each word in a given text file.

from pyspark import SparkContext, SparkConf

# Create a Spark context
conf = SparkConf().setAppName("WordCount")
sc = SparkContext(conf=conf)

# Read the input text file
lines = sc.textFile("C:\Users\OneDrive\Documents\input.txt")

# Split each line into words and create a flat map
words = lines.flatMap(lambda line: line.split())

# Map each word to a tuple of (word, 1) for counting
word_counts = words.map(lambda word: (word, 1))

# Reduce by key to count the occurrences of each word
word_counts = word_counts.reduceByKey(lambda x, y: x + y)

# Print the word counts
for word, count in word_counts.collect():
    print(f"{word}: {count}")

# Stop the Spark context
sc.stop()

