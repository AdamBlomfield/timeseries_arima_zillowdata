# Import and filter data
import pandas as pd
from statsmodels.tsa.stattools import adfuller 
import numpy as np
import matplotlib.pyplot as plt


def detrend_test(TS, alpha=0.05, maxlag=4, suppress_output=False):
    '''Selecting the best method for detrending timeseries based on lowest p-value of the augmented Dickey-Fuller.
       TS: timeseries dataframe
       alpha: alpha value for Dickey-Fuller '''
    
    new_TS = pd.DataFrame()
    
    plist = []  
    plist_zips = []
    
    # Keep track of which zipcodes require a log 1st difference transformation
    log_1diff = []
    
    for column in list(TS.columns):  #go through each zipcode in the DF
        p_values = []
        
        # First Difference
            # find the first difference for each row in the zipcode
        data_1diff = TS[column].diff(periods=1) 
            # perform Dickey Fuller test on first difference
        dftest = adfuller(data_1diff.dropna(),maxlag=maxlag)
            # Place first 4 outputs of the Dickey Fuller test in a dataframe and label the outputs appropriately in the index
        dfoutput_1diff = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
        for key, value in dftest[4].items():
            dfoutput_1diff['Critical Values {}'.format(key)] = value
            # Add p-value of first difference Dickey-Fuller p-value list
        p_values.append(dfoutput_1diff[1])
    
        # Log First Difference
            # find the log first difference for each row in the zipcode
        data_log_1diff = TS[column].apply(lambda x: np.log(x)) - TS[column].apply(lambda x: np.log(x)).shift(1)
            # perform Dickey Fuller test on first difference
        dftest = adfuller(data_log_1diff.dropna(),maxlag=maxlag)
            # Take first 4 outputs of the Dickey Fuller test and label the outputs appropriately
        dfoutput_log_1diff = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
        for key, value in dftest[4].items():
            dfoutput_log_1diff['Critical Values {}'.format(key)] = value
            # Add p-value of log first difference Dickey-Fuller p-value list
        p_values.append(dfoutput_log_1diff[1])

        # If first difference performed better, print the Dickey-Fuller results and plot
        if np.argmin(p_values)==0:
            data_1diff.plot(figsize=(20,6))
            plt.title('{} First Difference'.format(column))
            plt.show();
            print(dfoutput_1diff)
            new_TS[column]=data_1diff
        
        # If log first difference performed better, print the Dickey-Fuller results and plot
        elif np.argmin(p_values)==1:
            log_1diff.append(column)
            data_log_1diff.plot(figsize=(20,6))
            plt.title('{} Log First Difference'.format(column))
            plt.show();
            print(dfoutput_log_1diff)
            new_TS[column]=data_log_1diff
        
        # Add the smallest p value from tests, to the plist
        plist.append(min(p_values))
        # Add zipcodes with high p-values to plist_zips
        if min(p_values)>alpha:
            plist_zips.append(column)
    
    
    if suppress_output==False:
        print('\nNumber of p-values above alpha of {}:'.format(alpha),(np.array(plist)>alpha).sum())
        print('\nZipcodes with p-values above alpha of {}'.format(alpha), plist_zips)
        print('\nZipcodes requiring log first difference transformation: {}'.format(log_1diff))
        return new_TS, log_1diff