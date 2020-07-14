#!/usr/bin/python2.7

import argparse
import sys
import numpy as np
import itertools

# The goal of this script is to take in the files that have the list of choices made by Alex, Ben, and Chris in their 50 games of rock, paper, scissors, 
# calculate the probabilities of choosing each option for each player, and simulating 1000 matchups between each pair of competitors. Your output file 
# should be a comma delimited file (csv) of each matchup and the win-loss-draw percentages for each. We expect the following:

# Alex,Ben,% Alex wins,% Ben wins,% draws
# Alex,Chris,% Alex wins,% Chris wins,% draws
# Chris,Ben,% Chris wins,% Ben wins,% draws


# We have provided you the input files for Alex, Chris, and Ben. You should download them from the the python bootcamp git account using the command line wget command.
# The files are stored in the github repository: python_bootcamp_2020/HW_files/HW_week_2/

# You should read in each file using the argparse module as shown in class. While many methods of reading in options exist, for consistency's sake and ease of grading, 
# we expect the following flags:

# -a <Alex's choices>
# -b <Ben's choices>
# -c <Chris's choices>
# -o <output file>

# The player choices are in the form of a string for each round of "R", "P", or "S" (rock, paper, or scissors) separated by "\n"

# Note ideally the script would be more dynamic, e.g wouldn't explicitly require three different players but could instead handle variable numbers of players and do the simulated
# matchups accordingly. However, just to start, we are constraining the script to accept exactly three players. Feel free to try making it more generalizable if interested! We're happy
# to take a look either way

# at the very least you will need to import argparse to complete this assignment. Other libraries that might be useful (and are used in one possible solution) include
# itertools, numpy, scipy, and sys . Specifically I'd look into itertools.combination to get all the different possible matchups. While it's easy to code all possible
# combinations with just three players, the # of matchups get out of hand pretty quickly with more comparisons. Therefore, for generalizability's sake, I'd recommend
# using a tool like itertools.combination

# This template gives you the functions with their inputs and outputs listed that are used in the solution. Note that there are many ways to solve this problem, but this
# should provide a logical framework around which you can craft your solution if you need help getting started



# main function around which the rest of your script should be organized
def main():
	
	# need to read in the options using argparse

	# need to determine each TAs probabilities for each choice (R, P, or S)

	# need to simulate all the possible TA matchups

	# need to write the output file


	pass


def simulate_matchup(ta_1_probabilities, ta_2_probabilities, num_simulations):
	'''This function takes in the probabilities for two TAs and the number of desired simulations and performs the simulated matches for a specific matchup

	Inputs
	------
	ta_1_probabilities: list or numpy array of floats
		probabilities for each possible choice (rock, paper, and scissors) for a specific TA
	ta_2_probabilities: list or numpy array of floats
		probabilities for each possible choice (rock, paper, and scissors) for a second TA
	num_simulations: int
		the number of simulations desired to be run for a given matchup

	Returns
	------
	win_probabilities: list or numpy array
		a list holding the probabilities for each possible outcome, e.g [fraction where ta_1 wins, fraction where ta_2 wins, fraction of draws]
	'''

	win_probabilities = [0, 0, 0]

	# your code goes here


	return win_probabilities


def get_ta_choice_probabilities(ta_choice_file):
	'''This function takes in the file listing the choices a particular TA made in RPS and calculates the probabilities for each choice

	Inputs
	------
	ta_choice_file: string
		path specifying a file holding return-delimited RPS decisions made by a TA. 
		This string should be an option given to the script on the command line and parsed by argparse

	Returns
	------
	ta_choice_probabilities: list or numpy array of floats
		a list holding the probabilities for each possible RPS decision for this TA, calculated from the input file, e.g [fraction of Rocks, fraction of Papers, fraction of Scissors]
	'''

	ta_choice_probabilities = [0, 0, 0]

	# your code goes here

	return ta_choice_probabilities


if __name__ == "__main__":
    main()