import streamlit as st
import os
import sqlite3
import pandas as pd
from engine import index_pdfs, query_knowledge_base

st.set_page_config(page_title="NDLEA Field Assistant", page_icon="🦅", layout="wide")
st.title("🦅 NDLEA Secure Operational Assistant")
st.subheader("100% Offline Infrastructure-Grade Intelligence")

# --- INITIALIZE OFFLINE RELATIONAL STORAGE ---
DB_FILE = "offline_operations.db"

def init_sqlite_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS seizure_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            location TEXT,
            substance_type TEXT,
            weight_kg REAL,
            officer_notes TEXT
        )
    """)
    conn.commit()
    conn.close()

init_sqlite_db()

# --- SIDEBAR: DOCUMENT MGMT ---
st.sidebar.header("Operational Data Center")
uploaded_files = st.sidebar.file_uploader("Upload Tactical SOPs / Acts (PDF)", type="pdf", accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        with open(os.path.join("./data", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
    st.sidebar.success("Files saved locally inside /data folder.")

if st.sidebar.button("🛠️ Index / Update System Memory"):
    with st.spinner("Processing documents into local vector space..."):
        success = index_pdfs()
        if success:
            st.sidebar.success("System Ruggedized and Ready!")
        else:
            st.sidebar.error("No PDFs found in the /data folder to process.")

# --- MAIN INTERFACE: SPLIT SCREEN LAYOUT ---
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📋 Legal & Field Guide Framework")
    user_query = st.text_input("Query local frameworks (e.g., 'penalties for trafficking'):")
    if user_query:
        with st.spinner("Searching local encrypted memory..."):
            answer = query_knowledge_base(user_query)
            st.info(answer)

with col2:
    st.header("✍️ Secure Offline Incident Logger")
    with st.form("log_form", clear_on_submit=True):
        checkpoint_loc = st.text_input("Operational Sector / Checkpoint Location")
        drug_type = st.selectbox("Suspected Substance Profile", ["Cannabis Sativa", "Cocaine", "Heroin", "Methamphetamine", "Synthetic Opioids", "Other/Unidentified"])
        net_weight = st.number_input("Estimated Net Mass (KG)", min_value=0.0, step=0.1)
        field_notes = st.text_area("Field Assessment / Modus Operandi Notes")
        
        submit_btn = st.form_submit_button("Commit Entry to Offline Ledger")
        
        if submit_btn:
            # Insert log strictly into the laptop's hard drive
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO seizure_logs (location, substance_type, weight_kg, officer_notes)
                VALUES (?, ?, ?, ?)
            """, (checkpoint_loc, drug_type, net_weight, field_notes))
            conn.commit()
            conn.close()
            st.success("Entry securely isolated and committed to local disk storage!")

    # Display real-time data table from the local database file
    st.subheader("Recent Offline Logs Saved on Disk")
    conn = sqlite3.connect(DB_FILE)
    try:
        df = pd.read_sql_query("SELECT timestamp, location, substance_type, weight_kg FROM seizure_logs ORDER BY id DESC LIMIT 5", conn)
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.write("No logs saved yet.")
    conn.close()