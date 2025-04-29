import warnings
warnings.filterwarnings('ignore')

import streamlit as st
import pickle as pk
import numpy as np
import pandas as pd

#load the model and dataframe
df = pd.read_csv("df.csv")
predict_model = pk.load(open("model.pkl", "rb"))
st.title("Laptop Price Predictor")
# Make dictionaries according to data transformation used in model designing
# Dictionary for company brand name
comp_brand ={
    'APPLE': 0,
    'ASUS': 1,
    'Avita': 2,
    'DELL': 3,
    'HP': 4,
    'Lenovo': 5,
    'MSI' : 6,
    'acer': 7 
           
}
# Dictionary for processor_brand
pro_brand={
    'AMD': 0,
    'Intel': 1,
    'M1' : 2
}
# Dictionary for Processor name
pro_name={
    'Celeron Dual':0,
    'Core i3':1,
    'Core i5':2,  
    'Core i7':3,
    'Core i9':4,
    'M1':5,
    'Pentium Quad':6,
    'Ryzen 3':7,
    'Ryzen 5':8,
    'Ryzen 7':9,
    'Ryzen 9':10
}
# Dictionary for Processor generation
pro_gen={
    '10th':0,    
    '11th':1,
    '12th':2,
    '4th':3,
    '7th':4,
    '8th':5,
    '9th':6,   
    'Not Available':7
}
# Dictionary for RAM type
ram_t={
    'DDR3':0,
    'DDR4':1,
    'DDR5':2,
    'LPDDR3':3,
    'LPDDR4':4,
    'LPDDR4X':5  
 }
# Dictionary for Operating system
op_system={    
    'DOS':0,
    'Mac':1,
    'Windows':2
}
# Dictionary for Operating system type
op_system_type={
    '64-bit':1,
    '32-bit':0
}
# Dictionary for Laptop type
lp_type={
    'Casual':0,
    'Gaming':1,
    'ThinNlight':2
}
# Dictionary for Laptop warranty
warty={
     '1 year':0,
     '2 years':1,
     '3 years':2,
     'No warranty':3
}

#Now we will take user input one by one as per our dataframe
company = st.selectbox('Brand', df['brand'].unique())
processor_brand = st.selectbox('Processor Brand', df['processor_brand'].unique())
processor_name= st.selectbox('Processor Name', df['processor_name'].unique())
processor_generation= st.selectbox('Processor Generation', df['processor_gnrtn'].unique())
ram = st.selectbox("Ram(in GB)", [2,4,6,8,12,16,24,32,64])
ram_type= st.selectbox('Ram Type', df['ram_type'].unique())
ssd = st.selectbox("ssd(in GB)", df['ssd'].unique())
hdd = st.selectbox("hdd(in GB)", df['hdd'].unique())
os = st.selectbox("Operating System", df['os'].unique())
os_bit = st.selectbox("os type", df['os_bit'].unique())
graph_card = st.selectbox("Graphic Card(in GB)", [0,2,4,6,8])
weight = st.selectbox("Laptop Type", df['weight'].unique())
warranty = st.selectbox("Warranty", df['warranty'].unique())
touchscreen= st.selectbox("Touchscreen", ['NO','YES'])
ms_office= st.selectbox("MS Office", ['NO','YES'])
rating = st.selectbox("Rating", df['rating'].unique())
no_of_rating = st.number_input("Number of Ratings")
no_of_reviews = st.number_input("Number of Reviews")


if st.button('Predict Price'):
    if touchscreen == 'YES' :
        touchscreen = 1
    else :
        touchscreen = 0
    if ms_office == 'YES':
        ms_office = 1
    else :
        ms_office = 0
    query = np.array([comp_brand[company],pro_brand[processor_brand],pro_name[processor_name],pro_gen[processor_generation],ram,ram_t[ram_type],ssd,hdd,op_system[os],op_system_type[os_bit],graph_card,lp_type[weight],warty[warranty],touchscreen,ms_office,3,no_of_rating,no_of_reviews])
    query = query.reshape(1, 18)
    predict=str(int(predict_model.predict(query)[0]))
    st.title("Predicted Laptop Price =   " + predict +" Rs")

