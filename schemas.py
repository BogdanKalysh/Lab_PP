from marshmallow import Schema, fields, post_load, validates

class New_Student(Schema):
    name = fields.String(required = True)
    s_bal = fields.Integer()
    marks = fields.List(fields.Integer())


class Student_Info(Schema):
    student_id = fields.Integer()
    name = fields.String()
    s_bal = fields.Integer()
    marks = fields.List(fields.Integer())

class New_Teacher(Schema):
    name = fields.String(required = True)
    email = fields.String()
    password = fields.String()

class Teacher_Log_Info(Schema):
    email = fields.String(required = True)
    password = fields.String(required = True)

class Teacher_Info(Schema):
    teacher_id = fields.Integer()
    name = fields.String()
    email = fields.String()