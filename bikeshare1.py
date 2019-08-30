#!/usr/bin/env python
# coding: utf-8

# In[4]:


import time
import datetime
import pandas as pd
import numpy as np

# import and read data from csv#
df1 = pd.read_csv('/Users/srav/Desktop/DataScience/chicago.csv')
df1.head

df2 = pd.read_csv('/Users/srav/Desktop/DataScience/new_york_city.csv')
df2.head

df3 = pd.read_csv('/Users/srav/Desktop/DataScience/washington.csv')
df3.head

display(df1.head, df2.head, df3.head)

df = pd.merge(df1,df2,df3)


# first define a variable for a city name and then define filters on the variable##

city_data= ['chicago', 'new_york_city', 'washington']

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
            city = input(" Enter city name: ")
            if city not in city_data:
                print(" Enter the correct City name: ")
            else:
                city = city.lower()
                break
                
    print(city)

    
    while True:
        month_name= ['january', 'febuary', 'march','april', 'may', 'june']
            month = str(input(" Enter month name: "))
            if month not in month_name:
                   print(" Enter the correct month name: ")
            
            else:
                month= month.lower()
                break       
    print(month)
    
    while True: 
        weekday = ['Monday','Tuesday','Wednesday', 'Thursday','Friday','Saturday','Sunday']
        if day not in weekday:
                print("Enter a valid day:")
        if day == 2:
            return "Monday"
        if day == 3:
            return "Tuesday"
        if day == 4:
            return "Wednesday"
        if day ==5:
            return "Thursday"
        if day == 6:
            return "Friday"
        if day ==7:
            return "Saturday"
        if day == 1:
            return "Sunday"
            break 
    else:
        print("Sorry, enter a valid day:")
        
print('-'*40)             
print(city, month, day)
return city, month, day

def load_data(city, month, day):
    df=pd.read_csv(city_data[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday
    df['hour']=df['Start Time'].dt.hour
    month_name= ['january', 'febuary', 'march','april', 'may', 'june']
    if month!='all':
        month=months.index(month)
        df=df[df['month']==month]
        
    if day !=7:
        df=df[df['day_of_week']==day]
        

    return df
              
def station_stats(df):
   
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station is:{}'.format(start_station))
   
    # TO DO: display most commonly used end station

    end_station = df['End Station'].mode()[0]
    print('Most commonly used end station is:{}'.format(end_station))

    
    def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is :{}".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Total travel time is :{}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types=df.groupby(['User Type']).sum()
    print('User Types\n',user_types)
    
    
    # TO DO: Display counts of gender

    if Gender in df.columns:
        gender_counts=df['Gender'].value_counts()
        print("Gender Counts")
        print(gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
       
        if 'Birth Year' in df.columns:
        early_year=df['Birth Year'].max()
        late_year=df['Birth Year'].min()
        common_year=df['Birth Year'].mode()
        print('The earliest birth year is: {}'.format(early_year))
        print('The most recent birth year is: {}'.format(late_year))
        print('The most common birth year is: {}'.format(common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:






# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




