from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class DDD(models.Model):
    id = models.AutoField(primary_key=True)
    ddd = models.IntegerField('DDD', validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=100)

    class Meta:
        verbose_name_plural = "DDDs"

    def _str_(self):
        return self.ddd