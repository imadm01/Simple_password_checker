# Password Strength Checker

This is a simple password strength checker I built using Python and Streamlit. It helps users understand how strong or weak their passwords are and also checks if the password is commonly used or leaked.

## What this project does

- Lets users enter their password securely.
- Checks for:
  - Minimum length (at least 8 characters)
  - Presence of lowercase and uppercase letters
  - Presence of digits
  - Presence of special characters
- Compares the password with a list of commonly leaked passwords.
- Gives instant feedback on password strength.

## Leaked Password Detection

For quicker detection, I used a file named `leaked_passwords.txt` which contains 100 of the most common leaked passwords.

You can also use larger password breach lists like `rockyou.txt` or the dumps from `Have I Been Pwned`, but keep in mind:
- These files are huge.
- It may take a lot of time to load and check passwords against them.

## Why I made this

I built this to understand the basics of password security and to learn how real-world password validation works. This also helped me practice using Streamlit for creating simple interactive apps.

## How to run

1. Install Streamlit:
```bash
pip install streamlit
```

2. Make sure `leaked_passwords.txt` is in the same folder as your script.

3. Run the app:
```bash
streamlit run password_checker.py
```
4. Enter the password to check the strength or if it has been leaked.

## Screenshots

Screenshots of the project are stored in the `images/` folder.
