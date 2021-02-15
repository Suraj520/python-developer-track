# Write your code here
#
#necessary imports
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import date,timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy import select
#creating the base class
class ToDo:
    Base = declarative_base()
    #defining the child class
    class Table(Base):
        """The database model of a task"""
        # noinspection SpellCheckingInspection
        __tablename__ = 'task'
        id = Column(Integer, primary_key=True)
        task = Column(String, default='default_value')
        deadline = Column(Date, default=date.today())
        def __repr__(self):
            return self.task
    #constructor
    def __init__(self):
        self.session = None
        self.init_database()

    #initialising database
    def init_database(self):
        """Creates and initializes a database"""
        engine = create_engine('sqlite:///todo.db?check_same_thread=False')
        self.Base.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)()

    #method to display missed tasks
    def display_missed_tasks(self,display=None):
        #i.e tasks which are before the calendar
        rows = self.session.query(self.Table).filter(self.Table.deadline < datetime.date.today()).order_by(self.Table.deadline).all()
        if display =="1":
            print("Missed tasks:")
            if rows:
                for num, task in enumerate(rows, start=1):
                    date = task.deadline.day
                    month = task.deadline.strftime('%b')
                    print("{0}. {1}. {2} {3}".format(num, task.task, date,month))
            else:
                print("Nothing to do!")
        return rows

    #method to add task with deadline to database
    def add_to_db(self, task,deadline):
        self.task = task
        self.deadline = deadline
        #making a new row
        new_row = self.Table(task=self.task, deadline=date.fromisoformat(self.deadline))
        self.session.add(new_row)
        self.session.commit()
        print("The task has been added!")

    #method to display today's task
    def display_today_task(self):
        #query
        rows = self.session.query(self.Table).filter(self.Table.deadline == date.today()).order_by(self.Table.id).all()
        if rows:
            for row in rows:
                print("{0}. {1}".format(row.id, row.task))
        else:
            print("Nothing to do!")

    #method to display the task of entire week.
    def display_week_task(self):
        start_date = date.today()
        end_date = date.today() + timedelta(days=7)
        rows = self.session.query(self.Table).filter(self.Table.deadline.between(start_date,end_date)).order_by(self.Table.deadline).all()
        #range
        week_dates = [start_date + timedelta(days=day) for day in range((end_date - start_date).days)]
        #iterating over each week date and printing the task
        for day in week_dates:
            print("\n{0} {1} {2}:".format(day.strftime('%A'),day.day, day.strftime('%b')))
            rows = self.session.query(self.Table).filter(self.Table.deadline == day).order_by(self.Table.id).all()
            if rows:
                for row in rows:
                    print("{0}. {1}".format(row.id, row.task))
            else:
                print("Nothing to do!")

    #method to display all tasks in calendar
    def display_all_task(self,display=None):
        print("All tasks:")
        #for debugging by printing the contents of the table, uncoment the following block of code
        # stmt = select('*').select_from(self.Table)
        # result = self.session.execute(stmt).fetchall()
        # print(result)
        rows = self.session.query(self.Table).order_by(self.Table.deadline).all()
        #print(rows)
        if display=="1":
            if rows:
                for num, task in enumerate(rows, start=1):
                    date = task.deadline.day
                    month = task.deadline.strftime('%b')
                    print("{0}. {1}. {2} {3}".format(num, task.task, date,month))
            else:
                print("Nothing to do!")
        return rows


    #method to delete tasks from calendar
    def delete_missed_tasks(self):
        tasks = self.display_all_task()
        #for debugging by printing the contents of the table, uncoment the following block of code
        # stmt = select('*').select_from(self.Table)
        # result = self.session.execute(stmt).fetchall()
        # print(result)
        ########################################################
        if not tasks:
            print("Nothing to delete\n")
            return
        print("\nChose the number of the task you want to delete:")
        index = int(input())-1
        self.session.delete(tasks[index])
        self.session.commit()
        print("The task has been deleted!\n")
#creating an instance of To do class and operating in the main section
todo = ToDo()
while(True):
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")
    user_input = input()
    if user_input == "1":
        print()
        today = date.today()
        print("Today {0} {1}:".format(today.day, today.strftime('%b')))
        todo.display_today_task()
        print()
    elif user_input == "2":
        print()
        todo.display_week_task()
    elif user_input == "3":
        print()
        todo.display_all_task(display="1")
    elif user_input == "4":
        print()
        todo.display_missed_tasks(display="1")
        print()
        #Missed tasks
    elif user_input == "5":
        print()
        print("Enter Task")
        task = input()
        print("Enter deadline")
        deadline = input()
        todo.add_to_db(task, deadline)
    elif user_input == "6":
        print()
        todo.delete_missed_tasks()
        #Delete tasks
    elif user_input == "0":
        print()
        print("Bye!")
        break

