
# class Hotel(Document):
#     def __str__(self):
#         return self.name

#     address = StringField(max_length=200)
#     # pub_date = models.DateTimeField('date published')
#     benefits = StringField(max_length=200)
#     destination = StringField(max_length=200)
#     image_urls = StringField(max_length=200)
#     link = StringField(max_length=200)
#     name = StringField(max_length=200)
#     room_type = StringField(max_length=200)
#     images = StringField(max_length=200)
#     price = IntField(default=0)
#     star = FloatField()
    

# class Choice(models.Model):
#     def __str__(self):
#         return self.choice_text

#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
    