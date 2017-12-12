# Functional specification

## Problem Statements
The project is designed to predict revenue/profit of movies for users who could be theater owner to set the screens in advance or professionals in media field who want to find some business insights from movies.

## User profile
The computational environments the user should be familiar with are listed as:
* iPython Notebook
* GUI

## Elements of the problem statement
* Access movie information data through OMDB API and TMDB API and joint data
* Data analysis and visualization
* Predict movie revenue via regression model and compare the prediction results with real boxoffice
* Construct web UI which contains the two sections: previous prediction results section and a section where users can get the predicted boxoffice of a movie they provided

## Use Case
* First section of web shows the prediction results from our dataset(i.e.prediction performance, visulization, accuracy and error analysis)
* In second section, user can provide the attritubes of the movie(genre, director, releasing date etc.) for regression model generated from training dataset to predict the boxoffice
