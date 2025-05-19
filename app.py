import streamlit as st

def convert_units(value: float, unit_from: str, unit_to: str):
    # print("value>>>", value)
    # print("unit_from>>>", unit_from)
    # print("unit_to>>>", unit_to)

    # 1 kilometer = 1000 meters
    # 1 meter = 0.001 kilometer
    # 1 kilogram = 1000 grams
    # 1 gram = 0.001 kilograms

    if unit_from == "kilometers" and unit_to == "meters":
        return value * 1000
    elif unit_from == "meters" and unit_to == "kilometers":
        return value * 0.001
    elif unit_from == "kilograms" and unit_to == "grams":
        return value * 1000
    elif unit_from == "grams" and unit_to == "kilograms":
        return value * 0.001
    else:
        return "Conversion not supported"
    
# result1 = convert_units(1, "kilometers", "meters")
# print("The value in meter is:", result1) 
# result2 = convert_units(5, "grams", "kilograms")
# print("The value in kilograms is:", result2) 

def main():
    st.title("Unit Converter")
    st.write("Welcome to the Unit Converter!")
    value = st.number_input("Enter the value you want to convert: ", min_value=0.0)
    unit_from = st.text_input("Enter the unit you want to convert from (kilometers, meters, kilograms, grams): ")
    unit_to = st.text_input("Enter the unit you want to convert to (kilometers, meters, kilograms, grams): ")

    if st.button("Convert"):
        result = convert_units(value, unit_from, unit_to)
        st.write("The converted value is:", result)

    # print("value", value)
    # print("unit_from", unit_from)
    # print("unit_to", unit_to)
    
main()