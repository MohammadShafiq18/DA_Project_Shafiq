#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: <Mohammad Shafiq>
#Group Name: <PYTHON_OKAY>
#Class: <PN2004K>
#Date: <16/2/2021>
#Version: <V2>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#import matplotlib for pie chart
import matplotlib.pyplot as plt
#count of each of the elements present in the container
from collections import Counter
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
    df = pd.read_csv('MonthyVisitors.csv')
    #df = df.iloc[a:b, c:d]
    #get excel data (CSV format) to dataframe
    #a = year starting year -2
    #b = month ending year - 2
    #c = starting country
    #d = ending country
    df = df.iloc[204:336 ,20:31]

    print(df)

    #input variables
    country_list = []
    visitor_list = []
    total_visitor = []


    #Specifying which colunmn to iterate
    for i in df.columns[0:11]:
      country_list.append(i)
      for x in df[i]:
        visitor_list.append(x)
    for x in range(0,len(visitor_list)):
      #converting the na to 0 string interger for addition
      if x ==" na ":
        visitor_list[x]=0
      else:
        visitor_list[x]=int(visitor_list[x])
    c = (len(visitor_list))/(len(country_list))
    i1=0
    i2= int(c)
    #Adding total for one country and appending it to total_visitor list
    for i in range(0,len(country_list)):
      total_visitor.append(sum(visitor_list[i1:i2]))
      i1 = i1 +int(c)
      i2 = i2 +int(c)
    Country_Visitor_dict = { country_list[i]: total_visitor[i] for i in range(len(country_list))}
    #sort dictionary in descending order
    sort_Country_Visitor_dict = sorted(Country_Visitor_dict.items(), key=lambda x: x[1], reverse=True)
    #convert list to dictionary
    Country_Visitor_dict  = dict(sort_Country_Visitor_dict)
    #counter = number of visitor in the country
    k =Counter(Country_Visitor_dict)
    #highest visitors
    Top_3_Visitors = k.most_common(3)
    
    #Get from dataframe to get top Visitors
    df = pd.DataFrame(Top_3_Visitors,columns = ["Country","Travellers"])
    #print the data table in descending order
    print(df)


    #Initialize lists
    labels = []
    sizes = []
    #get data from Excel for countries
    for x in df["Country"]:
      labels.append(x)
    for y in df["Travellers"]:
      sizes.append(y)
    #initialize list and variable
    distance = 0.1
    seperate = []
    #Add the variable distance into the  separate list 3 times
    for i in range(0, len(df['Travellers'])):
      seperate.append(distance)
    #To create pie chart
    plt.pie(sizes,labels=labels, explode=seperate, startangle=90, autopct='%1.2f%%',shadow=True)
    plt.axis('equal')

    plt.legend(loc="best")
    #show pie chart
    plt.show()


#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

    #print number of rows in dataframe
    print("There are " + str(len(df)) + " data rows read. \n")

    #display dataframe (rows and columns)
    print("The following dataframe are read as follows: \n")
    print(df)

    #display a specific country (Australia) in column #33
    country_label = df.columns[33]
    print("\n\n" + country_label + "was selected.")

    #display a sorted dataframe based on selected country
    print(" The" + country_label + "was sorted in ascending order. \n")
    sorted_df =df.sort_values(country_label,ascending=[0])
    print(sorted_df)

    
    
    


    return
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################