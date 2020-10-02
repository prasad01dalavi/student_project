from app import db
from models import Student


def register_student(student):
    """
    Save Student's details in database
    """
    database_query = Student(
        name=student['name'],
        student_class=student['class'],
        gender=student['gender'],
    )
    db.session.add(database_query)
    db.session.commit()
    return {'status': 'success', 'reason': 'student added'}


def get_student(roll_number):
    """
    Get Student Details by Roll number
    """
    student = Student.query.get(roll_number)
    student_details = {
        "id": student.roll_number,
        "name": student.name,
        "class": student.student_class,
        "gender": student.gender
    }
    return student_details


def delete_student(roll_number):
    """
    Delete Student Details by Roll Number
    """
    try:
        student = Student.query.filter_by(roll_number=roll_number).delete()
        db.session.commit()
        return {'status': 'success', 'reason': 'student details removed'}
    except Exception as e:
        # Exception while trying to delete the already deleted student details
        return {'status': 'failure', 'reason': str(e)}
