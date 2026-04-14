import streamlit as st
from PIL import Image
import time
import os

st.set_page_config(layout="centered")
st.title("🔐 Gesture Lock Status")

locked_img = Image.open(r"/Users/jayeshvishwakarma/Documents/Documents/Stuffs/Hand-Gesture-Lock/lock.jpg")
unlocked_img = Image.open(r"/Users/jayeshvishwakarma/Documents/Documents/Stuffs/Hand-Gesture-Lock/unlock.jpg")

if not os.path.exists("status.txt"):
    with open("status.txt", "w") as f:
        f.write("LOCKED")

def get_status():
    with open("status.txt", "r") as f:
        return f.read().strip()

status = get_status()

if status == "UNLOCKED":
    st.image(unlocked_img, caption="✅ Access Granted", width=300)
else:
    st.image(locked_img, caption="🔒 Locked", width=300)

if st.button("🔒 Lock Again"):
    with open("status.txt", "w") as f:
        f.write("LOCKED")
    st.rerun()

st.caption("Auto-refreshing every 2 seconds...")
time.sleep(2)
st.rerun()
