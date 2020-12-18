from flask import Blueprint, jsonify, request
from schemas import *
from models import *


blueprint = Blueprint("Reiting",__name__)


@blueprint.route("/students", methods = ["POST"])
def add_student():
    try:
        student_data = New_Student().load(request.json)
        stud_obj = student(**student_data)
        session = Session()
        session.add(stud_obj)
        session.commit()
    except Exception:
        return(jsonify({"code":400,"error": "wrong data"}))
    
    return jsonify(Student_Info().dump(stud_obj)),200


@blueprint.route("/students", methods = ["GET"])
def get_students():
    try:
        session = Session()
        students_all = session.query(student).all()
    except Exception:
        return jsonify({"code":400,"error": "wrong student data"})

    return jsonify(Student_Info(many = True).dump(students_all)),200


@blueprint.route("/students/<student_id>", methods = ["GET"])
def get_student(student_id):
    try:
        session = Session()

        student_obj = session.query(student).filter_by(student_id = student_id).one()
    except Exception:
        return jsonify({"code":400,"error": "wrong student id"})

    return jsonify(Student_Info().dump(student_obj)),200


@blueprint.route("/students/top/<s_bal>", methods = ["GET"])
def get_top_students(s_bal):
    try:
        session = Session()
        students_obj = session.query(student).filter(student.s_bal >= int(s_bal)).all()

    except Exception:
        return(jsonify({"code":400,"error": "wrong student id"}))

    return jsonify(Student_Info(many = True).dump(students_obj)),200
 

@blueprint.route("/students/<student_id>", methods = ["PUT"])
def put_student(student_id):
    try:
        session = Session()

        student_data = New_Student().load(request.json)
        original_student_data = session.query(student).filter_by(student_id = student_id).one()

        for key , value in student_data.items():
            setattr(original_student_data,key,value)
        session.commit()
    except Exception:
        return(jsonify({"code":400,"error": "wrong student data"}))

    return jsonify(Student_Info().dump(original_student_data)),200


@blueprint.route("/students/<student_id>", methods = ["DELETE"])
def del_student(student_id):
    try:
        session = Session()

        session.query(student).filter_by(student_id = student_id).delete()
        session.commit()
    
    except Exception:
        return(jsonify({"code": 400 ,"error": "Wrong student id"}))
    return jsonify({"Student deleted ": 200})






@blueprint.route("/teacher/signup",methods = ["POST"])
def add_teacher():
    try:
        teacher_data = New_Teacher().load(request.json)
        teach_obj = teacher(**teacher_data)
        session = Session()
        session.add(teach_obj)
        session.commit()
    except Exception:
        return jsonify({"code":400,"error": "wrong data"})
    
    return jsonify(Teacher_Info().dump(teach_obj)),200

@blueprint.route("/teacher/login", methods = ["GET"])
def login_teacher():
    teacher_data = Teacher_Log_Info().load(request.json)
    return("Successful login"), 200


@blueprint.route("/teacher/logout", methods = ["GET"])
def logout_teacher():
    return("Successful logout"), 200

@blueprint.route("/teacher/<teacher_id>", methods = ["PUT"])
def put_teacher(teacher_id):
    try:
        session = Session()

        teacher_data = New_Teacher().load(request.json)
        original_teacher_data = session.query(teacher).filter_by(teacher_id = teacher_id).one()

        for key , value in teacher_data.items():
            setattr(original_teacher_data,key,value)
        session.commit()
    except Exception:
        return(jsonify({"code":400,"error": "wrong teacher data"}))

    return jsonify(Teacher_Info().dump(original_teacher_data)),200


@blueprint.route("/teacher/<teacher_id>", methods = ["DELETE"])
def del_teacher(teacher_id):
    try:
        session = Session()
        if session.query(teacher).filter_by(teacher_id = teacher_id) == Null:
            return(jsonify({"code": 400 ,"error": "Wrong teacher id"}))
        session.query(teacher).filter_by(teacher_id = teacher_id).delete()
        session.commit()
    except Exception:
        return(jsonify({"code": 400 ,"error": "Wrong teacher id"}))

    return jsonify({"Teacher deleted ": 200})