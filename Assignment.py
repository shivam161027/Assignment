# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.exc import IntegrityError
# from datetime import datetime
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
# db = SQLAlchemy(app)
#
#
# # User model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.String(50), nullable=False)
#     fullname = db.Column(db.String(100), nullable=False)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     submitted_by = db.Column(db.String(50), nullable=False)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
#
#
# # Course model
# class Course(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     coursename = db.Column(db.String(100), nullable=False)
#     department = db.Column(db.String(100), nullable=False)
#     semester = db.Column(db.String(50), nullable=False)
#     class_name = db.Column(db.String(50), nullable=False)
#     lecture_hours = db.Column(db.Integer, nullable=False)
#     submitted_by = db.Column(db.String(50), nullable=False)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
#
#
# # AttendanceLog model
# class AttendanceLog(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     student_id = db.Column(db.Integer, nullable=False)
#     course_id = db.Column(db.Integer, nullable=False)
#     present = db.Column(db.Boolean, default=False)
#     submitted_by = db.Column(db.String(50), nullable=False)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
#
#
# # Department model
# class Department(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     department_name = db.Column(db.String(100), nullable=False)
#     submitted_by = db.Column(db.String(50), nullable=False)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
#
#
# # Student model
# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     fullname = db.Column(db.String(100), nullable=False)
#     department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
#     class_name = db.Column(db.String(50), nullable=False)
#     submitted_by = db.Column(db.String(50), nullable=False)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
#
#
# # Create the database tables
# db.create_all()
#
#
# # Route to create a new user
# @app.route('/users', methods=['POST'])
# def create_user():
#     try:
#         data = request.json
#         with app.app_context():
#             new_user = User(**data)
#             db.session.add(new_user)
#             db.session.commit()
#         return jsonify({'message': 'User created successfully'}), 201
#     except KeyError as e:
#         return jsonify({'message': f'Missing required field: {str(e)}'}), 400
#     except IntegrityError:
#         return jsonify({'message': 'Username or email already exists'}), 400
#     except Exception:
#         return jsonify({'message': 'Internal server error'}), 500
#
#
# # Route to create a new course
# @app.route('/courses', methods=['POST'])
# def create_course():
#     try:
#         data = request.json
#         with app.app_context():
#             new_course = Course(**data)
#             db.session.add(new_course)
#             db.session.commit()
#         return jsonify({'message': 'Course created successfully'}), 201
#     except KeyError as e:
#         return jsonify({'message': f'Missing required field: {str(e)}'}), 400
#     except Exception:
#         return jsonify({'message': 'Internal server error'}), 500
#
#
# # Route to create a new department
# @app.route('/departments', methods=['POST'])
# def create_department():
#     try:
#         data = request.json
#         with app.app_context():
#             new_department = Department(**data)
#             db.session.add(new_department)
#             db.session.commit()
#         return jsonify({'message': 'Department created successfully'}), 201
#     except KeyError as e:
#         return jsonify({'message': f'Missing required field: {str(e)}'}), 400
#     except Exception:
#         return jsonify({'message': 'Internal server error'}), 500
#
#
# # Route to create a new student
# @app.route('/students', methods=['POST'])
# def create_student():
#     try:
#         data = request.json
#         with app.app_context():
#             new_student = Student(**data)
#             db.session.add(new_student)
#             db.session.commit()
#         return jsonify({'message': 'Student created successfully'}), 201
#     except KeyError as e:
#         return jsonify({'message': f'Missing required field: {str(e)}'}), 400
#     except Exception:
#         return jsonify({'message': 'Internal server error'}), 500
#
#
# # Route to mark attendance
# @app.route('/attendance', methods=['POST'])
# def mark_attendance():
#     try:
#         data = request.json
#         with app.app_context():
#             new_attendance = AttendanceLog(**data)
#             db.session.add(new_attendance)
#             db.session.commit()
#         return jsonify({'message': 'Attendance marked successfully'}), 201
#     except KeyError as e:
#         return jsonify({'message': f'Missing required field: {str(e)}'}), 400
#     except Exception:
#         return jsonify({'message': 'Internal server error'}), 500
#
#
# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)


from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        type = db.Column(db.String(50))
        fullname = db.Column(db.String(100))
        username = db.Column(db.String(50))
        email = db.Column(db.String(100))
        password = db.Column(db.String(100))
        submitted_by = db.Column(db.Integer)
        updated_at = db.Column(db.DateTime)

        def serialize(self):
            return {
                'id': self.id,
                'type': self.type,
                'fullname': self.fullname,
                'username': self.username,
                'email': self.email,
                'submitted_by': self.submitted_by,
                'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
            }

    class Course(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        course_name = db.Column(db.String(100))
        department = db.Column(db.String(100))
        semester = db.Column(db.String(50))
        class_ = db.Column(db.String(50))
        lecture_hours = db.Column(db.Integer)
        submitted_by = db.Column(db.Integer)
        updated_at = db.Column(db.DateTime)

        def serialize(self):
            return {
                'id': self.id,
                'course_name': self.course_name,
                'department': self.department,
                'semester': self.semester,
                'class': self.class_,
                'lecture_hours': self.lecture_hours,
                'submitted_by': self.submitted_by,
                'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
            }

    class AttendanceLog(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
        course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
        present = db.Column(db.Boolean)
        submitted_by = db.Column(db.Integer)
        updated_at = db.Column(db.DateTime)

        def serialize(self):
            return {
                'id': self.id,
                'student_id': self.student_id,
                'course_id': self.course_id,
                'present': self.present,
                'submitted_by': self.submitted_by,
                'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
            }

    class Department(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        department_name = db.Column(db.String(100))
        submitted_by = db.Column(db.Integer)
        updated_at = db.Column(db.DateTime)

        def serialize(self):
            return {
                'id': self.id,
                'department_name': self.department_name,
                'submitted_by': self.submitted_by,
                'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
            }

    class Student(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        full_name = db.Column(db.String(100))
        department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
        class_ = db.Column(db.String(50))
        submitted_by = db.Column(db.Integer)
        updated_at = db.Column(db.DateTime)

        def serialize(self):
            return {
                'id': self.id,
                'full_name': self.full_name,
                'department_id': self.department_id,
                'class': self.class_,
                'submitted_by': self.submitted_by,
                'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
            }

    # API endpoints for User management
    @app.route('/users', methods=['GET'])
    def get_users():
        try:
            users = User.query.all()
            return jsonify(users=[user.serialize() for user in users])
        except SQLAlchemyError as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/users', methods=['POST'])
    def create_user():
        try:
            data = request.get_json()
            user = User(
                type=data['type'],
                fullname=data['fullname'],
                username=data['username'],
                email=data['email'],
                password=data['password'],
                submitted_by=data['submitted_by'],
                updated_at=data['updated_at']
            )
            db.session.add(user)
            db.session.commit()
            return jsonify(user.serialize()), 201
        except KeyError as e:
            return jsonify({'error': f'Missing required field: {str(e)}'}), 400
        except SQLAlchemyError as e:
            return jsonify({'error': str(e)}), 500

    # API endpoints for Course management
    @app.route('/courses', methods=['GET'])
    def get_courses():
        try:
            courses = Course.query.all()
            return jsonify(courses=[course.serialize() for course in courses])
        except SQLAlchemyError as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/courses', methods=['POST'])
    def create_course():
        try:
            data = request.get_json()
            course = Course(
                course_name=data['course_name'],
                department=data['department'],
                semester=data['semester'],
                class_=data['class'],
                lecture_hours=data['lecture_hours'],
                submitted_by=data['submitted_by'],
                updated_at=data['updated_at']
            )
            db.session.add(course)
            db.session.commit()
            return jsonify(course.serialize()), 201
        except KeyError as e:
            return jsonify({'error': f'Missing required field: {str(e)}'}), 400
        except SQLAlchemyError as e:
            return jsonify({'error': str(e)}), 500

    # API endpoints for AttendanceLog management
    @app.route('/attendancelogs', methods=['GET'])
    def get_attendancelogs():
        try:
            attendancelogs = AttendanceLog.query.all()
            return jsonify(attendancelogs=[log.serialize() for log in attendancelogs])
        except SQLAlchemyError as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/attendancelogs', methods=['POST'])
    def create_attendancelog():
        try:
            data = request.get_json()
            attendancelog = AttendanceLog(
                student_id=data['student_id'],
                course_id=data['course_id'],
                present=data['present'],
                submitted_by=data['submitted_by'],
                updated_at=data['updated_at']
            )
            db.session.add(attendancelog)
            db.session.commit()
            return jsonify(attendancelog.serialize()), 201
        except KeyError as e:
            return jsonify({'error': f'Missing required field: {str(e)}'}), 400
        except SQLAlchemyError as e:
            return jsonify({'error': str(e)}), 500

    # API endpoints for Department management
    @app.route('/departments', methods=['GET'])
    def get_departments():
        try:
            departments = Department.query.all()
            return jsonify(departments=[department.serialize() for department in departments])
        except SQLAlchemyError as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/departments', methods=['POST'])
    def create_department():
        try:
            data = request.get_json()
            department = Department(
                department_name=data['department_name'],
                submitted_by=data['submitted_by'],
                updated_at=data['updated_at']
            )
            db.session.add(department)
            db.session.commit()
            return jsonify(department.serialize()), 201
        except KeyError as e:
            return jsonify({'error': f'Missing required field: {str(e)}'}), 400
        except SQLAlchemyError as e:
            return jsonify({'error': str(e)}), 500

    # API endpoints for Student management
    @app.route('/students', methods=['GET'])
    def get_students():
        try:
            students = Student.query.all()
            return jsonify(students=[student.serialize() for student in students])
        except SQLAlchemyError as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/students', methods=['POST'])
    def create_student():
        try:
            data = request.get_json()
            student = Student(
                full_name=data['full_name'],
                department_id=data['department_id'],
                class_=data['class'],
                submitted_by=data['submitted_by'],
                updated_at=data['updated_at']
            )
            db.session.add(student)
            db.session.commit()
            return jsonify(student.serialize()), 201
        except KeyError as e:
            return jsonify({'error': f'Missing required field: {str(e)}'}), 400
        except SQLAlchemyError as e:
            return jsonify({'error': str(e)}), 500

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        app.run(debug=True)
