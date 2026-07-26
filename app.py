import streamlit as st

st.set_page_config (
    page_title = "BMI Calculator",
    page_icon = "💪🏻",
    layout = "centered")

st.title("💪🏻BMI Calculator")

weight = st.number_input(
    "Enter your weight(in kgs)",
    min_value = 1.0,
    max_value = 500.0,
    step = 0.5
)

height = st.number_input(
    "Enter your height (in cm)",
    min_value= 50.0,
    max_value= 300.0,
    step= 0.5
)

if st.button("Calculate BMI"):
    height_cm = height/100
    bmi = weight/(height_cm **2)

    st.subheader(f"Your BMI is **{bmi:.2f}**")

    if bmi < 18.5:
        st.warning("Underweight")
        st.write("➡️Consider consulting a healthcare professional about healthy weight gain")

    elif bmi < 25:
        st.success("Healthy Weight")
        st.write("➡️Congratulations keep maintaining the healthy weight")

    elif bmi < 30:
        st.info("Overweight")
        st.write("➡️Regular exercise and a balanced diest may help in improving your weight!")

    else :
        st.error("Obese")
        st.write("➡️Consider consulting a healthcare professional about healthy weight gain")

st.divider()

st.markdown("**BMI Classification Table**")

st.table({
    "Category" : ["Underweight", "Healthy Weight", "Overweight", "Obese"],
    "BMI" : [" < 18.5" , "18.5 - 24.9", "25 - 29.9", " 30 and above"]
    })



    