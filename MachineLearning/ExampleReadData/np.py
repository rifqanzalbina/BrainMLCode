# Import Library
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("MachineLearning/ExampleReadData/hrsccv.csv",index_col="Name",parse_dates=["Hire Date"])

df = pd.DataFrame(df)
df['Hire Date'] = pd.to_datetime(df['Hire Date'])

plt.figure(figsize=(10, 6))
plt.plot(df['Hire Date'], df['Salary'], marker='o', linestyle='-', label='Salary')
plt.plot(df['Hire Date'], df['Sick Days remaining'], marker='o', linestyle='-', label='Sick Days Remaining')
plt.xlabel('Tanggal Rekrut') # Hire date
plt.ylabel('Nilai') # Value
plt.title('Data karyawan') # Employee Data
plt.legend()
plt.xticks(rotation=45)
plt.show()