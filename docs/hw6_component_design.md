# Component Design


## Component list. 
- Get movie revenue and information and combine them
- Conduct missing value imputation, extract features
- Visualize features
- Built regression models, perform analsis and compare models
- Deploy analysis result to WebUI
- ...

## Component specifications. 
### Data collection
- Name: 
  get_revenue(), info_data(), combine()
- What it does: 
  This component is used to send requests to web API to collect the metadata. 
- Inputs: 
  get_revenue: API key of TMDB, Pages go through when movie is sorted by popularity. Info_data: movie_id list, the list contains all the movie with their IMDB id. combine: `.csv` files
- Outputs: 
  get_revenue: `.csv` file contain movie id, corresponding budget and revenue. Info_data: `.csv` file contain the other infomations of the movie collected (Actor, Director, Rating, Votes, Release date, etc.). combine: Combined `.csv` file
- How it works:
  First function in the component calls the API of TMDB to get the movie id, the budget and revenue of the most popular movies for the last decade. Info_data uses the movie id collected to collect the other infomations from OMDB API. combine function joints two dataset using the key column: movie id.

### Conduct Data Cleaning
- Name:
  clean_data() 
- What it does:  
  Clean the initial raw data. Categorize several multilevel variables into a more obvious formation that will work better in the model. Remove or compensate the missing value with average value based on different data types. 
- Inputs:   
  Actors(string|Categorical variable), Country(String|Categorical variable), Director(String|Categorical variable), Genre(String|Categorical variable), Language(Integer|Continuous variable), Production(String|Categorical variable), Released(Integer|Continuous variables)
- Outputs:   
  Dataframe of cleaned data that is ready to build the model and do the data visualization.
- How it works:   
  Extract the month of "Released date" and categorize it into "quarter" variable.   
  Form a new column to decide whether it is the weekdays/weekends based on "Released data".    
  Sort out the famous "Director" and rate it.    
  Categorize "Genre" into 10 main kinds of movies and design an algorithm to sort it.    
  Clean the variable "Production" in case of duplicate factors.     
  Deal with the missing value. If the NA appears in categorical data, remove it. Else, use the average value to compensate it.     

### Build Regression Models
- Name:
  reg_model(), tree_model(), compare_model()
- What it does:
  Build several models and compare models 
- Inputs:
  The models will take columns "profit, actors, director, genre, rating, votes, num_languages, production, month, day_of_week, runtime and year" from the DataFrame "combine_data" as input. The data will be split into training and testing sets and the functions each take the two sets of data as input. 
- Outputs:
  The functions will return an array of estimated coefficients and the model fit.
- How it works:
  To implement regression models, we will use the python class imported from the Scikit-learn package ---  sklearn.linear_model.In this component, we will use dvarious functions/algorithms, including OLS, Ridge and LASSO regression to build predictive models for movie profits. And we will compare among the models.In the future, if a user input information of a movie , our model will give an estimated profit for this movie.
  
### Web UI
- Name:
get_movie_prediciton()
show_analysis()
- What it does:
Taking user inputs and parsing them using Python HTMLParser library and feed into according variables in predictive model.
UI will show static image of the team's analysis of movie trends.
- Inputs:
To call prediciton:
On the html based platform user will input in text or numbers format for:
"Top 3 Actors", "Director", "Genre", "num_languages", "Production", "Release Month", "Release day_of_week", "runtime and year" and "Rating"
To call analysis:
Simply click on "show analysis"
- Outputs:
Predicted voting (popularity) and revnue
Static image of the team's analysis of movie trends.
- How it works:
The UI is a simply web based form that users can input their assumed movie information and get a predicted revenue. The platform will take the information, send to HTMLParser (the team will build this function using this library), and feed intot eh predictive model mentioned above.
UI will show static image of the team's analysis of movie trends.
