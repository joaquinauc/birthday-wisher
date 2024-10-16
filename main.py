##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
# actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import pandas
from random import randint

now = dt.datetime.now()
month = now.month
day = now.day

my_email = "joaquinp_urrea@hotmail.com"
password = "Califa02."

birthdays_data = pandas.read_csv("birthdays.csv")
person_data = birthdays_data[(birthdays_data.day == day) & (birthdays_data.month == month)]
# birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in birthdays_data.iterrows()}

for person in range(len(person_data["name"])):
    with open(f"letter_templates/letter_{randint(1, 3)}.txt") as file:
        letter = file.read()
        replaced_letter = letter.replace("[NAME]", f"{person_data["name"][person]}")

        subject = "Happy Birthday!"
        body = replaced_letter
        msg = f"Subject: {subject}\n\n{body}"  # The \n\n is to write the body of the msg, it recognizes it as such.

        with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
            connection.starttls()  # It makes the connection secure
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=person_data["email"][person], msg=msg)
            connection.close()
