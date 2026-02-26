import streamlit as st
from utils import get_prediction

st.set_page_config(page_title="Customer Churn Prediction", layout="wide")
st.title("Customer Churn Prediction")
st.markdown("Enter customer details o predct curn risk.")

with st.form("churn_form"):
    col1,col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender",["Male","Female"])
        senior = st.selectbox("Senior Citizen", ["Yes", "No"])
        partner = st.selectbox("Partner", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["Yes", "No"])
        tenure = st.slider("Tenure (months)", 0, 72, 12)

        phone = st.selectbox("Phone Service", ["Yes", "No"])
        multiple = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])

        internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

        contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
        billing = st.selectbox("Paperless Billing", ["Yes", "No"])
    with col2:
        online_sec = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
        backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
        device = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
        tech = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
        tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
        movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

        payment = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

        monthly = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
        total = st.number_input("Total Charges", min_value=0.0, value=1000.0)

    #Prediction button
    # st.markdown("###")

    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        submit = st.form_submit_button("Predict", use_container_width=True)

if submit:

    payload = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MultipleLines": multiple,
        "InternetService": internet,
        "OnlineSecurity": online_sec,
        "OnlineBackup": backup,
        "DeviceProtection": device,
        "TechSupport": tech,
        "StreamingTV": tv,
        "StreamingMovies": movies,
        "Contract": contract,
        "PaperlessBilling": billing,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    result, error = get_prediction(payload)

    if error:
        st.error(f"API Error: {error}")
    else:
        prediction = result["prediction"]
        probability = result["probability"]

        if prediction == "Yes":
            st.error(f"Customer is likely to CHURN")
        else:
            st.success(f"Customer is NOT likely to churn")

        st.write(f"**Probability:** {probability}")