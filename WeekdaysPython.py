# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:37:38 2020

@author: pcoff
"""

def Weekdays(first_month, first_day, second_month, second_day):
    """
    :type day: int
    :type month: int
    :type year: int
    :rtype: int
    """

    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    WEEKEND = (2, 3)

    first_date = 0
    second_date = 0
    num_weekdays = 0
    
    #get num days for date 1 since epoch
    for i in range(first_month - 1):
        first_date += month_list[i]
    first_date += first_day
    
    #get num days for date 2 since epoch
    for i in range(second_month - 1):
        second_date += month_list[i]
    second_date += second_day
 
    # get num days between date 1 and date 2
    days_between = second_date - first_date   
 
    # for each full week between, add 5 to num_weekdays
    while (days_between >= 7):
        num_weekdays += 5
        days_between -= 7
    
    # for remaining days, determine what days are weekdays and add them to num_weekdays
    while (days_between > 0):
        if first_date % 7 not in WEEKEND:
            # when the date is not a saturday or sunday
            num_weekdays += 1
        days_between -= 1
        first_date += 1
        
    return num_weekdays
    
    
 
print(Weekdays(1, 1, 2, 3))