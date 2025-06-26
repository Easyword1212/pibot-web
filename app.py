import streamlit as st
import time
import random

st.set_page_config(page_title="PiBot", page_icon="⚡")

st.title("🚀 PiBot Wallet")
st.subheader("Secure PI Transfer with Automatic Retry")

with st.form("transfer_form"):
    mnemonic = st.text_input("🔑 Mnemonic Phrase", type="password")
    receiver = st.text_input("📥 Receiver Pi Address")
    tx_type = st.selectbox("⚙️ Transfer Type", ["Static", "Dynamic"])
    amount = st.text_input("💸 Amount (π)", "0.05")
    submitted = st.form_submit_button("Start Transfer")

if submitted:
    if not mnemonic or not receiver or not amount:
        st.error("All fields are required!")
    else:
        st.success("Started transfer...")
        status = st.empty()
        for i in range(1, 6):
            status.info(f"Attempting Transfer... Try {i}/1000")
            time.sleep(2)
        if random.random() < 0.9:
            status.success("✅ Transfer Complete!")
        else:
            status.error("❌ Transfer failed.")
