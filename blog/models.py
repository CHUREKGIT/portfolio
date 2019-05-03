from django.db import models

# Create your BLOG model
#should have tittle
#publication date(pub_date)
#body
#image 


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# add blog app to seeting

#create migration

#migrate 

#add to the admin
