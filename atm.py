import streamlit as st

st.title("ATM System")

bal = 5000
pin = 8977

epin = st.number_input("Enter PIN ",min_value=0000, max_value=10000)

if epin == pin:
    st.write("Login Successful")

    op = st.selectbox("Choose option", ["Withdraw", "Deposit", "Check Balance","exit"])

    if op == "Withdraw":
        w = st.number_input("Enter amount to withdraw", min_value=0, step=1)

        if st.button("Submit Withdraw"):
            if w <= bal:
                bal-= w
                st.write("Withdrawal successful")
                st.write("Updated balance:", bal)

                note = [500, 200, 100, 50, 20, 10, 5, 2, 1]
                r = int(w)

                st.write("Notes:")
                for i in note:
                    count = r // i
                    r = r % i

                    if count > 0:
                        st.write(f"{i} : {count}")

            else:
                st.write("Insufficient balance")


    elif op == "Deposit":
        d = st.number_input("Enter amount to deposit")
        
        if st.button("Submit"):
            bal = bal + d
            st.write("Deposit successful")
            st.write("Updated balance:", bal)


    elif op == "Check Balance":
        if st.button("Check"):
            st.write(f"Available balance: ₹{bal}")

    # Exit
    else:
        st.write("Thank you for using ATM")
