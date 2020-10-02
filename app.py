from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy


# MySQL Configurations
mysql_user = "root"
mysql_password = "your_mysql_root_password"
mysql_db = "student_db"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
    f'mysql+pymysql://{mysql_user}:{mysql_password}@localhost:3306/{mysql_db}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
import database  


@app.route('/api/students', methods=['POST'])
def register_student():
    """
    Create Students Entry
    """
    print(request.json)
    response = database.register_student(request.json)
    return make_response(jsonify(response), 200)


@app.route('/api/students/roll_number', methods=['GET'])
def get_student():
    """
    Get Student's Details by Roll Number
    """
    response = database.get_student(request.json['roll_number'])
    return make_response(jsonify(response), 200)


@app.route('/api/students/roll_number', methods=['DELETE'])
def delete_student():
    """
    Delete Student's Details by Roll Number
    """
    response = database.delete_student(request.json['roll_number'])
    return make_response(jsonify(response), 200)


if __name__ == '__main__':
    app.run(debug=True)
