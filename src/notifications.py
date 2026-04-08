# notifications.py
import smtplib
from email.message import EmailMessage
import logging

def send_overdue_notification(reader_email, book_title, days_overdue):
    msg = EmailMessage()
    try:
        msg.set_content(f"Уважаемый читатель! Книга '{book_title}' просрочена на {days_overdue} дней. Пожалуйста, верните её в библиотеку.")
        msg['Subject'] = 'Напоминание о просрочке книги'
        msg['From'] = 'library@example.com'
        msg['To'] = reader_email
    except Exception as e:
        logging.error(f"Код упал фикси. \nОшибка: {e}")
    logging.info(f"Уведомление отправлено на {reader_email}")
    return True
