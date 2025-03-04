import streamlit as st

#image
st.image("gad7.png", use_container_width=True, caption="Program By: Marcus C. Rodriguez")

# Title of the app
st.header("Discussion 14: (GAD-7) Questionnaire")
st.markdown(
    "<hr style='border: 5px solid; border-image-source: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); border-image-slice: 1;'>",
    unsafe_allow_html=True,
)

st.write(
    "Over the last 2 weeks, how often have you been bothered by the following problems? "
    "Please select the most appropriate answer for each question."
)

# GAD-7 Questions
questions = [
    "Feeling nervous, anxious, or on edge",
    "Not being able to stop or control worrying",
    "Worrying too much about different things",
    "Trouble relaxing",
    "Being so restless that it is hard to sit still",
    "Becoming easily annoyed or irritable",
    "Feeling afraid as if something awful might happen",
]

# Response options
response_options = {
    "Not at all (0)": 0,
    "Several days (1)": 1,
    "More than half the days (2)": 2,
    "Nearly every day (3)": 3,
}

# Store responses
responses = []

# Collect user input for each question
for i, question in enumerate(questions):
    response = st.radio(f"**{i+1}. {question}**", list(response_options.keys()), index=0)
    responses.append(response_options[response])

# Calculate GAD-7 Total Score
total_score = sum(responses)

# Interpretation of GAD-7 Score
if total_score < 5:
    severity = "Minimal Anxiety"
elif 5 <= total_score < 10:
    severity = "Mild Anxiety"
elif 10 <= total_score < 15:
    severity = "Moderate Anxiety"
else:
    severity = "Severe Anxiety"

# Display Results
if st.button("Submit"):
    st.subheader("Results:")
    st.write(f"**Your GAD-7 Total Score:** {total_score}")
    st.write(f"**Severity Level:** {severity}")

    st.markdown(
        "**Interpretation Guidelines:**  \n"
        "- **0-4:** Minimal Anxiety (No intervention required)  \n"
        "- **5-9:** Mild Anxiety (Monitor symptoms)  \n"
        "- **10-14:** Moderate Anxiety (Consider further evaluation)  \n"
        "- **15-21:** Severe Anxiety (Professional treatment recommended)  \n"
    )

# APA 7 Citation
st.markdown(
    "**Reference:**  \n"
    "Spitzer, R. L., Kroenke, K., Williams, J. B. W., & Löwe, B. (2006). "
    "A brief measure for assessing generalized anxiety disorder: The GAD-7. "
    "*Archives of Internal Medicine, 166*(10), 1092-1097. "
    "[https://doi.org/10.1001/archinte.166.10.1092](https://doi.org/10.1001/archinte.166.10.1092)"
)

