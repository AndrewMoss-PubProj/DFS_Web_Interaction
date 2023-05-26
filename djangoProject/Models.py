from django.db import models

class lineup (models.Model):
    P_1 = models.CharField(_('P.1', max_length=255))
    P_2 = models.CharField(_('P.2', max_length=255))
    C = models.CharField(_('C', max_length=255))
    First_Base = models.CharField(_('1B', max_length=255))
    Second_Base = models.CharField(_('2B', max_length=255))
    Third_Base = models.CharField(_('3B', max_length=255))
    SS = models.CharField(_('SS', max_length=255))
    OF_1 = models.CharField(_('OF.1', max_length=255))
    OF_2 = models.CharField(_('OF.2', max_length=255))
    OF_3 = models.CharField(_('OF.3', max_length=255))
    # Salary = models.BigIntegerField

