from 上的各种课.大三上.sql.sql_alchemy.test import session
from 上的各种课.大三上.sql.sql_alchemy.test import Course
course = session.query(Course).first()
print(course)
course = session.query(Course).all()
print(course)
courses = session.query(Course).filter_by(course_name='Python').all()
print(courses)
query_result = session.query(Course).filter_by(course_name = 'Python').filter_by(teacher_name = 'Teacher Liu')
session.query(Course).filter_by(course_name='Python').filter_by(teacher_name='Jack').update({'teacher_name': '***'})
session.commit()
session.close()
delete_courses = session.query(Course).filter_by(course_name = 'Python').first()
if courses:
    session.delete(delete_courses)
    session.commit()
    session.close()