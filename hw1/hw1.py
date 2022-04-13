#hw1.py
#Julian Harris
#4 April 2022

"""Program reads in a txt file and saves data to dictionary. Functions are provided to process txt data,
to create lists based on votes, to return votes received based on color, and to print the dictionary."""

import sys

#process_file: Reads and parses input, creates a dictionary, returns dictionary of votes in tuples with color keys
#parameters: Name of input txt file
#returns: Dictionary loaded with txt file input
def process_file(fileName):
    fileOne = open(fileName)
    colorDic = {}
    Lines = fileOne.readlines() #List of strings, each is a line

    for line in Lines:
        line = line.split()
        for voteRank, color in enumerate(line): #voteRank is our index, color is the value
            if(colorDic.get(color, "miss") == "miss"): #If color is not in our dictionary, add it
                colorDic[color] = [0, 0, 0]
            colorDic[color][voteRank] += 1 #adding to specific vote

    for color in colorDic: #converting lists to tuples.
        colorDic[color] = tuple(colorDic[color])

    fileOne.close()
    return colorDic

#get_first_place_votes: Returns number of 1st place votes for the provided color
#parameters: Dictionary, and color to be used as key
#returns: Returns int count of votes from given key
def get_first_place_votes(colorDic, color):
    return colorDic[color][0] #0 is first place, 1 is second place, 2 is third place

#create_favorite_color_list: Creates an ordered list of colors based on who had the most votes
#parameters: Dictionary 
#returns: List of strings of ranked colors
def create_favorite_color_list(colorDic):
    voteRanks = sorted(colorDic.values(), reverse=True) #Favorites holds our list in tuple vote form
    colorRank = [] 
    for rankedValue in voteRanks:
        for key, value in colorDic.items():
            if(rankedValue == value):
                colorRank.append(key)
    return colorRank

#create_color_score_dict
#parameters: Dictionary
#returns: Dictionary of colors, where instead of a tuple with raw counts there is a score based on votes received
def create_color_score_dict(colorDic):
    scoreDict = {}
    for color, votes in colorDic.items():
        scoreDict[color] = (votes[0]*3 + votes[1]*2 + votes[2]) 
    return scoreDict

#Prints the dictionary in sorted order (use sorted function). Print each entry on a separate line in the following format: key:value
def print_dictionary(colorDic):
    keys = sorted(colorDic)
    for key in keys:
        print(key, ": ", colorDic[key], sep = '')
    return

#test driver code
colorDic = (process_file(sys.argv[1])) #1 & 2
print_dictionary(colorDic) #3
blue = get_first_place_votes(colorDic, "blue") #4
print(blue) #5
green = get_first_place_votes(colorDic, "green") #6
print(green) #7
rankings = create_favorite_color_list(colorDic) #8
print(rankings) #9
scoreDict = create_color_score_dict(colorDic) #10
print_dictionary(scoreDict) #11
