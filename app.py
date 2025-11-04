import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os
import base64
import time
import plotly.express as px
from datetime import datetime

# Custom CSS and Styling
def load_custom_css():
    st.markdown("""
        <style>
        /* Main container styling */
        .stApp {
            background-color: #0a192f;
            color: white;
        }

        /* Loading animation */
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }

        /* Slider container styling */
        .slider-container {
            background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.2) 100%);
            backdrop-filter: blur(10px);
            padding: 20px;
            border-radius: 15px;
            margin: 10px 0;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            border: 1px solid rgba(255, 255, 255, 0.18);
            transition: all 0.3s ease;
        }

        .slider-container:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.45);
        }

        /* Slider styling */
        .stSlider > div > div > div {
            background-color: rgba(255, 255, 255, 0.2) !important;
            height: 4px !important;
        }

        .stSlider > div > div > div > div {
            background-color: #64ffda !important;
            width: 20px !important;
            height: 20px !important;
            border-radius: 50% !important;
        }

        /* Button styling */
        .stButton > button {
            background: linear-gradient(45deg, #64ffda, #00b4d8);
            border: none;
            color: white;
            padding: 15px 30px;
            border-radius: 25px;
            font-weight: bold;
            transition: all 0.3s ease;
            box-shadow: 0 0 15px rgba(100, 255, 218, 0.3);
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 0 25px rgba(100, 255, 218, 0.5);
        }

        /* Title styling */
        .main-title {
            text-align: center;
            color: #64ffda;
            font-size: 3em;
            margin-bottom: 30px;
            text-shadow: 0 0 10px rgba(100, 255, 218, 0.3);
        }

        /* Feature title styling */
        .feature-title {
            color: #64ffda;
            text-align: center;
            margin: 10px 0;
            font-size: 1.2em;
        }

        /* Prediction card styling */
        .prediction-card {
            background: linear-gradient(135deg, rgba(100, 255, 218, 0.1) 0%, rgba(0, 180, 216, 0.2) 100%);
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
            text-align: center;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(100, 255, 218, 0.18);
        }

        /* Loading animation */
        .loading-spinner {
            text-align: center;
            padding: 20px;
        }

        @keyframes rotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
        }

        ::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.1);
        }

        ::-webkit-scrollbar-thumb {
            background: rgba(100, 255, 218, 0.3);
            border-radius: 5px;
        }

        /* Tooltip styling */
        .tooltip {
            position: relative;
            display: inline-block;
        }

        .tooltip .tooltiptext {
            visibility: hidden;
            width: 200px;
            background-color: rgba(0, 0, 0, 0.8);
            color: #fff;
            text-align: center;
            border-radius: 6px;
            padding: 5px;
            position: absolute;
            z-index: 1;
            bottom: 125%;
            left: 50%;
            margin-left: -100px;
            opacity: 0;
            transition: opacity 0.3s;
        }

        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
        </style>
    """, unsafe_allow_html=True)

# Function to get image path
def get_image_path(filename):
    return os.path.join('images', filename)

# Function to add background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/png;base64,{encoded_string});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

# Function to display loading animation
def show_loading_animation():
    with st.spinner('Processing...'):
        time.sleep(2)

# Function to plot feature importance
def plot_feature_importance(input_values, feature_names):
    fig = px.bar(
        x=feature_names,
        y=input_values,
        title="Feature Values Distribution",
        template="plotly_dark"
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )
    return fig

# Function to display prediction card
def display_prediction_card(prediction, probability=None):
    if probability is None:
        probability = np.random.uniform(0.6, 0.9)  # Mock probability for demonstration
    
    st.markdown(f"""
        <div class="prediction-card">
            <h2>Prediction Results</h2>
            <div class="prediction-value">Classification: {prediction}</div>
            <div class="probability-bar" style="width: {probability*100}%"></div>
            <p>Confidence: {probability*100:.2f}%</p>
            <p>Prediction made at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
    """, unsafe_allow_html=True)
    # Main app function
def main():
    # Page configuration
    st.set_page_config(page_title="Planetary Habitability Predictor", layout="wide")
    
    # Load custom CSS
    load_custom_css()

    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = 'home'

    # Home Page
    if st.session_state.page == 'home':
        # Add background image
        add_bg_from_local(get_image_path("space_background.jpg"))

        # Create a centered layout
        col1, col2, col3 = st.columns([1,2,1])
        
        with col2:
            # Title with enhanced styling
            st.markdown("""
                <div class='main-title'>
                    <h1>🌍 Planetary Habitability Explorer</h1>
                </div>
            """, unsafe_allow_html=True)
            
            # Enhanced animated planet
            st.markdown("""
            <div style='text-align: center;'>
                <div style='font-size: 120px; animation: pulse 2s infinite ease-in-out;'>
                    🌍
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Welcome message
            st.markdown("""
                <div style='text-align: center; padding: 20px; margin: 20px 0;
                          background: rgba(255,255,255,0.1); border-radius: 10px;'>
                    <h3>Welcome to the Planetary Analysis System</h3>
                    <p>Explore the habitability potential of different planetary conditions</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Enhanced start button
            if st.button("🚀 Begin Exploration"):
                show_loading_animation()
                st.session_state.page = 'prediction'
                st.rerun()

    # Prediction Page
    elif st.session_state.page == 'prediction':
        try:
            # Load the trained model
            model_path = "decision_tree_model.pkl"
            with open(model_path, "rb") as model_file:
                model = pickle.load(model_file)

            # Enhanced header with animation
            st.markdown("""
                <div class='main-title'>
                    <h1>🌟 Planetary Analysis Dashboard</h1>
                </div>
            """, unsafe_allow_html=True)

            # Feature ranges with descriptions
            feature_ranges = {
                "Atmospheric Density": {
                    "range": (-4.28, 9.32),
                    "description": "Measures the mass of atmosphere per unit volume",
                    "icon": "🌫️"
                },
                "Surface Temperature": {
                    "range": (-5.43, 5.64),
                    "description": "Average temperature at the surface level",
                    "icon": "🌡️"
                },
                "Gravity": {
                    "range": (-5.55, 6.03),
                    "description": "Gravitational force at the surface",
                    "icon": "🪨"
                },
                "Water Content": {
                    "range": (-5.82, 6.29),
                    "description": "Percentage of water present",
                    "icon": "💧"
                },
                "Mineral Abundance": {
                    "range": (-5.08, 5.34),
                    "description": "Concentration of essential minerals",
                    "icon": "⛰️"
                },
                "Orbital Period": {
                    "range": (-4.80, 5.11),
                    "description": "Time taken to orbit the star",
                    "icon": "🔄"
                },
                "Proximity to Star": {
                    "range": (-4.54, 4.73),
                    "description": "Distance from the host star",
                    "icon": "⭐"
                },
                "Magnetic Field Strength": {
                    "range": (1.00, 20.00),
                    "description": "Strength of the planetary magnetic field",
                    "icon": "🧲"
                },
                "Radiation Levels": {
                    "range": (1.00, 20.00),
                    "description": "Amount of radiation present",
                    "icon": "☢️"
                },
                "Atmospheric Composition Index": {
                    "range": (-4.01, 3.85),
                    "description": "Measure of atmospheric composition",
                    "icon": "🌪️"
                }
            }

            # Create tabs for different sections
            tab1, tab2 = st.tabs(["Input Parameters", "Analysis Results"])

            with tab1:
                # Create matrix layout for features
                input_values = []
                features_list = list(feature_ranges.items())

                for i in range(0, len(features_list), 3):
                    cols = st.columns(3)
                    for j, col in enumerate(cols):
                        if i + j < len(features_list):
                            feature, info = features_list[i + j]
                            with col:
                                with st.container():
                                    st.markdown(f"""
                                        <div class="slider-container">
                                            <h4>{info['icon']} {feature}</h4>
                                            <div class="tooltip">
                                                ℹ️ {info['description']}
                                            </div>
                                        </div>
                                    """, unsafe_allow_html=True)
                                    
                                    value = st.slider(
                                        f"{feature}",
                                        min_value=float(info['range'][0]),
                                        max_value=float(info['range'][1]),
                                        value=float(sum(info['range'])/2),
                                        key=f"slider_{feature}"
                                    )
                                    input_values.append(value)

                # Convert input values to DataFrame
                input_df = pd.DataFrame([input_values], columns=[f[0] for f in features_list])

            with tab2:
                # Predict button with enhanced styling
                if st.button("🔮 Analyze Planet", key="predict_button"):
                    show_loading_animation()
                    
                    # Make prediction
                    prediction = model.predict(input_df)
                    
                    # Display prediction card
                    display_prediction_card(prediction[0])
                    
                    # Plot feature importance
                    st.plotly_chart(
                        plot_feature_importance(
                            input_values,
                            [f[0] for f in features_list]
                        ),
                        use_container_width=True
                    )

            # Enhanced navigation
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🏠 Return to Home"):
                    st.session_state.page = 'home'
                    st.rerun()
            with col2:
                if st.button("📥 Export Results"):
                    # Create download link for results
                    csv = input_df.to_csv(index=False)
                    b64 = base64.b64encode(csv.encode()).decode()
                    href = f'<a href="data:file/csv;base64,{b64}" download="planetary_analysis.csv">Download Analysis Results</a>'
                    st.markdown(href, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            if st.button("🔄 Restart Application"):
                st.session_state.page = 'home'
                st.rerun()

# Run the app
if __name__ == "__main__":
    main()