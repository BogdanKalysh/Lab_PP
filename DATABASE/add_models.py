from models import Session, teacher, student

session0 = Session()

teacher0 = teacher(teacher_id = 1, name = "Ya", email = "miy@gmail.com", password = "takiy")
student0 = student(student_id = 1, name = "Tlumok",s_bal = 10, marks = [9,11)

session0.add(teacher0)
session0.add(student0)

session0.commit()

session0.close()

# psql -h localhost -d students_rating -U postgres -p 5432 -a -q -f create_table.sql
# python add_models.py 
# чекнути пгадмін
# alembic revision --autogenerate
# alembic upgrade head
# env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2