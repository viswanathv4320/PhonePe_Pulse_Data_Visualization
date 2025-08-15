import pandas as pd
import os
import json
from datetime import datetime, UTC

# AGGREGATED FOLDER DATA
def aggregated_data(base_path):

    agg_country_ins_rows = []
    agg_state_ins_rows = []
    agg_country_tran_rows = []
    agg_state_tran_rows = []
    agg_country_user_rows = []
    agg_state_user_rows = []

    for agg_type in os.listdir(base_path):
        agg_type_path = os.path.join(base_path, agg_type)

        if agg_type == "insurance":
            agg_ins_country_path = os.path.join(agg_type_path, "country", "india")

            for item in os.listdir(agg_ins_country_path):
                item_path = os.path.join(agg_ins_country_path, item)
                if not os.path.isdir(item_path):
                    continue

                if item.isdigit():
                    year = item
                    year_path = item_path

                    for quarter_file in os.listdir(year_path):
                        quarter_path = os.path.join(year_path, quarter_file)
                        if not quarter_file.endswith(".json"):
                            continue
                        quarter = quarter_file.replace(".json", "")

                        with open(quarter_path, "r") as f:
                            data = json.load(f)

                        from_ts = datetime.fromtimestamp(data["data"]["from"] / 1000, tz=UTC).isoformat()
                        to_ts = datetime.fromtimestamp(data["data"]["to"] / 1000, tz=UTC).isoformat()

                        for transaction in data["data"].get("transactionData", []):
                            transaction_name = transaction.get("name", None)
                            for payment in transaction.get("paymentInstruments", []):
                                row = {
                                    "level": "country",
                                    "year": year,
                                    "quarter": quarter,
                                    "from_timestamp": from_ts,
                                    "to_timestamp": to_ts,
                                    "transaction_name": transaction_name,
                                    "instrument_type": payment.get("type", None),
                                    "count": payment.get("count", None),
                                    "amount": payment.get("amount", None)
                                }
                                agg_country_ins_rows.append(row)

                elif item == "state":
                    state_path = item_path
                    for state_name in os.listdir(state_path):
                        state_folder = os.path.join(state_path, state_name)
                        if not os.path.isdir(state_folder):
                            continue

                        for year in os.listdir(state_folder):
                            year_path = os.path.join(state_folder, year)
                            if not os.path.isdir(year_path):
                                continue

                            for quarter_file in os.listdir(year_path):
                                file_path = os.path.join(year_path, quarter_file)
                                if not quarter_file.endswith(".json"):
                                    continue
                                quarter = quarter_file.replace(".json", "")

                                with open(file_path, "r") as f:
                                    data = json.load(f)

                                from_ts = datetime.fromtimestamp(data["data"]["from"] / 1000, tz=UTC).isoformat()
                                to_ts = datetime.fromtimestamp(data["data"]["to"] / 1000, tz=UTC).isoformat()

                                for transaction in data["data"].get("transactionData", []):
                                    for payment in transaction.get("paymentInstruments", []):
                                        row = {
                                            "level": "state",
                                            "state": state_name,
                                            "year": year,
                                            "quarter": quarter,
                                            "from_timestamp": from_ts,
                                            "to_timestamp": to_ts,
                                            "transaction_name": transaction.get("name", None),
                                            "instrument_type": payment.get("type", None),
                                            "count": payment.get("count", None),
                                            "amount": payment.get("amount", None)
                                        }
                                        agg_state_ins_rows.append(row)

        elif agg_type == "transaction":
            agg_tran_country_path = os.path.join(agg_type_path, "country", "india")

            for item in os.listdir(agg_tran_country_path):
                item_path = os.path.join(agg_tran_country_path, item)
                if not os.path.isdir(item_path):
                    continue

                if item.isdigit():
                    year = item
                    year_path = item_path

                    for quarter_file in os.listdir(year_path):
                        quarter_path = os.path.join(year_path, quarter_file)
                        if not quarter_file.endswith(".json"):
                            continue
                        quarter = quarter_file.replace(".json", "")

                        with open(quarter_path, "r") as f:
                            data = json.load(f)

                        from_ts = datetime.fromtimestamp(data["data"]["from"] / 1000, tz=UTC).isoformat()
                        to_ts = datetime.fromtimestamp(data["data"]["to"] / 1000, tz=UTC).isoformat()

                        for transaction in data["data"]["transactionData"]:
                            for payment in transaction["paymentInstruments"]:
                                row = {
                                    "level": "country",
                                    "year": year,
                                    "quarter": quarter,
                                    "from_timestamp": from_ts,
                                    "to_timestamp": to_ts,
                                    "transaction_name": transaction.get("name", None),
                                    "instrument_type": payment.get("type", None),
                                    "count": payment.get("count", None),
                                    "amount": payment.get("amount", None)
                                }
                                agg_country_tran_rows.append(row)

                elif item == "state":
                    state_path = item_path
                    for state_name in os.listdir(state_path):
                        state_folder = os.path.join(state_path, state_name)
                        if not os.path.isdir(state_folder):
                            continue

                        for year in os.listdir(state_folder):
                            year_path = os.path.join(state_folder, year)
                            if not os.path.isdir(year_path):
                                continue

                            for quarter_file in os.listdir(year_path):
                                file_path = os.path.join(year_path, quarter_file)
                                if not quarter_file.endswith(".json"):
                                    continue
                                quarter = quarter_file.replace(".json", "")

                                with open(file_path, "r") as f:
                                    data = json.load(f)

                                from_ts = datetime.fromtimestamp(data["data"]["from"] / 1000, tz=UTC).isoformat()
                                to_ts = datetime.fromtimestamp(data["data"]["to"] / 1000, tz=UTC).isoformat()

                                for transaction in data["data"]["transactionData"]:
                                    for payment in transaction["paymentInstruments"]:
                                        row = {
                                            "level": "state",
                                            "state": state_name,
                                            "year": year,
                                            "quarter": quarter,
                                            "from_timestamp": from_ts,
                                            "to_timestamp": to_ts,
                                            "transaction_name": transaction.get("name", None),
                                            "instrument_type": payment.get("type", None),
                                            "count": payment.get("count", None),
                                            "amount": payment.get("amount", None)
                                        }
                                        agg_state_tran_rows.append(row)

        elif agg_type == "user":
            agg_user_country_path = os.path.join(agg_type_path, "country", "india")

            for item in os.listdir(agg_user_country_path):
                item_path = os.path.join(agg_user_country_path, item)
                if not os.path.isdir(item_path):
                    continue

                if item.isdigit():
                    year = item
                    year_path = item_path

                    for quarter_file in os.listdir(year_path):
                        quarter_path = os.path.join(year_path, quarter_file)
                        if not quarter_file.endswith(".json"):
                            continue
                        quarter = quarter_file.replace(".json", "")

                        with open(quarter_path, "r") as f:
                            data = json.load(f)

                        aggregated = data["data"].get("aggregated", {})
                        users_by_device = data["data"].get("usersByDevice", {})

                        reg_users = aggregated.get("registeredUsers", None)
                        app_opens = aggregated.get("appOpens", None)

                        if users_by_device and isinstance(users_by_device, list):
                            for device in users_by_device:
                                row = {
                                    "level": "country",
                                    "registered_users": reg_users,
                                    "app_opens": app_opens,
                                    "brand": device.get("brand", None),
                                    "count": device.get("count", None),
                                    "percentage": device.get("percentage", None)
                                }
                                agg_country_user_rows.append(row)

                elif item == "state":
                    state_path = item_path
                    for state_name in os.listdir(state_path):
                        state_folder = os.path.join(state_path, state_name)
                        if not os.path.isdir(state_folder):
                            continue

                        for year in os.listdir(state_folder):
                            year_path = os.path.join(state_folder, year)
                            if not os.path.isdir(year_path):
                                continue

                            for quarter_file in os.listdir(year_path):
                                file_path = os.path.join(year_path, quarter_file)
                                if not quarter_file.endswith(".json"):
                                    continue
                                quarter = quarter_file.replace(".json", "")

                                with open(file_path, "r") as f:
                                    data = json.load(f)

                                aggregated = data["data"].get("aggregated", {})
                                users_by_device = data["data"].get("usersByDevice", {})

                                reg_users = aggregated.get("registeredUsers", None)
                                app_opens = aggregated.get("appOpens", None)

                                if users_by_device and isinstance(users_by_device, list):
                                    for device in users_by_device:
                                        row = {
                                            "level": "state",
                                            "state": state_name,
                                            "registered_users": reg_users,
                                            "app_opens": app_opens,
                                            "brand": device.get("brand", None),
                                            "count": device.get("count", None),
                                            "percentage": device.get("percentage", None)
                                        }
                                        agg_state_user_rows.append(row)

    return {
        "insurance": {
            "country": agg_country_ins_rows,
            "state": agg_state_ins_rows
        },
        "transaction": {
            "country": agg_country_tran_rows,
            "state": agg_state_tran_rows
        },
        "user": {
            "country": agg_country_user_rows,
            "state": agg_state_user_rows
        }
    }

    
if __name__ == "__main__":
    base_path = "/Users/viswanath/Phonepe_Pulse_Data_Visualization/pulse/data/aggregated"
    
    result = aggregated_data(base_path)

# MAP FOLDER DATA
def map_data(base_path):
    import os, json

    dis_map_ins = []
    state_map_ins = []
    dis_hover_ins = []
    state_hover_ins = []
    dis_map_tran = []
    state_map_tran = []
    dis_map_user = []
    state_map_user = []
    dis_hover_tran = []
    dis_hover_user = []

    def safe_listdir(path):
        return [x for x in os.listdir(path) if not x.startswith(".")]

    for map_type in safe_listdir(base_path):
        map_type_path = os.path.join(base_path, map_type)
        if not os.path.isdir(map_type_path):
            continue

        # ---------------- INSURANCE ----------------
        if map_type == "insurance":
            # State-level grid
            state_path = os.path.join(map_type_path, "country", "india", "state")
            if os.path.isdir(state_path):
                for state in safe_listdir(state_path):
                    state_dir = os.path.join(state_path, state)
                    if not os.path.isdir(state_dir): 
                        continue
                    for year in safe_listdir(state_dir):
                        year_dir = os.path.join(state_dir, year)
                        if not os.path.isdir(year_dir): 
                            continue
                        for qfile in safe_listdir(year_dir):
                            if not qfile.endswith(".json"): 
                                continue
                            with open(os.path.join(year_dir, qfile)) as f:
                                data = json.load(f)
                            for entry in data.get("data", {}).get("data", []):
                                if isinstance(entry, dict):
                                    state_map_ins.append({
                                        "lat": entry.get("lat"),
                                        "lng": entry.get("lng"),
                                        "metric": entry.get("metric"),
                                        "label": entry.get("label"),
                                        "state": state,
                                        "year": int(year),
                                        "quarter": int(qfile.split(".")[0]),
                                    })

            # Hover – state
            hover_state = os.path.join(map_type_path, "hover", "country", "india")
            if os.path.isdir(hover_state):
                for year in safe_listdir(hover_state):
                    for qfile in safe_listdir(os.path.join(hover_state, year)):
                        if not qfile.endswith(".json"): 
                            continue
                        with open(os.path.join(hover_state, year, qfile)) as f:
                            data = json.load(f)
                        for state, details in data.get("data", {}).get("hoverData", {}).items():
                            metric0 = (details.get("metric") or [{}])[0]
                            state_hover_ins.append({
                                "state": state,
                                "count": metric0.get("count", 0),
                                "amount": metric0.get("amount", 0.0),
                                "type": metric0.get("type"),
                                "year": int(year),
                                "quarter": int(qfile.split(".")[0]),
                            })

            # Hover – district
            hover_dist = os.path.join(map_type_path, "hover", "country", "india", "state")
            if os.path.isdir(hover_dist):
                for state in safe_listdir(hover_dist):
                    state_dir = os.path.join(hover_dist, state)
                    for year in safe_listdir(state_dir):
                        for qfile in safe_listdir(os.path.join(state_dir, year)):
                            if not qfile.endswith(".json"): 
                                continue
                            with open(os.path.join(state_dir, year, qfile)) as f:
                                data = json.load(f)
                            for district, details in data.get("data", {}).get("hoverData", {}).items():
                                metric0 = (details.get("metric") or [{}])[0]
                                dis_hover_ins.append({
                                    "state": state,
                                    "district": district,
                                    "count": metric0.get("count", 0),
                                    "amount": metric0.get("amount", 0.0),
                                    "type": metric0.get("type"),
                                    "year": int(year),
                                    "quarter": int(qfile.split(".")[0]),
                                })

        # ---------------- TRANSACTION ----------------
        if map_type == "transaction":
            # Hover – state (list)
            hover_state = os.path.join(map_type_path, "hover", "country", "india")
            if os.path.isdir(hover_state):
                for year in safe_listdir(hover_state):
                    for qfile in safe_listdir(os.path.join(hover_state, year)):
                        if not qfile.endswith(".json"): 
                            continue
                        with open(os.path.join(hover_state, year, qfile)) as f:
                            data = json.load(f)
                        for item in data.get("data", {}).get("hoverDataList", []):
                            metric0 = (item.get("metric") or [{}])[0]
                            state_map_tran.append({
                                "state": item.get("name"),
                                "count": metric0.get("count", 0),
                                "amount": metric0.get("amount", 0.0),
                                "year": int(year),
                                "quarter": int(qfile.split(".")[0]),
                            })

            # Hover – district (list or dict)
            hover_dist = os.path.join(map_type_path, "hover", "country", "india", "state")
            if os.path.isdir(hover_dist):
                for state in safe_listdir(hover_dist):
                    state_dir = os.path.join(hover_dist, state)
                    for year in safe_listdir(state_dir):
                        for qfile in safe_listdir(os.path.join(state_dir, year)):
                            if not qfile.endswith(".json"): 
                                continue
                            with open(os.path.join(state_dir, year, qfile)) as f:
                                data = json.load(f)
                            dd = data.get("data", {})
                            if "hoverDataList" in dd:
                                for item in dd["hoverDataList"]:
                                    metric0 = (item.get("metric") or [{}])[0]
                                    dis_map_tran.append({
                                        "state": state,
                                        "district": item.get("name"),
                                        "count": metric0.get("count", 0),
                                        "amount": metric0.get("amount", 0.0),
                                        "instrument_type": metric0.get("type"),
                                        "year": int(year),
                                        "quarter": int(qfile.split(".")[0]),
                                    })
                            else:
                                for district, details in dd.get("hoverData", {}).items():
                                    metric0 = (details.get("metric") or [{}])[0]
                                    dis_map_tran.append({
                                        "state": state,
                                        "district": district,
                                        "count": metric0.get("count", 0),
                                        "amount": metric0.get("amount", 0.0),
                                        "instrument_type": metric0.get("type"),
                                        "year": int(year),
                                        "quarter": int(qfile.split(".")[0]),
                                    })

        # ---------------- USER ----------------
        if map_type == "user":
            # Hover – state
            hover_state = os.path.join(map_type_path, "hover", "country", "india")
            if os.path.isdir(hover_state):
                for year in safe_listdir(hover_state):
                    for qfile in safe_listdir(os.path.join(hover_state, year)):
                        if not qfile.endswith(".json"): 
                            continue
                        with open(os.path.join(hover_state, year, qfile)) as f:
                            data = json.load(f)
                        for state, details in data.get("data", {}).get("hoverData", {}).items():
                            state_map_user.append({
                                "state": state,
                                "registered_users": details.get("registeredUsers", 0),
                                "app_opens": details.get("appOpens", 0),
                                "year": int(year),
                                "quarter": int(qfile.split(".")[0]),
                            })

            # Hover – district
            hover_dist = os.path.join(map_type_path, "hover", "country", "india", "state")
            if os.path.isdir(hover_dist):
                for state in safe_listdir(hover_dist):
                    state_dir = os.path.join(hover_dist, state)
                    for year in safe_listdir(state_dir):
                        for qfile in safe_listdir(os.path.join(state_dir, year)):
                            if not qfile.endswith(".json"): 
                                continue
                            with open(os.path.join(state_dir, year, qfile)) as f:
                                data = json.load(f)
                            for district, details in data.get("data", {}).get("hoverData", {}).items():
                                dis_map_user.append({
                                    "state": state,
                                    "district": district,
                                    "registered_users": details.get("registeredUsers", 0),
                                    "app_opens": details.get("appOpens", 0),
                                    "year": int(year),
                                    "quarter": int(qfile.split(".")[0]),
                                })

    dis_hover_tran = list(dis_map_tran)
    dis_hover_user = list(dis_map_user)

    return (
        dis_map_ins,
        state_map_ins,
        dis_hover_ins,
        state_hover_ins,
        dis_map_tran,
        state_map_tran,
        dis_map_user,
        state_map_user,
        dis_hover_tran,
        dis_hover_user
    )


# TOP FOLDER DATA
def top_data(base_path):
    import os
    import json

    def is_hidden_or_not_dir(path):
        name = os.path.basename(path)
        return name.startswith(".") or not os.path.isdir(path)

    def is_not_json_file(path):
        name = os.path.basename(path)
        return name.startswith(".") or (not name.endswith(".json")) or (not os.path.isfile(path))

    top_country_ins_rows = []
    top_state_ins_rows = []
    top_country_tran_rows = []
    top_state_tran_rows = []
    top_country_user_rows = []
    top_state_user_rows = []

    for top_type in os.listdir(base_path):
        top_type_path = os.path.join(base_path, top_type)
        if is_hidden_or_not_dir(top_type_path):
            continue

        # ------------------------- INSURANCE -------------------------
        if top_type == "insurance":
            # Country level
            country_path = os.path.join(top_type_path, "country", "india")
            if not os.path.isdir(country_path):
                pass
            else:
                for year in os.listdir(country_path):
                    year_path = os.path.join(country_path, year)
                    if is_hidden_or_not_dir(year_path):
                        continue
                    for quarter_file in os.listdir(year_path):
                        quarter_path = os.path.join(year_path, quarter_file)
                        if is_not_json_file(quarter_path):
                            continue
                        quarter = quarter_file.replace(".json", "")
                        try:
                            with open(quarter_path, "r") as f:
                                data = json.load(f)
                        except Exception:
                            continue

                        sep_data = data.get("data", {})

                        for state in sep_data.get("states", []):
                            metric = state.get("metric", {}) or {}
                            top_country_ins_rows.append({
                                "level": "state",
                                "year": year,
                                "quarter": quarter,
                                "entity": state.get("entityName"),
                                "count": metric.get("count"),
                                "amount": metric.get("amount"),
                            })

                        for district in sep_data.get("districts", []):
                            metric = district.get("metric", {}) or {}
                            top_country_ins_rows.append({
                                "level": "district",
                                "year": year,
                                "quarter": quarter,
                                "entity": district.get("entityName"),
                                "count": metric.get("count"),
                                "amount": metric.get("amount"),
                            })

                        for pincode in sep_data.get("pincodes", []):
                            metric = pincode.get("metric", {}) or {}
                            top_country_ins_rows.append({
                                "level": "pincode",
                                "year": year,
                                "quarter": quarter,
                                "entity": pincode.get("entityName"),
                                "count": metric.get("count"),
                                "amount": metric.get("amount"),
                            })

            # State level
            state_path = os.path.join(top_type_path, "country", "india", "state")
            if os.path.isdir(state_path):
                for state_name in os.listdir(state_path):
                    state_folder = os.path.join(state_path, state_name)
                    if is_hidden_or_not_dir(state_folder):
                        continue
                    for year in os.listdir(state_folder):
                        year_path = os.path.join(state_folder, year)
                        if is_hidden_or_not_dir(year_path):
                            continue
                        for quarter_file in os.listdir(year_path):
                            quarter_path = os.path.join(year_path, quarter_file)
                            if is_not_json_file(quarter_path):
                                continue
                            quarter = quarter_file.replace(".json", "")
                            try:
                                with open(quarter_path, "r") as f:
                                    data = json.load(f)
                            except Exception:
                                continue

                            sep_data = data.get("data", {})

                            for district in sep_data.get("districts", []):
                                metric = district.get("metric", {}) or {}
                                top_state_ins_rows.append({
                                    "state": state_name,
                                    "level": "district",
                                    "year": year,
                                    "quarter": quarter,
                                    "entity": district.get("entityName"),
                                    "count": metric.get("count"),
                                    "amount": metric.get("amount"),
                                })

                            for pincode in sep_data.get("pincodes", []):
                                metric = pincode.get("metric", {}) or {}
                                top_state_ins_rows.append({
                                    "state": state_name,
                                    "level": "pincode",
                                    "year": year,
                                    "quarter": quarter,
                                    "entity": pincode.get("entityName"),
                                    "count": metric.get("count"),
                                    "amount": metric.get("amount"),
                                })

        # ------------------------- TRANSACTION -------------------------
        if top_type == "transaction":
            # Country level
            country_path = os.path.join(top_type_path, "country", "india")
            if os.path.isdir(country_path):
                for year in os.listdir(country_path):
                    year_path = os.path.join(country_path, year)
                    if is_hidden_or_not_dir(year_path):
                        continue
                    for quarter_file in os.listdir(year_path):
                        quarter_path = os.path.join(year_path, quarter_file)
                        if is_not_json_file(quarter_path):
                            continue
                        quarter = quarter_file.replace(".json", "")
                        try:
                            with open(quarter_path, "r") as f:
                                data = json.load(f)
                        except Exception:
                            continue

                        sep_data = data.get("data", {})

                        for state in sep_data.get("states", []):
                            metric = state.get("metric", {}) or {}
                            top_country_tran_rows.append({
                                "level": "state",
                                "year": year,
                                "quarter": quarter,
                                "entity": state.get("entityName"),
                                "count": metric.get("count"),
                                "amount": metric.get("amount"),
                            })

                        for district in sep_data.get("districts", []):
                            metric = district.get("metric", {}) or {}
                            top_country_tran_rows.append({
                                "level": "district",
                                "year": year,
                                "quarter": quarter,
                                "entity": district.get("entityName"),
                                "count": metric.get("count"),
                                "amount": metric.get("amount"),
                            })

                        for pincode in sep_data.get("pincodes", []):
                            metric = pincode.get("metric", {}) or {}
                            top_country_tran_rows.append({
                                "level": "pincode",
                                "year": year,
                                "quarter": quarter,
                                "entity": pincode.get("entityName"),
                                "count": metric.get("count"),
                                "amount": metric.get("amount"),
                            })

            # State level
            state_path = os.path.join(top_type_path, "country", "india", "state")
            if os.path.isdir(state_path):
                for state_name in os.listdir(state_path):
                    state_folder = os.path.join(state_path, state_name)
                    if is_hidden_or_not_dir(state_folder):
                        continue
                    for year in os.listdir(state_folder):
                        year_path = os.path.join(state_folder, year)
                        if is_hidden_or_not_dir(year_path):
                            continue
                        for quarter_file in os.listdir(year_path):
                            quarter_path = os.path.join(year_path, quarter_file)
                            if is_not_json_file(quarter_path):
                                continue
                            quarter = quarter_file.replace(".json", "")
                            try:
                                with open(quarter_path, "r") as f:
                                    data = json.load(f)
                            except Exception:
                                continue

                            sep_data = data.get("data", {})

                            for district in sep_data.get("districts", []):
                                metric = district.get("metric", {}) or {}
                                top_state_tran_rows.append({
                                    "state": state_name,
                                    "level": "district",
                                    "year": year,
                                    "quarter": quarter,
                                    "entity": district.get("entityName"),
                                    "count": metric.get("count"),
                                    "amount": metric.get("amount"),
                                })

                            for pincode in sep_data.get("pincodes", []):
                                metric = pincode.get("metric", {}) or {}
                                top_state_tran_rows.append({
                                    "state": state_name,
                                    "level": "pincode",
                                    "year": year,
                                    "quarter": quarter,
                                    "entity": pincode.get("entityName"),
                                    "count": metric.get("count"),
                                    "amount": metric.get("amount"),
                                })

        # ------------------------- USER -------------------------
        if top_type == "user":
            # Country level
            country_path = os.path.join(top_type_path, "country", "india")
            if os.path.isdir(country_path):
                for year in os.listdir(country_path):
                    year_path = os.path.join(country_path, year)
                    if is_hidden_or_not_dir(year_path):
                        continue
                    for quarter_file in os.listdir(year_path):
                        quarter_path = os.path.join(year_path, quarter_file)
                        if is_not_json_file(quarter_path):
                            continue
                        quarter = quarter_file.replace(".json", "")
                        try:
                            with open(quarter_path, "r") as f:
                                data = json.load(f)
                        except Exception:
                            continue

                        sep_data = data.get("data", {})

                        for state in sep_data.get("states", []):
                            top_country_user_rows.append({
                                "level": "state",
                                "year": year,
                                "quarter": quarter,
                                "entity": state.get("name"),
                                "registeredUsers": state.get("registeredUsers"),
                            })

                        for district in sep_data.get("districts", []):
                            top_country_user_rows.append({
                                "level": "district",
                                "year": year,
                                "quarter": quarter,
                                "entity": district.get("name"),
                                "registeredUsers": district.get("registeredUsers"),
                            })

                        for pincode in sep_data.get("pincodes", []):
                            top_country_user_rows.append({
                                "level": "pincode",
                                "year": year,
                                "quarter": quarter,
                                "entity": pincode.get("name"),
                                "registeredUsers": pincode.get("registeredUsers"),
                            })

            # State level
            state_path = os.path.join(top_type_path, "country", "india", "state")
            if os.path.isdir(state_path):
                for state_name in os.listdir(state_path):
                    state_folder = os.path.join(state_path, state_name)
                    if is_hidden_or_not_dir(state_folder):
                        continue
                    for year in os.listdir(state_folder):
                        year_path = os.path.join(state_folder, year)
                        if is_hidden_or_not_dir(year_path):
                            continue
                        for quarter_file in os.listdir(year_path):
                            quarter_path = os.path.join(year_path, quarter_file)
                            if is_not_json_file(quarter_path):
                                continue
                            quarter = quarter_file.replace(".json", "")
                            try:
                                with open(quarter_path, "r") as f:
                                    data = json.load(f)
                            except Exception:
                                continue

                            sep_data = data.get("data", {})

                            for district in sep_data.get("districts", []):
                                top_state_user_rows.append({
                                    "state": state_name,
                                    "level": "district",
                                    "year": year,
                                    "quarter": quarter,
                                    "entity": district.get("name"),
                                    "registeredUsers": district.get("registeredUsers"),
                                })

                            for pincode in sep_data.get("pincodes", []):
                                top_state_user_rows.append({
                                    "state": state_name,
                                    "level": "pincode",
                                    "year": year,
                                    "quarter": quarter,
                                    "entity": pincode.get("name"),
                                    "registeredUsers": pincode.get("registeredUsers"),
                                })

    return (
        top_country_ins_rows,
        top_state_ins_rows,
        top_country_tran_rows,
        top_state_tran_rows,
        top_country_user_rows,
        top_state_user_rows
    )

