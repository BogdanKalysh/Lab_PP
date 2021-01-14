from app import *
from models import *

from flask_testing import TestCase
import unittest
import json
from sqlalchemy.orm import close_all_sessions


student = {
    "name": "student1",
    "s_bal": 3,
    "marks": [1, 3, 5]
}
student_wrong = {
    "name": "student1",
    "s_bal": "duyfu",
    "marks": [1, 3, 5]
}
teacher = {
    "name": "teacher1",
    "email": "email@gmail.com",
    "password": "password"
}
teacher_wrong = {
    "name": "teacher1",
    "email": "email@gmail.com",
    "password": "password"
}
def get_token():
    Base.metadata.create_all(engine)
    client = app.test_client()
    response = client.post('/rating/teacher/signup', json={'email': teacher["email"], 'name': teacher["name"], 'password': teacher["password"]})

    return dict(client.get('/rating/teacher/login', json={'email': teacher["email"], 'password': teacher["password"]}).json)['access_token']

class TestingUser(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        close_all_sessions()
        Base.metadata.create_all(engine)

    def tearDown(self):
        close_all_sessions()
        Base.metadata.drop_all(engine)

    def test_add_teacher(self):
        client = app.test_client()

        response = client.post('/rating/teacher/signup', json={'email': teacher["email"], 'name': teacher["name"], 'password': teacher["password"]})
        self.assertEqual(response.status_code, 200)

        response = client.post('/rating/teacher/signup', json={'email': teacher_wrong["email"], 'name': teacher_wrong["name"], 'password': teacher_wrong["password"]})
        self.assertEqual(response.status_code, 404)

    def test_add_student(self):
        client = app.test_client()
        correct_response = client.post('/rating/students', json={'s_bal': student["s_bal"], 'name': student["name"], 'marks': student["marks"]}, headers={'Authorization': 'Bearer ' + str(get_token())})
        self.assertEqual(correct_response.status_code, 200)

        wrong_response = client.post('/rating/students', json={'s_bal': student_wrong["s_bal"], 'name': student_wrong["name"], 'marks': student_wrong["marks"]}, headers={'Authorization': 'Bearer ' + str(get_token())})
        self.assertEqual(wrong_response.status_code, 401)

    def test_login_user(self):
        client = app.test_client()
        response = client.post('/rating/teacher/signup', json={'email': teacher["email"], 'name': teacher["name"], 'password': teacher["password"]})
        self.assertEqual(response.status_code, 200)

        login_data = {
            "email": "email@gmail.com",
            "password": "password"
        }
        teacher_data = json.dumps(login_data).encode('utf-8')

        correct_response = client.open(path='/rating/teacher/login', method='GET', data=teacher_data, headers={'Content-Type': 'application/json'})
        self.assertEqual(correct_response.status_code, 200)

        wrong_login_data = {
            "email": "email1111@gmail.com",
            "password": "passworddddd"
        }
        wrong_teacher_data = json.dumps(wrong_login_data).encode('utf-8')

        wrong_response = client.open(path='/rating/teacher/login', method='GET', data=wrong_teacher_data, headers={'Content-Type': 'application/json'})
        self.assertEqual(wrong_response.status_code, 400)

    def test_logout_user(self):
        client = app.test_client()
        response = client.get(path='/rating/teacher/logout', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + str(get_token())})
        self.assertEqual(response.status_code, 200)

    def test_put_teacher_by_id(self):
        client = app.test_client()
        correct_response = client.post('/rating/teacher/signup', json={'email': teacher["email"], 'name': teacher["name"], 'password': teacher["password"]})
        response = client.put(path='/rating/teacher/1', json={'email': teacher["email"], 'name': teacher["name"], 'password': teacher["password"]}, headers={'Authorization': 'Bearer ' + str(get_token())})
        self.assertEqual(response.status_code, 200)
        wrong_response = client.put(path='/rating/teacher/1111',json={'email': teacher["email"], 'name': teacher["name"], 'password': teacher["password"]}, headers={'Authorization': 'Bearer ' + str(get_token())})
        self.assertEqual(wrong_response.status_code, 401)

    def test_put_student_by_id(self):
        client = app.test_client()
        correct_response = client.post('/rating/students', json={'s_bal': student["s_bal"], 'name': student["name"], 'marks': student["marks"]}, headers={'Authorization': 'Bearer ' + str(get_token())})
        response = client.put(path='/rating/students/1', json={'s_bal': student["s_bal"], 'name': student["name"], 'marks': student["marks"]}, headers={'Authorization': 'Bearer ' + str(get_token())})
        self.assertEqual(response.status_code, 200)
        wrong_response = client.put(path='/rating/students/1111', json={'s_bal': student["s_bal"], 'name': student["name"], 'marks': student["marks"]}, headers={'Authorization': 'Bearer ' + str(get_token())})
        self.assertEqual(wrong_response.status_code, 401)

    def test_get_student_by_id(self):
        client = app.test_client()
        correct_response = client.post('/rating/students', json={'s_bal': student["s_bal"], 'name': student["name"],'marks': student["marks"]}, headers={'Authorization': 'Bearer ' + str(get_token())})
        response = client.get(path='/rating/students/1')
        self.assertEqual(response.status_code, 200)
        wrong_response = client.get(path='/rating/students/1111')
        self.assertEqual(wrong_response.status_code, 400)

    def test_get_all_students(self):
        client = app.test_client()
        correct_response = client.post('/rating/students', json={'s_bal': student["s_bal"], 'name': student["name"], 'marks': student["marks"]})
        response = client.get(path='/rating/students')
        self.assertEqual(response.status_code, 200)
        wrong_response = client.get(path='/rating/students/')
        self.assertEqual(wrong_response.status_code, 404)

    def test_get_top_students(self):
        client = app.test_client()
        correct_response = client.post('/rating/students', json={'s_bal': student["s_bal"], 'name': student["name"], 'marks': student["marks"]})
        response = client.get(path='/rating/students/top/2')
        self.assertEqual(response.status_code, 200)
        wrong_response = client.get(path='/rating/students/top/ytejty')
        self.assertEqual(wrong_response.status_code, 404)

    def test_delete_teacher(self):
        client = app.test_client()
        correct_response = client.post('/rating/teacher/signup', json={'email': teacher["email"], 'name': teacher["name"], 'password': teacher["password"]}, headers={'Authorization': 'Bearer ' + str(get_token())})
        response = client.delete(path='/rating/teacher/1', headers={'Authorization': 'Bearer ' + str(get_token())})
        self.assertEqual(response.status_code, 200)
        wrong_response = client.delete(path='/rating/teacher/aaaa', headers={'Authorization': 'Bearer ' + str(get_token())})
        self.assertEqual(wrong_response.status_code, 404)

    def test_delete_student(self):
        client = app.test_client()
        correct_response = client.post('/rating/students', json={'s_bal': student["s_bal"], 'name': student["name"], 'marks': student["marks"]}, headers={'Authorization': 'Bearer ' + str(get_token())})
        response = client.delete(path='/rating/students/1', headers={'Authorization': 'Bearer ' + str(get_token())})
        self.assertEqual(response.status_code, 200)
        wrong_response = client.delete(path='/rating/students/rehh', headers={'Authorization': 'Bearer ' + str(get_token())})
        self.assertEqual(wrong_response.status_code, 401)



if __name__ == '__main__':
    unittest.main()


