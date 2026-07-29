import pandas as pd
import random


# -----------------------------
# Sample Districts
# -----------------------------

districts = [
    "Hyderabad",
    "Warangal",
    "Karimnagar",
    "Nizamabad",
    "Khammam",
    "Adilabad",
    "Mahabubnagar",
    "Nalgonda"
]

years = [2019, 2020, 2021, 2022, 2023]


# -----------------------------
# Create District Dimension
# -----------------------------

district_df = pd.DataFrame({
    "dist_code": range(1, len(districts)+1),
    "district": districts
})

district_df.to_csv(
    "dim_districts.csv",
    index=False
)



# -----------------------------
# Create Date Dimension
# -----------------------------

dates = []

date_id = 1

for year in years:
    for month in range(1,13):

        dates.append({

            "date_id": date_id,
            "date": f"{year}-{month:02d}-01",
            "year": year,
            "month": month,
            "quarter": f"Q{((month-1)//3)+1}"

        })

        date_id += 1


date_df = pd.DataFrame(dates)

date_df.to_csv(
    "dim_date.csv",
    index=False
)



# -----------------------------
# FACT TRANSPORT
# -----------------------------

transport = []


for dist_code, district in enumerate(districts, start=1):

    for year in years:

        for month in range(1,13):

            transport.append({

                "date": f"{year}-{month:02d}-01",

                "year": year,

                "month": month,

                "dist_code": dist_code,

                "district": district,


                "vehicle_sales":
                    random.randint(5000,15000),

                "registrations":
                    random.randint(1000,5000),

                "permits":
                    random.randint(500,3000)

            })


transport_df = pd.DataFrame(transport)


transport_df.to_csv(
    "fact_transport.csv",
    index=False
)




# -----------------------------
# FACT TS iPASS
# -----------------------------

ipass = []


for dist_code, district in enumerate(districts, start=1):

    for year in years:

        for month in range(1,13):

            ipass.append({

                "date": f"{year}-{month:02d}-01",

                "year": year,

                "month": month,

                "dist_code": dist_code,

                "district": district,


                "companies":
                    random.randint(50,300),

                "jobs":
                    random.randint(100,2000),

                "investment":
                    random.randint(1000000,100000000)

            })


ipass_df = pd.DataFrame(ipass)


ipass_df.to_csv(
    "fact_TS_iPASS.csv",
    index=False
)




# -----------------------------
# FACT STAMPS
# -----------------------------

stamps = []


for dist_code, district in enumerate(districts, start=1):

    for year in years:

        for month in range(1,13):

            stamps.append({

                "date": f"{year}-{month:02d}-01",

                "year": year,

                "month": month,

                "dist_code": dist_code,

                "district": district,


                "documents_registered":
                    random.randint(10000,50000),

                "revenue":
                    random.randint(1000000,10000000),

                "estamp_challans":
                    random.randint(5000,25000)

            })


stamps_df = pd.DataFrame(stamps)


stamps_df.to_csv(
    "fact_stamps.csv",
    index=False
)



print("="*60)
print("ALL CSV FILES CREATED SUCCESSFULLY")
print("="*60)

print("\nFiles Generated:")
print("1. dim_districts.csv")
print("2. dim_date.csv")
print("3. fact_transport.csv")
print("4. fact_TS_iPASS.csv")
print("5. fact_stamps.csv")