from statsmodels.tsa.stattools import adfuller 
import matplotlib.pyplot as plt
import pandas as pd

# Function to plot chicago zipcodes price over time
def price_over_time(data, y_lim_min=75_000, y_lim_max=1_500_000):
    # Plot Data
    ax = data.plot(figsize=(14,8), linewidth=2, fontsize=14)

    # Set y limit
    ax.set(ylim=(y_lim_min,y_lim_max))
    
    # Plot title and axis labels
    title = "Chicago Zipcodes' House Prices between {} and {}".format(y_lim_min, y_lim_max)
    ax.set(xlabel='Year', ylabel='Price (USD)', title=title )

    # Remove legend
    ax.legend().remove()
    
    
# Function to help us check whether a zipcode's price is stationary over time
def stationarity_check(TS, column, plot_std=True):
    '''Outputs a plot of the Rolling Mean and Standard Deviation and prints results of the Dickey-Fuller Test
      TS: Time Series, this is the dataframe from which you are pulling your information
      column: This is the column within the TS that you are interested in
      plot_std: optional to plot the standard deviation or not'''
    
    # Calculate rolling statistics
    rolmean = TS[column].rolling(window = 8, center = False).mean()
    rolstd = TS[column].rolling(window = 8, center = False).std()
    
    # Perform the Dickey Fuller Test
    dftest = adfuller(TS[column].dropna())
    
    # Formatting
    fig = plt.figure(figsize=(14,8))
    
    #Plot rolling statistics:
    orig = plt.plot(TS[column], color='blue',label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
        # Optional plot of standard deviation
    if plot_std:
        std = plt.plot(rolstd, color='black', label = 'Rolling Std')
        plt.title('Rolling Mean & Standard Deviation for {}'.format(column)) # alternative title
    else:
        plt.title('Rolling Mean for {}'.format(column)) # alternative title
    
    # Legend and show
    plt.legend(loc='best')
    plt.show(block=False)
    
    # Print Dickey-Fuller test results
    print ('Results of Dickey-Fuller Test:')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value {}'.format(key)] = value
    print (dfoutput)
    

    
def ACF_PACF(TS, lags=30):
    for column in list(TS.columns):
        # Put column's heading in top left
        print('\nACF & PACF for {}'.format(column))
        
        # Plot
        plt.figure(figsize=(20,6));
            # Plot ACF
        plot_acf(TS[column].dropna(), lags=lags);
        plt.title('Auto-correlation Function for {}'.format(column));
        plt.xlabel('Lag');
        plt.ylabel('Auto-correlation');
        plt.show();
            # Plot PACF
        plot_pacf(TS[column].dropna(), lags=lags);
        plt.title('Partial Auto-correlation Function for {}'.format(column));
        plt.xlabel('Lag');
        plt.ylabel('Auto-correlation');
        plt.show();
        
        # Divide up each column's pair of plots
        print('__________________________________________________________________________________')
        
def plot_timeseries_model(data,column,res):
    '''Function will plot the original data, alongside any data for validation and prediction
    
       data: dataframe to be used
       column: the column to be plotted in your dataframe
       res: results
       '''
    
    # Model in Validation Period
    column = column # zipcode column to be put in (string or integer format, depending on how you've referenced before)
    data = data

    # Set the x axis/timeline (in months)
    # (2013-01) till (2017-10) is 57 months (inclusive)
    date_start = 57 # this is number of months since the start of data to start of validation period
    date_end = 63   # this is the number of months since the start of data to end of validation period

    # Produce a new column with the forecast for 2017-11 to 2018-04 (validation period)
    data['{}_forecast'.format(column)] = res.predict(start=date_start, end=date_end, dynamic=False)

    # Plot this new forecasted column with the original data column
    ax = data[[column, '{}_forecast'.format(column)]]
        # figsize
    ax.plot(figsize=(16,12))
        # Title and Axis
    date_start_year = data.index[date_start].year
    date_start_month = data.index[date_start].month
    date_end_year = data.index[date_end].year
    date_end_month = data.index[date_end].month
    
    # Chart formatting
    ax.set(title="Median House Price in Chicago's {} Zipcode\n Between {}-{} and {}-{}".format(column[0],
                data[date_start_year], data[date_start_month], data[date_end_year], data[date_end_month]),
                xlabel='Date', ylabel='House Price in Dollars (USD)')
    