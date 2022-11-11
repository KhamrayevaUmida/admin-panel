from django.db import models

class Institut(models.Model):
    name = models.CharField(max_length=50)
    fakultet_soni = models.IntegerField(default=5)
    name_rektor = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}: {self.fakultet_soni} ta fakulteti mavjud; {self.name_rektor}"


class Fakultet(models.Model):
    name = models.CharField(max_length=30)
    talaba_soni = models.IntegerField(default=100)
    dekan = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}: {self.talaba_soni} ta talabasi mavjud; {self.dekan}"


class Talaba(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField(default=18)

    def __str__(self):
        return f"{self.name} {self.surname} {self.age}"

class Fan(models.Model):
    name = models.CharField(max_length=20)
    teacher = models.CharField(max_length=20)
    modul = models.IntegerField(default=2)

    def __str__(self):
        return f"{self.name} fan uqituvchisi {self.teacher}; kredit modul {self.modul}"


class Olimpiada(models.Model):
    yunalish = models.CharField(max_length=20)
    qatnashuvchilar = models.IntegerField(default=10)
    time = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.yunalish}: qatnashuvchilar soni {self.qatnashuvchilar}; berilgan vaqt {self.time}"


class Maktab(models.Model):
    name = models.CharField(max_length=20)
    sinf = models.IntegerField(default=1)
    sinf_raxbar = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}; {self.sinf}; {self.sinf_raxbar} "
