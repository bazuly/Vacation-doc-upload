from hr_app.models import HrEmailModel
from django.core.mail import EmailMessage
import os


""" Email sending """


def email_hr_handler(name, vacation_date_start, vacation_date_end, vacation_file_path, job_title):
    hr_email_instance = HrEmailModel.objects.all()
    email_list = [email.email for email in hr_email_instance]
    subject = f'Заявление на отпуск от {name}, должность: {job_title}'
    message = f'Прошу предоставить отпуск в период с {vacation_date_start} по {vacation_date_end}'
    email = EmailMessage(subject, message, to=email_list)
    
    if vacation_file_path is not None and os.path.exists(vacation_file_path):
        email.attach_file(vacation_file_path)
        
    email.send()