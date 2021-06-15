# Julia Cuellar
# DSC 630
# Final project

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols


# Display quake data
def read_file():
    quake = pd.read_csv('quakes.csv')
    quake.rename(columns={'Unnamed: 0': 'num'}, inplace=True)
    quake.drop(['num'], axis=1, inplace=True)
    print('Data:\n', quake)


# Display described and length of quake data
def des_len():
    quake = pd.read_csv('quakes.csv')
    quake.rename(columns={'Unnamed: 0': 'num'}, inplace=True)
    quake.drop(['num'], axis=1, inplace=True)
    print('Described quake data:\n', quake.describe())
    print('Length of quake data:\n', len(quake))


# Check the nulls from quake file
def check_null():
    quake = pd.read_csv('quakes.csv')
    quake.rename(columns={'Unnamed: 0': 'num'}, inplace=True)
    quake.drop(['num'], axis=1, inplace=True)
    print("Display quake data with null:\n", quake.isnull())
    print("Display counts of null from quake data:\n", quake.isnull().sum())


# Display pair plot of quake data
def showPair_Quake():
    quake = pd.read_csv('quakes.csv')
    quake.rename(columns={'Unnamed: 0': 'num'}, inplace=True)
    quake.drop(['num'], axis=1, inplace=True)
    sns.pairplot(quake)
    plt.suptitle('Pair plot of quakes')
    plt.show()


# Display boxplot of latitude
def showBox_Lat():
    quake = pd.read_csv('quakes.csv')
    quake.rename(columns={'Unnamed: 0': 'num'}, inplace=True)
    quake.drop(['num'], axis=1, inplace=True)
    sns.boxplot(x="lat", data=quake)
    plt.title('Latitude')
    plt.show()


# Display boxplot of longitude
def showBox_Long():
    quake = pd.read_csv('quakes.csv')
    quake.rename(columns={'Unnamed: 0': 'num'}, inplace=True)
    quake.drop(['num'], axis=1, inplace=True)
    sns.boxplot(x="long", data=quake)
    plt.title('Longitude')
    plt.show()


# Display boxplot of depth
def showBox_Depth():
    quake = pd.read_csv('quakes.csv')
    quake.rename(columns={'Unnamed: 0': 'num'}, inplace=True)
    quake.drop(['num'], axis=1, inplace=True)
    sns.boxplot(x="depth", data=quake)
    plt.title('Depth')
    plt.show()


# Display boxplot of mag
def showBox_Mag():
    quake = pd.read_csv('quakes.csv')
    quake.rename(columns={'Unnamed: 0': 'num'}, inplace=True)
    quake.drop(['num'], axis=1, inplace=True)
    sns.boxplot(x="mag", data=quake)
    plt.title('Magnitude')
    plt.show()


# Display boxplot of stations
def showBox_Station():
    quake = pd.read_csv('quakes.csv')
    quake.rename(columns={'Unnamed: 0': 'num'}, inplace=True)
    quake.drop(['num'], axis=1, inplace=True)
    sns.boxplot(x="stations", data=quake)
    plt.title('Stations')
    plt.show()


# Create a multiple linear regression model for latitude versus longitude
def reg_model_l():
    quake = pd.read_csv('quakes.csv')
    quake.rename(columns={'Unnamed: 0': 'num'}, inplace=True)
    quake.drop(['num'], axis=1, inplace=True)
    fit = ols('lat ~ C(long)', data=quake).fit()
    print("Multiple linear regression model for latitude versus longitude:\n", fit.summary())
    res = fit.resid
    fig = sm.qqplot(res, fit=True, line="45")
    plt.title('Latitude & Longitude of an Earthquake')
    plt.show()


if __name__ == "__main__":
    read_file()
    des_len()
    check_null()
    showPair_Quake()
    showBox_Lat()
    showBox_Long()
    showBox_Depth()
    showBox_Mag()
    showBox_Station()
    reg_model_l()