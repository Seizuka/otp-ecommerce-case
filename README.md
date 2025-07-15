# 📦 OTP Gmail Automation for Blibli E-commerce

A Selenium-based automation project that simulates user login on [Blibli e-commerce](https://www.blibli.com/) by retrieving One-Time Password (OTP) from Gmail inbox.

## 📌 Use Case
Automate the following scenario:

1. Navigate to [https://account.bliblitiket.com/login](https://account.bliblitiket.com/login).
2. Input the registered email/phone number.
3. Request OTP to be sent to Gmail.
4. Programmatically fetch the OTP from Gmail using IMAP.
5. Submit the OTP to complete login.

This project is designed for automation QA testing purposes in e-commerce OTP workflows.

---

## 🧩 Project Structure
<pre>
otp-ecommerce-case/
├── pages/
│ └── login_page.py # Page Object Model for login interactions
├── test_cases/
│ └── otp_login.py # Main test flow
├── data/
│ └── login_data.json # Test data (email/phone number)
├── utils/
│ └── gmail_reader.py # Gmail IMAP OTP extractor
├── config.py # Gmail & Blibli credentials (email, app password, selectors)
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── main.py # Entry point
</pre>

---

## ⚙️ Setup & Installation

### 1. 🔐 Gmail App Password

To access Gmail inbox via IMAP:

- Enable **2-Step Verification** on your Gmail account.
- Generate an **App Password** from [Google Security Settings](https://myaccount.google.com/apppasswords).
- Use that password in `config.py`.

```python
# config.py
GMAIL_USER = "your_email@gmail.com"
GMAIL_APP_PASSWORD = "your_app_password"  # App-specific password from Gmail

📥 Install Dependencies
git clone https://github.com/Seizuka/otp-ecommerce-case.git
cd otp-ecommerce-case

🚀 Running the Automation
python main.py

📬 OTP Reader Logic
Located in utils/gmail_reader.py, it connects to Gmail using IMAP and extracts the 6-digit OTP using regex from the most recent unread email containing a specific subject or sender.

🛡️ Notes & Limitations
Works only with Gmail (via IMAP).
Requires real Blibli account with OTP login enabled.
App password is mandatory (not standard Gmail password).
Captcha or bot protection may affect login flow.

📄 License
MIT License — free to use, share, and modify.

🙋 Author
Made with 💻 by Seizuka — QA Automation Engineer



