# Title: Data On The Field
# Authors: 
Joshua Krone,
Pranjal Adhikari

# Project Description 
In this project we are going to collect data of all tracked NFL games. We will then allow the score of all games to be seen based on the date inputted by the user. This will allow the user to go into any game they want that day and see the stats of that game. This includes player stats and team stats. This will create a NFL stat archieve which can be useful for football fans and fantasy football fans.
# Project Outline 
1. Interface plan: For the interface we will have an interactable input area where you can type in a valid date. This will then open the list of games that day. The games will be clickable which will take you further into that game and show the stats
2. Data Collection and Storage Plan: We will utilize the API of ESPN Scoreboard ('/sports/football/nfl/scoreboard?dates=YYYYMMDD') which is public and free and store them in a CSV, we will be getting the statistics of the game including the score, fouls and more.
3. Data Analysis and Visualization Plan: For data analysis all of the game scores will be shown based on the date. When a certain game is clicked it will list the team stats and a list of the player stats. We plan on using graphs to showcase some of the stats so they can be compared to the other team or other players
