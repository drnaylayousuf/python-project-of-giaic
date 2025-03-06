import streamlit as st

# Inject custom CSS for gradient background, shocking pink text color, and unique design
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #ffafbd, #ffc3a0);  /* Gradient from pink to light orange */
        background-size: cover;
        background-position: center;
        height: 100vh;
        color: white;  /* Default text color */
    }

    h1 {
        text-align: center;
        font-size: 3em;
        color: #FF6EC7;  /* Shocking Pink color for the title */
        animation: fadeIn 2s ease-in-out;
    }

    h2 {
        text-align: center;
        font-size: 2em;
        color: #FF6EC7; /* Shocking pink color for subheading */
    }

    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }

    .stApp {
        background:  #ffafbd; /* Transparent dark background */
    }
    
    .result {
        font-size: 1.5em;
        font-weight: bold;
        color: white;  /* White text on dark pink for readability */   /*  color: #FF6EC7;  Shocking pink for the result */
        text-align: center;
        padding: 10px;
        border: 2px solid #FF6EC7;
        border-radius: 8px;
        background-color: #D5006D; /* Dark Pink background */   /*  background-color: rgba(255, 255, 255, 0.3);  Semi-transparent background */
    
           margin-top: 20px;
    }

    
    
    .stSelectbox, .stNumberInput {
        width: 100%;
        font-size: 1.2em;
        padding: 10px;
    }
    
    .stButton {
        background-color: #FF6EC7;
        color: white;
        font-size: 1.2em;
        padding: 10px 20px;
        border-radius: 5px;
    }
    
    .stButton:hover {
        background-color: #ff4081;
    }
    </style>
    <h1 style="color: #FF6EC7; text-align: center;">⚖️ ⚙️ Unit Converter</h1>
    """, unsafe_allow_html=True)

# Main content area
st.subheader("🧮 Welcome to the Unit Converter! ⚙️")

# Select conversion type (Length, Weight, or Temperature)
conversion_type = st.selectbox(
    "Select the conversion type:",
    ["Length", "Weight", "Temperature"]
)

# Define the unit converter logic
if conversion_type == "Length":
    st.subheader("Length Converter")
    
    from_unit = st.selectbox("From unit", ["Meters", "Kilometers", "Miles", "Centimeters", "Millimeters"])
    to_unit = st.selectbox("To unit", ["Meters", "Kilometers", "Miles", "Centimeters", "Millimeters"])
    
    value = st.number_input(f"Enter value in {from_unit}", min_value=0.0)

    # Conversion factors for length
    length_conversion = {
        "Meters": {"Kilometers": 0.001, "Miles": 0.000621371, "Centimeters": 100, "Millimeters": 1000},
        "Kilometers": {"Meters": 1000, "Miles": 0.621371, "Centimeters": 100000, "Millimeters": 1000000},
        "Miles": {"Meters": 1609.34, "Kilometers": 1.60934, "Centimeters": 160934, "Millimeters": 1609340},
        "Centimeters": {"Meters": 0.01, "Kilometers": 0.00001, "Miles": 0.0000062137, "Millimeters": 10},
        "Millimeters": {"Meters": 0.001, "Kilometers": 0.000001, "Miles": 0.000000621371, "Centimeters": 0.1}
    }

    if value > 0:
        result = value * length_conversion[from_unit][to_unit]
        st.markdown(f'<div class="result">{value} {from_unit} is equal to {result:.4f} {to_unit}</div>', unsafe_allow_html=True)

elif conversion_type == "Weight":
    st.subheader("Weight Converter")
    
    from_unit = st.selectbox("From unit", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("To unit", ["Kilograms", "Grams", "Pounds", "Ounces"])
    
    value = st.number_input(f"Enter value in {from_unit}", min_value=0.0)

    # Conversion factors for weight
    weight_conversion = {
        "Kilograms": {"Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274},
        "Grams": {"Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274},
        "Pounds": {"Kilograms": 0.453592, "Grams": 453.592, "Ounces": 16},
        "Ounces": {"Kilograms": 0.0283495, "Grams": 28.3495, "Pounds": 0.0625}
    }

    if value > 0:
        result = value * weight_conversion[from_unit][to_unit]
        st.markdown(f'<div class="result">{value} {from_unit} is equal to {result:.4f} {to_unit}</div>', unsafe_allow_html=True)

elif conversion_type == "Temperature":
    st.subheader("Temperature Converter")
    
    from_unit = st.selectbox("From unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To unit", ["Celsius", "Fahrenheit", "Kelvin"])
    
    value = st.number_input(f"Enter value in {from_unit}", min_value=-273.15)

    # Conversion logic for temperature
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif to_unit == "Kelvin":
            result = value + 273.15
        else:
            result = value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        else:
            result = value
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            result = value - 273.15
        elif to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        else:
            result = value

    if value > -273.15:
        st.markdown(f'<div class="result">{value} {from_unit} is equal to {result:.4f} {to_unit}</div>', unsafe_allow_html=True)
