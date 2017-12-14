# Component Design

## Component list
**1. Collect Data:** Collect movie revenue, other information and combine them
**2. Clean Data:** Conduct missing value imputation, filter features and transfer some features to specific format
**3. Visulization:** Visulize the correlations between features and revenue
**4. Build models:** Build regression models and results difference
**5. User Interface:** User interface for normal users and researchers to interact with package

## Component specifications
### Collect Data
* Functions: `get_tmdb_id_list,get_profit,get_info,call_data`
* What it does:
	This component is used to send requests to different web API to collect the metadatas, and combine them into a raw dataset(`.csv`)
* How it works:
	* First function`get_tmdb_id` is used to collect the tmdb list of the most popular movies in a given time period.
	* `get_profit` uses the tmdb list generated from `get_tmdb_id_list` to extract the budget and revenue information of the movie in the list one by one.
	* `get_info` collects the other information (including release date, actors, rating, imdb voting...) og the movie in the list.
	* `call_data` works as a combination of the functions listed above and combine all th data together to generate a `.csv` file as raw data.
* Inputs:
	* get_tmdb_id_list: time range,page range for each year
	* get_profit: tmdb id list
	* get_info: imdb id list
	* call_data: time range,page range for each year,file path
* Ouputs:
	* get_tmdb_id_list: dataframe of tmdb id list
	* get_profit: dataframe contains tmdb movie id list, their budget and profit
	* get_info: dataframe contains tmdb movie id list, other information
	* call_data: `.csv` file contains all the raw data

### Clean Data
* Functions: `clean_director_actor,clean_regression_data`
* What it does:  
	Clean the raw data from previous component. Categorize several multilevel variables into a more obvious formation that will work better in the model. Remove or compensate the missing value with average value based on different data types. 
* How it works:
	* `clean_director_actor` gets the average popularity of leading actors and director and merge them into dataframe
	* `clean_regression_data` cleans and categorizes other information such as inserting a new column to present whether movie is released on weekend based on "Released date", categorizing "Genre" into 13 main kinds of movies, cleaning the variable "Production" in case of duplicate factors, etc.
* Inputs:
	* `.csv` file as raw dataset from Collect data component
* Outputs:
	* `.csv` file as analysis ready dataset

### Visulization
* Functions: `scatter_plot,box_plot`
* What it does:
	* Draw the plots for two continus variables and the plot of revenue versus features in the movie
* How it works:
	* `scatter_plot` draws a scatter plot for two continuous variables in the movie data
	* `box_plot`draws a boxplot plot revenue versus categorical in the movie data
* Inputs:
	* directory path of data file
* Outputs:
	* Plots

### Build Regression Models
* Functions: `model_evaluation,save_model`
* What it does:
      Using machine learning methods to build several models, make comparisons and save the models. 
* How it works:
      * Model_evaluation function is to run different types of models, i.e. linear regression, tree model, ridge, lasso model. Using k-fold cross validation to calculate. Compare the error and the accuracy of models between different methods. 
      * Save_model function is to save regression models to local machine as .pkl files.
* Inputs:
      * model_evaluation: model_name (linaer, ridge, lasso), dataset, number of fold for cross validation
      * save_model: model_name, file_name, path
* Outputs:
      * model_evaluation: established prediction model 
      * saved model as `.pkl` file

### User Interface
* File: `user_interface.py`
* What it does:
	* User in this system, user can predict the revenue of a movie with customized parameters. Researchers can check more details using our modules and even build their own prediction models.
* How it works:
	* The user interface is built using python lib `tkinter` which can take user's actions and inputs. Present estimated revenue for normal users. Launch jupyter notebook for researcher use.  
* Inputs:
	* Values of features 
* Outputs:
	* Estimated revenue
	* Jupyter notebook for demonstration of functions