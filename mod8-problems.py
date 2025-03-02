# mod8-problems.py

'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to
it.
Write a Python script that reads a file gardening_tips.txt and prints
out each tip one by one.
'''

file = open("gardening_tips.txt", "w")
file.write("1. Water your plants early in the morning.\n")
file.write("2. Use mulch to retain moisture and suppress weeds.\n")
file.write("3. Plants need Love, not Hate.\n")
file.write("4. Sing to your plants.\n")
file.write("5. Plants love Classical Music.\n")
file.write("6. Wisper sweet nothings onto your plants petals.\n")
file.write("7. Most importantly, ALWAYS hug your trees!\n")
file.close()

file = open("gardening_tips.txt", "r")
for line in file:
    print(line.strip())
file.close()

'''
#2. Write a Python program that allows users to log their hiking trips. The program
should:
- Use a while loop to repeatedly ask for a hike name and distance in miles
- Save each entry to hiking_log.txt (each hike on a new line)
- When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''

file = open("hiking_log.txt", "w")
file.close()

hike_name = input("Hike Name or 0 to quit: ")

while hike_name != "0":
    distance = input("Distance in miles: ")
    file = open("hiking_log.txt", "a")
    file.write(f"{hike_name}, {distance}\n")
    file.close()
    hike_name = input("Enter hike name (or 0 to exit): ") #get the next hike name.

print("\nHiking Log:")
file = open("hiking_log.txt", "r")
for line in file:
    print(line.strip())
file.close()

'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
it. Write a Python program that:
- Reads the file
- Requests 5 inputs from the user: 5 words the user would like to count the
frequency of
- Counts how many times each word appears
- Creates a dictionary of the words and their counts
- Print the dictionary to the console
'''

# Read lyrics from song_lyrics.txt
file = open("song_lyrics.txt", "r")
lyrics_content = file.read().lower()
file.close()

lyrics = lyrics_content.split()

word_counts = {}
search_words = [None] * 5  # Initialize a list of 5 None elements

# Get 5 words from the user
for i in range(5):
    word = input(f"Enter word {i + 1} to count: ").lower()
    search_words[i] = word  # Assign the input to the current index

for word in lyrics:
    if word in search_words:
        word_counts[word] = word_counts.get(word, 0) + 1

print("\nWord Counts:")
print(word_counts)

'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated
by commas.
Write a program that reads the poll.txt file
Count how many votes "yea" or "nay" received and print the results.
'''

file = open("poll.txt", "r")
votes_str = file.read().lower()
file.close()

votes = votes_str.split(",")

yea_count = 0
nay_count = 0

for vote in votes:
    if vote == "yea":
        yea_count += 1
    elif vote == "nay":
        nay_count += 1

print(f"Yea votes: {yea_count}")
print(f"Nay votes: {nay_count}")
