from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from datetime import timedelta

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# first_row = rows[0] # In case rows list is not empty
# print(first_row.task)  # Will print value of the string_field
# print(first_row.id)  # Will print the id of the row.
# print(first_row)  # Will print the string that was returned by __repr__ method

def add_task():
    task = input('Enter task')
    deadline = input('Enter deadline')
    new_row = Task(task=task,
                   deadline=datetime.strptime(deadline, '%Y-%m-%d').date())
    session.add(new_row)
    session.commit()
    print('The task has been added!')


def weeks_tasks():
    today = datetime.today().date()
    for i in range(1, 8):
        rows = session.query(Task).filter(Task.deadline == today).all()
        if len(rows) == 0:
            print(f"{today.strftime('%A')} {today.day} {today.strftime('%b')}")
            print('Nothing to do!\n')
        else:
            print(f"{today.strftime('%A')} {today.day} {today.strftime('%b')}")
            for i in rows:
                print(i)
            print()
        today = today + timedelta(days=1)


def today_tasks():
    today = datetime.today().date()
    rows = session.query(Task).filter(Task.deadline == datetime.today().date()).all()
    if len(rows) == 0:
        print('Nothing to do!')
    else:
        print(f"Today {today.day} {today.strftime('%b')}")
        for i in rows:
            print(i)


def all_tasks():
    rows = session.query(Task, Task.deadline).all()
    if len(rows) == 0:
        print('Nothing to do!')
    else:
        rows.sort(key=lambda x: x[1])
        n = 1
        for i in rows:
            print(f"{n}) {i[0]} {i[1].day} {i[1].strftime('%b')}")
            n += 1


def missed_task():
    rows = session.query(Task, Task.deadline).filter(Task.deadline < datetime.today().date()).all()
    print('Missed tasks:')
    if len(rows) == 0:
        print('Nothing is missed!')
    else:
        rows.sort(key=lambda x: x[1])
        for i in rows:
            print(f"{i[0]} {i[1].day} {i[1].strftime('%b')}")


def del_task():
    rows = session.query(Task, Task.deadline).all()
    if len(rows) == 0:
        print('Nothing to del!')
    else:
        rows.sort(key=lambda x: x[1])
        n = 1
        for i in rows:
            print(f"{n}) {i[0]} {i[1].day} {i[1].strftime('%b')}")
            n += 1
    print('Chose the number of the task you want to delete:')
    all_tasks()
    us_input = int(input())
    session.query(Task).filter(Task.task == str(rows[us_input - 1][0])).delete()
    session.commit()


def menu():
    user_input = input('''1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
''')
    if user_input == '1':
        today_tasks()
    elif user_input == '2':
        weeks_tasks()
    elif user_input == '3':
        all_tasks()
    elif user_input == '4':
        missed_task()
    elif user_input == '5':
        add_task()
    elif user_input == '6':
        del_task()
    else:
        print('Bye!')
        exit()


while True:
    menu()
    print()
