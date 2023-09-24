import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium

# Title and Introduction
st.title("Real-time Public Transport Tracking App")
st.write(
    "Welcome to the Real-time Public Transport Tracking App. This app allows you to track the real-time "
    "location of buses, trains, and trams in your city."
)

# Sidebar
st.sidebar.title("Menu")
selected_page = st.sidebar.radio(
    "Select a Page", ["Home", "Bus Tracker", "Train Tracker", "Tram Tracker"]
)

# Home Page Content
if selected_page == "Home":
    st.header("About the App")
    st.write(
        "This app is designed to provide real-time tracking information for public transport vehicles "
        "in your area. You can select a specific tracker from the menu on the left to view the live "
        "locations of buses, trains, or trams."
    )

    st.header("How to Use")
    st.write(
        "1. Use the menu on the left to select a specific tracker (Bus, Train, or Tram)."
        "\n2. The selected tracker's real-time map will be displayed on the respective page."
        "\n3. You can interact with the map to view vehicle locations and details."
        "\n4. Enjoy real-time tracking of public transport in your city!"
    )

    st.header("Features")
    st.write(
        "This app offers the following features:"
        "\n- Real-time tracking of buses, trains, and trams."
        "\n- Interactive maps for each tracker."
        "\n- Vehicle details and information."
        "\n- User-friendly interface for commuters."
    )




# Bus Tracker Page
elif selected_page == "Bus Tracker":
    # Sample data (replace with your real-time transit data source)
    sample_data = pd.DataFrame({
        'Route': ['22', '1', '8', '56'],
        'Latitude': [42.3601, 42.3521, 42.3654, 42.3585],
        'Longitude': [-71.0589, -71.0554, -71.0622, -71.0603],
        'NextStop': ['Station X', 'Station Y', 'Station Z', 'Station W'],
        'MinutesToArrival': [5, 8, 3, 12]
    })

    # Streamlit app layout
    st.title('Real-Time Public Transport Tracker')
    st.header("bus Vehicle Tracking")
    selected_route = st.selectbox('Select a Route', sample_data['Route'].unique())

    # Filter data based on the selected route
    filtered_data = sample_data[sample_data['Route'] == selected_route]

    # Display a map with vehicle locations
    m = folium.Map(location=[filtered_data['Latitude'].mean(), filtered_data['Longitude'].mean()], zoom_start=14)
    for i, row in filtered_data.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']], popup=f"Next Stop: {row['NextStop']}").add_to(m)
    folium_static(m)

    # Display a table with real-time vehicle information
    st.write('Real-Time Vehicle Information:')
    st.write(filtered_data)

# Train Tracker Page
elif selected_page == "Train Tracker":
    sample_data_train = pd.DataFrame({
    'Route': ['Train Red', 'Train Blue', 'Train Green', 'Train Yellow'],
    'Latitude': [42.3501, 42.3552, 42.3603, 42.3654],
    'Longitude': [-71.0609, -71.0588, -71.0567, -71.0546],
    'NextStop': ['Train Station 1', 'Train Station 2', 'Train Station 3', 'Train Station 4'],
    'MinutesToArrival': [8, 5, 6, 7]
})
    st.header("Train Live Vehicle Tracking")
    selected_route_train = st.selectbox('Select a Train Route', sample_data_train['Route'].unique())

    # Filter data based on the selected train route
    filtered_data_train = sample_data_train[sample_data_train['Route'] == selected_route_train]

    # Display a map with train locations
    m_train = folium.Map(location=[filtered_data_train['Latitude'].mean(), filtered_data_train['Longitude'].mean()], zoom_start=14)
    for i, row in filtered_data_train.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']], popup=f"Next Stop: {row['NextStop']}").add_to(m_train)
    folium_static(m_train)

    # Display a table with real-time train information
    st.write('Real-Time Train Information:')
    st.write(filtered_data_train)

# Tram Tracker Page
elif selected_page == "Tram Tracker":
    sample_data_tram = pd.DataFrame({
    'Route': ['T1', 'T2', 'T3', 'T4'],
    'Latitude': [42.3651, 42.3511, 42.3644, 42.3575],
    'Longitude': [-71.0579, -71.0552, -71.0629, -71.0610],
    'NextStop': ['Tram Station A', 'Tram Station B', 'Tram Station C', 'Tram Station D'],
    'MinutesToArrival': [6, 7, 4, 10]
})
    st.header("Tram Live Vehicle Tracking")
    selected_route_tram = st.selectbox('Select a Tram Route', sample_data_tram['Route'].unique())

    # Filter data based on the selected tram route
    filtered_data_tram = sample_data_tram[sample_data_tram['Route'] == selected_route_tram]

    # Display a map with tram locations
    m_tram = folium.Map(location=[filtered_data_tram['Latitude'].mean(), filtered_data_tram['Longitude'].mean()], zoom_start=14)
    for i, row in filtered_data_tram.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']], popup=f"Next Stop: {row['NextStop']}").add_to(m_tram)
    folium_static(m_tram)

    # Display a table with real-time tram information
    st.write('Real-Time Tram Information:')
    st.write(filtered_data_tram)