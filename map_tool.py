import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="Map Tool", layout="wide")
st.title("🗺️ Interactive Map Tool")

m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
st.write("Click anywhere on the map to drop a marker.")

map_data = st_folium(m, width=700, height=500)

if map_data and map_data.get("last_clicked"):
    lat = map_data["last_clicked"]["lat"]
    lng = map_data["last_clicked"]["lng"]
    st.success(f"📍 You clicked at: {lat:.4f}, {lng:.4f}")
