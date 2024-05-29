import pandas as pd
from pandas_profiling import ProfileReport
df = pd.read_csv("C:/Users/Hp/Downloads/NHANES_Select_Infectious_Diseases_Prevalence_Estimates (1).csv")
print(df)
profile= ProfileReport(df)
profile.to_file("output.html")















