from datetime import datetime
import pandas
import random
import smtplib

email = "shockwave2325@gmail.com"
password = "ohtaezfpcxsppeaa"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_friend = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_doc:
        contents = letter_doc.read()
        contents = contents.replace("[NAME]",birthday_friend["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(from_addr=email, to_addrs=birthday_friend["email"], msg=f"Subject=Happy Birthday!\n\n{contents}")


