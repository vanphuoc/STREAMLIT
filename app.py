
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
    # st.text('Column 1')
    FS300Dwell_days = st.number_input("FS300Dwell_days", min_value=0.0, max_value=10.0, value=0.0,step=0.5, format="%.2f", key="FS300Dwell_days", help="put your module FS300Dwell_days", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    LamSimDwell_Attr = st.number_input("LamSimDwell_Attr", min_value=0.0, max_value=150.0, value=0.0,step=0.5, format="%.2f", key="LamSimDwell_Attr", help="put your module LamSimDwell_Attr", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    BSAInterStageDwell = st.number_input("BSAInterStageDwell", min_value=0.0, max_value=57.0, value=0.0,step=0.5, format="%.2f", key="BSAInterStageDwell", help="put your module  BSAInterStageDwell", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    rccc = st.number_input("rccc", min_value=1.0, max_value=2.0, value=1.0,step=0.1, format="%.2f", key="rccc", help="put your module  rccc ", on_change=None, args=None, kwargs=None, placeholder="do not this fill is blank", disabled=False, label_visibility="visible")
    IntensityVoltage = st.number_input("IntensityVoltage", min_value=6.0, max_value=8.0, value=6.0,step=0.1, format="%.2f", key="IntensityVoltage", help="put your module  IntensityVoltage", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    Hipot_Result  = st.number_input("Hipot_Result ", min_value=0.0, max_value=2.0, value=0.0,step=0.1, format="%.2f", key="Hipot_Result ", help="put your module  Hipot_Result  ", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    Hipot_ResultCode  = st.number_input("Hipot_ResultCode ", min_value=0.0, max_value=55.0, value=0.0,step=1.0, format="%.2f", key="Hipot_ResultCode ", help="put your module  Hipot_ResultCode", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    LeakageCurrent  = st.number_input("LeakageCurrent ", min_value=0.0, max_value=155.0, value=0.0,step=1.0, format="%.2f", key="LeakageCurrent ", help="put your module  LeakageCurrent  ", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    Continuity_Hipot  = st.number_input("Continuity_Hipot ", min_value=0.0, max_value=120.0, value=0.0,step=1.0, format="%.2f", key="Continuity_Hipot ", help="put your module  Continuity_Hipot", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    GlassFloat_Attr  = st.number_input("GlassFloat_Attr ", min_value=600.0, max_value=630.0, value=600.0,step=1.0, format="%.2f", key="GlassFloat_Attr ", help="put your module GlassFloat_Attr", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    CoaterRun  = st.number_input("CoaterRun ", min_value=70.0, max_value=120.0, value=70.0,step=1.0, format="%.2f", key="CoaterRun ", help="put your module CoaterRun  ", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    B1_IntegratedIntensity_Avg  = st.number_input("B1_IntegratedIntensity_Avg ", min_value=15900.0, max_value=35400.0, value=15900.0,step=1.0, format="%.2f", key="B1_IntegratedIntensity_Avg ", help="put your module B1_IntegratedIntensity_Avg", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    B1_IntegratedIntensity_StDev  = st.number_input("B1_IntegratedIntensity_StDev ", min_value=1150.0, max_value=39400.0, value=1150.0,step=1.0, format="%.2f", key="B1_IntegratedIntensity_StDev ", help="put your module B1_IntegratedIntensity_StDev", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    SPL_CV  = st.number_input("SPL_CV ", min_value=0.0, max_value=2.0, value=0.0,step=0.1, format="%.2f", key="SPL_CV ", help="put your module SPL_CV", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    SPL_PeakWL  = st.number_input("SPL_PeakWL ", min_value=800.0, max_value=900.0, value=800.0,step=1.0, format="%.2f", key="SPL_PeakWL ", help="put your module SPL_PeakWL", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    IBA_Med  = st.number_input("IBA_Med ", min_value=5.0, max_value=7.0, value=5.0,step=0.1, format="%.2f", key="IBA_Med ", help="put your module IBA_Med", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    BandGapRange_DeltaWL_Avg  = st.number_input("BandGapRange_DeltaWL_Avg ", min_value=50.0, max_value=80.0, value=50.0,step=1.0, format="%.2f", key="BandGapRange_DeltaWL_Avg ", help="put your module BandGapRange_DeltaWL_Avg", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    BE_Med  = st.number_input("BE_Med ", min_value=800.0, max_value=900.0, value=800.0,step=1.0, format="%.2f", key="BE_Med ", help="put your module BE_Med", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    TotalDwell_260_280_300_hrs  = st.number_input("TotalDwell_260_280_300_hrs ", min_value=0.0, max_value=2100.0, value=0.0,step=1.0, format="%.2f", key="TotalDwell_260_280_300_hrs ", help="put your module TotalDwell_260_280_300_hrs", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")



with col2:
    # st.text('Column 2')
    Coater_Run  = st.number_input("Coater_Run ", min_value=80.0, max_value=110.0, value=80.0,step=1.0, format="%.2f", key="Coater_Run ", help="put your module Coater_Run", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    Coater_Sequence  = st.number_input("Coater_Sequence ", min_value=0.0, max_value=177900.0, value=0.0,step=1.0, format="%.2f", key="Coater_Sequence ", help="put your module Coater_Sequence", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    CdSeThx_Nominal  = st.number_input("CdSeThx_Nominal ", min_value=2000.0, max_value=4000.0, value=2000.0,step=1.0, format="%.2f", key="CdSeThx_Nominal ", help="put your module CdSeThx_Nominal", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    C451_Avg_Thickness  = st.number_input("C451 Avg. Thickness ", min_value=20.0, max_value=1600.0, value=20.0,step=1.0, format="%.2f", key="C451 Avg. Thickness ", help="put your module C451 Avg. Thickness", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    C452_Avg_Thickness  = st.number_input("C452 Avg. Thickness ", min_value=1000.0, max_value=3600.0, value=1000.0,step=1.0, format="%.2f", key="C452 Avg. Thickness ", help="put your module C452 Avg. Thickness", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    C453_Avg_Thickness  = st.number_input("C453 Avg. Thickness ", min_value=2000.0, max_value=4000.0, value=2000.0,step=1.0, format="%.2f", key="C453 Avg. Thickness ", help="put your module C453 Avg. Thickness", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    C451_StdDev_Thickness  = st.number_input("C451 StdDev. Thickness ", min_value=0.0, max_value=120.0, value=0.0,step=1.0, format="%.2f", key="C451 StdDev. Thickness ", help="put your module C451 StdDev. Thickness", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    C461_Avg_Thickness  = st.number_input("C461 Avg. Thickness ", min_value=0.0, max_value=3.0, value=0.0,step=0.1, format="%.2f", key="C461 Avg. Thickness ", help="put your module C461 Avg. Thickness", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    C462_Avg_Thickness  = st.number_input("C462 Avg. Thickness ", min_value=0.0, max_value=4.0, value=0.0,step=0.1, format="%.2f", key="C462 Avg. Thickness ", help="put your module C462 Avg. Thickness", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    C463_Avg_Thickness  = st.number_input("C463 Avg. Thickness ", min_value=0.0, max_value=5.0, value=0.0,step=0.1, format="%.2f", key="C463 Avg. Thickness ", help="put your module C463 Avg. Thickness", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    C451_WebX  = st.number_input("C451 Web-X ", min_value=0.0, max_value=220.0, value=0.0,step=1.0, format="%.2f", key="C451 Web-X ", help="put your module C451 Web-X", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    C452_WebX  = st.number_input("C452 Web-X ", min_value=0.0, max_value=550.0, value=0.0,step=1.0, format="%.2f", key="C452 Web-X ", help="put your module C452 Web-X", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    C453_WebX  = st.number_input("C453 Web-X ", min_value=0.0, max_value=1800.0, value=0.0,step=1.0, format="%.2f", key="C453 Web-X ", help="put your module C453 Web-X", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    Exsitu_Avg_Thickness  = st.number_input("Exsitu Avg. Thickness ", min_value=0.0, max_value=5.0, value=0.0,step=0.1, format="%.2f", key="Exsitu Avg. Thickness ", help="put your module Exsitu Avg. Thickness", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    Exsitu_StdDev_Thickness  = st.number_input("Exsitu StdDev. Thickness ", min_value=0.0, max_value=1.0, value=0.0,step=0.1, format="%.2f", key="Exsitu StdDev. Thickness ", help="put your module Exsitu StdDev. Thickness", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    Exsitu_Avg_Roughness  = st.number_input("Exsitu Avg. Roughness ", min_value=1000.0, max_value=1400.0, value=1000.0,step=1.0, format="%.2f", key="Exsitu Avg. Roughness ", help="put your module Exsitu Avg. Roughness", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    Exsitu_StdDev_Roughness  = st.number_input("Exsitu StdDev. Roughness ", min_value=0.0, max_value=70.0, value=0.0,step=0.1, format="%.2f", key="Exsitu StdDev. Roughness ", help="put your module Exsitu StdDev. Roughness", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    Exsitu_Roughness_Min  = st.number_input("Exsitu Roughness Min ", min_value=900.0, max_value=1400.0, value=900.0,step=1.0, format="%.2f", key="Exsitu Roughness Min ", help="put your module Exsitu Roughness Min", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    Exsitu_Roughness_Max  = st.number_input("Exsitu Roughness Max", min_value=1000.0, max_value=1400.0, value=1000.0,step=1.0, format="%.2f", key="Exsitu Roughness Max", help="put your module Exsitu Roughness Max", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")
    Exsitu_Roughness_Arbr  = st.number_input("Roughness_Arbs ", min_value=50.0, max_value=126.0, value=50.0,step=0.1, format="%.2f", key="Roughness_Arbs", help="put your module Exsitu Roughness Arbr", on_change=None, args=None, kwargs=None, placeholder="Please fill in this field", disabled=False, label_visibility="visible")


with col3:
    # st.text('Column 3')
    EquipmentName = st.selectbox(
    'EquipmentName',
    ('DMT21A-CDCL2_THKa', 'DMT21A-CDCL2_THKb'),key = 'EquipmentName', help="put your module  EquipmentName"  )
    VTDLite_EquipmentName = st.selectbox(
    'EquipmentName',
    ('DMT21A-VTD_COATER', 'DMT21B-VTD_COATER','DMT21C-VTD_COATER'),key = 'VTDLite_EquipmentName',help="put your module  VTDLite_EquipmentName  ")

#%%
# if st.button('Pmax vaule prediction'):
#     result = predict(np.array([[sepal_l, sepal_w, petal_l, petal_w]]))
#     st.text(result[0])#%%
st.text('')
st.text('')
st.markdown(
    '`Create by` [DNM IT/MES/ME](https://twitter.com/santiviquez) | \
         `Code:` [GitHub](https://github.com/vanphuoc/TEST)')
# %%
