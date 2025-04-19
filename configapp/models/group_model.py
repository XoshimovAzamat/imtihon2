from .teacher_model import *
from .user_model import *

class GroupStudent(BaseModel):
    title = models.CharField(max_length=40, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher, related_name='teacher_get')

    def __str__(self):
        return self.title
