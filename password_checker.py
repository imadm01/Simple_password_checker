import streamlit as st
import re

# Title displayed on the streamlit page
st.title("🔐️Password Strength Checker")

# Input password
password = st.text_input("Enter your password", type="password")

# Load common passwords from file
try:
    with open("leaked_passwords.txt", "r") as file:
        common_passwords = set(file.read().splitlines())
except:
    common_passwords = set()

# Password strength checker function
def check_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[@#$%^&+=!]", password) is None

    score = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])
    return score

# Result
if password:
    if password in common_passwords:
        st.error("⚠️ This password is commonly used and may have been leaked!")
    else:
        strength = check_strength(password)
        if strength <= 2:
            st.error("🔴 Weak Password")
        elif strength <= 4:
            st.warning("🟡 Moderate Password")
        else:
            st.success("🟢 Strong Password")
