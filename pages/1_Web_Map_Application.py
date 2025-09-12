import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import numpy as np



st.set_page_config(layout="wide")
st.sidebar.info("Contact")
st.sidebar.markdown('[Twiter]')

col1, col2 = st.columns([7, 3])

options = list(leafmap.basemaps.keys())

with col2:
    #dropdown = st.selectbox("Basemap",["HYBRID", "ROADMAP","TERRAIN","SATELLITE"])
    dropdown = st.selectbox("Basemap", options)
    #url = st.text_input("Enter url", )
    
    default_url = leafmap.basemaps[dropdown].tiles
    
    url = st.text_input("Enter url", default_url)

    # Upload CSV(s)
    uploaded_files = st.file_uploader(
        "Choose CSV file(s)",
        type="csv",
        accept_multiple_files=True
    )

    if uploaded_files:
        for uploaded_file in uploaded_files:
            # Read CSV directly into DataFrame
            df = pd.read_csv(uploaded_file)
            
            st.text(f"📊 Data from: {uploaded_file.name}")
            st.dataframe(df)  # Show nicely scrollable table
    else:
        # Demo DataFrame if no upload
        df = pd.DataFrame(
            np.random.randn(50, 20),
            columns=[f"col {i}" for i in range(20)]
        )
        st.subheader("📊 Example Data (no file uploaded)")
        st.dataframe(df)

m =leafmap.Map()
m.add_basemap(dropdown)

if url: 
    m.add_tile_layer(url, name="Tile Layer", attribution=' ')

with col1:
    m.to_streamlit()

