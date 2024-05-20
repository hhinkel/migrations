from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey


Base = declarative_base()
metadata = Base.metadata


class Student(Base):
    __table_args__ = ({'schema': 'mydb'})
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True)
    age = Column(Integer)
    note = Column(String(200))
    create_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"


class Student_Classes(Base):
    __table_args__ = ({'schema': 'mydb'})
    __tablename__ = "student_classes"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    class_number = Column(Integer)
    class_name = Column(String(60))


class Classes(Base):
    __table_args__ = ({'schema': 'classes'})
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True)
    class_number = Column(Integer)
    class_name = Column(String(60))
    class_description = Column(String(200))
