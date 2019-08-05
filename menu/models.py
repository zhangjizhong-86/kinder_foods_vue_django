from django.db import models

# Create your models here.
class Menu(models.Model):
	week = models.CharField(max_length=30,verbose_name=u"周", primary_key=True)
	date = models.DateField(verbose_name=u"日期")
	diet = models.CharField(max_length=45,verbose_name=u"进食时间")
	food = models.CharField(max_length=20,verbose_name=u"餐食")
	comment = models.CharField(max_length=100,verbose_name=u"备注")
	class Meta:
		verbose_name= u"幼儿园菜单"
		db_table = u"kinder_foods"
