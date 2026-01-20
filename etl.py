import pandas as pd
customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")

merged = orders.merge(customers,on="customer_id",how="left")
orphans = merged[merged["name"].isna()]

print(f"Total orders:{len(orders)}")
print(f"orphan orders found:{len(orphans)}")

clean_data = merged.dropna(subset=["name"])

summary = (clean_data.groupby(["customer_id","name"],as_index=False).agg(total_orders=("order_id","count"),total_amount=("amount","sum")))

final_report = summary.sort_values("total_amount",ascending=False)

final_report.to_csv("final_report.csv",index=False)
orphans.to_csv("orphan_orders.csv",index=False)


print("pipeline finished successfully")
print(final_report)
