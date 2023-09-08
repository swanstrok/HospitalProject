from django.db import models


# Create your models here.

class Department(models.Model):
    """Класс отделений стационара"""
    PROFILE_CHOICE = (
        (1, 'Терапевтический'),
        (2, 'Хирургический'),
    )

    name = models.CharField(max_length=255, verbose_name='Название', unique=True)
    profile = models.SmallIntegerField(verbose_name='Профиль', choices=PROFILE_CHOICE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'
        ordering = ('name',)


class Patient(models.Model):
    """Модель пациента"""
    BLOOD_TYPE_CHOICE = (
        (1, 'I (0)'),
        (2, 'II (A)'),
        (3, 'III (B)'),
        (4, 'IV (AB)')
    )

    RH_CHOICE = (
        (1, 'Rh+'),
        (2, 'Rh-'),
    )

    surname = models.CharField(max_length=80, verbose_name='Фамилия', db_index=True)
    name = models.CharField(max_length=80, verbose_name='Имя')
    patronymic = models.CharField(max_length=80, verbose_name='Отчество', null=True)
    year_of_birth = models.IntegerField(verbose_name='Год рождения')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    blood_type = models.SmallIntegerField(verbose_name='Группа крови', choices=BLOOD_TYPE_CHOICE)
    blood_rh = models.SmallIntegerField(verbose_name='Резус', choices=RH_CHOICE)
    diagnosis = models.CharField(verbose_name='Предварительный диагноз', max_length=255)
    datetime_receipt = models.DateTimeField(verbose_name='Дата и время поступления',
                                            auto_now_add=True, db_index=True)
    department_id = models.ForeignKey(verbose_name='Отделение', to='Department',
                                      on_delete=models.CASCADE)
    is_discharge = models.BooleanField(verbose_name='Выписан', default=False, db_index=True)
    datetime_discharge = models.DateField(verbose_name='Дата выписки', null=True, blank=True,
                                          db_index=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        ordering = ('id', 'name')
