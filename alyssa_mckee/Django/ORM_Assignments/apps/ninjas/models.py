from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class Dojo(models.Model):
	CITY_CHOICES=[
		("Silicon Valley","Silicon Valley"),
		("Seatle","Seatle"),
		("Los Angelos","Los Angelos"),
		("Dallas","Dallas"),
		("Washington DC","Washington DC"),
		("Chicago","Chicago"),
		("Tulsa","Tulsa"),
		("New York","New York")
	]
	STATE_CHOICES=[
		("CA","California"),
		("WA","Washington"),
		("TX","Texas"),
		("VA","Virginia"),
		("IL","Illinois"),
		("OK","Oklahoma"),
		("NY","New York")
	]
	name = 			models.CharField(max_length=255)
	city =			models.CharField(max_length=255, choices=CITY_CHOICES)
	state =			models.CharField(max_length=255, choices=STATE_CHOICES)
	desc = 			models.TextField(default = "")
	
	def __str__(self):
		return "||Dojo: {} {} {} {}||".format(self.name, self.city, self.state, self.desc)
	def save(self, *args, **kwargs):
		if self.city == "Silicon Valley" and self.state != "CA":
			raise ValidationError("City and State dont match")
		if self.city == "Seatle" and self.state != "WA":
			raise ValidationError("City and State dont match")
		if self.city == "Los Angelos" and self.state != "CA":
			raise ValidationError("City and State dont match")
		if self.city == "Dallas" and self.state != "TX":
			raise ValidationError("City and State dont match")
		if self.city == "Washington DC" and self.state != "VA":
			raise ValidationError("City and State dont match")
		if self.city == "Chicago" and self.state != "IL":
			raise ValidationError("City and State dont match")
		if self.city == "Tulsa" and self.state != "OK":
			raise ValidationError("City and State dont match")
		if self.city == "New York" and self.state != "NY":
			raise ValidationError("City and State dont match")
		#would be better if I had models for these... is there any better way to do this?
		
		super().save(*args, **kwargs)
	
	
class Ninja(models.Model):
	dojo_id = 		models.ForeignKey(Dojo)
	first_name = 	models.CharField(max_length=255)
	last_name = 	models.CharField(max_length=255)
	
	def __str__(self):
		return "<Ninja: {} {} dojo: {}>".format(self.first_name, self.last_name, self.dojo_id)