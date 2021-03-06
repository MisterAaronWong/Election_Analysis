# Election_Analysis (Module 3.6.5)

## Project Overview
The Colorado Board of Education requested an election audit of a recent local congressional election. The data analyzed included: the candidates involved that received votes, the total number of votes casted, the number/percentage of votes each candidate received, and the winner of the election based on the popular vote. 

## Resources
-Data Source: election_results.csv

-Software: Python 3.9.6, Visual Studio Code 1.61.2

## Summary
The analysis of the elction show that:

-There were 369,711 total votes cast in the election.

-The candidates were:
  * Charles Casper Stockham
  * Diana DeGette
  * Raymon Anthony Doane

-The candidate results were:
  
  * Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  
  * Diana DeGette received 73.8% of the vote and 272,692 number of votes.
  
  * Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.

-The winner of the election was:
  
  * Diana DeGette who received 73.8% of the vote and 272,692 number of votes.

# Election Audit (Module 3 Challenge, Deliverable 3)

## Overview of Election Audit
The purpose of this election audit was to analyze the results of a recent local election in Colorado and report these results to the election commission. The relevant information in the data that was analyzed include: the names of the candidates, the number of votes each candidate received, the percentage of votes each candidate received, the total number of votes, and the winner of the election. Additionally, the coter turnout for each county, the percentage of votes received from each county of the total votes, and the county with the highest turnout was analyzed and determined. To obtain these results, a python script was created and run.

## Election-Audit Results
To perform the analysis to produce both the county vote results along with the candidate vote results, the following code was run:
![mod3code image](Resources/mod3code.png)

The analysis resulted in the following outcomes:

-Total Votes in the Congressional Election: 369,711

-County Breakdown:
  
  * Jefferson County: 38,855 votes casted _(10.5% of the total votes casted)_ 
  
  * Denver County: 306,055 votes casted _(82.8% of the total votes casted)_

  * Arapahoe County: 24,801 votes casted _(6.7% of the total votes casted)_

 Denver County had the largest number of votes.
 
 -Candidate Breakdown:
  * Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  
  * Diana DeGette received 73.8% of the vote and 272,692 number of votes.
  
  * Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
  
 Diana DeGette won the election with 272,692 number of votes, receiving 73.8% of the vote.
 
 See below for a clearer view of the results presented in the terminal when the code is run:
 ![txtfileimage](Resources/txtfilewrite.png)

## Election-Audit Summary
The python script used for this election audit is very useful and could be reused with slight modifcations for other future elections as well. The existing code can be recycled and reused as long as the csv file that contains all the data is similar to the csv file used for this audit. If the csv has slight differences to the location of the data in the dataset, then the code would simply need to be modified to index to the correct column or row. If there are additional candidates and counties to consider in the future, this can easily be conducted with a similar code as long as the code properly references the data from the dataset.

One example of a modication that can be made is that if there are additional factors in the election data to consider. For instance, mail-in ballots, votes that were phsyically casted at a voting station, gender of voter, age of voter, etc. and their respective data. Another modification that could be made is to go in even further depth and analyze the county vote turnout for each specific candidate. For instance, how many votes Diana DeGette received from each county and the percentage. This would require a bit more modication to the code.
