# Component Design


## Component list. 
- Access movie id from TMDB and obtain revenue_df via OMDB API
- Get movie information_df through OMDB API
- Combine revenue_df and information_df and save as .csv
- Conduct missing value imputation
- Visualize features
- Extract features
- Built regression models
- Perform regression analysis and tune parameters on each model
- Compare regression models
- Deploy analysis result to WebUI
- ...

## Component specifications. 
- Name. This should be the name that you use in the component's implementation (e.g., the name of a python class or function).
- What it does. This should be a high level description of the roles of the component.
- Inputs. Be specific about the data types. For DataFrames, specify the column names and the types of the column values.
- Outputs. Same consideration as with inputs.
- How it works (ideally with pseudo code).

- Conduct Data Cleaning
  - Name  
    -DataCleaning.py 

  - What it does  
    -Clean the initial raw data. Categorize several multilevel variables into a more obvious formation that will work better in the model. Remove or compensate the missing value with average value based on different data types. 

  - Inputs.   
    -Actors(string|Categorical variable), Country(String|Categorical variable), Director(String|Categorical variable), Genre(String|Categorical variable), Language(Integer|Continuous variable), Production(String|Categorical variable), Released(Integer|Continuous variables)

  - Outputs.   
    -Dataframe of cleaned data that is ready to build the model and do the data visualization.

  - How it works (ideally with pseudo code).   
    -Extract the month of "Released date" and categorize it into "quarter" variable.   
    -Form a new column to decide whether it is the weekdays/weekends based on "Released data".    
    -Sort out the famous "Director" and rate it.    
    -Categorize "Genre" into 10 main kinds of movies and design an algorithm to sort it.    
    -Clean the variable "Production" in case of duplicate factors.     
    -Deal with the missing value. If the NA appears in categorical data, remove it. Else, use the average value to compensate it.     

Component 4: Regression Models
To implement regression models, we will use the python class imported from the Scikit-learn package ---  sklearn.linear_model.
In this component, we will use dvarious functions/algorithms, including OLS, Ridge and LASSO regression to build predictive models for movie profits. And we will compare among the models. 

The models will take columns "profit, actors, director, genre, rating, votes, num_languages, production, month, day_of_week, runtime and year" from the DataFrame "combine_data" as input. The data will be split into training and testing sets and the functions each take the two sets of data as input. The functions will return an array of estimated coefficients and the model fit.

In the future, if a user input information of a movie , our model will give an estimated profit for this movie.
