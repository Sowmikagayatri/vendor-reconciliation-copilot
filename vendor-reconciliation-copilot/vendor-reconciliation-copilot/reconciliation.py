import pandas as pd

# Read the CSV files
vendor = pd.read_csv("data/vendor_statement.csv")
company = pd.read_csv("data/company_statement.csv")

print("\n========== VENDOR STATEMENT ==========")
print(vendor)

print("\n========== COMPANY STATEMENT ==========")
print(company)

# Compare both statements using Transaction ID
merged = pd.merge(
    vendor,
    company,
    on="Transaction ID",
    how="outer",
    suffixes=("_vendor", "_company"),
    indicator=True
)

# Matched transactions
matched = merged[merged["_merge"] == "both"]

# Missing transactions
missing = merged[merged["_merge"] != "both"]

# Amount mismatches
amount_mismatches = matched[
    matched["Amount_vendor"] != matched["Amount_company"]
]

print("\n========== RECONCILIATION RESULTS ==========")

print("\nMatched transactions:")
print(matched)

print("\nMissing transactions:")
print(missing)

print("\nAmount mismatches:")
print(amount_mismatches)

print("\n----------------------------------------")
print("Matched transactions:", len(matched))
print("Missing transactions:", len(missing))
print("Amount mismatches:", len(amount_mismatches))
print("----------------------------------------")