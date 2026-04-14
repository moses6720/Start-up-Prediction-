import streamlit as st
import pandas as pd
import pickle

# load trained model
model = pickle.load(open("model.pkl","rb"))

# page config
st.set_page_config(
    page_title="Startup Success Predictor",
    page_icon="🚀",
    layout="wide"
)

# header
st.title("🚀 Startup Success Prediction System")
st.markdown(
"""
Predict whether a startup is likely to succeed based on business fundamentals.

This tool uses Machine Learning to analyze funding, market size, team strength, and revenue potential.
"""
)

st.divider()

# layout columns
col1, col2 = st.columns(2)

# left column
with col1:

    st.subheader("📊 Business Metrics")

    funding_rounds = st.slider(
        "Funding Rounds",
        0, 10, 2
    )

    team_size = st.slider(
        "Team Size",
        1, 500, 20
    )

    founder_exp = st.slider(
        "Founder Experience (years)",
        0, 30, 5
    )

    market_size = st.number_input(
        "Market Size (Billion USD)",
        min_value=0.0,
        value=5.0
    )

# right column
with col2:

    st.subheader("💰 Financial Metrics")

    users = st.number_input(
        "Product Users",
        min_value=0,
        value=10000
    )

    revenue = st.number_input(
        "Revenue (Million USD)",
        min_value=0.0,
        value=1.0
    )

    burn_rate = st.number_input(
        "Burn Rate (Million USD)",
        min_value=0.0,
        value=0.5
    )

st.divider()

# categories
st.subheader("🏢 Business Information")

col3, col4, col5 = st.columns(3)

with col3:

    investor_type = st.selectbox(
        "Investor Type",
        ["VC","Angel","Private Equity","Seed"]
    )

with col4:

    sector = st.selectbox(
        "Sector",
        ["AI","Fintech","Healthcare","Ecommerce","SaaS","EdTech"]
    )

with col5:

    founder_background = st.selectbox(
        "Founder Background",
        ["Technical","Business","Mixed"]
    )

st.divider()

# prediction button
if st.button("🔍 Predict Startup Success"):

    input_data = pd.DataFrame({

        'funding_rounds':[funding_rounds],
        'founder_experience_years':[founder_exp],
        'team_size':[team_size],
        'market_size_billion':[market_size],
        'product_traction_users':[users],
        'burn_rate_million':[burn_rate],
        'revenue_million':[revenue],
        'investor_type':[investor_type],
        'sector':[sector],
        'founder_background':[founder_background]

    })

    # convert categorical values
    input_data = pd.get_dummies(input_data)

    # match columns with training data
    model_columns = pickle.load(open("model_columns.pkl","rb"))

    input_data = input_data.reindex(
        columns=model_columns,
        fill_value=0
    )

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    st.divider()

    st.subheader("📈 Prediction Result")

    col6, col7 = st.columns(2)

    with col6:

        if prediction == 1:
            st.success("✅ Startup likely to SUCCEED")
        else:
            st.error("❌ Startup likely to FAIL")

    with col7:

        st.metric(
            "Success Probability",
            f"{probability[1]*100:.2f}%"
        )

    st.progress(probability[1])

st.divider()

st.caption(
"Machine Learning model trained using Random Forest algorithm."
)