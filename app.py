import streamlit as st
import json
import pandas as pd
import plotly.express as px
from data_transform import load_cleaned_data

from db_handler import connect_to_db  # (not used yet, reserved for Insights)

# App layout
st.set_page_config(page_title="PhonePe Pulse Dashboard", layout="wide")

# ---------- Sidebar ----------
st.sidebar.title("📊 Explore Data")
menu = st.sidebar.radio("Navigate", ["Home", "About", "Geo-Visualization", "Insights"])

# ---------- Home ----------
if menu == "Home":
    st.markdown("""
        <style>
        .hero-title { font-size: 48px; font-weight: 800; margin-bottom: .25rem; }
        .hero-sub { font-size: 18px; opacity: .85; }
        .section-title { font-size: 22px; font-weight: 700; margin: 18px 0 6px; }
        .tip { background: rgba(255,255,255,.04); border: 1px solid rgba(255,255,255,.08);
               padding: 10px 14px; border-radius: 10px; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="hero-title">📱 PhonePe Pulse India Dashboard</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-sub">Explore India’s digital payments landscape with interactive maps and insights powered by the open-source PhonePe Pulse dataset.</div>',
        unsafe_allow_html=True
    )
    st.write("")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("### 🗺️ Geo‑Visualization")
        st.markdown("- State & district maps\n- Transactions, Users, Insurance\n- Hover to see details")
    with c2:
        st.markdown("### 📈 Insights")
        st.markdown("- Quarterly trends\n- Top states & rankings\n- Device brand breakdown")
    with c3:
        st.markdown("### 🧰 Data")
        st.markdown("- 2018 → present (where available)\n- State/District granularity\n- Aggregated from Pulse JSON")

    st.markdown('<div class="section-title">🗂 Data Sources</div>', unsafe_allow_html=True)
    st.markdown("""
        - **Transactions** — Total amount (₹) and count of digital payments  
        - **Users** — Registered users, app opens, device brand shares  
        - **Insurance** — Premium amounts and transaction counts  
    """)

    st.markdown('<div class="section-title">🔍 How to Use</div>', unsafe_allow_html=True)
    st.markdown("""
        1. Go to **Geo‑Visualization** to view India or a single state (district view).  
        2. Pick **Data Type** (Transactions, Users, Insurance), **Year**, and **Quarter**.  
        3. Open **Insights** for trends, top‑10 rankings, and comparisons.  
    """)

    st.markdown('<div class="tip">💡 <b>Tip:</b> Start with <b>Geo‑Visualization</b> → choose <i>Country (All States)</i> to see the national picture, then drill down to districts.</div>', unsafe_allow_html=True)


# ---------- About ----------
elif menu == "About":
    st.title("📌 About This Project")
    st.markdown("""
    ### What is PhonePe?
    PhonePe is a digital payments platform accessible in 11 Indian languages. It enables users to perform UPI payments, recharges, bill payments, and more.

    ### What is PhonePe Pulse?
    PhonePe Pulse is an open-source geospatial data platform that shares digital transaction insights across India at the state, district, and pincode level.

    ### What does this dashboard do?
    - Extracts and stores Pulse data in a MySQL database
    - Creates interactive geo-visualizations with Plotly
    - Offers user-friendly filtering and insights
                
    🧾 **Note:**  
    - Transaction map shows total ₹ value transacted  
    - User map shows registered users per state  
    - Insurance map shows ₹ insurance premium paid  
    """)

# ---------- Geo Visualization ----------
elif menu == "Geo-Visualization":
    st.title("🗺️ Geo Visualization")
    st.markdown("Explore transaction, user, and insurance data on the Indian map.")

    @st.cache_data
    def load_geo_data():
        data = load_cleaned_data()

        def ensure_cols(df_like, cols):
            df = pd.DataFrame(df_like)
            for c in cols:
                if c not in df.columns:
                    df[c] = pd.NA
            return df[cols]

        return {
            "agg_transaction": ensure_cols(
                data["agg_tran_state"],
                ["state","year","quarter","amount","count",
                 "transaction_name","instrument_type","from_timestamp","to_timestamp","level","year_quarter"]
            ),
            "map_user": ensure_cols(
                data["map_user_state"],
                ["state","year","quarter","registered_users","app_opens"]
            ),
            "map_insurance": ensure_cols(
                data["map_ins_state"],
                ["lat","lng","metric","label","state","year","quarter"]
            ),
            "hover_ins_state": ensure_cols(
                data["hover_ins_state"],
                ["state","count","amount","type","year","quarter"]
            ),
            "map_district_tran": ensure_cols(
                data.get("map_district_tran", []),
                ["state","district","count","amount","instrument_type","year","quarter"]
            ),
        }

    geo_data = load_geo_data()

    # 🗂 Load GeoJSON
    with open("india_telengana.geojson", "r") as f:
        india_geojson = json.load(f)

    # ---------- Controls ----------
    map_scope = st.selectbox("Select Scope", ["Country (All States)", "State (Districts View)"])
    data_type = st.selectbox("Select Data Type", ["Transactions", "Users", "Insurance"])

    # Build year/quarter choices from the chosen data source to avoid empty combos
    if data_type == "Transactions":
        src_df = geo_data["agg_transaction"]
    elif data_type == "Users":
        src_df = geo_data["map_user"]
    else:
        src_df = pd.concat([geo_data["map_insurance"], geo_data["hover_ins_state"]], ignore_index=True)

    years = sorted(pd.Series(src_df["year"]).dropna().astype(int).unique().tolist())
    quarters = sorted(pd.Series(src_df["quarter"]).dropna().astype(int).unique().tolist())

    if not years or not quarters:
        st.warning("No data available for this data type.")
        st.stop()

    col1, col2 = st.columns(2)
    with col1:
        year = st.selectbox("Select Year", years, index=len(years)-1)
    with col2:
        quarter = st.selectbox("Select Quarter", quarters, index=0)

    # Hyphenated-to-geojson state name normalization
    state_name_map = {
        "Andaman-&-Nicobar-Islands": "Andaman and Nicobar",
        "Andhra-Pradesh": "Andhra Pradesh",
        "Arunachal-Pradesh": "Arunachal Pradesh",
        "Assam": "Assam",
        "Bihar": "Bihar",
        "Chandigarh": "Chandigarh",
        "Chhattisgarh": "Chhattisgarh",
        "Dadra-&-Nagar-Haveli-&-Daman-&-Diu": "Dadra and Nagar Haveli",
        "Delhi": "Delhi",
        "Goa": "Goa",
        "Gujarat": "Gujarat",
        "Haryana": "Haryana",
        "Himachal-Pradesh": "Himachal Pradesh",
        "Jammu-&-Kashmir": "Jammu and Kashmir",
        "Jharkhand": "Jharkhand",
        "Karnataka": "Karnataka",
        "Kerala": "Kerala",
        "Ladakh": "Jammu and Kashmir",
        "Lakshadweep": "Lakshadweep",
        "Madhya-Pradesh": "Madhya Pradesh",
        "Maharashtra": "Maharashtra",
        "Manipur": "Manipur",
        "Meghalaya": "Meghalaya",
        "Mizoram": "Mizoram",
        "Nagaland": "Nagaland",
        "Odisha": "Orissa",
        "Puducherry": "Puducherry",
        "Punjab": "Punjab",
        "Rajasthan": "Rajasthan",
        "Sikkim": "Sikkim",
        "Tamil-Nadu": "Tamil Nadu",
        "Telangana": "Telangana",
        "Tripura": "Tripura",
        "Uttar-Pradesh": "Uttar Pradesh",
        "Uttarakhand": "Uttaranchal",
        "West-Bengal": "West Bengal"
    }

    # ---------- Render button ----------
    if st.button("Generate Map"):
        # COUNTRY LEVEL VIEW
        if map_scope == "Country (All States)":

            df_grouped = None
            color_col = ""
            hover_cols = []
            title = ""

            if data_type == "Transactions":
                df = geo_data["agg_transaction"]
                df_filtered = df[(df["year"] == year) & (df["quarter"] == quarter)]
                df_grouped = df_filtered.groupby("state", as_index=False).agg({"amount": "sum", "count": "sum"})
                df_grouped["state"] = df_grouped["state"].replace(state_name_map)
                color_col = "amount"
                hover_cols = ["state", "amount", "count"]
                title = f"Total Transaction Amount by State - Q{quarter} {year}"

            elif data_type == "Users":
                df = geo_data["map_user"]
                df_filtered = df[(df["year"] == year) & (df["quarter"] == quarter)].copy()
                df_filtered["state"] = (
                    df_filtered["state"].astype(str).str.strip().str.replace("-", " ").str.title().replace(state_name_map)
                )
                df_grouped = df_filtered.groupby("state", as_index=False)["registered_users"].sum()
                color_col = "registered_users"
                hover_cols = ["state", "registered_users"]
                title = f"Registered Users by State - Q{quarter} {year}"

            else:  # Insurance
                grid = geo_data["map_insurance"]
                df_grid = grid[(grid["year"] == year) & (grid["quarter"] == quarter)].copy()

                if df_grid.empty:
                    hv = geo_data["hover_ins_state"]
                    df_hov = hv[(hv["year"] == year) & (hv["quarter"] == quarter)].copy()
                    df_grouped = df_hov.groupby("state", as_index=False)["amount"].sum()
                else:
                    df_grid["state"] = df_grid["state"].astype(str)
                    df_grouped = df_grid.groupby("state", as_index=False)["metric"].sum()
                    df_grouped = df_grouped.rename(columns={"metric": "amount"})

                # Normalize names
                df_grouped["state"] = (
                    df_grouped["state"].astype(str).str.strip().str.replace("-", " ").str.title().replace({
                        "Andaman & Nicobar Islands": "Andaman and Nicobar",
                        "Dadra & Nagar Haveli & Daman & Diu": "Dadra and Nagar Haveli",
                        "Odisha": "Orissa",
                        "Uttarakhand": "Uttaranchal",
                        "Jammu & Kashmir": "Jammu and Kashmir",
                    })
                )

                color_col = "amount"
                hover_cols = ["state", "amount"]
                title = f"Insurance Premium Collected by State - Q{quarter} {year}"

            # Handle empty data
            if df_grouped is None or df_grouped.empty:
                st.warning("⚠️ No data available for the selected filters.")
            else:
                fig = px.choropleth(
                    df_grouped,
                    geojson=india_geojson,
                    featureidkey="properties.NAME_1",
                    locations="state",
                    color=color_col,
                    hover_data=hover_cols,
                    title=title,
                    height=600
                )
                fig.update_traces(marker_line_width=0.5, marker_line_color="white")
                fig.update_geos(
                    fitbounds="locations",
                    visible=False,
                    showcountries=True,
                    showcoastlines=True,
                    showland=True
                )
                st.plotly_chart(fig, use_container_width=True)

                with st.expander("📄 View Data Table"):
                    st.dataframe(df_grouped)

        # STATE / DISTRICT VIEW
        else:
            st.markdown("### 🔍 District-wise View")

            # Restricting available states to those that actually have district data for the selected period
            dis_df = geo_data["map_district_tran"]
            dis_period = dis_df[(dis_df["year"] == year) & (dis_df["quarter"] == quarter)]
            available_states = sorted(dis_period["state"].dropna().astype(str).unique().tolist())
            if not available_states:
                st.warning("⚠️ No district-level transaction data available for this period.")
                st.stop()

            selected_state = st.selectbox("Choose a State", available_states)

            df_filtered = dis_period[dis_period["state"] == selected_state].copy()
            if df_filtered.empty:
                st.warning("⚠️ No district data available for the selected state and time.")
            else:
                with open("2011_Dist.geojson", "r") as f:
                    dist_geojson = json.load(f)

                df_filtered["district"] = df_filtered["district"].astype(str).str.title()

                fig = px.choropleth(
                    df_filtered,
                    geojson=dist_geojson,
                    featureidkey="properties.district",
                    locations="district",
                    color="amount",
                    hover_data=["district", "count", "amount"],
                    color_continuous_scale="Plasma",
                    title=f"District-Level Transactions in {selected_state} - Q{quarter} {year}",
                    height=600
                )
                fig.update_geos(fitbounds="locations", visible=False)
                fig.update_traces(marker_line_width=0.5, marker_line_color="white")
                st.plotly_chart(fig, use_container_width=True)

                with st.expander("📄 View District Data"):
                    st.dataframe(df_filtered)

# ---------- Insights ----------
elif menu == "Insights":
    st.title("📈 Data Insights")
    st.markdown("Use the dropdown to explore analytics and insights from PhonePe Pulse data.")

    # Load all transformed data
    data = load_cleaned_data()

    insight_option = st.selectbox("Select Insight", [
        "1. Top 10 States by Transaction Amount",
        "2. Top 10 States by Transaction Count",
        "3. Quarterly Transaction Trend (State-wise)",
        "4. Top 10 States by Registered Users",
        "5. Device Brand Distribution",
        "6. Quarterly Registered Users Trend (State-wise)",
        "7. Top 10 States by Insurance Premium Paid",
        "8. Top 10 States by Insurance Count",
        "9. App Opens vs Registered Users (State-wise)",
        "10. Insurance Premium vs Transaction Amount"
    ])

    # === 1. Top 10 States by Transaction Amount ===
    if insight_option == "1. Top 10 States by Transaction Amount":
        df = data["agg_tran_state"].groupby("state", as_index=False)["amount"].sum()
        top_df = df.sort_values(by="amount", ascending=False).head(10)
        st.subheader("💸 Top 10 States by Total Transaction Amount")
        st.bar_chart(top_df.set_index("state")["amount"])

    # === 2. Top 10 States by Transaction Count ===
    elif insight_option == "2. Top 10 States by Transaction Count":
        df = data["agg_tran_state"].groupby("state", as_index=False)["count"].sum()
        top_df = df.sort_values(by="count", ascending=False).head(10)
        st.subheader("🔢 Top 10 States by Transaction Count")
        st.bar_chart(top_df.set_index("state")["count"])

    # === 3. Quarterly Transaction Trend (State-wise) ===
    elif insight_option == "3. Quarterly Transaction Trend (State-wise)":
        df_all = data["agg_tran_state"].copy()

        df_all["year"] = pd.to_numeric(df_all["year"], errors="coerce").astype("Int64")
        df_all["quarter"] = pd.to_numeric(df_all["quarter"], errors="coerce").astype("Int64")
        df_all["amount"] = pd.to_numeric(df_all["amount"], errors="coerce")

        state = st.selectbox("Select State", sorted(df_all["state"].dropna().unique()))

        df_state_q = (
            df_all[df_all["state"] == state]
            .groupby(["year", "quarter"], as_index=False)["amount"].sum()
            .dropna(subset=["year", "quarter"])
            .sort_values(["year", "quarter"])
        )
        df_state_q["year_quarter"] = df_state_q["year"].astype(int).astype(str) + "-Q" + df_state_q["quarter"].astype(int).astype(str)

        if df_state_q.empty:
            st.warning(f"No transaction data available for {state}.")
        else:
            st.subheader(f"📈 Transaction Amount Trend for {state}")
            fig = px.line(
                df_state_q,
                x="year_quarter",
                y="amount",
                markers=True,
                labels={"year_quarter": "Quarter", "amount": "Transaction Amount (₹)"},
                height=420,
            )
            st.plotly_chart(fig, use_container_width=True)

            with st.expander("📄 Data"):
                st.dataframe(df_state_q[["year", "quarter", "amount"]].reset_index(drop=True))


    # === 4. Top 10 States by Registered Users ===
    elif insight_option == "4. Top 10 States by Registered Users":
        df = data["agg_user_state"].groupby("state", as_index=False)["registered_users"].sum()
        top_df = df.sort_values(by="registered_users", ascending=False).head(10)
        st.subheader("👥 Top 10 States by Registered Users")
        st.bar_chart(top_df.set_index("state")["registered_users"])

    # === 5. Device Brand Distribution ===
    elif insight_option == "5. Device Brand Distribution":
        df = data["agg_user_state"]
        brand_df = df.groupby("brand", as_index=False)["count"].sum()
        brand_df = brand_df[brand_df["brand"] != "nan"].sort_values(by="count", ascending=False)
        st.subheader("📱 Device Brand Usage by PhonePe Users")
        st.bar_chart(brand_df.set_index("brand")["count"])

    # === 6. Quarterly Registered Users Trend (State-wise) ===
    elif insight_option == "6. Quarterly Registered Users Trend (State-wise)":

        df = pd.DataFrame(data["map_user_state"]).copy()

        for c in ["state", "year", "quarter", "registered_users"]:
            if c not in df.columns:
                df[c] = pd.NA

        df = df.dropna(subset=["year", "quarter"])
        df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
        df["quarter"] = pd.to_numeric(df["quarter"], errors="coerce").astype("Int64")
        df["state"] = df["state"].astype(str).str.strip().str.title()

        if df.empty:
            st.warning("No user data with year/quarter available.")
        else:
            state = st.selectbox("Select State", sorted(df["state"].dropna().unique()))
            df_filtered = df[df["state"] == state].sort_values(by=["year", "quarter"]).copy()
            if df_filtered.empty:
                st.warning(f"No data for {state}.")
            else:
                df_filtered["year_quarter"] = df_filtered["year"].astype(str) + "-Q" + df_filtered["quarter"].astype(str)
                st.subheader(f"📈 Registered Users Trend in {state}")
                st.line_chart(df_filtered.set_index("year_quarter")["registered_users"])

    # === 7. Top 10 States by Insurance Premium Paid ===
    elif insight_option == "7. Top 10 States by Insurance Premium Paid":

        grid = pd.DataFrame(data["map_ins_state"])[["state", "metric"]].copy()
        hov  = pd.DataFrame(data["hover_ins_state"])[["state", "amount"]].rename(columns={"amount": "metric"})
        df = pd.concat([grid, hov], ignore_index=True)

        df["state"] = df["state"].astype(str)
        df["metric"] = pd.to_numeric(df["metric"], errors="coerce")
        df = df.dropna(subset=["state", "metric"])
        df = df[df["state"].str.lower() != "nan"]

        top_df = (df.groupby("state", as_index=False)["metric"].sum()
                    .sort_values("metric", ascending=False)
                    .head(10))

        st.subheader(" Top 10 States by Insurance Premium Paid")

        if top_df.empty:
            st.info("No insurance premium data available.")
        else:
            st.bar_chart(top_df.set_index("state")["metric"])

            st.markdown("#### Answers (ranked)")
            for i, r in enumerate(top_df.itertuples(index=False), start=1):
                st.markdown(f"**{i}. {r.state}** — ₹{float(r.metric):,.2f}")

            st.markdown("#### 📄 Table")
            st.dataframe(top_df.reset_index(drop=True))

            st.download_button(
                "Download CSV (Insurance Premium Paid — Top 10)",
                top_df.to_csv(index=False).encode("utf-8"),
                file_name="top10_insurance_premium_paid.csv",
                mime="text/csv",
            )

    # === 8. Top 10 States by Insurance Count ===
    elif insight_option == "8. Top 10 States by Insurance Count":

        hov_state = pd.DataFrame(data["hover_ins_state"])[["state", "count"]]
        hov_dist  = pd.DataFrame(data.get("hover_district_ins", []))[["state", "count"]] if "hover_district_ins" in data else pd.DataFrame(columns=["state","count"])
        df = pd.concat([hov_state, hov_dist], ignore_index=True)

        df["state"] = df["state"].astype(str)
        df["count"] = pd.to_numeric(df["count"], errors="coerce")
        df = df.dropna(subset=["state", "count"])
        df = df[df["state"].str.lower() != "nan"]

        top_df = (df.groupby("state", as_index=False)["count"].sum()
                    .sort_values("count", ascending=False)
                    .head(10))

        st.subheader("📦 Top 10 States by Insurance Transactions")

        if top_df.empty:
            st.info("No insurance count data available.")
        else:
            st.bar_chart(top_df.set_index("state")["count"])

            st.markdown("#### ✅ Answers (ranked)")
            for i, r in enumerate(top_df.itertuples(index=False), start=1):
                st.markdown(f"**{i}. {r.state}** — {int(r.count):,} transactions")

            st.markdown("#### 📄 Table")
            st.dataframe(top_df.reset_index(drop=True))

            st.download_button(
                "Download CSV (Insurance Count — Top 10)",
                top_df.to_csv(index=False).encode("utf-8"),
                file_name="top10_insurance_count.csv",
                mime="text/csv",
            )

    # === 9. App Opens vs Registered Users ===
    elif insight_option == "9. App Opens vs Registered Users (State-wise)":
        df = data["agg_user_state"].groupby("state", as_index=False).agg({
            "registered_users": "sum",
            "app_opens": "sum"
        }).copy()

        df["registered_users"] = pd.to_numeric(df["registered_users"], errors="coerce")
        df["app_opens"] = pd.to_numeric(df["app_opens"], errors="coerce")
        df = df.dropna(subset=["registered_users", "app_opens"])

        st.subheader("📊 App Opens vs Registered Users")
        fig = px.scatter(
            df,
            x="registered_users",
            y="app_opens",
            hover_name="state",
            labels={"registered_users": "Registered Users", "app_opens": "App Opens"},
            height=500,
        )
        st.plotly_chart(fig, use_container_width=True)


    # === 10. Insurance Premium vs Transaction Amount ===
    elif insight_option == "10. Insurance Premium vs Transaction Amount":
        df_tran = data["agg_tran_state"].groupby("state", as_index=False)["amount"].sum()
        df_ins = data["map_ins_state"].groupby("state", as_index=False)["metric"].sum()
        merged = pd.merge(df_tran, df_ins, on="state", how="inner").rename(
            columns={"amount": "transaction_amount", "metric": "insurance_amount"}
        )

        merged["transaction_amount"] = pd.to_numeric(merged["transaction_amount"], errors="coerce")
        merged["insurance_amount"] = pd.to_numeric(merged["insurance_amount"], errors="coerce")
        merged = merged.dropna(subset=["transaction_amount", "insurance_amount"])

        st.subheader("📊 Insurance Premium vs Transaction Amount")
        fig = px.scatter(
            merged,
            x="transaction_amount",
            y="insurance_amount",
            hover_name="state",
            labels={"transaction_amount": "Transaction Amount (₹)", "insurance_amount": "Insurance Premium (₹)"},
            height=500,
        )
        st.plotly_chart(fig, use_container_width=True)

