
#%%

import streamlit as st
import pandas as pd
import numpy as np
from custom_transformer import ColumnSelector

# %%
st.title('Solar Panel Pmax Prediction')
st.markdown('Predict Pmax value of module depen on module attribute')
# %%
st.header('Please fill in Module Attribute information')
col1, col2,col3 = st.columns(3)
with col1:
    st.text('Column 1')
    # title = st.text_input('FS300Dwell_days range from 0 to 9,4', 'please input a positvie number', key=int,help='put your module attribute',placeholder='please fill in this field')
    FS300Dwell_days = st.number_input("FS300Dwell_days", min_value=0.0, max_value=9.4, value=0.0,step=0.5, format="%.2f", key="FS300Dwell_days", help="put your module FS300Dwell_days ", on_change=None, args=None, kwargs=None, placeholder="do not this fill is blank", disabled=False, label_visibility="visible")
    st.write('The value you are input is:%2f', FS300Dwell_days)
    
    Hipot_Result  = st.number_input(" Hipot_Result ", min_value=0.0, max_value=1.0, value=0.0,step=0.1, format="%.2f", key=" Hipot_Result ", help="put your module  Hipot_Result  ", on_change=None, args=None, kwargs=None, placeholder="do not this fill is blank", disabled=False, label_visibility="visible")
    st.write('The value you are input is:%2f',  Hipot_Result )

with col2:
    st.text('Column 2')
    LamSimDwell_Attr = st.number_input("LamSimDwell_Attr", min_value=0.0, max_value=145.0, value=0.0,step=0.5, format="%.2f", key="LamSimDwell_Attr", help="put your module LamSimDwell_Attr ", on_change=None, args=None, kwargs=None, placeholder="do not this fill is blank", disabled=False, label_visibility="visible")
    st.write('The value you are input is:%2f', LamSimDwell_Attr)

    IntensityVoltage = st.number_input(" IntensityVoltage", min_value=6.0, max_value=8.0, value=6.0,step=0.1, format="%.2f", key=" IntensityVoltage", help="put your module  IntensityVoltage ", on_change=None, args=None, kwargs=None, placeholder="do not this fill is blank", disabled=False, label_visibility="visible")
    st.write('The value you are input is:%2f',  IntensityVoltage)
with col3:
    st.text('Column 3')
    BSAInterStageDwell = st.number_input(" BSAInterStageDwell", min_value=0.0, max_value=53.0, value=0.0,step=0.5, format="%.2f", key=" BSAInterStageDwell", help="put your module  BSAInterStageDwell ", on_change=None, args=None, kwargs=None, placeholder="do not this fill is blank", disabled=False, label_visibility="visible")
    st.write('The value you are input is:%2f',  BSAInterStageDwell)

    rccc = st.number_input(" rccc", min_value=1.0, max_value=2.0, value=1.0,step=0.1, format="%.2f", key=" rccc", help="put your module  rccc ", on_change=None, args=None, kwargs=None, placeholder="do not this fill is blank", disabled=False, label_visibility="visible")
    st.write('The value you are input is: %2f',  rccc)


#%%
# if st.button('Pmax vaule prediction'):
#     result = predict(np.array([[sepal_l, sepal_w, petal_l, petal_w]]))
#     st.text(result[0])#%%
st.text('')
st.text('')
st.markdown(
    '`Create by` [santiviquez](https://twitter.com/santiviquez) | \
         `Code:` [GitHub](https://github.com/santiviquez/iris-streamlit)')
# %%
