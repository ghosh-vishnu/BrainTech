from django.db import models

class Certificate(models.Model):
    certificate_number = models.CharField(max_length=255, unique=True, null=True,default='')
    name = models.CharField(max_length=255, null=True,default='')
    type = models.CharField(max_length=255, null=True)
    offer = models.CharField(max_length=255, null=True)
    issued = models.DateField(null=True)
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)  # Store certificates here

    def __str__(self):
        return self.certificate_number