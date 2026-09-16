import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("../db/lesson.db")

# Calculate total price for each order
query = """
SELECT
    orders.order_id,
    SUM(products.price * line_items.quantity) AS total_price
FROM orders
JOIN line_items
    ON orders.order_id = line_items.order_id
JOIN products
    ON line_items.product_id = products.product_id
GROUP BY orders.order_id
ORDER BY orders.order_id;
"""

df = pd.read_sql_query(query, conn)
conn.close()

# Add cumulative revenue
df["cumulative"] = df["total_price"].cumsum()

print(df)

# Create line plot
df.plot(
    x="order_id",
    y="cumulative",
    kind="line",
    title="Cumulative Revenue by Order"
)

plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue")
plt.tight_layout()
plt.show()