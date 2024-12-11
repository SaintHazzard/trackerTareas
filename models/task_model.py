from sqlalchemy import Column, Integer, String, Boolean
from models.database import Base, SessionLocal, init_db

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    completed = Column(Boolean, default=False)


init_db()

def create_task(title,description, completed=False):
    session = SessionLocal()
    new_task = Task(title=title, description=description, completed=completed)
    session.add(new_task)
    session.commit()
    session.close()

def get_all_tasks():
    session = SessionLocal()
    tasks = session.query(Task).all()
    session.close()
    return tasks

def update_task(task_id, completed=None):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        if completed is not None:
            task.completed = completed
        session.commit()
    session.close()

def delete_task(task_id):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        session.delete(task)
        session.commit()
    session.close()
