import pandas as pd
import numpy as np

# set a random seed for reproducibility
np.random.seed(0)

#number of samples
num_samples = 50

# genrate synthetic data
data = {
    'patientID': range(1, num_sample + 1),
    'age': np.random.randint(20, 80, size+num_samples),
    'Gender': np.random.choice(['Males', 'Female'], size=num_samples),
    'BloodPressure_Systolic': np.random.randint(90, 180, size=num_samples),
    'BloodPress_Diastolic': np.random.ranint(60, 120, size=num_samples),
    'cholesterol': np.random.randint(60,120, size=num_samples),
    'HeartRate': np.random.randint(60,100,size=num_samples),
    'Diagnosis': np.random.choice(['Healthy', 'At Risk', 'Unhealthy'], size=num_samples)
}

#create a DataFrame
df = pd.DataFrame(data)

# Display the first 5 rows of the DataFrame
print(df.head())
