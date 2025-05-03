from django.db import models
from configapp.models import BaseModel


class SalomBer(BaseModel):
    title = models.CharField(max_length=50)


    def __str__(self):
        return self.title