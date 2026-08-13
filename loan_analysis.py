import numpy as np

# Open the CSV file
file = open("loan_dataset.csv", "r")

# Read the data using numpy genfromtxt with comma delimiter
data = np.genfromtxt(file, delimiter=",", skip_header=1)

# Close the file after reading
file.close()

# Extract the loan amount column (index 4, 0-based)
loan_amounts = data[:, 4]

# Calculate basic statistics using numpy functions
mean_loan = np.mean(loan_amounts)
median_loan = np.median(loan_amounts)
std_loan = np.std(loan_amounts)

# Print the results
print("=" * 50)
print("Loan Dataset Statistical Analysis")
print("=" * 50)
print(f"Number of loans: {len(loan_amounts)}")
print(f"Mean loan amount: ${mean_loan:,.2f}")
print(f"Median loan amount: ${median_loan:,.2f}")
print(f"Standard deviation: ${std_loan:,.2f}")
print("=" * 50)

