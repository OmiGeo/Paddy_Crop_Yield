
import streamlit as st
import pandas as pd
import pickle

# Load the trained model from the pickle file
with open('adaboost_regression3.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit UI
def main():
    st.title('Paddy Yield Prediction')

    # Input fields
    st.header('Enter Input Features:')
    area = st.number_input('Area (acre)', value=0.0)
    wind_speed = st.number_input('Wind Speed', value=0.0)
    rainfall = st.number_input('Rainfall', value=0.0)
    Tempreature = st.number_input('Tempreature', value=0.0)
    profile_soil_moisture = st.number_input('Profile Soil Moisture', value=0.0)
    rootzone_soil_wetness = st.number_input('Rootzone Soil Wetness', value=0.0)
    open_wells = st.number_input('Number of Open Wells', value=0.0)
    bore_wells = st.number_input('Number of Bore Wells', value=0.0)
    canal_length = st.number_input('Canal Length', value=0.0)
    ponds = st.number_input('Number of Ponds', value=0.0)
    factamfos = st.number_input('Factamfos', value=0.0)
    potash = st.number_input('Potash', value=0.0)
    urea = st.number_input('Urea', value=0.0)
    

    # Prediction button
    if st.button('Predict'):
        # Convert input to DataFrame
        input_data = pd.DataFrame({
            'area (acre)': [area],
            'wind speed': [wind_speed],
            'Rainfall': [rainfall],
            'Tempreature' : [Tempreature],
            'profile soil moisture': [profile_soil_moisture],
            'rootzone soil wetness': [rootzone_soil_wetness],
            'no of open well': [open_wells],
            'no of bore wells': [bore_wells],
            'canal length': [canal_length],
            'no of ponds': [ponds],
            'Factamfos': [factamfos],
            'Potash': [potash],
            'Urea': [urea]
            
        })

        # Predict using the model
        prediction = model.predict(input_data)

        # Display prediction
        st.success(f'Predicted Paddy Yield: {prediction[0]} tonnes/hectares')

if __name__ == '__main__':
    main()



