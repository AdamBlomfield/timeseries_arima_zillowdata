# mod_4_project
==============================
## Project Description
------------
The project seeks to discover the 5 best zipcodes to invest in, in the Chicago area. 5 potential definitions were used for "best" to cater for different styles of investors. Historic Chicago house price data was used to build a time series model and predict where house prices would be at a future date.

Prediction intervals were made for 6 months and 12 months into the future.
House prices for each zipcode in Chicago were taken from Zillow's database and were calculated as the median price of two-bedroom homes for each month from April 1996 to April 2018.  
ARIMA model used to predict future house prices

Model's Prediction of House Price:

![alt text](https://github.com/AdamBlomfield/mod_4_project/tree/master/reports/figures/prediction_chart.png "Chart to show our prediction of house price")

## Project Organization
------------
The directory structure for this projects is below. Brief descriptions follow the diagram.

```
mod_4_project
├── LICENSE
│
├── Makefile  : Makefile with commands to perform selected tasks, e.g. `make clean_data`
│
├── README.md : Project README file containing description provided for project.
│
├── .env      : file to hold environment variables (see below for instructions)
│
├── test_environment.py
│
├── data
│   ├── processed : directory to hold interim and final versions of processed data.
│   └── raw : holds original data. This data should be read only.
│
├── models  : holds binary, json (among other formats) of initial, trained models.
│
├── notebooks : holds notebooks for eda, model, and evaluation. Use naming convention yourInitials_projectName_useCase.ipynb
│
├── references : data dictionaries, user notes project, external references.
│
├── reports : interim and final reports, slides for presentations, accompanying visualizations.
│   └── figures
│
├── requirements.txt
│
├── setup.py
│
├── src : local python scripts. Pre-supplied code stubs include clean_data, model and visualize.
    ├── __make_data__.py
    ├── __settings__.py
    ├── clean_data.py
    ├── custom.py
    ├── model.py
    └── visualize.py

```

## Next steps
---------------
### Use with github
As part of the project creation process a local git repository is initialized and committed. If you want to store the repo on github perform the following steps:

1. Create a an empty repository (no License or README) on github with the name mod_4_project.git.
2. Push the local repo to github. From within the root directory of your local project execute the following:

```
  git remote add origin https://github.com/(Your Github UserName Here)/mod_4_project.git
  git push -u origin master
```

3. Create a branch with (replace ```branch_name``` with whatever you want to call your branch):
```
  git branch branch_name
```
4. Checkout the branch:
```
  git checkout branch_name
```

If you are working with a group do not share jupyter notebooks. The other members of the group should pull from the master repository, create and checkout their own branch, then create separate notebooks within the notebook directories (e.g., copy and rename the original files). Be sure to follow the naming convention. All subsequent work done on the project should be done in the respective branches.


### Environment Variables
-------------------
The template includes a file ```.env``` which is used to hold values that shouldn't be shared on github, for example an apikey to be used with an online api or other client credentials. The notebooks make these items accessible locally, but will not retain them in the online github repository. You must install ```python-dotenv``` to access this functionality. You can install it stand alone as follows:

```
  pip install -U python-dotenv
```
Or you can install all required packages with the instructions given in the next section.

#### Accessing Environment Variables in Jupyter Notebook
-------------
Notebook access to the constants and variables stored in the ```.env``` file is described here. In a code cell the line (e.g. assume you have a variable named ```APIKEY = 'Your_APIKEY'``` in the  ```.env``` file)
```
  mykey = %env APIKEY`  
```
will place the value ```'Your_APIKEY'``` into ```mykey```

### Installing development requirements
------------
If your current environment does not meet requirements for using this template execute the following:
```
  pip install -r requirements.txt
```


## Explanation of the Tests
-------------
ARIMA (Auto Regressive Integrated Moving Average):
simple stochastic time series model that is trained on data (by regressing a variable based on historic values of that variable) and then will forecast data for future time points. Complex relationships between different time points can be captured by ARIMA as it factors in values of lagged terms as well as error terms.

## Limitations & Assumptions
Based on the resources and data available a time series model was used, rather than an explanatory model. The focus of the project was to predict what will happen to price, not to know why a change happens.
Our time series model extrapolated trends and seasonal patterns in the historic data for median house prices in order to predict future prices.  The assumption here is that future prices will be influenced by past statistical properties.  
Our predictions are not based off of exogenous influential factors, such as a large change in housing demand due to a large corporation moving its HQ to Chicago. To mitigate this potential impact on price, we have included an "error" term with our model.
Our model did not include Zipcodes of 60619 and 60649 as we were unable to render their trends to approximately stationary through mathematical transformations.  

## Built with
-------------
[Zillow Housing Data](https://www.zillow.com/research/data/)

## Team
-------------
Filis Coba
Dr. Ryan Miller
Adam Blomfield
