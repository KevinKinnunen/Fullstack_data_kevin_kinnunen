import streamlit as st
from utils.query_database import QueryDatabase

class ContentKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.content_view_time;").df

    def display_content(self):
        df = self._content
        st.markdown("## KPIer för videor")
        st.markdown("Nedan visas KPIer för totalt antal")

        kpi_options = {
            "videor": len(df),
            "visade timmar": df["Visningstid_timmar"].sum(),
            "prenumeranter": df["Prenumeranter"].sum(),
            "exponeringar": df["Exponeringar"].sum(),
            # --- Added kpis --- 
            "avg viewing time": df["Visningstid_timmar"].mean(), # Avg ctr across all videos
            "avg click freq": df["Klickfrekvens_exponering_%"].mean(), # Avg click freq %
            "avg views per vid": df["Visningar"].mean() # Avg view per vid
        }

        selected_kpis = st.multiselect( # st.multiselect to allow users to select options from the KPI options list
            "Välj vilka KPIer du vill visa",
            options=kpi_options.keys(), # All available KPIs are shown as options
            default=list(kpi_options.keys()) # All KPI options are visible by default
        )

        for col, kpi in zip(st.columns(len(selected_kpis)), selected_kpis):
            with col: 
                st.metric(kpi, round(kpi_options[kpi]))
        #st.dataframe(df)

# create more KPIs here
class DeviceKPI:
    pass 
