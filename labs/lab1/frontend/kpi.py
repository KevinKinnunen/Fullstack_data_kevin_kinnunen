import streamlit as st
from utils.query_database import QueryDatabase

class ContentKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.content_view_time;").df

    def display_content(self):
        df = self._content
        st.markdown("## KPIer för videor")
        st.markdown("Nedan visas KPIer för totalt antal")

        kpis = {
            "videor": len(df),
            "visade timmar": df["Visningstid_timmar"].sum(),
            "prenumeranter": df["Prenumeranter"].sum(),
            "exponeringar": df["Exponeringar"].sum(),
            # --- Added kpis --- 
            "avg viewing time": df["Visningstid_timmar"].mean(), # Avg ctr across all videos
            "avg click freq": df["Klickfrekvens_exponering_%"].mean(), # Avg click freq %
            "avg views per vid": df["Visningar"].mean() # Avg view per vid
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col: 
                st.metric(kpi, round(kpis[kpi]))
        #st.dataframe(df)

# create more KPIs here
class DeviceKPI:
    pass 
