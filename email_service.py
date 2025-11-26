# email_service.py

import smtplib
from email.mime.text import MIMEText

def send_email(recipient, subject, body):
    """
    Sends an email to the given recipient.
    BUG: SMTP server connection string is incorrect, so emails fail.
    """
    # Bug: wrong SMTP server port (should be 587 for TLS)
    smtp_server = "smtp.example.com"
    smtp_port = 25  
    sender_email = "noreply@example.com"

    # Compose email
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, "password123")  # Example password
        server.send_message(msg)
        server.quit()
        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    send_email("user@example.com", "Test Email", "Hello! This is a test.")
