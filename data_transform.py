import pandas as pd
from data_extraction import aggregated_data, map_data, top_data

def load_cleaned_data():
    # ---------------------- AGGREGATED DATA ----------------------
    agg_path = "pulse/data/aggregated"
    agg_data = aggregated_data(agg_path)

    df_agg_tran_state = pd.DataFrame(agg_data["transaction"]["state"])
    df_agg_user_state = pd.DataFrame(agg_data["user"]["state"])
    df_agg_insurance_state = pd.DataFrame(agg_data["insurance"]["state"])

    # Clean transaction data
    df_agg_tran_state["transaction_name"] = df_agg_tran_state["transaction_name"].str.strip().str.title()
    df_agg_tran_state["instrument_type"] = df_agg_tran_state["instrument_type"].str.strip().str.upper()
    df_agg_tran_state["level"] = df_agg_tran_state["level"].str.lower().str.strip()
    df_agg_tran_state["state"] = df_agg_tran_state["state"].str.strip().str.title()
    df_agg_tran_state["year"] = df_agg_tran_state["year"].astype(int)
    df_agg_tran_state["quarter"] = df_agg_tran_state["quarter"].astype(int)
    df_agg_tran_state["from_timestamp"] = pd.to_datetime(df_agg_tran_state["from_timestamp"])
    df_agg_tran_state["to_timestamp"] = pd.to_datetime(df_agg_tran_state["to_timestamp"])
    df_agg_tran_state["count"] = pd.to_numeric(df_agg_tran_state["count"], errors="coerce").fillna(0).astype(int)
    df_agg_tran_state["amount"] = pd.to_numeric(df_agg_tran_state["amount"], errors="coerce").fillna(0.0)
    df_agg_tran_state["year_quarter"] = df_agg_tran_state["year"].astype(str) + "-Q" + df_agg_tran_state["quarter"].astype(str)

    # Clean user data
    df_agg_user_state["level"] = df_agg_user_state["level"].str.lower().str.strip()
    df_agg_user_state["state"] = df_agg_user_state["state"].str.strip().str.title()
    df_agg_user_state["registered_users"] = pd.to_numeric(df_agg_user_state["registered_users"], errors="coerce").fillna(0).astype(int)
    df_agg_user_state["app_opens"] = pd.to_numeric(df_agg_user_state["app_opens"], errors="coerce").fillna(0).astype(int)
    df_agg_user_state["brand"] = df_agg_user_state["brand"].astype(str).str.strip()
    df_agg_user_state["count"] = pd.to_numeric(df_agg_user_state["count"], errors="coerce").fillna(0).astype(int)
    df_agg_user_state["percentage"] = pd.to_numeric(df_agg_user_state["percentage"], errors="coerce").fillna(0.0)

    # Clean insurance data
    df_agg_insurance_state["level"] = df_agg_insurance_state["level"].str.lower().str.strip()
    df_agg_insurance_state["state"] = df_agg_insurance_state["state"].str.strip().str.title()
    df_agg_insurance_state["year"] = df_agg_insurance_state["year"].astype(int)
    df_agg_insurance_state["quarter"] = df_agg_insurance_state["quarter"].astype(int)
    df_agg_insurance_state["from_timestamp"] = pd.to_datetime(df_agg_insurance_state["from_timestamp"])
    df_agg_insurance_state["to_timestamp"] = pd.to_datetime(df_agg_insurance_state["to_timestamp"])
    df_agg_insurance_state["transaction_name"] = df_agg_insurance_state["transaction_name"].astype(str).str.strip().str.title()
    df_agg_insurance_state["instrument_type"] = df_agg_insurance_state["instrument_type"].astype(str).str.upper()
    df_agg_insurance_state["count"] = pd.to_numeric(df_agg_insurance_state["count"], errors="coerce").fillna(0).astype(int)
    df_agg_insurance_state["amount"] = pd.to_numeric(df_agg_insurance_state["amount"], errors="coerce").fillna(0.0)
    df_agg_insurance_state["year_quarter"] = df_agg_insurance_state["year"].astype(str) + "-Q" + df_agg_insurance_state["quarter"].astype(str)

    # ---------------------- MAP DATA ----------------------
    map_path = "pulse/data/map"
    (
        dis_map_ins, state_map_ins,
        dis_hover_ins, state_hover_ins,
        dis_map_tran, state_map_tran,
        dis_map_user, state_map_user,
        dis_hover_tran, dis_hover_user
    ) = map_data(map_path)

    df_dis_map_ins    = pd.DataFrame(dis_map_ins)
    df_state_map_ins  = pd.DataFrame(
        state_map_ins,
        columns=["lat", "lng", "metric", "label", "state", "year", "quarter"]
    )

    df_dis_hover_ins  = pd.DataFrame(dis_hover_ins,  columns=["state","district","count","amount","type","year","quarter"])
    df_state_hover_ins = pd.DataFrame(state_hover_ins, columns=["state","count","amount","type","year","quarter"])

    df_dis_map_tran   = pd.DataFrame(dis_map_tran,   columns=["state","district","count","amount","instrument_type","year","quarter"])
    df_state_map_tran = pd.DataFrame(state_map_tran)

    df_dis_map_user   = pd.DataFrame(dis_map_user,   columns=["state","district","registered_users","app_opens","year","quarter"])
    df_state_map_user = pd.DataFrame(state_map_user)

    df_dis_hover_tran = pd.DataFrame(dis_hover_tran, columns=["state","district","count","amount","instrument_type","year","quarter"])
    df_dis_hover_user = pd.DataFrame(dis_hover_user, columns=["state","district","registered_users","app_opens","year","quarter"])

    # ---------- District Transaction Map ----------
    if not df_dis_map_tran.empty:
        df_dis_map_tran["year"] = pd.to_numeric(df_dis_map_tran["year"], errors="coerce").astype("Int64")
        df_dis_map_tran["quarter"] = pd.to_numeric(df_dis_map_tran["quarter"], errors="coerce").astype("Int64")
        df_dis_map_tran["count"] = pd.to_numeric(df_dis_map_tran["count"], errors="coerce").fillna(0).astype(int)
        df_dis_map_tran["amount"] = pd.to_numeric(df_dis_map_tran["amount"], errors="coerce").fillna(0.0)
        df_dis_map_tran["district"] = df_dis_map_tran["district"].astype(str).str.strip().str.title()
        df_dis_map_tran["state"] = df_dis_map_tran["state"].astype(str).str.strip().str.title()

    # ---------- District User Map ----------
    if not df_dis_map_user.empty:
        df_dis_map_user["year"] = pd.to_numeric(df_dis_map_user["year"], errors="coerce").astype("Int64")
        df_dis_map_user["quarter"] = pd.to_numeric(df_dis_map_user["quarter"], errors="coerce").astype("Int64")
        df_dis_map_user["registered_users"] = pd.to_numeric(df_dis_map_user["registered_users"], errors="coerce").fillna(0).astype(int)
        df_dis_map_user["app_opens"] = pd.to_numeric(df_dis_map_user["app_opens"], errors="coerce").fillna(0).astype(int)
        df_dis_map_user["district"] = df_dis_map_user["district"].astype(str).str.strip().str.title()
        df_dis_map_user["state"] = df_dis_map_user["state"].astype(str).str.strip().str.title()

    # ---------- District Insurance Grid ----------
    if not df_dis_map_ins.empty:
        df_dis_map_ins["year"] = pd.to_numeric(df_dis_map_ins["year"], errors="coerce").astype("Int64")
        df_dis_map_ins["quarter"] = pd.to_numeric(df_dis_map_ins["quarter"], errors="coerce").astype("Int64")
        df_dis_map_ins["metric"] = pd.to_numeric(df_dis_map_ins["metric"], errors="coerce").fillna(0.0)
        df_dis_map_ins["label"] = df_dis_map_ins["label"].astype(str).str.strip().str.title()
        if "state" in df_dis_map_ins.columns:
            df_dis_map_ins["state"] = df_dis_map_ins["state"].astype(str).str.strip().str.title()

    # ---------- Hover Insurance (district-level) ----------
    if not df_dis_hover_ins.empty:
        df_dis_hover_ins["year"] = pd.to_numeric(df_dis_hover_ins["year"], errors="coerce").astype("Int64")
        df_dis_hover_ins["quarter"] = pd.to_numeric(df_dis_hover_ins["quarter"], errors="coerce").astype("Int64")
        df_dis_hover_ins["type"] = df_dis_hover_ins["type"].astype(str).str.upper()
        df_dis_hover_ins["state"] = df_dis_hover_ins["state"].astype(str).str.strip().str.title()
        df_dis_hover_ins["district"] = df_dis_hover_ins["district"].astype(str).str.strip().str.title()
        df_dis_hover_ins["count"] = pd.to_numeric(df_dis_hover_ins["count"], errors="coerce").fillna(0).astype(int)
        df_dis_hover_ins["amount"] = pd.to_numeric(df_dis_hover_ins["amount"], errors="coerce").fillna(0.0)

    # ---------- Hover Transaction (district-level) ----------
    if not df_dis_hover_tran.empty:
        df_dis_hover_tran["year"] = pd.to_numeric(df_dis_hover_tran["year"], errors="coerce").astype("Int64")
        df_dis_hover_tran["quarter"] = pd.to_numeric(df_dis_hover_tran["quarter"], errors="coerce").astype("Int64")
        df_dis_hover_tran["instrument_type"] = df_dis_hover_tran["instrument_type"].astype(str).str.upper()
        df_dis_hover_tran["count"] = pd.to_numeric(df_dis_hover_tran["count"], errors="coerce").fillna(0).astype(int)
        df_dis_hover_tran["amount"] = pd.to_numeric(df_dis_hover_tran["amount"], errors="coerce").fillna(0.0)
        df_dis_hover_tran["district"] = df_dis_hover_tran["district"].astype(str).str.strip().str.title()
        df_dis_hover_tran["state"] = df_dis_hover_tran["state"].astype(str).str.strip().str.title()

    # ---------- Hover User (district-level) ----------
    if not df_dis_hover_user.empty:
        df_dis_hover_user["year"] = pd.to_numeric(df_dis_hover_user["year"], errors="coerce").astype("Int64")
        df_dis_hover_user["quarter"] = pd.to_numeric(df_dis_hover_user["quarter"], errors="coerce").astype("Int64")
        df_dis_hover_user["registered_users"] = pd.to_numeric(df_dis_hover_user["registered_users"], errors="coerce").fillna(0).astype(int)
        df_dis_hover_user["app_opens"] = pd.to_numeric(df_dis_hover_user["app_opens"], errors="coerce").fillna(0).astype(int)
        df_dis_hover_user["district"] = df_dis_hover_user["district"].astype(str).str.strip().str.title()
        df_dis_hover_user["state"] = df_dis_hover_user["state"].astype(str).str.strip().str.title()

    # ---------- State-level Insurance Grid and Hover ----------
    if not df_state_map_ins.empty:
        df_state_map_ins["year"] = df_state_map_ins["year"].astype(int)
        df_state_map_ins["quarter"] = df_state_map_ins["quarter"].astype(int)
        df_state_map_ins["metric"] = pd.to_numeric(df_state_map_ins["metric"], errors="coerce").fillna(0.0)
        df_state_map_ins["label"] = df_state_map_ins["label"].str.strip().str.title()

    if not df_state_hover_ins.empty:
        df_state_hover_ins["year"] = df_state_hover_ins["year"].astype(int)
        df_state_hover_ins["quarter"] = df_state_hover_ins["quarter"].astype(int)
        df_state_hover_ins["type"] = df_state_hover_ins["type"].str.upper()
        df_state_hover_ins["state"] = df_state_hover_ins["state"].str.strip().str.title()
        df_state_hover_ins["count"] = pd.to_numeric(df_state_hover_ins["count"], errors="coerce").fillna(0).astype(int)
        df_state_hover_ins["amount"] = pd.to_numeric(df_state_hover_ins["amount"], errors="coerce").fillna(0.0)

    # ---------- State-level Transaction Grid ----------
    # State-level Transaction Grid
    if not df_state_map_tran.empty:
        df_state_map_tran["year"] = df_state_map_tran["year"].astype(int)
        df_state_map_tran["quarter"] = df_state_map_tran["quarter"].astype(int)
        df_state_map_tran["count"] = pd.to_numeric(df_state_map_tran["count"], errors="coerce").fillna(0).astype(int)
        df_state_map_tran["amount"] = pd.to_numeric(df_state_map_tran["amount"], errors="coerce").fillna(0.0)

        if "instrument_type" in df_state_map_tran.columns:
            df_state_map_tran["instrument_type"] = df_state_map_tran["instrument_type"].astype(str).str.upper()
        else:
            df_state_map_tran["instrument_type"] = pd.NA

    # ---------- State-level User Grid ----------
    if not df_state_map_user.empty:
        df_state_map_user["year"] = df_state_map_user["year"].astype(int)
        df_state_map_user["quarter"] = df_state_map_user["quarter"].astype(int)
        df_state_map_user["registered_users"] = pd.to_numeric(df_state_map_user["registered_users"], errors="coerce").fillna(0).astype(int)
        df_state_map_user["app_opens"] = pd.to_numeric(df_state_map_user["app_opens"], errors="coerce").fillna(0).astype(int)

    # ---------------------- TOP DATA ----------------------
    top_path = "pulse/data/top"
    (
        _, state_top_ins,
        _, state_top_tran,
        _, state_top_user
    ) = top_data(top_path)

    df_top_ins_state = pd.DataFrame(state_top_ins)
    df_top_tran_state = pd.DataFrame(state_top_tran)
    df_top_user_state = pd.DataFrame(state_top_user)

    for df in [df_top_ins_state, df_top_tran_state]:
        if not df.empty:
            df["year"] = df["year"].astype(int)
            df["quarter"] = df["quarter"].astype(int)
            df["entity"] = df["entity"].astype(str).str.strip().str.title()
            df["count"] = pd.to_numeric(df["count"], errors="coerce").fillna(0).astype(int)
            df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0.0)

    if not df_top_user_state.empty:
        df_top_user_state["year"] = df_top_user_state["year"].astype(int)
        df_top_user_state["quarter"] = df_top_user_state["quarter"].astype(int)
        df_top_user_state["entity"] = df_top_user_state["entity"].astype(str).str.strip().str.title()
        df_top_user_state["registeredUsers"] = pd.to_numeric(df_top_user_state["registeredUsers"], errors="coerce").fillna(0).astype(int)

    # ---------------------- RETURN CLEANED DATAFRAMES ----------------------
    return {
        "agg_tran_state": df_agg_tran_state,
        "agg_user_state": df_agg_user_state,
        "agg_insurance_state": df_agg_insurance_state,
        "map_ins_state": df_state_map_ins,
        "hover_ins_state": df_state_hover_ins,
        "map_tran_state": df_state_map_tran,
        "map_user_state": df_state_map_user,
        "map_district_ins": df_dis_map_ins,
        "hover_district_ins": df_dis_hover_ins,
        "map_district_tran": df_dis_map_tran,
        "hover_district_tran": df_dis_hover_tran,
        "map_district_user": df_dis_map_user,
        "hover_district_user": df_dis_hover_user,
        "top_ins_state": df_top_ins_state,
        "top_tran_state": df_top_tran_state,
        "top_user_state": df_top_user_state
    }
