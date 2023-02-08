from django.db import models
from embed_video.fields import EmbedVideoField

class Games(models.Model):
	title = models.CharField('Назва', max_length=50)
	text = models.TextField('Опис')
	date = models.DateField('Дата публікації')
	Gameimg = models.FileField('Фото ігри')
	Scrgame1= models.FileField('скріни з ігри',blank=True)
	Scrgame2= models.FileField('скріни з ігри',blank=True )
	Scrgame3= models.FileField('скріни з ігри',blank=True)
	Scrgame4= models.FileField('скріни з ігри',blank=True)
	Scrgame5= models.FileField('скріни з ігри',blank=True)
	Scrgame6= models.FileField('скріни з ігри',blank=True)
	Videolink = EmbedVideoField('Відео',blank=True)
	Creators = models.CharField('Студія', max_length=250)
	Rate = models.CharField('Рейтинг', max_length=5)
	Steaml =  models.URLField('Steam', max_length=50,blank=True)
	GOGl =  models.URLField('GOG', max_length=50,blank=True)
	Epic_Games =  models.URLField('Epic Games', max_length=50,blank=True)


	def __str__(self):
		return self.title
