#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:37:59 2021

@author: vikash
"""
import json


#  *******Function to calculate BMI **********
def cal_bmi(height, weight):
    height =height/100
    return weight/(height*height)

#  *******Function to Calculate BMI Category and BMI Range Health risk **********
def find_bmi_catogries(bmi):
    if bmi <= 18.4:
        return "Underweight", "Malnutrition risk"
    elif bmi <= 24.9:
        return "Normal weight", "Low risk"
    elif bmi <= 29.9:
        return "Overweight", "Enhanced risk"
    elif bmi <= 34.9:
        return "Moderately obese", "Medium risk"
    elif bmi <=39.9:
        return "Severely obesek" , "High risk"
    else:
        return "Very severely obese", "Very high risk"
    
#  ***************** sample Jason Data ***********
my_json_string = """{
   "bmi_data": [
        {
         "Gender": "Female",
         "HeightCm": 167,
         "WeightKg": 82
      },
        
       {
         "Gender": "Female",
         "HeightCm": 150,
         "WeightKg": 70
      },
       
       {
         "Gender": "Female",
         "HeightCm": 166,
         "WeightKg": 62
      },

      {
         "Gender": "Male",
         "HeightCm": 171,
         "WeightKg": 96
      },
      {
         "Gender": "Male",
         "HeightCm": 180,
         "WeightKg": 77
      },
      
     {
         "Gender": "Male",
         "HeightCm": 161,
         "WeightKg": 85
      }
    
   ]
   }
   """

#   *********** You can also upload Json file using ************
#input_file = open ('stores-small.json')
#json_array = json.load(input_file)


y = json.loads(my_json_string)

  
#  *******Store JSon value in List **********
bmi_data = y['bmi_data']



total_overweight = 0
for data in bmi_data:
    print(data)
    bmi =cal_bmi(data['HeightCm'],data['WeightKg'])
    bmi_catogries ,health_risk= find_bmi_catogries(bmi)
    if bmi_catogries == "Overweight":
        total_overweight += 1
    print(f"BMI Value = {bmi}, BMI Category = {bmi_catogries} and  Health risk = {health_risk}")
    
print(f"Tatal Overweight persion = {total_overweight}")

    
    
                                                                     
                                                                         
             
                                        
             
                
             
                
             
                
             
                
             
                
             
                
             
                
             
                
             
                
             
                
             
                
             
                
             