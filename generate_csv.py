import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

transport = pd.read_csv("fact_transport.csv")

ipass = pd.read_csv("fact_TS_iPASS.csv")

stamps = pd.read_csv("fact_stamps.csv")

date_dim = pd.read_csv("dim_date.csv")

district_dim = pd.read_csv("dim_districts.csv")


print("Files Loaded Successfully")


# ---------------------------------------------------
# CHECK COLUMNS
# ---------------------------------------------------

print("\nTransport Columns")
print(transport.columns)

print("\nIPASS Columns")
print(ipass.columns)

print("\nStamps Columns")
print(stamps.columns)



# ---------------------------------------------------
# MERGE FACT TABLES
# ---------------------------------------------------

# Merge transport and iPASS

merged_df = pd.merge(
    transport,
    ipass,
    on=[
        "date",
        "fiscal_year",
        "month",
        "dist_code",
        "district"
    ],
    how="inner"
)


# Merge stamps

merged_df = pd.merge(
    merged_df,
    stamps,
    on=[
        "date",
        "fiscal_year",
        "month",
        "dist_code",
        "district"
    ],
    how="inner"
)


print("\nFact Tables Merged")


# ---------------------------------------------------
# MERGE DISTRICT DIMENSION
# ---------------------------------------------------

merged_df = pd.merge(
    merged_df,
    district_dim,
    on="dist_code",
    how="left"
)


# Remove duplicate district columns

if "district_x" in merged_df.columns:
    merged_df.drop(
        columns=["district_y"],
        inplace=True
    )

    merged_df.rename(
        columns={"district_x":"district"},
        inplace=True
    )


print("\nAfter District Merge")
print(merged_df.columns)



# ---------------------------------------------------
# MERGE DATE DIMENSION
# ---------------------------------------------------

merged_df = pd.merge(
    merged_df,
    date_dim,
    on=[
        "date",
        "fiscal_year",
        "month"
    ],
    how="left"
)


print("\nFinal Dataset")
print(merged_df.head())



# ---------------------------------------------------
# FILTER YEARS
# ---------------------------------------------------

filtered_df = merged_df[
    merged_df["fiscal_year"].isin(
        [2019,2022]
    )
]


print("\nFiltered Data")
print(filtered_df.head())



# ---------------------------------------------------
# ANALYSIS 1
# Vehicle Growth
# ---------------------------------------------------

vehicle_growth = (
    filtered_df
    .groupby("fiscal_year")
    ["vehicle_sales"]
    .sum()
)


plt.figure(figsize=(8,5))

vehicle_growth.plot(
    kind="bar"
)

plt.title(
    "Vehicle Sales Growth"
)

plt.xlabel(
    "Fiscal Year"
)

plt.ylabel(
    "Vehicle Sales"
)

plt.show()



# ---------------------------------------------------
# ANALYSIS 2
# District Investment
# ---------------------------------------------------

investment = (
    filtered_df
    .groupby("district")
    ["investment"]
    .sum()
    .sort_values(
        ascending=False
    )
)


plt.figure(figsize=(10,5))

investment.plot(
    kind="bar"
)

plt.title(
    "District Wise Investment"
)

plt.xlabel(
    "District"
)

plt.ylabel(
    "Investment"
)

plt.xticks(
    rotation=45
)

plt.show()



# ---------------------------------------------------
# ANALYSIS 3
# Registration Revenue
# ---------------------------------------------------

revenue = (
    filtered_df
    .groupby("district")
    ["revenue"]
    .sum()
    .sort_values(
        ascending=False
    )
)


plt.figure(figsize=(10,5))

sns.barplot(
    x=revenue.index,
    y=revenue.values
)


plt.title(
    "District Wise Stamp Revenue"
)

plt.xlabel(
    "District"
)

plt.ylabel(
    "Revenue"
)

plt.xticks(
    rotation=45
)

plt.show()



# ---------------------------------------------------
# SAVE FINAL DATASET
# ---------------------------------------------------

merged_df.to_csv(
    "Telangana_final_analysis.csv",
    index=False
)


print("\nAnalysis Completed Successfully")
print("Output file created:")
print("Telangana_final_analysis.csv")