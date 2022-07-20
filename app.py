
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:1234@127.0.0.1:3306/world'
db = SQLAlchemy(app)



class Student(db.Model):
    __tablename__ = "Student"
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(20))
    student_course = db.Column(db.String(100))
    age = db.Column(db.Integer)

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,student_name,student_course,age):
        self.student_name = student_name
        self.student_course = student_course
        self.age = age
    def __repr__(self):
        return '' % self.id
db.create_all()
class StudentSchema(SQLAlchemySchema):
    class Meta:
        model = Student
        load_instance = True
        include_relationships=True
        sqla_session = db.session
    id = auto_field(dump_only=True)
    student_name = auto_field(required=True)
    student_course = auto_field(required=True)
    age = auto_field(required=True)

@app.route('/students', methods = ['GET'])
def index():
    get_students = Student.query.all()
    student_schema = StudentSchema(many=True)
    students = student_schema.dump(get_students)
    return make_response(jsonify({"student": students}))

@app.route('/students/<id>', methods = ['PUT'])
def update_student_by_id(id):
    data = request.get_json()
    get_student = Student.query.get(id)
    if data.get('student_name'):
        get_student.student_name = data['student_name']
    if data.get('student_course'):
        get_student.student_course = data['student_course']
    if data.get('age'):
        get_student.age= data['age']    
    db.session.add(get_student)
    db.session.commit()
    student_schema = StudentSchema(only=['id', 'student_name', 'student_course','age'])
    student = student_schema.dump(get_student)
    return make_response(jsonify({"student": student}))

@app.route('/students/<id>', methods = ['DELETE'])
def delete_product_by_id(id):
    get_student = Student.query.get(id)
    db.session.delete(get_student)
    db.session.commit()
    return make_response("",204)

@app.route('/students', methods = ['POST'])
def create_product():
    data = request.get_json()
    student_schema = StudentSchema()
    student = student_schema.load(data)
    result = student_schema.dump(student.create())
    return make_response(jsonify({"Student": result}),200)
if __name__ == "__main__":
    app.run(debug=True)
