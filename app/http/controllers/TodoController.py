from masonite.controllers import Controller
from masonite.request import Request
from app.Todo import Todo


class TodoController(Controller):

    def __init__(self, request:Request):
        self.request = request
    """Class Docstring Description
    """

    def show(self):
            id = self.request.param("id")
            return Todo.where("id", id).get()

    def index(self):
            return Todo.all()

    def create(self):
        subject = self.request.input("subject")
        details = self.request.input("details")
        todo = Todo.create({"subject": subject, "details": details})
        return todo

    def update(self):
        id = self.request.param("id")
        subject = self.request.input("subject")
        details = self.request.input("details")
        Todo.where("id", id).update({"subject": subject, "details": details})
        return Todo.where("id", id).get()

    def destroy(self):
        id = self.request.param("id")
        todo = Todo.where("id", id).get()
        Todo.where("id", id).delete()
        return todo