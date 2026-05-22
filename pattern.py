import streamlit as st

st.title("⭐ Pattern Hub")
st.sidebar.title("Pattern Hub")


pattern = st.sidebar.selectbox("Select Pattern", ["Star Pattern", "Number Pattern", "Pyramid Pattern","Reverse Star Pattern"])

rows = st.sidebar.number_input("Enter number", min_value=1, step=1)

if st.sidebar.button("Generate Pattern"):

    rows = int(rows)  

    if pattern == "Star Pattern":
        st.title("⭐ Star Pattern")

        result = ""
        for i in range(1, rows + 1):
            for j in range(1, i + 1):
                result += "* "
            result += "\n"

        st.text(result)

    elif pattern=="Number Pattern":
        st.title("🔢 Number Pattern")

        result = ""
        for i in range(1, rows + 1):
            for j in range(1, i + 1):
                result += str(j) + " "
            result += "\n"

        st.text(result)

    elif pattern=="Pyramid Pattern":
        st.title("🔢 Pyramid Pattern")

        result = ""
        for i in range(1, rows + 1):
            for j in range(1, rows - i + 1):
                result += " "
            for k in range(1, i + 1):
                result += str(k) + " "
            result += "\n"

        st.text(result)

    elif pattern=="Reverse Star Pattern":
        st.title("⭐ Reverse Star Pattern")

        result = ""
        for i in range(1, rows + 1):
            for j in range(1, rows - i + 1):
                result += " "
            for k in range(1, i + 1):
                result += "* "
            result += "\n"

        st.text(result)
    else:
        st.write("Please select a pattern")

    st.write("Pattern generated successfully")

 