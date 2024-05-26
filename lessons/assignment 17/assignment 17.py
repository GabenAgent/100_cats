from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from config import host, user, password, db_name

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subjects = relationship('StudentSubject', back_populates='student')


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    students = relationship('StudentSubject', back_populates='subject')


class StudentSubject(Base):
    __tablename__ = 'student_subject'
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.id'), primary_key=True)
    student = relationship('Student', back_populates='subjects')
    subject = relationship('Subject', back_populates='students')


DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}/{db_name}"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

english = Subject(name='English')
not_english = Subject(name='Not English')
student1 = Student(name='Hugo')
student2 = Student(name='Boss')

session.add_all([
    StudentSubject(student=student1, subject=english),
    StudentSubject(student=student2, subject=english),
    StudentSubject(student=student2, subject=not_english)
])
session.commit()

english_class_students = session.query(Student.name).\
    join(StudentSubject).\
    join(Subject).\
    filter(Subject.name == 'English').\
    distinct().\
    all()

unique_students = set(student.name for student in english_class_students)

for student in english_class_students:
    print(student.name)
