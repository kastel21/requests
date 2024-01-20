from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo, Category, NotificationTime, DateKeep
import dateutil.parser as parser
from django.core.mail import send_mail
from django.http import HttpResponse
from datetime import datetime, time
import sqlite3
import time, traceback
import threading
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    todo_items = Todo.objects.filter(Q(creator=request.user.username)).order_by('-due_date')[:10]
    
    if request.user.is_staff:

        todo_items = Todo.objects.filter(Q(completed=False)).order_by('-due_date')[:10]

    page = request.GET.get('page', 1)

    paginator = Paginator(todo_items, 50)
    try:
        todo_items = paginator.page(page)
    except PageNotAnInteger:
        todo_items = paginator.page(1)
    except EmptyPage:
        todo_items = paginator.page(paginator.num_pages)


    category_items = Category.objects.all()
    notification_time = NotificationTime.objects.all()

    current_date_time = datetime.now()
    dt_string = current_date_time.strftime("%m/%d/%Y %I:%M %p")
    splited_dt_string = dt_string.split(" ")

    context = {
        'todo_items': todo_items,
        'category_items': category_items,
        'notification_time' : notification_time,
        'hide_side_bar' : False,
        'current_date': splited_dt_string[0] + str().join(" ") + splited_dt_string[1] + str().join(" ") + splited_dt_string[2]
    }
    return render(request, 'todos/index.html', context)

@login_required(login_url='login')
def addTodo(request):
    if request.method == "POST":
            receiver_email = ""
            notification_time = "not available"

            # sendEmail(request, receiver_email, notification_time)

            new_item = Todo(todo_text = request.POST['todo_text'],
                            date_created = (parser.parse(request.POST['date_created'])).isoformat(),
                            due_date = (parser.parse(request.POST['due_date'])).isoformat(),
                            category_id = request.POST['todo_category'],
                            email_notification = request.user.email,
                            amount = request.POST['amount'],
                            priority = request.POST['priority'],
                            creator = request.user.username,

                            notification_time = notification_time)

            new_item.save()
            category_id = request.POST['todo_category']
            category = get_object_or_404(Category, pk=category_id)
            category.todo_count += 1
            category.save()
            return redirect("/todo")
    else:
        return redirect("/todo")


@login_required(login_url='login')
def addCategory(request):
    new_category = Category(category_name = request.POST['category_name'])
    new_category.save()
    return redirect("/todo")

@login_required(login_url='login')
def edit(request, todo_id):
    hide_side_bar = False

    if request.path == "/todo/" + str(todo_id) + "/edit/":
        hide_side_bar = True

    todo = get_object_or_404(Todo, pk=todo_id)
    due_date = todo.due_date.strftime("%m/%d/%Y %I:%M %p")
    splited_due_date_string = due_date.split(" ")

    context = {
        'todo_id' : todo_id,
        'todo_text' : todo.todo_text,
        'due_date': splited_due_date_string[0] + str().join(" ") + splited_due_date_string[1] + str().join(" ") + splited_due_date_string[2],
        'hideSideBar' : hide_side_bar,
        'amount':todo.amount,
        'priority':todo.priority,
        'completed':todo.completed,


    }
    return render(request, 'todos/edit.html', context)

@login_required(login_url='login')
def update(request, todo_id):

    edited_item = request.POST['todo_text']
    completed = request.POST['completed']

    #print('value',completed)
    edited_due_date = (parser.parse(request.POST['due_date'])).isoformat()
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.todo_text = edited_item
    todo.due_date = edited_due_date
    todo.completed = completed
    todo.save()

    return redirect("/todo")

@login_required(login_url='login')
def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    Todo.delete(todo)

    category = get_object_or_404(Category, pk= todo.category_id)
    category.todo_count -= 1
    category.save()
    return redirect("/todo")


def sendEmail(request, receiver_email, notification_time):

    email_body = """
    You have added a new todo_item.
    You can edit and delete the todo_item anytime.
    Your item will expire in """ + str(notification_time) + "!"

    send_mail(
        'Todo_Notification',
        email_body,
        'noreply@todo_application.ca',
        [receiver_email],
        fail_silently=False,
    )
    return HttpResponse('Mail successfully sent')

@login_required(login_url='login')
def check_time1( task):
  delay =1
  next_time = time.time() + delay
  while True:
    time.sleep(max(0, next_time - time.time()))
    try:
      task()
    except Exception:
      traceback.print_exc()
    # skip tasks if we are behind schedule:
    next_time += (time.time() - next_time) // delay * delay + delay

from datetime import datetime

@login_required(login_url='login')
def is_expired1():
    # connection = sqlite3.connect('db.sqlite3')
    # cursor = connection.cursor()
    # cursor.execute(" SELECT * FROM todos_todo where email_notification != '' AND notification_time != 'None' AND sent_reminder == 'False' ")
    # rows = cursor.fetchall()
    now = datetime.now() 
    day = now.strftime("%d")
    time = now.strftime("%H:%M")

    today = DateKeep.objects.get(id=1)




    #print('time',time)


    if "07:41" == time and today.day not in day:
        todo_notify_time = 0
        #print('day',day)

        rows = Todo.objects.filter(completed=False)

        for record in rows:
            #print("text",record.todo_text)
            #print("id",record.id)

            message = "Task "+record.todo_text+" is pending processing and is due on "+ str(record.due_date)
            send_reminders(record.email_notification,message)

        today.day = day
        today.save()


threading.Thread(target=lambda: check_time1( is_expired1)).start()




@login_required(login_url='login')
def send_reminders(email,msg):
        finance = 'pmusaruro@brti.co.zw'


        # send_mail(
    #     subject='TimeSheets Pending Approval',
    #     message=message,
    #     from_email=settings.EMAIL_HOST_USER,
    #     recipient_list=[emails[0],emails[1]]
    #     )

        mimemsg = MIMEMultipart()
        mimemsg['From']="fpriority@brti.co.zw"
        mimemsg['To']=finance
        mimemsg['Cc']=email
        mimemsg['Subject']="Finance Priority List "
        mimemsg.attach(MIMEText(msg, 'plain'))

                # with open(mail_attachment, "rb") as attachment:
                #     mimefile = MIMEBase('application', 'octet-stream')
                #     #mimefile.set_payload((attachment).read())
                # #     encoders.encode_base64(mimefile)
                # #     mimefile.add_header('Content-Disposition', "attachment; filename= %s" % mail_attachment_name)
                #     #mimemsg.attach(mimefile)
        connection = smtplib.SMTP(host='smtp.office365.com', port=587)
        connection.starttls()
        connection.login("fpriority@brti.co.zw","p@s3w0rd?1995")
        connection.send_message(mimemsg)
        connection.quit()



