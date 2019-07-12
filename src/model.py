from statsmodels.tsa.arima_model import ARIMA
from datetime import datetime 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

def evaluate_arima_model(X, test, arima_order):
    '''Provides the Mean Squared Error for the train vs test
    arima_order = configuration of (p,d,q)'''
    # prepare training dataset
    history = [x for x in X]
    # make predictions
    predictions = []
    for t in range(len(test)):
        model = ARIMA(np.array(X.dropna()), order=arima_order)
        model_fit = model.fit(disp=0)
        yhat = model_fit.forecast()[0]
        predictions.append(yhat)
        history.append(test[t])
    # calculate out of sample error
    mse = mean_squared_error(test, predictions)
    return mse


def evaluate_models(train_column, test, p_values, d_values, q_values):
    best_pdq, best_score = None, float('inf')
    for p in p_values:
        for d in d_values:
            for q in q_values:
                arima_order = (p,d,q)
                try:
                    rmse = np.sqrt(evaluate_arima_model(train_column, test, arima_order))
                    if rmse < best_score:
                        best_pdq, best_score = arima_order, rmse
                except:
                    continue
    print('Best ARIMA {} RMSE= {}'.format(best_pdq, best_score))
    return best_pdq



def predict_arima_model(data, column, arima_order, periods):
    '''Output: Final predicted median price for zipcode, the zipcode's price growth in absolute terms as well as %, 
    the risk associated with the zipcode investment and finally a prediction chart to illustrate the 
    prediction intervals'''
    
    # Perform ARIMA model on the chosen Zipcode
    model = ARIMA(np.array(data[column].dropna()), order=arima_order)
    res = model.fit(disp=0)
    pred= res.forecast(steps=periods)
    
    from dateutil.relativedelta import relativedelta
    # Extend the date range of the dataframe
    start = datetime.strptime("2017-11-01", "%Y-%m-%d")
    date_list = [start + relativedelta(months=x) for x in range(0,periods)]
    future = pd.DataFrame(data=pred[0], index=date_list)
    complete= pd.concat([data[column], future])
    
    # plot the data, prediction and confidence intervals
        # Data
    plt.plot(data[column])
        # Prediction
    plt.plot(future, color='red', lw=5, ls='--')
        # Confidence Intervals
    lower = [pred[2][x][0] for x in range(len(pred[2]))]
    lower_bound = pd.DataFrame(data=lower, index=date_list)
    upper = [pred[2][x][1] for x in range(len(pred[2]))]
    upper_bound = pd.DataFrame(data=upper, index=date_list)
    plt.fill_between(upper_bound.index, upper, lower, color='r', alpha=.3)
    
    # Make the chart title and axis labels
    plt.xlabel('Time (years)')
    plt.ylim(np.min(data[column])-50000,np.max(data[column])+150000)
    plt.ylabel('Median Housing Price')
    plt.title('Median House Price Prediction for Zipcode {}'.format(column))
    plt.show();
    
    # Print out Final Price, Growth ($ and %) and the associated risk
    final_price = future[0][-1]
    growth_level = final_price - data[column][-1]
    growth_perc = ((final_price - data[column][-1])/data[column][-1])*100
    risk = ((upper[-1]-lower[-1])/lower[-1])*100
    print(' Final Predicted Price: ${}'.format(round(final_price),0),'\n',
          'Total Growth: ${}'.format(round(growth_level,0)),'\n',
          'Percentage Growth: {}%'.format(round(growth_perc,2)),'\n',
          'Risk: {}%'.format(round(risk,2)))
    return pred