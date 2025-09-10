# Import the pandas library, which is essential for data manipulation and analysis
import pandas as pd

# Create a sample dictionary representing workout data
# This could be data logged from your strength training sessions
data = {
    'date': ['2025-08-01', '2025-08-03', '2025-08-05', '2025-08-08'],
    'exercise': ['Squat', 'Bench Press', 'Squat', 'Bench Press'],
    'weight_kg': [100, 75, 105, 80],
    'reps': [5, 8, 5, 6]
}

# Convert the dictionary into a pandas DataFrame
# A DataFrame is a powerful table-like data structure
df = pd.DataFrame(data)

# Print the entire DataFrame to see what our data looks like
print("Original Workout Data:")
print(df)

# --- Perform a simple analysis ---
# Filter the data to only include 'Squat' exercises
squat_data = df[df['exercise'] == 'Squat']

# Calculate the average weight lifted for squats
average_squat_weight = squat_data['weight_kg'].mean()

# Print the result in a clear, formatted message
print("\n--- Analysis Result ---")
print(f"Average weight lifted for 'Squat' is: {average_squat_weight} kg")