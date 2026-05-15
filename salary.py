import streamlit as st

st.title("Employee Salary Management System")

base_salary = 25000
salary_per_hour = 200
working_days = 28


ih = st.number_input("Enter Employee Entry Hour:", min_value=1, max_value=12)
im = st.number_input("Enter Employee Entry Minutes:", min_value=0, max_value=59)
entry_period = st.radio("Entry Time Period:", ["AM", "PM"])

# Exit Time
oh = st.number_input("Enter Employee Exit Hour:", min_value=1, max_value=12)
om = st.number_input("Enter Employee Exit Minutes:", min_value=0, max_value=59)
exit_period = st.radio("Exit Time Period:", ["AM", "PM"])

if st.button("Calculate Salary"):

    if entry_period == "PM" and ih != 12:
        ih += 12
    if entry_period == "AM" and ih == 12:
        ih = 0

    if exit_period == "PM" and oh != 12:
        oh += 12
    if exit_period == "AM" and oh == 12:
        oh = 0

    in_time = ih * 60 + im
    out_time = oh * 60 + om

    if out_time < in_time:
        st.write("Out time cannot be before In time")
    else:
        total_minutes = out_time - in_time
        hours = total_minutes / 60


        basic_salary_day = hours * salary_per_hour
        basic_salary = basic_salary_day * working_days

        hra = basic_salary * 0.20
        da = basic_salary * 0.10
        gross_salary = basic_salary + hra + da

        st.write("Calculation Done")

        st.write("Daily Working Hours:",hours)
        st.write("Monthly Basic Salary: ",base_salary)
        st.write("HRA (20%):",hra)
        st.write("DA (10%): ",da)
        st.write("Gross Monthly Salary:",gross_salary)