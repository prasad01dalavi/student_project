from app import db


class Student(db.Model):
    """
    Student's Information
    """
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(),
                           server_onupdate=db.func.now())
    roll_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    student_class = db.Column(db.String(20))
    gender = db.Column(db.String(20))

    def __repr__(self):
        return '<Student %r>' % self.name
