# src/config.py
import os
from dotenv import load_dotenv

try:
    import streamlit as st
    HAS_STREAMLIT = True
except ImportError:
    HAS_STREAMLIT = False

# Load the .env file
load_dotenv()

# Access variables - try Streamlit secrets first, then .env
if HAS_STREAMLIT:
    try:
        DATA_DIR = st.secrets.get("DATA_PATH", "data/")
        OUTPUT_DIR = st.secrets.get("OUTPUT_PATH", "output/")
    except:
        DATA_DIR = os.getenv("DATA_PATH", "data/")
        OUTPUT_DIR = os.getenv("OUTPUT_PATH", "output/")
else:
    DATA_DIR = os.getenv("DATA_PATH", "data/")
    OUTPUT_DIR = os.getenv("OUTPUT_PATH", "output/")

# Verify they exist
if not os.path.exists(DATA_DIR):
    raise FileNotFoundError(f"Data directory not found at: {DATA_DIR}")

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR) # Create if it doesn't exist