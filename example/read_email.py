# -*- coding: utf-8 -*-
import imaplib
import email
from email.header import decode_header, Header
from bs4 import BeautifulSoup
import quopri
import re

# Replace with your Gmail email address and password
EMAIL = "your_name@gmail.com"
PASSWORD = "your-password"


def read_emails(to_email):
    mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")

    # Search for all emails in the inbox
    subject = "Facture de chaîne"
    encoded_subject = Header(subject, "utf-8").encode()
    print(encoded_subject)

    status, response = mail.search(None, f'(TO "{to_email}" UNSEEN)')
    email_ids = response[0].split()

    for e_id in email_ids:
        # Fist of all get only subject from email
        _, msg_data = mail.fetch(
            e_id,
            "(BODY[HEADER.FIELDS (SUBJECT)])",
            # "(RFC822)",
        )
        msg = email.message_from_bytes(msg_data[0][1])
        subj, encoding = decode_header(msg.get("Subject"))[0]
        if encoding:
            subj = subj.decode(encoding)
        print(subj)

        if subject == subj:
            # If email is found get all data
            _, msg_data = mail.fetch(
                e_id,
                "(RFC822)",
            )
            msg = email.message_from_bytes(msg_data[0][1])

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/html":
                        html = part.get_payload(decode=True).decode("utf-8")
                        parse_html(html)
            elif msg.get_content_type() == "text/html":
                html = msg.get_payload(decode=True).decode("utf-8")
                parse_html(html)

            # Mark message as read
            mail.uid("STORE", e_id, "+FLAGS", "\\Seen")

    mail.logout()


def parse_html(html):
    ascii_encoded_html = html.encode("ascii", errors="ignore")
    # Remove 3D tags.
    # For example following tag
    #    <div data-template-name=3D"channel_invoice_v2"></div>
    # will be replaced like following
    #    <div data-template-name="channel_invoice_v2"></div>
    decoded_html = quopri.decodestring(ascii_encoded_html).decode("utf-8", errors='replace')
    soup = BeautifulSoup(decoded_html, "lxml")
    target_div = soup.find("div", attrs={"data-template-name": "channel_invoice_v2"})

    if target_div:
        print(f"Found the target div: {target_div}")
    else:
        print("Target div not found")

    text_content = soup.text
    match = re.search("Date \n*March 17, 2023", text_content)

    if match:
        print(f"Found the search pattern: {match.group()}")
    else:
        print("Search pattern not found")


if __name__ == "__main__":
    to_email = "your_name+addchannelcsqa_3055EvFclC@gmail.com"
    read_emails(to_email)
