import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Bulldozer Price Predictor", page_icon="🚜", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1526633888268-0523d02a6e79?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
        font-family: 'Roboto', sans-serif;
    }
    .hero {
        text-align: center;
        padding: 40px 30px;
        border-radius: 25px;
        background: rgba(0, 0, 0, 0.65);
        box-shadow: 0 15px 40px rgba(0,0,0,0.5);
        border: 2px solid rgba(255,255,255,0.18);
        margin-bottom: 30px;
    }
    .hero h1 {
        color: #FFD700;
        margin-bottom: 0.2em;
        font-size: 3.8rem;
        letter-spacing: 1px;
    }
    .hero p {
        color: #f4f4f4;
        font-size: 1.17rem;
        max-width: 900px;
        margin: auto;
        line-height: 1.6;
    }
    .panel {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255,255,255,0.18);
        border-radius: 25px;
        padding: 30px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        margin-bottom: 30px;
        backdrop-filter: blur(8px);
    }
    .panel h2 {
        color: #FFD700;
        font-size: 1.9rem;
        margin-bottom: 15px;
    }
    .card {
        background: linear-gradient(180deg, rgba(255,255,255,0.12), rgba(255,255,255,0.05));
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 25px;
        padding: 25px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.45);
    }
    .card h3 {
        color: #FFB74D;
        margin-bottom: 15px;
    }
    .card p {
        color: #f3f3f3;
        line-height: 1.7;
    }
    .stButton>button {
        background: linear-gradient(90deg, #FF6B35, #F9A825);
        color: #111;
        font-size: 1.2rem;
        font-weight: 700;
        padding: 18px 32px;
        border-radius: 14px;
        border: none;
        box-shadow: 0 12px 25px rgba(0,0,0,0.35);
        transition: transform 0.25s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
    }
    .result {
        background: linear-gradient(135deg, #00C6FF, #0072FF);
        padding: 35px;
        border-radius: 28px;
        text-align: center;
        font-size: 2.6rem;
        font-weight: 800;
        color: white;
        box-shadow: 0 25px 60px rgba(0,0,0,0.55);
        border: 2px solid rgba(255,255,255,0.25);
        margin-top: 30px;
    }
    .sidebar .stMarkdown {
        color: #ffffff;
    }
    .footer {
        text-align: center;
        color: #ffffff;
        padding: 20px;
        margin-top: 30px;
        border-top: 1px solid rgba(255,255,255,0.18);
        font-size: 0.95rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load the trained model
model = joblib.load('random_forest_model.pkl')

st.markdown(
    '<div class="hero"><h1>🚜 Bulldozer Price Predictor</h1><p>Predict machine sale value with a polished ML interface. Choose relevant specifications and get an instant price estimate with a premium experience.</p></div>',
    unsafe_allow_html=True,
)

with st.container():
    left, right = st.columns([2, 1])

    with left:
        st.markdown('<div class="panel"><h2>Enter Bulldozer Specifications</h2></div>', unsafe_allow_html=True)
        year_made_options = list(range(1980, 2013))
        year_made = st.selectbox('📅 Year Made', year_made_options, index=year_made_options.index(1995), help='Manufacturing year of the bulldozer')
        machine_hours_options = [0, 100, 500, 1000, 2000, 5000, 10000, 20000]
        machine_hours = st.selectbox('⏱ Machine Hours', machine_hours_options, index=3, help='Recorded hours on the machine')
        sale_year_options = list(range(2000, 2013))
        sale_year = st.selectbox('🗓 Sale Year', sale_year_options, index=sale_year_options.index(2006), help='Year of sale')
        sale_month_options = list(range(1, 13))
        sale_month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        sale_month = st.selectbox('📆 Sale Month', sale_month_options, index=5, format_func=lambda x: sale_month_names[x-1], help='Month of sale')
        sale_day_options = list(range(1, 32))
        sale_day = st.selectbox('📌 Sale Day', sale_day_options, index=14, help='Day of sale')

        if st.button('🚀 Predict Price'):
            input_data = {
                'YearMade': year_made,
                'MachineHoursCurrentMeter': machine_hours,
                'saleYear': sale_year,
                'saleMonth': sale_month,
                'saleDay': sale_day,
            }
            input_df = pd.DataFrame([input_data]).reindex(columns=model.feature_names_in_, fill_value=0)
            prediction = model.predict(input_df)[0]
            st.markdown(f'<div class="result">💰 Estimated Sale Price: ${prediction:.2f}</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="card"><h3>Why this matters</h3><p>Use this tool to quickly estimate bulldozer resale pricing. The interface is designed to keep the experience clean, modern, and focused on results.</p></div>', unsafe_allow_html=True)
        st.image('https://images.unsplash.com/photo-1581094655388-2e3c41ab9fbe?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80', caption='Heavy machinery valuation made easy', use_column_width=True)

st.markdown('<div class="footer">Built with Streamlit • High-level UI for bulldozer price prediction</div>', unsafe_allow_html=True)