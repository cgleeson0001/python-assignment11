import plotly.express as px
import plotly.data as pldata

# Load the wind dataset
df = pldata.wind(return_type="pandas")

# Print first and last 10 rows
print("First 10 rows:")
print(df.head(10))

print("\nLast 10 rows:")
print(df.tail(10))

# Clean the strength column and convert it to float
df["strength"] = (
    df["strength"]
    .str.replace(r"\D.*", "", regex=True)
    .astype(float)
)

print("\nCleaned data:")
print(df.head())

# Create interactive scatter plot
fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Wind Strength vs. Frequency",
    labels={
        "strength": "Wind Strength",
        "frequency": "Frequency",
        "direction": "Direction"
    }
)

# Save and open the interactive plot
fig.write_html("wind.html", auto_open=True)