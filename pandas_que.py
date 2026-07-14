import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# streamlit run pandas_que.py
st.title("📊 Pandas Questions Solutions and Code")

list_questions = [
    "1. Remove rows containing at least one NaN value",
    "2. Remove rows only if all values are NaN",
    "3. Drop all columns containing NaN",
    "4. Remove outliers from DataFrame",
    "5. Remove duplicate rows and reset index",
    "6. Remove mpg and cylinders columns from uploaded CSV",
    "7. Use the file heights_weights.csv which contains 10000 non-null values for heights and weights. The Male column shows 1 if the person is a Male and 0 if the person is a Female",
    "8. Use the file ipl-matches.csv which contains data of all the IPL matches from year 2008 to 2022. Read this csv file and display the basic information like memory and data types for this data frame. Write python code for the following cases:",
    "9.Use the file spotify.csv and python code for the following cases:",
    "10.Read this csv file car data.csv and display the basic information like memory and data types for this data frame.",
    "11.data_result.csv and python code for the following cases:",
    "12.Use the file movies.csv which contains 1629 rows and 18 columns. Read this csv file and display the basic information like memory and data types for this data frame.",
    "13.You are given a CSV file named ipl-matches.csv, which contains data of all Indian Premier League (IPL) matches played from the year 2008 to 2022.Read the dataset and display the basic information about the DataFrame.",
    "14.Sort employees by Dept (Ascending) and Salary (Descending). After sorting, sort the index in descending order. Display the final DataFrame",
    "15.Create a column Average using apply() row-wise. Create a column Grade based on: ≥ 80 → Distinction, ≥ 60 → First, Otherwise → Second. Display final DataFrame.",
    "16.Replace 'Absent' with 0. Convert the column to integer type. Print mean marks. Print number of students scoring above 50.",
    "17.Concatenate row-wise using outer join. Count total missing values. Sort the result by ID.",
    "18.Perform outer merge using indicator=True. Count: Students present in both tables, Only in students, Only in marks",
    "19.Group by Dept. Calculate mean, median, and max salary using agg()",
    "20.Calculate range (max - min) per team using groupby + apply.",
    "21.Detect outliers using IQR method. Remove outliers. Print cleaned dataset",
    "22.Find number of unique cities per department. Take one random employee per department. Display results.",
    "23.Create a new column TotalAmount = Price × Quantity using apply() row-wise. Sort the DataFrame by TotalAmount in descending order. Display the final DataFrame",
    "24.Group employees by Department. Calculate total salary and average salary per department. Display departments where average salary is greater than 50,000.",
    "25.Find the number of employees per department using size(). Find the employee with highest experience in each department using nth() or sorting. Display results",
    "26.The dataset provided in 'kc_house_data.csv' contains house sale prices for King County, which includes Seattle. It includes homes sold between May 2014 and May 2015. Perform the following tasks:",
    "27.Using 'supermarket_sales.csv' file do the following operations and give required answer by using proper programming process.",
    
]
st.sidebar.title("📋 Pandas Questions")
selected_question = st.sidebar.selectbox("Select a Question", list_questions)

#---------------------------------------------------------
# Question 1
#---------------------------------------------------------

if selected_question == list_questions[0]:

    st.header("Question 1")
    st.markdown("1. Remove rows containing at least one NaN value")

    data = {
        'Name': ['A', 'B', 'C', 'D'],
        'Age': [25, np.nan, 30, 22],
        'City': ['Ahmedabad', 'Surat', np.nan, 'Rajkot']
    }
    # create a DataFrame
    df = pd.DataFrame(data)

    st.subheader("Original DataFrame")
    st.write(df)

    # remove rows with one NaN value   
    clean_df = df.dropna()

    # show the cleaned DataFrame
    st.subheader("After Removing NaN Rows")
    st.write(clean_df)

    if st.button("Show Solution Code"):
        st.code("""
import pandas as pd
import numpy as np

data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Age': [25, np.nan, 30, 22],
    'City': ['Ahmedabad', 'Surat', np.nan, 'Rajkot']
}

# create a DataFrame
df = pd.DataFrame(data)

# remove rows with one NaN value
clean_df = df.dropna()

st.write(clean_df)
""")

#---------------------------------------------------------
# Question 2
#---------------------------------------------------------
elif selected_question == list_questions[1]:

    st.header("Question 2")
    st.markdown("2. Remove rows only if all values are NaN")

    data = {
        "Employee": ["Ram", "Shyam", "Mohan", np.nan],
        "Salary": [25000, np.nan, 30000, np.nan],
        "Bonus": [2000, np.nan, np.nan, np.nan]
    }

    # create a DataFrame
    df = pd.DataFrame(data)

    st.subheader("Original DataFrame")
    st.write(df)

    # remove rows only if all values are NaN
    remove_null = df.dropna(how="all")

    st.subheader("After Removing All-NaN Rows")
    st.write(remove_null)

    if st.button("Show Solution Code"):
        st.code("""
import pandas as pd
import numpy as np

data = {
    "Employee": ["Ram", "Shyam", "Mohan", np.nan],
    "Salary": [25000, np.nan, 30000, np.nan],
    "Bonus": [2000, np.nan, np.nan, np.nan]
}
# create a DataFrame
df = pd.DataFrame(data)

# remove rows only if all values are NaN
remove_null = df.dropna(how="all")

st.write(remove_null)
""")


#---------------------------------------------------------
# Question 3
#---------------------------------------------------------
elif selected_question == list_questions[2]:

    st.header("Question 3")
    st.markdown("3. Drop all columns containing NaN")

    data = {
        "Name": ["Amit", "Riya", "Karan"],
        "Age": [23, np.nan, 25],
        "City": ["Surat", "Mumbai", None],
        "Marks": [85, 90, 88]
    }

    # create a DataFrame
    df = pd.DataFrame(data)

    st.subheader("Original DataFrame")
    st.write(df)

    # drop columns with NaN
    df_clean = df.dropna(axis=1)

    # show the cleaned DataFrame
    st.subheader("After Dropping Columns with NaN")
    st.write(df_clean)

    if st.button("Show Solution Code"):
        st.code("""
import pandas as pd
import numpy as np

data = {
    "Name": ["Amit", "Riya", "Karan"],
    "Age": [23, np.nan, 25],
    "City": ["Surat", "Mumbai", None],
    "Marks": [85, 90, 88]
}

# create a DataFrame
df = pd.DataFrame(data)

# drop columns with NaN
df_clean = df.dropna(axis=1)

# show the cleaned DataFrame
st.write(df_clean)
""")


#---------------------------------------------------------
# Question 4
#---------------------------------------------------------
elif selected_question == list_questions[3]:

    st.header("Question 4")
    st.markdown("4. Remove outliers from DataFrame")

    data = {
        "Student": ["A","B","C","D","E","F","G","H","I","J"],
        "Marks": [45, 50, 52, 48, 49, 51, 47, 53, 200, 5]
    }

    # create a DataFrame
    df = pd.DataFrame(data)

    st.subheader("Original DataFrame")
    st.write(df)

    # calculate IQR method
    Q1 = df["Marks"].quantile(0.25)
    Q3 = df["Marks"].quantile(0.75)

    # calculate IQR 
    IQR = Q3 - Q1

    # calculate lower and upper bound
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # remove outliers
    remove_out = df[
        (df["Marks"] >= lower_bound) &
        (df["Marks"] <= upper_bound)
    ]

    # show the cleaned DataFrame
    st.subheader("After Removing Outliers")
    st.write(remove_out)

    if st.button("Show Solution Code"):
        st.code("""
import pandas as pd

data = {
    "Student": ["A","B","C","D","E","F","G","H","I","J"],
    "Marks": [45, 50, 52, 48, 49, 51, 47, 53, 200, 5]
}

# create a DataFrame
df = pd.DataFrame(data)

# calculate IQR method
Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)

# calculate IQR
IQR = Q3 - Q1

# calculate lower and upper bound
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# remove outliers
remove_out = df[
    (df["Marks"] >= lower_bound) &
    (df["Marks"] <= upper_bound)
]

# show the cleaned DataFrame
st.write(remove_out)
""")


#---------------------------------------------------------
# Question 5
#---------------------------------------------------------
elif selected_question == list_questions[4]:

    st.header("Question 5")
    st.markdown("5. Remove duplicates from DataFrame")

    data = {
        "A": ["TeamA", "TeamB", "TeamB", "TeamC", "TeamA"],
        "B": [50, 40, 40, 30, 50],
        "C": [True, False, False, False, True]
    }


    df = pd.DataFrame(data)

    st.subheader("Original DataFrame")
    st.write(df)

    # remove duplicates
    remove_dup = df.drop_duplicates()

    # reset index
    remove_dup = remove_dup.reset_index(drop=True)

    st.subheader("After Removing Duplicates")
    st.write(remove_dup)

    if st.button("Show Solution Code"):
        st.code("""
import pandas as pd

data = {
    "A": ["TeamA", "TeamB", "TeamB", "TeamC", "TeamA"],
    "B": [50, 40, 40, 30, 50],
    "C": [True, False, False, False, True]
}

# create a DataFrame    
df = pd.DataFrame(data)

# remove duplicates
remove_dup = df.drop_duplicates()

# reset index
remove_dup = remove_dup.reset_index(drop=True)

# show the cleaned DataFrame
st.write(remove_dup)
""")


#---------------------------------------------------------
# Question 6
#---------------------------------------------------------
elif selected_question == list_questions[5]:

    st.header("Question 6")
    st.markdown("6. Remove mpg and cylinders columns from uploaded CSV")
    
    st.warning("Upload auto-mpg.csv File")

    file = st.file_uploader(
        "Choose CSV File",
        type=["csv"]
    )

    if file is not None:

        try:
            df = pd.read_csv(file)

            st.subheader("Original DataFrame")
            st.write(df)

            # drop columns mpg and cylinders
            df = df.drop(
                ["mpg", "cylinders"],
                axis=1
            )

            st.subheader("After Removing Columns")
            st.write(df)

        except Exception as e:
            st.error(f"Error: {e}")

    if st.button("Show Solution Code"):
        st.code("""
import pandas as pd

# upload auto-mpg.csv file
file = st.file_uploader(
    "Choose CSV File",
    type=["csv"]
)

# drop columns mpg and cylinders
if file is not None:
    df = pd.read_csv(file)

    df = df.drop(
        ["mpg", "cylinders"],
        axis=1
    )

    st.write(df)
""")

#---------------------------------------------------------
# Question 7
#---------------------------------------------------------
elif selected_question == list_questions[6]:

    st.header("Question 7")

    st.markdown("7.  Use the file heights_weights.csv which contains 10000 non-null values for heights and weights. The Male column shows 1 if the person is a Male and 0 if the person is a Female.")

    st.warning("Upload heights_weights.csv File")
    file = st.file_uploader(
        "Choose CSV File",
        type=["csv"]
    )

    if file is not None:

        df = pd.read_csv(file)
        st.info("Click button to show DataFrame")
    

        if st.button("1.Convert this file into a pandas Data Frame. (0.5 marks)"):

            st.subheader("Original DataFrame")
            st.write(df)

        if st.button("2. Display basic information like memory and data types for this data frame. (0.5 marks)"):

            st.subheader("Data Types")
            st.write(df.dtypes)

            st.subheader("Memory Usage")
            st.write(df.memory_usage())

        if st.button("3.Display basic statistics like mean, std, quartiles, etc. for this data frame. (0.5 marks)"):

            st.subheader("Basic Statistics")
            st.write(df.describe())

        if st.button("4.Create a correlation table for the data frame and comment about what kind of correlation is there between Height and Weight. (0.5 marks)"):

            st.subheader("Correlation Table")
            st.write(df[["Height", "Weight"]].corr())
        
        if st.button("5.Do Height and Weight contain any outliers? (1 mark)"):
            # show outliers IOR method and contains outliers
            Q1 = df['Height'].quantile(0.25)
            Q3 = df['Height'].quantile(0.75)

            IQR = Q3 - Q1

            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            hig_out = df["Height"][
                (df['Height'] < lower) | (df['Height'] > upper)
            ]
            st.success(f"Height Outliers : {hig_out.shape[0]}")


            # Weight Outliers

            Q1 = df['Weight'].quantile(0.25)
            Q3 = df['Weight'].quantile(0.75)

            IQR = Q3 - Q1

            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            wei_out = df["Weight"][
                (df['Weight'] < lower) | (df['Weight'] > upper)
            ]
            st.success(f"Weight Outliers : {wei_out.shape[0]}")

        if st.button("Show Solution Code"):
            st.code("""
import streamlit as st
import pandas as pd
        

# upload heights_weights.csv file
file = st.file_uploader(
    "Choose CSV File",
    type=["csv"]
)

# drop columns mpg and cylinders
if file is not None:
    data = pd.read_csv(file)
                        
    #1.Convert this file into a pandas Data Frame. (0.5 marks)
     df=pd.DataFrame(data)
    
    #2.Display basic information like memory and data types for this data frame. (0.5 marks)
    st.write(df.dtypes)
    st.write(df.memory_usage())
    
    #3.Display basic statistics like mean, std, quartiles, etc. for this data frame. (0.5 marks)
    st.write(df.describe())
    
    #4. Create a correlation table for the data frame and comment about what kind of correlation is there between Height and Weight. (0.5 marks)
    st.write(df[["Height", "Weight"]].corr())
    
    #5. Do Height and Weight contain any outliers? (1 mark)
    Q1 = df['Height'].quantile(0.25)
    Q3 = df['Height'].quantile(0.75
    IQR = Q3 - Q
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQ
    hig_out = df["Height"][
        (df['Height'] < lower) | (df['Height'] > upper)
    ]
    st.success(f"Height Outliers : {hig_out.shape[0]}")
    # Weight Outlier
    Q1 = df['Weight'].quantile(0.25)
    Q3 = df['Weight'].quantile(0.75
    IQR = Q3 - Q
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQ
    wei_out = df["Weight"][
        (df['Weight'] < lower) | (df['Weight'] > upper)
    
    st.success(f"Weight Outliers : {wei_out.shape[0]}")
                        
""")

#---------------------------------------------------------
# Question 8
#---------------------------------------------------------
elif selected_question == list_questions[7]:
    st.header("Question 8")
    st.markdown("8 . Use the file ipl-matches.csv which contains data of all the IPL matches from year 2008 to 2022. Read this csv file and display the basic information like memory and data types for this data frame. Write python code for the following cases:")

    st.warning("Upload ipl-matches.csv File")

    file = st.file_uploader(
        "Choose CSV File",
        type=["csv"]
    )
    
    if file is not None:

        df = pd.read_csv(file)
        st.subheader("Original DataFrame")
        st.write(df)
        st.write("----")
        st.subheader("display the basic information like memory and data types for this data frame.")
        st.subheader("Data Types")
        st.write(df.dtypes)
        st.subheader("Memory Usage")
        st.write(df.memory_usage())

        st.info("Click button to show DataFrame")

        if st.button("1.List out all matches gone in superovers"):
            super_over=df[df["SuperOver"]=="Y"]
            st.write(super_over)
        
        if st.button("2. How Many Matches won by Chennai Super Kings at Kolkata."):
            won_csk=df[
                (df["Team1"]=="Chennai Super Kings")&
                (df["City"]=="Kolkata")&
                (df["WinningTeam"]=="Chennai Super King")
            ]
            st.subheader("Matches won by Chennai Super Kings at Kolkata :\n")
            st.success(f"Matches won by Chennai Super Kings at Kolkata : {won_csk.shape[0]}")

        if st.button("3. In How Many Matches MS Dhoni is Player of Match Vs Mumbai Indians."):
            pom_ms = df[
            (
                ((df['Team1'] == 'Chennai Super Kings') & (df['Team2'] == 'Mumbai Indians')) |
                ((df['Team1'] == 'Mumbai Indians') & (df['Team2'] == 'Chennai Super Kings'))
            ) &
            (df['Player_of_Match'] == 'MS Dhoni')
            ]
            st.subheader("ms dhoni is Player of Match Vs Mumbai Indians :\n")
            st.write(pom_ms)
            st.success(f"ms dhoni is Player of Match Vs Mumbai Indians: {pom_ms.shape[0]}")
        
        if st.button("4.display list of all matches in which Gujarat Titans won the Toss and Elected to Bat and won the match."):
            gt_bat_and_win=df[
                (df["TossWinner"]=="Gujarat Titans")&
                (df["TossDecision"]=="bat")&
                (df["WinningTeam"]=="Gujarat Titans")
            ]
            st.subheader("Gujarat Titans won the Toss and Elected to Bat and won the match :")
            st.write(gt_bat_and_win)
            st.success(f"Gujarat Titans won the Toss and Elected to Bat and won the match : {gt_bat_and_win.shape[0]}")
        
        if st.button("5. Display list of all matches won by Gujarat Titans"):
            won_gt=df[
                (df["WinningTeam"]=="Gujarat Titans")
            ]
            st.subheader("matches won by Gujarat Titans:")
            st.write(won_gt)
            st.success(f"matches won by Gujarat Titans : {won_gt.shape[0]}")

        
        if st.button("Show Solution Code"):
            st.code("""
import pandas as 
import streamlit as st

# upload ipl-matches.csv file
file = st.file_uploader(
    "Choose CSV File",
    type=["csv"]
)
if file is not None:
    df = pd.read_csv("ipl-matches.csv)

    st.subheader("Original DataFrame")
    st.write(df)
    st.write("----")
    # basic information like memory and data types for this data frame
    st.subheader("Data Types")
    st.write(df.dtypes)
    st.subheader("Memory Usage")
    st.write(df.memory_usage())
                        
    #1. List out all matches gone in superovers
    super_over=df[df["SuperOver"]=="Y"]
    st.write(super_over)
                        
    #2.How Many Matches won by Chennai Super Kings at Kolkata
    won_csk=df[
                (df["Team1"]=="Chennai Super Kings")&
                (df["City"]=="Kolkata")&
                (df["WinningTeam"]=="Chennai Super King")
            ].shape[0]
    st.success(f"Matches won by Chennai Super Kings at Kolkata : {won_csk}")
                        
    #3. In How Many Matches MS Dhoni is Player of Match Vs Mumbai Indians
    pom_ms = df[
    (
        ((df['Team1'] == 'Chennai Super Kings') & (df['Team2'] == 'Mumbai Indians')) |
        ((df['Team1'] == 'Mumbai Indians') & (df['Team2'] == 'Chennai Super Kings'))
    ) &
    (df['Player_of_Match'] == 'MS Dhoni')
    ].shape[0]
    st.success(f"ms dhoni is Player of Match Vs Mumbai Indians: {pom_ms}")

    #4.display list of all matches in which Gujarat Titans won the Toss and Elected to Bat and won the match
    gt_bat_and_win=df[
        (df["TossWinner"]=="Gujarat Titans")&    
        (df["TossDecision"]=="bat")&
        (df["WinningTeam"]=="Gujarat Titans")
    ]
    st.success(f"Gujarat Titans won the Toss and Elected to Bat and won the match : {gt_bat_and_win.shape[0]}")

    #5.Display list of all matches won by Gujarat Titans
    won_gt=df[
        (df["WinningTeam"]=="Gujarat Titans")
    ].shape[0]
    st.success(f"matches won by Gujarat Titans : {won_gt}")
""")

#---------------------------------------------------------
# Question 9
#---------------------------------------------------------

elif selected_question == list_questions[8]:
    st.header("Question 9")
    st.markdown("9. Use the file spotify.csv and answer the following questions.")

    st.warning("Upload spotify.csv File")
    file = st.file_uploader(
        "Choose CSV File",
        type=["csv"]
    )

    if file is not None:
        df = pd.read_csv(file)
        st.info("Click button to show DataFrame")
    

        if st.button("1.Convert this file into a pandas Data Frame."):

            st.subheader("Original DataFrame")
            st.write(df)
        
        if st.button("2.Display basic information like memory and data types for this data frame."):

            st.subheader("Data Types")
            st.write(df.dtypes)

            st.subheader("Memory Usage")
            st.write(df.memory_usage())

        if st.button("3.Display basic statistics like mean, std, quartiles, etc. for this data frame."):

            st.subheader("Basic Statistics")
            st.write(df.describe())

        if st.button("4.Create a correlation table for the data frame and comment about what kind of correlation is there between danceability and energy ."):
            corr_table=df[['danceability', 'energy']].corr()
            st.write(f"Create a correlation table for the data frame :\n")
            st.write(corr_table)
        
        if st.button("5. Display first five rows for this data frame."):
            st.write(df.head())
        
        if st.button("6. Display last five rows for this data frame."):
            st.write(df.tail())

        if st.button("7.isplay the rows between 15 to 39 for this data frame."):
            st.write(df.iloc[15:40])
        
        if st.button("8.Display the data only for last five rows and last five columns for this data frame."):
            st.write(df.iloc[-5:,-5:])
        
        if st.button("9. Display the shape for this data frame."):
            st.success(f"the shape for this data frame : {df.shape}")
    
        if st.button("10 Display the sum of NULL values for all the columns."):
            st.write(df.isnull().sum())
        
        if st.button("11 Remove first 3 columns from this Data Frame."):
            st.write(df.iloc[:,3:])
        
        if st.button("12 . Remove first 10 rows from this Data Frame. "):
            st.write(df.iloc[11:])

        if st.button("13.After removing first 3 columns and first 10 rows from this data frame find outliers for the column popularity."):
            new_df = df.iloc[10:, 3:]

            Q1 = new_df["popularity"].quantile(0.25)
            Q3 = new_df["popularity"].quantile(0.75)

            st.success(f"Q1 : {Q1}")
            st.success(f"Q3 : {Q3}")


            iqr = Q3 - Q1
            st.success(f" Iqr :{iqr}")

            lower = Q1 - 1.5 * iqr
            upper = Q3 + 1.5 * iqr


            outliers = new_df[(new_df["popularity"] < lower) | 
                            (new_df["popularity"] > upper)]

            st.write("Outliers in popularity column:")
            st.write(outliers)
            
        if st.button("14.After removing first 3 columns and first 10 rows from this data frame remove outliers for the column energy then display the data frame."):
            new_df = df.iloc[10:, 3:]
            Q1 = new_df["energy"].quantile(0.25)
            Q3 = new_df["energy"].quantile(0.75)

            st.success(f"Q1 : {Q1}")
            st.success(f"Q3 : {Q3}")


            iqr = Q3 - Q1
            st.success(f" Iqr :{iqr}")

            lower = Q1 - 1.5 * iqr
            upper = Q3 + 1.5 * iqr


            outliers = new_df[(new_df["energy"] < lower) | 
                            (new_df["energy"] > upper)]

            st.write("Outliers in energy column:")
            st.write(outliers)
        
        if st.button("15.Display cross tabulation between time_signature and track_genre for actual Data Frame. "):
            st.write(pd.crosstab(df["time_signature"], df["track_genre"]))

        if st.button("Show Solution Code"):
            st.code(""" 
import streamlit as st
import pandas as pd
        

# upload spotify.csv file
file = st.file_uploader(
    "Choose CSV File",
    type=["csv"]
)
if file is not None:
    # 1.Convert this file into a pandas Data Frame.
    df = pd.read_csv(file)
    st.write(df)

    # 2.Display basic information like memory and data types for this data frame.
    st.write(df.dtypes)
    st.write(df.memory_usage())

    # 3.Display basic statistics like mean, std, quartiles, etc. for this data frame.
    st.write(df.describe())

    # 4.Create a correlation table for the data frame and comment about what kind of correlation is there between danceability and energy .
    corr_table=df[['danceability', 'energy']].corr()
    st.write(f"Create a correlation table for the data frame :")
    st.write(corr_table)

    # 5.Display first five rows for this data frame.
    st.write(df.head())

    # 6.Display last five rows for this data frame.
    st.write(df.tail())

    # 7.isplay the rows between 15 to 39 for this data frame.
    st.write(df.iloc[15:40])

    # 8.Display the data only for last five rows and last five columns for this data frame. 
    st.write(df.iloc[-5:,-5:])

    # 9. Display the shape for this data frame. 
    st.success(f"the shape for this data frame : {df.shape}")

    # 10 Display the sum of NULL values for all the columns.
    st.write(df.isnull().sum())

    # 11 Remove first 3 columns from this Data Frame.   
    st.write(df.iloc[:,3:])

    # 12 . Remove first 10 rows from this Data Frame.   
    st.write(df.iloc[11:])

    # 13.After removing first 3 columns and first 10 rows from this data frame find outliers for the column popularity. 
    new_df = df.iloc[10:, 3:]

    Q1 = new_df["popularity"].quantile(0.25)
    Q3 = new_df["popularity"].quantile(0.75)

    st.success(f"Q1 : {Q1}")
    st.success(f"Q3 : {Q3}")


    iqr = Q3 - Q1
    st.success(f" Iqr :{iqr}")

    lower = Q1 - 1.5 * iqr
    upper = Q3 + 1.5 * iqr


    outliers = new_df[(new_df["popularity"] < lower) | 
                    (new_df["popularity"] > upper)]

    st.write("Outliers in popularity column:")
    st.write(outliers)

    # 14.After removing first 3 columns and first 10 rows from this data frame remove outliers for the column energy then display the data frame. 
    new_df = df.iloc[10:, 3:]
    Q1 = new_df["energy"].quantile(0.25)
    Q3 = new_df["energy"].quantile(0.75)

    st.success(f"Q1 : {Q1}")
    st.success(f"Q3 : {Q3}")


    iqr = Q3 - Q1
    st.success(f" Iqr :{iqr}")

    lower = Q1 - 1.5 * iqr
    upper = Q3 + 1.5 * iqr


    outliers = new_df[(new_df["energy"] < lower) | 
                    (new_df["energy"] > upper)]

    st.write("Outliers in energy column:")
    st.write(outliers)

    # 15.Display cross tabulation between time_signature and track_genre for actual Data Frame. 
    st.write(pd.crosstab(df["time_signature"],df["track_genre"]))
                        
    """)
        
#----------------------
# Questions 10
# ---------------------

elif selected_question == list_questions[9]:
    st.header("Question 10")
    st.markdown("10.Read this csv file car data.csv and display the basic information like memory and data types for this data frame.")

    st.warning("car data.csv File")
    file = st.file_uploader(
        "Choose CSV File",
        type=["csv"]
    )

    if file is not None:
        df = pd.read_csv(file)

        st.subheader("Original DataFrame")
        st.write(df)

        if st.button("1.How Many ritz car are there with kms driven more than 30000km."):
            Ritz_car = df[
                (df["Car_Name"]=="ritz")&
                (df["Kms_Driven"]>30000)
            ].shape[0]
            st.success(f"Ritz car are there with kms driven more than 30000km :- {Ritz_car} ")
        
        if st.button("2.How many Petrol cars are of the year 2017 and whose selling price > 10 lakhs."):
            Petrol_car = df[
                (df["Year"]==2017)&
                (df["Fuel_Type"]=="Petrol")&
                (df["Selling_Price"]>10)
            ].shape[0]
            st.success(f"Petrol cars are of the year 2017 and whose selling price > 10 lakhs :- {Petrol_car} ")

        if st.button("3.How many swift cars are there with selling price < 4 Lakhs."):
            swift_car = df[
                (df["Car_Name"]=="swift")&
                (df["Selling_Price"]<4)
            ].shape[0]
            st.success(f"swift cars are there with selling price < 4 Lakhs :- {swift_car} ")
        
        if st.button("4..How many Automatic Transmission Petrol Car are of the year 2015 whose selling price is > 10 Lakhs."):
            Petrol_car = df[
                (df["Transmission"]=="Automatic")&
                (df["Fuel_Type"]=="Petrol")&
                (df["Year"]==2015)&
                (df["Selling_Price"]>10)
            ].shape[0]
            st.success(f"Automatic Transmission Petrol Car are of the year 2015 whose selling price is > 10 Lakhs :- {Petrol_car} ")

        if st.button("5.List out Vehicles with Automatic Transmission and selling price < 1 Lakh."):
            Petrol_car = df[
                (df["Transmission"]=="Automatic")&
                (df["Selling_Price"]<1)
            ]
            st.subheader("List out Vehicles with Automatic Transmission and selling price < 1 Lakh :\n")
            st.write(Petrol_car)
            st.success(f"List out Vehicles with Automatic Transmission and selling price < 1 Lakh :- {Petrol_car.shape[0]}")
        
        if st.button("6.How Many Petrol Vehicles are there with kms driven more than 50000kms and Year is between 2010 to 2015(both Year included)."):
            Petrol_car = df[
                (df["Fuel_Type"]=="Petrol")&
                (df["Year"].between(2010,2015))&
                (df["Kms_Driven"]>50000)
            ].shape[0]
            st.success(f"Petrol Vehicles are there with kms driven more than 50000kms and Year is between 2010 to 2015(both Year included) :- {Petrol_car} ")
        
        if st.button("7.List out the cars whose price difference between present price and selling price is > 15 lakhs"):
            Petrol_car = df[
                (df["Present_Price"]-df["Selling_Price"])>15
            ]
            st.subheader("List out the cars whose price difference between present price and selling price is > 15 lakhs :\n")
            st.write(Petrol_car)
            st.success(f"List out the cars whose price difference between present price and selling price is > 15 lakhs :- {Petrol_car.shape[0]}")
        
        if st.button("8.How many Petrol vehicles are there whose kms driven < 5000km and selling price < 50000."):
            Petrol_car = df[
                (df["Fuel_Type"]=="Petrol")&
                (df["Kms_Driven"]<5000)&
                (df["Selling_Price"]<5)
            ].shape[0]
            st.success(f"Petrol vehicles are there whose kms driven < 5000km and selling price < 50000 :- {Petrol_car} ")
        
        if st.button("show Solution Code"):
            st.code("""

import pandas as pd
import numpy as 
                
st.warning("car data.csv File")
file = st.file_uploader(
    "Choose CSV File",
    type=["csv"]
)
if file is not None:
    df = pd.read_csv(file)

    st.subheader("Original DataFrame")
    st.write(df)

    # 1.How Many ritz car are there with kms driven more than 30000km.
    Ritz_car = df[
        (df["Car_Name"]=="ritz")&
        (df["Kms_Driven"]>30000)
    ].shape[0]
    st.success(f"Ritz car are there with kms driven more than 30000km :- {Ritz_car} ")

    # 2.How many Petrol cars are of the year 2017 and whose selling price > 10 lakhs.
    Petrol_car = df[
        (df["Year"]==2017)&
        (df["Fuel_Type"]=="Petrol")&
        (df["Selling_Price"]>10)
    ].shape[0]
    st.success(f"Petrol cars are of the year 2017 and whose selling price > 10 lakhs :- {Petrol_car} ")

    # 3.How many Swift cars are there with selling price < 4 Lakhs.
    Swift_car = df[
        (df["Car_Name"]=="swift")&
        (df["Selling_Price"]<4)
    ].shape[0]

    # 4..How many Automatic Transmission Petrol Car are of the year 2015 whose selling price is > 10 Lakhs.
    Petrol_car = df[
        (df["Transmission"]=="Automatic")&
        (df["Fuel_Type"]=="Petrol")&
        (df["Year"]==2015)&
        (df["Selling_Price"]>10)
    ].shape[0]
    st.success(f"Automatic Transmission Petrol Car are of the year 2015 whose selling price is > 10 Lakhs :- {Petrol_car} ")

    # 5.List out Vehicles with Automatic Transmission and selling price < 1 Lakh.
    Petrol_car = df[
        (df["Transmission"]=="Automatic")&
        (df["Selling_Price"]<1)
    ]
    st.subheader("List out Vehicles with Automatic Transmission and selling price < 1 Lakh :\n")
    st.write(Petrol_car)
    st.success(f"List out Vehicles with Automatic Transmission and selling price < 1 Lakh :- {Petrol_car.shape[0]}")

    # 6.How Many Petrol Vehicles are there with kms driven more than 50000kms and Year is between 2010 to 2015(both Year included).
    Petrol_car = df[
        (df["Fuel_Type"]=="Petrol")&
        (df["Year"]>2010)&
        (df["Year"]<2015)&
        (df["Kms_Driven"]>50000)
    ].shape[0]
    st.success(f"Petrol Vehicles are there with kms driven more than 50000kms and Year is between 2010 to 2015(both Year included) :- {Petrol_car} ")

    # 7.List out the cars whose price difference between present price and selling price is > 15 lakhs.
    Petrol_car = df[
        (df["Present_Price"]-df["Selling_Price"])>15
    ]
    st.subheader("List out the cars whose price difference between present price and selling price is > 15 lakhs :\n")
    st.write(Petrol_car)
    st.success(f"List out the cars whose price difference between present price and selling price is > 15 lakhs :- {Petrol_car.shape[0]}")

    # 8.How many Petrol vehicles are there whose kms driven < 5000km and selling price < 50000.
    Petrol_car = df[
        (df["Fuel_Type"]=="Petrol")&
        (df["Kms_Driven"]<5000)&
        (df["Selling_Price"]<5)
    ].shape[0]
    st.success(f"Petrol vehicles are there whose kms driven < 5000km and selling price < 50000 :- {Petrol_car} ")
                """)

# ---------------------------------------------------------
# Question 11
# ---------------------------------------------------------

elif selected_question == list_questions[10]:
    st.header("Question 11")
    st.markdown("11.data_result.csv and python code for the following cases:")
    st.warning("Upload data_result.csv File")

    st.subheader(" 1. Load the dataset into a pandas DataFrame (data_result.csv)  and answer the following questions.")
    file = st.file_uploader(
        "Choose CSV File",
        type=["csv"]
    )

    if file is not None:
            df = pd.read_csv(file)

            st.subheader("Original DataFrame")
            st.write(df)

            if st.button("2. View the first few rows of the dataset "):
                st.write(df.head())
            
            if st.button("3.Check the shape of the dataset"):
                st.write(df.shape)

            if st.button("4. View the first last rows of the dataset"):
                st.write(df.tail())

            if st.button("5.  Get summary statistics of numerical columns"):
                st.write(df.describe())

            if st.button("6. Get summary statistics of numerical columns with 0.58 and 0.87 percentiles"):
                st.write(df.describe(percentiles=[0.58, 0.87]))

            if st.button("7. Get summary statistics of all types of columns"):
                st.write(df.describe(include="all"))

            if st.button("8.Information of all columns"):
                st.subheader("Data Types")
                st.write(df.dtypes)
                st.subheader("Memory Usage")
                st.write(df.memory_usage())


            if st.button("9.Check for missing values"):
                st.write(df.isnull().sum())

            if st.button("10.Removing duplicates if duplicates"):
                Remove_dup =df.drop_duplicates(inplace=True)
                st.write(Remove_dup)
                st.write(df)

            if st.button("11. List out female students who have greater than 7 spi in all semesters."):
                female_student= df[
                        (df["Gender"] == 'Female') &
                        (df["Sem1_SPI"] > 7) &
                        (df["Sem2_SPI"] > 7) &
                        (df["Sem3_SPI"] > 7) &
                        (df["Sem4_SPI"] > 7) &
                        (df["Sem5_SPI"] > 7)
                    ]
                st.write(female_student)
            
            if st.button("12. Find number of  students those who have greater than 8 spi in all 5 semesters."):
                student=df[
                        (df["Sem1_SPI"] > 8) &
                        (df["Sem2_SPI"] > 8) &
                        (df["Sem3_SPI"] > 8) &
                        (df["Sem4_SPI"] > 8) &
                        (df["Sem5_SPI"] > 8)
                    ]

                st.write(student)
                st.success(f"Number of  students those who have greater than 8 spi in all 5 semesters :- {student.shape[0]}")       

            if st.button("13.Find outliers of sem 4 result. Also represent statistical analysis with visualization.(boxplot)Calculate Q1 and Q3"):
                # statistical analysis 
                Q1 = df['Sem4_SPI'].quantile(0.25)
                Q3 = df['Sem4_SPI'].quantile(0.75)

                st.success(f"Q1 : {Q1}")
                st.success(f"Q3 : {Q3}")

                IQR = Q3 - Q1
                st.success(f"IQR : {IQR}")
                lower = Q1 - 1.5 * IQR
                upper = Q3 + 1.5 * IQR

                outliers = df["Sem4_SPI"][
                    (df['Sem4_SPI'] < lower) | (df['Sem4_SPI'] > upper)
                ]

                st.write(outliers)
                st.success(f"Outliers : {outliers.shape[0]}")

                # visualization.(boxplot)Calculate

                fig, ax = plt.subplots(figsize=(8, 2))
                sns.boxplot(x=df['Sem4_SPI'], ax=ax, color='skyblue')
                ax.set_title("Boxplot of Sem4_SPI")
                st.pyplot(fig)
                    
    
            if st.button("show Solution Code"):
                st.code("""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
                        
# 1. Load the dataset into a pandas DataFrame (data_result.csv)  and answer the following questions.
file = st.file_uploader(
"Choose CSV File",
type=["csv"]
)
if file is not None:
    df = pd.read_csv(file)

    st.subheader("Original DataFrame")
    st.write(df)

    #2. View the first few rows of the dataset
    st.write(df.head())

    #3.Check the shape of the dataset
    st.write(df.shape)

    #4. View the first last rows of the dataset
    st.write(df.tail())

    #5.  Get summary statistics of numerical columns
    st.write(df.describe())

    #6. Get summary statistics of numerical columns with 0.58 and 0.87 percentiles
    st.write(df.describe(percentiles=[0.58, 0.87]))

    #7. Get summary statistics of all types of columns
    st.write(df.describe(include="all"))

    # 8.Information of all columns   
    st.subheader("Data Types")
    st.write(df.dtypes)
    st.subheader("Memory Usage")
    st.write(df.memory_usage())     

    #9.Check for missing values
    st.write(df.isnull().sum())

    #10.Removing duplicates if duplicates
    Remove_dup =df.drop_duplicates(inplace=True)
    st.write(Remove_dup)
    st.write(df)

    #11. List out female students who have greater than 7 spi in all semesters.
    female_student= df[
            (df["Gender"] == 'Female') &
            (df["Sem1_SPI"] > 7) &
            (df["Sem2_SPI"] > 7) &
            (df["Sem3_SPI"] > 7) &
            (df["Sem4_SPI"] > 7) &
            (df["Sem5_SPI"] > 7)
    ]
    st.write(female_student)
                            
    #12. Find number of  students those who have greater than 8 spi in all 5 semesters.
    student=df[
            (df["Sem1_SPI"] > 8) &
            (df["Sem2_SPI"] > 8) &
            (df["Sem3_SPI"] > 8) &
            (df["Sem4_SPI"] > 8) &
            (df["Sem5_SPI"] > 8)
    ]
    st.write(student)
    st.success(f"Number of  students those who have greater than 8 spi in all 5 semesters :- {student.shape[0]}")

    #13.Find outliers of sem 4 result. Also represent statistical analysis with visualization.(boxplot)Calculate Q1 and Q3
    Q1 = df['Sem4_SPI'].quantile(0.25)
    Q3 = df['Sem4_SPI'].quantile(0.75)

    st.success(f"Q1 : {Q1}")
    st.success(f"Q3 : {Q3}")

    IQR = Q3 - Q1
    st.success(f"IQR : {IQR}")
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df["Sem4_SPI"][
        (df['Sem4_SPI'] < lower) | (df['Sem4_SPI'] > upper)
    ]

    st.write(outliers)
    st.success(f"Outliers : {outliers.shape[0]}")

    # visualization.(boxplot)Calculate

    fig, ax = plt.subplots(figsize=(8, 2))
    sns.boxplot(x=df['Sem4_SPI'], ax=ax, color='skyblue')
    ax.set_title("Boxplot of Sem4_SPI")
    st.pyplot(fig)

                """)


#------------
# Question 12
#------------

elif selected_question == list_questions[11]:
    st.header("Question 12")
    st.markdown("12. Use the file movies.csv which contains 1629 rows and 18 columns. Read this csv file and display the basic information like memory and data types for this data frame. ")

    st.warning("Upload movies.csv File")
    file = st.file_uploader(
        "Choose CSV File",
        type=["csv"]
    )

    if file is not None:
            df = pd.read_csv(file)

            st.subheader("Original DataFrame")
            st.write(df)

            if st.button("1.List out Movies Released in Year 2019."):
               movies_2019 = df[df["year_of_release"] == 2019]
               st.write(movies_2019)
               st.success(f"Movies Released in Year 2019 : {movies_2019.shape[0]}")

            if st.button("2.How Many Movies are having IMDB Rating > 7 (Display Number of Movies)."):
                movie_imdb = df[df["imdb_rating"] > 7].shape[0]
                st.success(f" Number of Movies are having IMDB Rating > 7 : {movie_imdb}")

            if st.button("3.List out the Movies with ‘title’ and ‘story’ whose IMDB Votes > 20000."):
                movie_imdb = df[
                    (df["imdb_votes"]>20000)&
                    (df["story"]!="Nan")
                ][["original_title","story"]]
                st.write("Movies with IMDB Votes > 20000 :",movie_imdb)
                st.success(f"Number of Movies with IMDB Votes > 20000 : {movie_imdb.shape[0]}")
            
            if st.button("4.List out Movies Released in Year 2018, Display only Movie Title with Release Date of Year 2018 Movies."):

                movies_2018 = df[df["year_of_release"] == 2018][["original_title","release_date"]]
                st.write(movies_2018)
                st.success(f"Movies Released in Year 2018 : {movies_2018.shape[0]}")
    
            if st.button("5.Display only Movie Title with its Wikipedia Link."):
                result = df[["original_title", "wiki_link"]]
                st.write(result)
                st.success(f"Display only Movie Title with its Wikipedia Link : {result.shape[0]}")

            if st.button("show Solution Code"):
                st.code("""
import streamlit as st  
import pandas as pd
import numpy as np

#Upload ipl-matches.csv File
file = st.file_uploader(
"Choose CSV File",
type=["csv"]
)
if file is not None:
st.warning("Upload movies.csv File")
file = st.file_uploader(
    "Choose CSV File",
    type=["csv"]
)


if file is not None:
    df = pd.read_csv(file)

    st.subheader("Original DataFrame")
    st.write(df)
                        
    # 1.List out Movies Released in Year 2019.
    movies_2019 = df[df["year_of_release"] == 2019]
    st.write(movies_2019)
    st.success(f"Movies Released in Year 2019 : {movies_2019.shape[0]}")

    #2.How Many Movies are having IMDB Rating > 7 (Display Number of Movies).
    movie_imdb = df[df["imdb_rating"] > 7].shape[0]
    st.success(f" Number of Movies are having IMDB Rating > 7 : {movie_imdb}")

    #3.List out the Movies with ‘title’ and ‘story’ whose IMDB Votes > 20000.
    movie_imdb = df[
        (df["imdb_votes"]>20000)&
        (df["story"]!="Nan")
    ][["original_title","story"]]
    st.write("Movies with IMDB Votes > 20000 :",movie_imdb)
    st.success(f"Number of Movies with IMDB Votes > 20000 : {movie_imdb.shape[0]}")

    #4.List out Movies Released in Year 2018, Display only Movie Title with Release Date of Year 2018 Movies.
    movies_2018 = df[df["year_of_release"] == 2018][["original_title","release_date"]]
    st.write(movies_2018)
    st.success(f"Movies Released in Year 2018 : {movies_2018.shape[0]}")

    #5.Display only Movie Title with its Wikipedia Link.
    result = df[["original_title", "wiki_link"]]
    st.write(result)
    st.success(f"Display only Movie Title with its Wikipedia Link : {result.shape[0]}")

""")

#------------
# Question 13
#------------

elif selected_question == list_questions[12]:
    st.header("Question 13")
    st.markdown("13.You are given a CSV file named ipl-matches.csv, which contains data of all Indian Premier League (IPL) matches played from the year 2008 to 2022.Read the dataset and display the basic information about the DataFrame.",)

    st.warning("Upload ipl-matches.csv File")
    file = st.file_uploader(
        "Choose CSV File",
        type=["csv"]
    )

    if file is not None:
        df = pd.read_csv(file)

        st.subheader("Original DataFrame")
        st.write(df)
 
        if st.button("1.How many matches were won by Gujarat Titans in a Super Over ?"):
            won_gt=df[
                (df["WinningTeam"]=="Gujarat Titans")&
                (df["SuperOver"]=="Y")
            ].shape[0]
            st.success(f"matches won by Gujarat Titans in a Super Over : {won_gt}")
        

        if st.button("2. How Many Matches won by Royal Challengers Bangalore Vs Kolkata Knight Riders."):
            won_rcb_vs_kkr=df[
                ((df["Team1"]=="Royal Challengers Bangalore")&
                (df["Team2"]=="Kolkata Knight Riders")|
                (df["Team1"]=="Kolkata Knight Riders")&
                (df["Team2"]=="Royal Challengers Bangalore"))&
                (df["WinningTeam"]=="Royal Challengers Bangalore")
            ].shape[0]
            st.success(f"matches won by Royal Challengers Bangalore Vs Kolkata Knight Riders : {won_rcb_vs_kkr}")
        
        if st.button("3.How many Matches won by Toss Winner of the Match."):
            won_tw=df[
                (df["TossWinner"] == df["WinningTeam"])
            ].shape[0]
            st.success(f"matches won by Toss Winner of the Match : {won_tw}"
                       
            )
        
        if st.button("4.In how many matches was the result decided by the D/L method and the match was won by wickets?"):
            won_dl=df[
                 (df["method"]=="D/L")&
                 (df["WonBy"]=="Wickets")
            ].shape[0]
            st.success(f"matches was the result decided by the D/L method and the match was won by wickets : {won_dl}")

        if st.button("5.In how many matches Toss won by Rajasthan Royals & Won the Match."):
            won_rr=df[
                (df["TossWinner"] == "Rajasthan Royals")&
                (df["WinningTeam"] == "Rajasthan Royals")
            ].shape[0]
            st.success(f"matches Toss won by Rajasthan Royals & Won the Match : {won_rr}")

        if st.button("6.In how many matches V Kohli declared player of the match against Chennai Super Kings."):
            v_kohli=df[
                (df["Player_of_Match"] == "V Kohli")&
                (df["Team2"] == "Chennai Super Kings")
            ].shape[0]
            st.success(f"In how many matches V Kohli declared player of the match against Chennai Super Kings : {v_kohli}")

        if st.button("7.Which Team is the Toss Winner of the Final match Played in Dubai?"):        
            final_dubai=df[
                (df["City"] == "Dubai") &
                (df["MatchNumber"] == "Final")
            ]["TossWinner"].unique()[0]

            st.success(f"Which Team is the Toss Winner of the Final match Played in Dubai : {final_dubai}")
        
        if st.button("8.List out the Finals played by Kolkata Knight Riders in which Toss Won by Kolkata Knight Riders in the Finals and choose to field."):
            final_kkr=df[
                ((df["Team1"]=="Kolkata Knight Riders")|
                (df["Team2"]=="Kolkata Knight Riders"))&
                (df["TossWinner"]=="Kolkata Knight Riders")&
                (df["MatchNumber"]=="Final")&
                (df["TossDecision"]=="field")
            ]
            st.write(final_kkr)
            st.success(f"List out the Finals played by Kolkata Knight Riders in which Toss Won by Kolkata Knight Riders in the Finals and choose to field : {final_kkr.shape[0]}")

        if st.button("show Solution Code"):
            st.code("""
import pandas as pd
import streamlit as st
                    
# upload ipl-matches.csv file
file = st.file_uploader(
"Choose CSV File",
type=["csv"]
)
if file is not None:
    df = pd.read_csv(file)
    st.subheader("Original DataFrame")
    st.write(df)
    #1.How many matches were won by Gujarat Titans in a Super Over ?
    won_gt=df[
        (df["WinningTeam"]=="Gujarat Titans")&
        (df["SuperOver"]=="Y")
    ].shape[0]
    st.success(f"matches won by Gujarat Titans in a Super Over : {won_gt}
                        
    #2. How Many Matches won by Royal Challengers Bangalore Vs Kolkata Knight Riders.
    won_rcb_vs_kkr=df[
        ((df["Team1"]=="Royal Challengers Bangalore")&
        (df["Team2"]=="Kolkata Knight Riders")|
        (df["Team1"]=="Kolkata Knight Riders")&
        (df["Team2"]=="Royal Challengers Bangalore"))&
        (df["WinningTeam"]=="Royal Challengers Bangalore")
    ].shape[0]
    st.success(f"matches won by Royal Challengers Bangalore Vs Kolkata Knight Riders : {won_rcb_vs_kkr}
                        
    #3.How many Matches won by Toss Winner of the Match.
    won_tw=df[
        (df["TossWinner"] == df["WinningTeam"])
    ].shape[0]
    st.success(f"matches won by Toss Winner of the Match : {won_tw}
                        
    #4.In how many matches was the result decided by the D/L method and the match was won by wickets?
    won_dl=df[
        (df["method"]=="D/L")&
        (df["WonBy"]=="Wickets")
    ].shape[0]
    st.success(f"matches was the result decided by the D/L method and the match was won by wickets : {won_dl}

    #5.In how many matches Toss won by Rajasthan Royals & Won the Match.
    won_rr=df[
        (df["TossWinner"] == "Rajasthan Royals")&
        (df["WinningTeam"] == "Rajasthan Royals")
    ].shape[0]
    st.success(f"matches Toss won by Rajasthan Royals & Won the Match : {won_rr}

    #6.In how many matches V Kohli declared player of the match against Chennai Super Kings.
    v_kohli=df[
        (df["Player_of_Match"] == "V Kohli")&
        (df["Team2"] == "Chennai Super Kings")
    ].shape[0]
    st.success(f"In how many matches V Kohli declared player of the match against Chennai Super Kings : {v_kohli}

    #7.Which Team is the Toss Winner of the Final match Played in Dubai?
    final_dubai=df[
        (df["City"] == "Dubai") &
        (df["MatchNumber"] == "Final")
    ]["TossWinner"].unique()[0]

    st.success(f"Which Team is the Toss Winner of the Final match Played in Dubai : {final_dubai}
            
    #8.List out the Finals played by Kolkata Knight Riders in which Toss Won by Kolkata Knight Riders in the Finals and choose to field.
    final_kkr=df[
        ((df["Team1"]=="Kolkata Knight Riders")|
        (df["Team2"]=="Kolkata Knight Riders"))&
        (df["TossWinner"]=="Kolkata Knight Riders")&
        (df["MatchNumber"]=="Final")&
        (df["TossDecision"]=="field")
    ]
    st.write(final_kkr)
    st.success(f"List out the Finals played by Kolkata Knight Riders in which Toss Won by Kolkata Knight Riders in the Finals and choose to field : {final_kkr.shape[0]}
            """)


#------------
# Question 14
#------------

elif selected_question == list_questions[13]:

    st.header("Question 14")
    st.markdown("""df = pd.DataFrame(data)\n
    Sort employees by Dept (Ascending) and Salary (Descending).\n
    After sorting, sort the index in descending order.\n
    Display the final DataFrame.
    """)
    data = {
        "EmpID":[101,102,103,104,105],
        "Dept":["IT","HR","IT","Finance","HR"],
        "Salary":[60000,45000,80000,75000,50000],
        "Age":[25,32,29,41,28]
    }

    df = pd.DataFrame(data)
    st.write("Original DataFrame")
    st.write(df)

    # Sort by Dept (ascending) and Salary (descending) and sort index in descending order
    st.write("Sorted DataFrame")
    df_sorted = df.sort_values(by=["Dept", "Salary"], ascending=[True, False]).sort_index(ascending=False)

 
    st.write(df_sorted)

    if st.button("show Solution Code"):
        st.code("""
data = {
    "EmpID":[101,102,103,104,105],
    "Dept":["IT","HR","IT","Finance","HR"],
    "Salary":[60000,45000,80000,75000,50000],
    "Age":[25,32,29,41,28]

df = pd.DataFrame(data)
st.write("Original DataFrame")
st.write(df
# Sort by Dept (ascending) and Salary (descending) and sort index in descending order
st.write("Sorted DataFrame")
df_sorted = df.sort_values(by=["Dept", "Salary"], ascending=[True, False]).sort_index(ascending=False
st.write(df_sorted)
        """)

#------------
# Question 15
#------------

elif selected_question == list_questions[14]:

    st.header("Question 15")
    st.markdown("""df = pd.DataFrame(data)\n
    Create a column Average using apply() row-wise.\n
    Create a column Grade based on:\n
    ≥ 80 → Distinction\n
    ≥ 60 → First\n
    Otherwise → Second\n
    Display final DataFrame.
    """)
    df = pd.DataFrame({
    "Student":["A","B","C","D"],
    "Math":[70,45,90,60],
    "Science":[75,40,85,55]
    })

    st.write("Original DataFrame")
    st.write(df)

    # Create a column Average using row-wise
    df["Total"]=df["Math"]+df["Science"]
    df["Average"]=df["Total"]/2


    #  Create a column Grade based on:

    df["Grade"]=np.where(df["Average"]>80 ,"Distinction",np.where(df["Average"]>60,"First","Second"))
    print("Display final DataFrame \n")

    st.write("Afater creation of new columns")
    st.write(df)

    if st.button("show Solution Code"):
        st.code("""
import numpy as np
import pandas as pd
import streamlit as st
df = pd.DataFrame({
    "Student":["A","B","C","D"],
    "Math":[70,45,90,60],
    "Science":[75,40,85,55]
})
st.write("Original DataFrame")
st.write(df)
# Create a column Average using row-wise
df["Total"]=df["Math"]+df["Science"]
df["Average"]=df["Total"]/2
#  Create a column Grade based on:
df["Grade"]=np.where(df["Average"]>80 ,"Distinction",np.where(df["Average"]>60,"First","Second"))
print("Display final DataFrame \n")
st.write("Afater creation of new columns")
st.write(df)
        """)

#------------
# Question 16
#------------

elif selected_question == list_questions[15]:

    st.header("Question 16")
    st.markdown("""16.Replace "Absent" with 0.\n
            Convert the column to integer type.\n
            Print mean marks.\n
            Print number of students scoring above 50. """)
    
    df = pd.DataFrame({
    "Marks":["50","60","Absent","70","Absent"]
    })

    st.write("Original DataFrame")
    st.write(df)

    # Replace "Absent" with 0
    df["Marks"] = df["Marks"].replace("Absent", 0)
    st.write("Replace 'Absent' with 0 : \n")
    st.write(df)

    # Convert the column to integer type
    df["Marks"] = df["Marks"].astype(int)


    # Print mean marks
    st.write("Mean Marks:", df["Marks"].mean())

    # Print number of students scoring above 50
    st.write("Number of students scoring above 50:", len(df[df["Marks"] > 50]))

    if st.button("show Solution Code"):
        st.code("""
import pandas as pd
import streamlit as st
                
df = pd.DataFrame({
    "Marks":["50","60","Absent","70","Absent"]
})
st.write("Original DataFrame")
st.write(df)
                
# Replace "Absent" with 0
df["Marks"] = df["Marks"].replace("Absent", 0)
st.write("Replace 'Absent' with 0 :")
st.write(df)
                
# Convert the column to integer type
df["Marks"] = df["Marks"].astype(int)
                
# Print mean marks
st.write("Mean Marks:", df["Marks"].mean())
# Print number of students scoring above 50
st.write("Number of students scoring above 50:", len(df[df["Marks"] > 50]))
                
""")

#------------
# Question 17
#------------

elif selected_question == list_questions[16]:

    st.header("Question 17")
    st.markdown("""17.Concatenate row-wise using outer join.\n
                Count total missing values.\n
                Sort the result by ID.\n
                Display the final DataFrame.""")
    df1 = pd.DataFrame({
        "ID":[1,2,3],
        "Name":["A","B","C"]
    })

    df2 = pd.DataFrame({
        "ID":[2,3,4],
        "Marks":[80,90,70]
    })

    st.subheader("First DataFrame")
    st.write(df1)

    st.subheader("Second DataFrame")
    st.write(df2)

    # Concatenate row-wise using outer join
    new_df=pd.merge(df1,df2,how="outer",on="ID")

    st.write("Concatenated DataFrame:")
    st.write(new_df)


    # Count total missing  NUll values
    miss_value=new_df.isnull().sum().sum()
    st.success(f"Total missing Null values : {miss_value}")

    # Sort the result by ID
    st.write("Sorted DataFrame by ID:")
    st.write(new_df.sort_values("ID"))

    if st.button("show Solution Code"):
        st.code("""
import pandas as pd
import streamlit as st
df1 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["A","B","C"]
})
df2 = pd.DataFrame({
    "ID":[2,3,4],
    "Marks":[80,90,70]
})
st.subheader("First DataFrame")
st.write(df1)
                
st.subheader("Second DataFrame")
st.write(df2)
                
# Concatenate row-wise using outer join
new_df=pd.merge(df1,df2,how="outer",on="ID")
st.write("Concatenated DataFrame:")
st.write(new_df)
                
# Count total missing  NUll values
miss_value=new_df.isnull().sum().sum()
st.success(f"Total missing Null values : {miss_value}")
                
# Sort the result by ID
st.write("Sorted DataFrame by ID:")
st.write(new_df.sort_values("ID"))
""")

#------------
# Question 18
#------------

elif selected_question == list_questions[17]:   

    st.header("Question 18")
    st.markdown("""18.Perform outer merge using indicator=True.\n
        Count:\n
        Students present in both tables\n
        Only in students\n
        Only in marks""")
    
    students = pd.DataFrame({
    "ID":[1,2,3,4],
    "Name":["A","B","C","D"]
    })
    marks = pd.DataFrame({
        "ID":[2,3,5],
        "Score":[85,90,75]
    })

    st.subheader("Students DataFrame")
    st.write(students)

    st.subheader("Marks DataFrame")
    st.write(marks)

    # Perform outer merge using indicator=True
    merged_df = pd.merge(students, marks, how="outer", indicator=True)

    st.subheader("Merged DataFrame:")
    st.write(merged_df)

    # Count
    st.subheader("Count:")
    # students present in both tables
    st.write("Students present in both tables:",merged_df[merged_df["_merge"] == "both"].shape[0])
    # Only in students
    st.write("Only in students:", merged_df[merged_df["_merge"] == "left_only"].shape[0])
    # Only in marks
    st.write("Only in marks:",merged_df[merged_df["_merge"] == "right_only"].shape[0])

    if st.button("show Solution Code"):
        st.code("""
import pandas as pd
import streamlit as st
students = pd.DataFrame({
    "ID":[1,2,3,4],
    "Name":["A","B","C","D"]
})
marks = pd.DataFrame({
    "ID":[2,3,5],
    "Score":[85,90,75]
})
st.subheader("Students DataFrame")
st.write(students)
                
st.subheader("Marks DataFrame")
st.write(marks)
                
# Perform outer merge using indicator=True
merged_df = pd.merge(students, marks, how='outer', indicator=True)
st.subheader("Merged DataFrame:")
st.write(merged_df)
                
# Count
st.subheader("Count:")
# students present in both tables
st.write("Students present in both tables:",merged_df[merged_df["_merge"] == "both"].shape[0])
# Only in students
st.write("Only in students:", merged_df[merged_df["_merge"] == "left_only"].shape[0])
# Only in marks
st.write("Only in marks:",merged_df[merged_df["_merge"] == "right_only"].shape[0])
""")

#------------
# Question 19
#------------

elif selected_question == list_questions[18]:   

    st.header("Question 19")
    st.markdown("19.Group by Dept.\nCalculate mean, median, and max salary using agg().)")

    df = pd.DataFrame({
    "Dept":["IT","IT","HR","HR","Finance","Finance"],
    "Salary":[50000,70000,40000,60000,80000,75000]
    })

    st.subheader("Original DataFrame")
    st.write(df)

    # Group by Dept and calculate mean, median, and max salary using agg()
    st.subheader("Grouped DataFrame:")
    st.write(df.groupby("Dept")["Salary"].agg(["mean", "median", "max"]))

    if st.button("show Solution Code"):
        st.code("""
import pandas as pd
import streamlit as st
df = pd.DataFrame({
    "Dept":["IT","IT","HR","HR","Finance","Finance"],
    "Salary":[50000,70000,40000,60000,80000,75000]
})
st.subheader("Original DataFrame")
st.write(df)
                
# Group by Dept and calculate mean, median, and max salary using agg()
st.subheader("Grouped DataFrame:")
st.write(df.groupby("Dept")["Salary"].agg(["mean", "median", "max"]))
        """)

#------------
# Question 20
#------------

elif selected_question == list_questions[19]:   

    st.header("Question 20")
    st.markdown("20.Calculate range (max - min) per team using groupby + apply.")

    df = pd.DataFrame({
    "Team":["A","A","A","B","B"],
    "Runs":[50,70,80,40,60]
    })

    st.subheader("Original DataFrame")
    st.write(df)

    # Calculate range (max - min) per team using groupby + apply
    st.subheader("Grouped DataFrame:")
    st.write(df.groupby("Team")["Runs"].max()-df.groupby("Team")["Runs"].min())

    if st.button("show Solution Code"):
        st.code("""
import pandas as pd
import streamlit as st
                
df = pd.DataFrame({
    "Team":["A","A","A","B","B"],
    "Runs":[50,70,80,40,60]
})
st.subheader("Original DataFrame")
st.write(df)
                
# Calculate range (max - min) per team using groupby + apply
st.subheader("Grouped DataFrame:")
st.write(df.groupby("Team")["Runs"].max()-df.groupby("Team")["Runs"].min())
        """)

#------------
# Question 21
#------------

elif selected_question == list_questions[20]:   

    st.header("Question 21")
    st.markdown("""21.Detect outliers using IQR method.\n
                Remove outliers.\n
                Print cleaned dataset.""")
    df = pd.DataFrame({
    "Salary":[20000,22000,21000,25000,24000,300000]
    })

    st.subheader("Original DataFrame")
    st.write(df)

    # Detect outliers using IQR method
    Q1 = df["Salary"].quantile(0.25)
    Q3 = df["Salary"].quantile(0.75)

    IQR=Q1-Q3
  
    lower=Q1-1.5*IQR
    upper=Q3+1.5*IQR

    outliers = df[
        (df["Salary"] >lower) |
        (df["Salary"] < upper)
    ]

    st.subheader("Outliers:")
    st.write(outliers)

 


    if st.button("show Solution Code"):
        st.code("""
import pandas as pd
import streamlit as st
df = pd.DataFrame({
    "Salary":[20000,22000,21000,25000,24000,300000]
})
st.subheader("Original DataFrame")
st.write(df)

# Detect outliers using IQR method
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR=Q1-Q3

lower=Q1-1.5*IQR
upper=Q3+1.5*IQR

outliers = df[
    (df["Salary"] >lower) |
    (df["Salary"] < upper)
]

st.write(outliers)
        """)
    
#------------
# Question 22 Baki question
#------------

elif selected_question == list_questions[21]:   

    st.header("Question 22")
    st.markdown("""Find number of unique cities per department.\n
        Take one random employee per department.\n
        Display results.""")

    df = pd.DataFrame({
    "Dept":["IT","IT","HR","HR","Finance","Finance"],
    "Employee":["A","B","C","D","E","F"],
    "City":["X","X","Y","Z","X","Y"]
    })

    st.subheader("Original DataFrame")
    st.write(df)

    if st.button("show Solution Code"):
        st.code("""
import pandas as pd
import streamlit as st
df = pd.DataFrame({
    "Dept":["IT","IT","HR","HR","Finance","Finance"],
    "Employee":["A","B","C","D","E","F"],
    "City":["X","X","Y","Z","X","Y"]
})
st.subheader("Original DataFrame")
st.write(df)
} 
""")

    
#------------
# Question 23 
#------------

elif selected_question == list_questions[22]:
    st.header("Question 23")
    st.markdown("""Create a new column TotalAmount = Price × Quantity using apply() row-wise.\n
        Sort the DataFrame by TotalAmount in descending order.\n
        Display the final DataFrame""")   
    
    df = pd.DataFrame({
    "Product":["P1","P2","P3","P4","P5"],
    "Price":[100,200,150,300,250],
    "Quantity":[5,2,4,1,3]
    })

    st.subheader("Original DataFrame")
    st.write(df)
    
    # create a new column TotalAmount = Price × Quantity
    df["TotalAmount"]=df["Price"]*df["Quantity"]

    st.write("New DataFrame with TotalAmount column:")
    st.write(df)

    # Sort the DataFrame by TotalAmount in descending order
    sort=df.sort_values(by="TotalAmount",ascending=False)
    st.write("Sorted DataFrame by TotalAmount:")
    st.write(sort)

    if st.button("show Solution Code"):
        st.code("""
import pandas as pd
import streamlit as st
df = pd.DataFrame({
    "Product":["P1","P2","P3","P4","P5"],
    "Price":[100,200,150,300,250],
    "Quantity":[5,2,4,1,3]
})
st.subheader("Original DataFrame")
st.write(df)
                
df["TotalAmount"]=df["Price"]*df["Quantity"]
st.write("New DataFrame with TotalAmount column:")
st.write(df
                )
sort=df.sort_values(by="TotalAmount",ascending=False)
st.write("Sorted DataFrame by TotalAmount:")
st.write(sort)
        """)

#------------
# Question 24
#------------

elif selected_question == list_questions[23]:
    st.header("Question 24")
    st.markdown("""Group employees by Department.\n
        Calculate total salary and average salary per department.\n
        Display departments where average salary is greater than 50,000.""")
    
    df = pd.DataFrame({
        "Employee":["A","B","C","D","E"],
        "Dept":["IT","HR","IT","Finance","HR"],
        "Salary":[50000,40000,70000,80000,45000]
    })

    st.subheader("Original DataFrame")
    st.write(df)

    # Group employees by Department and calculate total salary and average salary per department
    st.subheader("Grouped DataFrame:")
    grouped_df=df.groupby("Dept").agg({'Salary': ["sum", "mean"]})
    st.write(grouped_df)

    # Display departments where average salary is greater than 50,000
    st.subheader("Departments with Average Salary > 50,000:")
    hig_av_salary = grouped_df[grouped_df[("Salary", "mean")] > 50000]
    st.write(hig_av_salary)

    if st.button("show Solution Code"):
        st.code("""
import pandas as pd
import streamlit as st
df = pd.DataFrame({
    "Employee":["A","B","C","D","E"],
    "Dept":["IT","HR","IT","Finance","HR"],
    "Salary":[50000,40000,70000,80000,45000]
})
st.subheader("Original DataFrame")
st.write(df)
                
st.subheader("Grouped DataFrame:")
grouped_df=df.groupby("Dept").agg({'Salary': ["sum", "mean"]})
st.write(grouped_df)
                
st.subheader("Departments with Average Salary > 50,000:")
hig_av_salary = grouped_df[grouped_df[("Salary", "mean")] > 50000]
st.write(hig_av_salary)
        """)

#------------
# Question 25
#------------

elif selected_question == list_questions[24]:
    st.header("Question 25")
    st.markdown("""Find the number of employees per department using size().\n
    Find the employee with highest experience in each department using nth() or sorting.\n
    Display results.""")

    df = pd.DataFrame({
    "Dept":["IT","IT","HR","HR","Finance","Finance"],
    "Employee":["A","B","C","D","E","F"],
    "Experience":[2,5,3,7,4,6]
    })

    st.subheader("Original DataFrame")
    st.write(df)

    # Find the number of employees per department using size()
    st.subheader("Number of Employees per Department:")
    st.write(df.groupby("Dept").size())

    # Find the employee with highest experience in each department using nth() or sorting
    st.subheader("Employee with Highest Experience per Department:")
    st.write(df.groupby("Dept").max())

    if st.button("show Solution Code"):
        st.code("""
import pandas as pd
import streamlit as st
df = pd.DataFrame({
    "Dept":["IT","IT","HR","HR","Finance","Finance"],
    "Employee":["A","B","C","D","E","F"],
    "Experience":[2,5,3,7,4,6]
})
st.subheader("Original DataFrame")
st.write(df)
                
st.subheader("Number of Employees per Department:")
st.write(df.groupby("Dept").size())
                
st.subheader("Employee with Highest Experience per Department:")
st.write(df.groupby("Dept").max())
        """)


#------------
# Question 26
#------------

elif selected_question == list_questions[25]:
    st.header("Question 26")
    st.markdown("The dataset provided in ‘kc_house_data.csv’ contains house sale prices for King County, which includes Seattle. It includes homes sold between May 2014 and May 2015Perform the following tasks : ")

    st.warning("Upload kc_house_data.csv File")
    file = st.file_uploader(
        "Choose CSV File",
        type=["csv"]
    )

    if file is not None:
        df = pd.read_csv(file)

        st.subheader("Original DataFrame")
        st.write("1.Load the csv to a dataframe named ‘house_survey’.")
        st.write(df)

    if st.button("2.Display the first 5 rows of the dataframe"):
        st.write(df.head())

    if st.button("3.Drop the columns 'id' and 'Unnamed: 0'"):
        df = df.drop(["id", "Unnamed: 0"], axis=1, inplace=True)

        st.write(df)

    if st.button("4.Check all the null values present in all the columns of the dataframe."):
        st.write(df.isnull().sum())

    if st.button("5. Fill the missing values of the column 'bedrooms' with the mean of the column."):
        st.write(df["bedrooms"].fillna(df["bedrooms"].mean(), inplace=True))
    
    if st.button("6. Fill the missing values of the column 'bathrooms' with the mean of the column."):
        st.write(df["bathrooms"].fillna(df["bathrooms"].mean(), inplace=True))
    
    if st.button("7.Use the Pandas method corr() to find the feature other than price that is most correlated with price and mention your answer as a comment."):
        st.write(df.corr()["price"].sort_values(ascending=False)[1:2])

    if st.button("""8 Fit a linear regression model to predict the 'price' using the list of features: ["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15" ,"sqft_above","grade","sqft_living"]"""):
        st.write("ans")
    
    if st.button("9. Consider 30% testing samples and use random state 10"):
        st.write("ans")
    
    if st.button("10. Find the Mean Squared Error."):
        st.write("ans")

    if st.button("show Solution Code"):
        st.code("""
import pandas as pd
import streamlit as st

st.warning("Upload kc_house_data.csv File")
file = st.file_uploader(
    "Choose CSV File",
    type=["csv"]
)
if file is not None:
    df = pd.read_csv(file)
    st.subheader("Original DataFrame")
    st.write("1.Load the csv to a dataframe named ‘house_survey’.")
    st.write(df)

# 2.Display the first 5 rows of the dataframe
st.write(df.head())

# 3.Drop the columns 'id' and 'Unnamed: 0'
df = df.drop(["id", "Unnamed: 0"], axis=1, inplace=True)
st.write(df)

# 4.Check all the null values present in all the columns of the dataframe.
st.write(df.isnull().sum())

# 5. Fill the missing values of the column 'bedrooms' with the mean of the column.
df["bedrooms"].fillna(df["bedrooms"].mean(), inplace=True)

# 6. Fill the missing values of the column 'bathrooms' with the mean of the column.
df["bathrooms"].fillna(df["bathrooms"].mean(), inplace=True)

# 7.Use the Pandas method corr() to find the feature other than price that is most correlated with price and mention your answer as a comment.  
st.write(df.corr()["price"].sort_values(ascending=False)[1:2])

# 8.8) Fit a linear regression model to predict the 'price' using the list of features:
["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15" ,"sqft_above","grade","sqft_living"]

# 9. Consider 30% testing samples and use random state 10
                
# 10. Find the Mean Squared Error
""")
    
#------------
# Question 27
#------------
elif selected_question == list_questions[26]:
    st.header("Question 27")
    st.markdown("Using ‘supermarket_sales.csv’ fi le do the following operations and give requiredanswer by using proper programming process. ")

    st.warning("Upload supermarket_sales.csv File")
    file = st.file_uploader(
        "Choose CSV File",
        type=["csv"]
    )

    if file is not None:
        df = pd.read_csv(file)

        st.subheader("Original DataFrame")
        st.write(df)
    
    if st.button("1.Load the dataset into a pandas DataFrame and read fi rst 8 rows."):
        st.write(df.head(8))

    if st.button("2). Check for missing values and fill it by mean values of that particular column if any."):

        st.subheader("Missing Values Before Filling")
        st.write(df.isnull().sum())

        # Fill numeric columns with mean
        df["Unit price"] = df["Unit price"].fillna(df["Unit price"].mean())
        df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())
        df["Rating"] = df["Rating"].fillna(df["Rating"].mean())

        st.subheader("Missing Values After Filling")
        st.write(df.isnull().sum())

        st.write(df)

    if st.button("3). Find the number of orders which have ‘Quantity’ less than 3 and which have (either ‘Rating’ greater than 8.5 or ‘Total’ greaterthan 600)."):
        Find_orders = df[(df["Quantity"] < 3) & ((df["Rating"] > 8.5) | (df["Total"] > 600))]
        st.write(Find_orders)
        st.success(f" Number of orders which have 'Quantity' less than 3 and which have (either 'Rating' greater than 8.5 or 'Total' greaterthan 600): {Find_orders.shape[0]} ")


    if st.button("4). Find the sum of ‘Total’ purchasing price spent by Member and Normal 'Customer type'."):
        st.write(df.groupby("Customer type")["Total"].sum())
        

    if st.button("5). Find the percentage of total of ‘grossincome’ based on the different ‘Payment’ methods used by customers. (Ewallet, Cash and Credit card)"):
        st.write(df.groupby("Payment")["gross income"].sum() / df["gross income"].sum() * 100)

    if st.button("6). Analyze the purchasing behavior ofmale and female customers using ‘Gender’ column. Find their average purchase prices using ‘Total’ column."):
        st.write(df.groupby("Gender")["Total"].mean())

    if st.button("7). Create a scatter plot that showsthe relationship between total amount spent and rating. (keep ‘+’ marker, with marker size 100 and green color)."):
            fig, ax = plt.subplots()
            ax.scatter(df["Total"], df["Rating"], marker="+", s=100, color="green")
            ax.set_xlabel("Total")
            ax.set_ylabel("Rating")
            ax.set_title("Total Amount Spent vs Rating")
            st.pyplot(fig)
    if st.button("8). Create a box plot that showsthe distribution of ‘Rating’ and ‘Quantity’. And comment about outliers in both columns."):    
            fig, ax = plt.subplots()
            df[["Rating", "Quantity"]].boxplot(ax=ax)
            ax.set_title("Distribution of Rating and Quantity")
            st.pyplot(fig)
            st.info("Check for dots beyond whiskers to identify outliers in each column.")

    if st.button("9). Find the correlation between ‘Quantity’ and ‘Rating’."):
        st.write(df[["Quantity", "Rating"]].corr())

    if st.button("Show Solution Code"):
        st.code("""
import pandas as pd

# 1. Load the dataset into a pandas DataFrame and read fi rst 8 rows.
df = pd.read_csv("supermarket_sales.csv")
st.write(df.head(8))

# 2. Check for missing values and fill it by mean values of that particular column if any.
st.write(df.isnull().sum()
# Fill numeric columns with mean
df["Unit price"] = df["Unit price"].fillna(df["Unit price"].mean())
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())
df["Rating"] = df["Rating"].fillna(df["Rating"].mean()
st.subheader("Missing Values After Filling")
st.write(df.isnull().sum()
st.write(df)

# 3. Find the number of orders which have ‘Quantity’ less than 3 and which have (either ‘Rating’ greater than 8.5 or ‘Total’ greaterthan 600).
Find_orders = df[(df["Quantity"] < 3) & ((df["Rating"] > 8.5) | (df["Total"] > 600))]
st.write(Find_orders)
st.success(f" Number of orders which have 'Quantity' less than 3 and which have (either 'Rating' greater than 8.5 or 'Total' greaterthan 600): {Find_orders.shape[0]} ")

# 4. Find the sum of ‘Total’ purchasing price spent by Member and Normal 'Customer type'.
st.write(df.groupby("Customer type")["Total"].sum())

# 5. Find the percentage of total of ‘grossincome’ based on the different ‘Payment’ methods used by customers. (Ewallet, Cash and Credit card)
st.write(df.groupby("Payment")["gross income"].sum() / df["gross income"].sum() * 100

# 6. Analyze the purchasing behavior ofmale and female customers using ‘Gender’ column. Find their average purchase prices using ‘Total’ column.
st.write(df.groupby("Gender")["Total"].mean()

# 7. Create a scatter plot that showsthe relationship between total amount spent and rating. (keep ‘+’ marker, with marker size 100 and green color).
fig, ax = plt.subplots()
ax.scatter(df["Total"], df["Rating"], marker="+", s=100, color="green")
ax.set_xlabel("Total")
ax.set_ylabel("Rating")
ax.set_title("Total Amount Spent vs Rating")
st.pyplot(fig)

# 8. Create a box plot that showsthe distribution of ‘Rating’ and ‘Quantity’. And comment about outliers in both columns.
fig, ax = plt.subplots()
df[["Rating", "Quantity"]].boxplot(ax=ax)
ax.set_title("Distribution of Rating and Quantity")
st.pyplot(fig)
st.info("Check for dots beyond whiskers to identify outliers in each column.")  

# 9. Find the correlation between ‘Quantity’ and ‘Rating’.
st.write(df[["Quantity", "Rating"]].corr()  


""")
        

