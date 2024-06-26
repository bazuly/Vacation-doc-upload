from hr_app.models import HrEmailModel, VacancyModel
from django.core.mail import EmailMessage
import os


"""
Email sending 
"""


def vacation_email_hr_handler(name, vacation_date_start, vacation_date_end, vacation_file_path, job_title):
    hr_email_instance = HrEmailModel.objects.all()
    email_list = [email.email for email in hr_email_instance]
    subject = f'Заявление на отпуск от {name}, должность: {job_title}'
    message = f'Добрый день. Прошу предоставить отпуск в период с {vacation_date_start} по {vacation_date_end}'
    email = EmailMessage(subject, message, to=email_list)
    
    if vacation_file_path is not None and os.path.exists(vacation_file_path):
        email.attach_file(vacation_file_path)
        
    email.send()
    

def vacancy_email_hr_handler(name, vacancy_name, vacancy_file_path, contact):
    hr_email_instance = HrEmailModel.objects.all()
    email_list = [email.email for email in hr_email_instance]
    subject = f'Отклик на вакансию {vacancy_name}'
    message = f'Добрый день. Отклик на вакансию {vacancy_name}. \nФИО: {name} \nКонтактная информация: {contact}' 
            
    email = EmailMessage(subject, message, to=email_list)
    
    if vacancy_file_path is not None and os.path.exists(vacancy_file_path):
        email.attach_file(vacancy_file_path)
        
    email.send()