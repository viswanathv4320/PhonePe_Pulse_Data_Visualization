from data_transform import (
    df_tran_state,
    df_agg_user_state,
    df_agg_insurance_state,
    df_map_user_state,
    df_map_tran_state,
    df_map_ins_state,
    df_hover_ins_state,
    df_top_tran_state,
    df_top_user_state,
    df_top_ins_state
)

from db_inserter import *

# Insert Aggregated Data
insert_agg_transaction_state(df_tran_state)
insert_agg_user_state(df_agg_user_state)
insert_agg_insurance_state(df_agg_insurance_state)

# Insert Map Data
insert_map_transaction_state(df_map_tran_state)
insert_map_user_state(df_map_user_state)
insert_map_insurance_state(df_map_ins_state)
insert_map_insurance_hover_state(df_hover_ins_state)

# Insert Top Data
insert_top_transaction_state(df_top_tran_state)
insert_top_user_state(df_top_user_state)
insert_top_insurance_state(df_top_ins_state)
