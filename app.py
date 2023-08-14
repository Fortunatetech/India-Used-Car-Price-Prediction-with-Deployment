# -*- coding: utf-8 -*-
"""
Created on Tue August 15, 2023

Designed By: Ayodele Ayodeji
"""

# -*- coding: utf-8 -*-
"""
Created on Tue August 15, 2023

Designed By: Ayodele Ayodeji
"""

import streamlit as st
from predict_Page import show_predict_page
from Explore_Dataset_Page import show_explore_page

page = st.sidebar.selectbox("Use the dropdown button bellow to Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()
    