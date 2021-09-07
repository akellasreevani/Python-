# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 17:39:47 2021

@author: Sreevani
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cars_data = pd.read_csv('Toyota.csv',index_col=0,
                        na_values=["??","????"])

cars_data.dropna(axis=0,inplace=True)

# =============================================================================
# Scatter Plot
#-----------------
# Price vs Age
sns .set(style= "darkgrid")
sns.regplot(x=cars_data['Age'], y=cars_data['Price'])
# by default, fit_reg = True 
# It estimates and plots a regression model relating the x and y variables
# =============================================================================

#Scatter Plot  of Price vs Age without the regression fit line 
sns.regplot(x=cars_data['Age'],
            y=cars_data['Price'],
            fit_reg=False)

#Scatter plot of Price vs Age by customizing the appearence of markers
sns.regplot(x=cars_data['Age'],
            y=cars_data['Price'],
            marker="*",
            fit_reg=False)

# =============================================================================
# Scatter plot of Price vs Age by FuelType
# -----------------------------------------
# > Using hue parameter, including another variable to show the fuel type
# categories with different colours
# =============================================================================
sns.lmplot(x='Age', y='Price',data=cars_data,
           fit_reg=False, hue='FuelType',
           legend=True, palette="Set1")


# =============================================================================
# Histogram
# ---------
# Histogram with default kernel density estimate
sns.distplot(cars_data['Age'])
#Histogram without default kernel density estimate
sns.distplot(cars_data['Age'],kde=False)
#Histogram with fixed no of bins
sns.distplot(cars_data['Age'],kde =False, bins=5)
# =============================================================================

# =============================================================================
# #Bar Plot
#  --------
# Frequency distribution of fuel types of the cars
sns.countplot(x="FuelType",data=cars_data)
# #Grouped bar plot
#  ----------------
# >Grouped bar plot of FuelType and Automatic
sns.countplot(x="FuelType", data=cars_data,hue="Automatic")
# =============================================================================

# =============================================================================
# Box and wishkers plot - numerical variable
# >Box and whiskers plot of Price to visually intrepret the five-number summary
sns.boxplot(y=cars_data['Price'])
# >Box and whiskers plot for numerical vs categorical variable 
# >Price of the cars for various fuel types
sns.boxplot(x=cars_data['FuelType'], y=cars_data['Price'])
#  Grouped box and whiskers plot
#   -----------------------------
# Grouped box and whiskers plot of price vs FuelType and Automatic
sns.boxplot(x='FuelType', y='Price',
            hue = "Automatic", data = cars_data)
# =============================================================================


# =============================================================================
# Box-whiskers plot and Histogram
#  >Lets plot box-whiskers plot and histogram on the same window
#  >split the plotting window into 2 parts
f,(ax_box, ax_hist) = plt.subplots(2,gridspec_kw ={"height_ratios":(.15,.85)})
# now add create two plots
sns.boxplot(cars_data['Price'], ax=ax_box)

sns.distplot(cars_data['Price'], ax=ax_hist, kde=False)

# =============================================================================
 
# =============================================================================
# Pairwise plots
#  >It is used to plot pairwise relationships in a dataset
#  >Creates scatterplots for joint relationships and histograms for univariate distributions
#  
sns.pairplot(cars_data, kind="scatter", hue="FuelType")
plt.show()
# =============================================================================









