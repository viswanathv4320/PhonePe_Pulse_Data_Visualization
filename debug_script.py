from data_extraction import aggregated_data, map_data, top_data
import pandas as pd

# Aggregated DataFrames
agg_data = aggregated_data("/Users/viswanath/Phonepe_Pulse_Data_Visualization/pulse/data/aggregated")

df_agg_ins_con = pd.DataFrame(agg_data["insurance"]["country"])
df_agg_ins_state = pd.DataFrame(agg_data["insurance"]["state"])
df_agg_tran_con = pd.DataFrame(agg_data["transaction"]["country"])
df_agg_tran_state = pd.DataFrame(agg_data["transaction"]["state"])
df_agg_user_con = pd.DataFrame(agg_data["user"]["country"])
df_agg_user_state = pd.DataFrame(agg_data["user"]["state"])

print("✅ Shape:", df_agg_ins_con.shape)
print(df_agg_ins_con.head())
print(df_agg_ins_con.isna().sum())
print(df_agg_ins_con.dtypes)

print("✅ Shape:", df_agg_ins_state.shape)
print(df_agg_ins_state.head())
print(df_agg_ins_state.isna().sum())
print(df_agg_ins_state.dtypes)

print("✅ Shape:", df_agg_tran_con.shape)
print(df_agg_tran_con.head())
print(df_agg_tran_con.isna().sum())
print(df_agg_tran_con.dtypes)

print("✅ Shape:", df_agg_tran_state.shape)
print(df_agg_tran_state.head())
print(df_agg_tran_state.isna().sum())
print(df_agg_tran_state.dtypes)

print("✅ Shape:", df_agg_user_con.shape)
print(df_agg_user_con.head())
print(df_agg_user_con.isna().sum())
print(df_agg_user_con.dtypes)

print("✅ Shape:", df_agg_user_state.shape)
print(df_agg_user_state.head())
print(df_agg_user_state.isna().sum())
print(df_agg_user_state.dtypes)


# Map DataFrames
map_outputs = map_data("/Users/viswanath/Phonepe_Pulse_Data_Visualization/pulse/data/map")

df_map_ins_con, df_map_ins_state, df_hover_ins_con, df_hover_ins_state, \
df_map_tran_con, df_map_tran_state, df_map_user_con, df_map_user_state = map_outputs

df_map_ins_con = pd.DataFrame(df_map_ins_con)
df_map_ins_state = pd.DataFrame(df_map_ins_state)
df_hover_ins_con = pd.DataFrame(df_hover_ins_con)
df_hover_ins_state = pd.DataFrame(df_hover_ins_state)
df_map_tran_con = pd.DataFrame(df_map_tran_con)
df_map_tran_state = pd.DataFrame(df_map_tran_state)
df_map_user_con = pd.DataFrame(df_map_user_con)
df_map_user_state = pd.DataFrame(df_map_user_state)

print("✅ Shape:", df_map_ins_con.shape)
print(df_map_ins_con.head())
print(df_map_ins_con.isna().sum())
print(df_map_ins_con.dtypes)

print("✅ Shape:", df_map_ins_state.shape)
print(df_map_ins_state.head())
print(df_map_ins_state.isna().sum())
print(df_map_ins_state.dtypes)

print("✅ Shape:", df_hover_ins_con.shape)
print(df_hover_ins_con.head())
print(df_hover_ins_con.isna().sum())
print(df_hover_ins_con.dtypes)

print("✅ Shape:", df_hover_ins_state.shape)
print(df_hover_ins_state.head())
print(df_hover_ins_state.isna().sum())
print(df_hover_ins_state.dtypes)

print("✅ Shape:", df_map_tran_con.shape)
print(df_map_tran_con.head())
print(df_map_tran_con.isna().sum())
print(df_map_tran_con.dtypes)

print("✅ Shape:", df_map_tran_state.shape)
print(df_map_tran_state.head())
print(df_map_tran_state.isna().sum())
print(df_map_tran_state.dtypes)

print("✅ Shape:", df_map_user_con.shape)
print(df_map_user_con.head())
print(df_map_user_con.isna().sum())
print(df_map_user_con.dtypes)

print("✅ Shape:", df_map_user_state.shape)
print(df_map_user_state.head())
print(df_map_user_state.isna().sum())
print(df_map_user_state.dtypes)


# Top DataFrames
top_outputs = top_data("/Users/viswanath/Phonepe_Pulse_Data_Visualization/pulse/data/top")

df_top_ins_con, df_top_ins_state, df_top_tran_con, df_top_tran_state, \
df_top_user_con, df_top_user_state = map(pd.DataFrame, top_outputs)

df_top_ins_con = pd.DataFrame(df_top_ins_con)
df_top_ins_state = pd.DataFrame(df_top_ins_state)
df_top_tran_con = pd.DataFrame(df_top_tran_con)
df_top_tran_state = pd.DataFrame(df_top_tran_state)
df_top_user_con = pd.DataFrame(df_top_user_con)
df_top_user_state = pd.DataFrame(df_top_user_state)

print("✅ Shape:", df_top_ins_con.shape)
print(df_top_ins_con.head())
print(df_top_ins_con.isna().sum())
print(df_top_ins_con.dtypes)

print("✅ Shape:", df_top_ins_state.shape)
print(df_top_ins_state.head())
print(df_top_ins_state.isna().sum())
print(df_top_ins_state.dtypes)

print("✅ Shape:", df_top_tran_con.shape)
print(df_top_tran_con.head())
print(df_top_tran_con.isna().sum())
print(df_top_tran_con.dtypes)

print("✅ Shape:", df_top_tran_state.shape)
print(df_top_tran_state.head())
print(df_top_tran_state.isna().sum())
print(df_top_tran_state.dtypes)

print("✅ Shape:", df_top_user_con.shape)
print(df_top_user_con.head())
print(df_top_user_con.isna().sum())
print(df_top_user_con.dtypes)

print("✅ Shape:", df_top_user_state.shape)
print(df_top_user_state.head())
print(df_top_user_state.isna().sum())
print(df_top_user_state.dtypes)
