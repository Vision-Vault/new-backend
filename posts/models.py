from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField
from accounts.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):

    ACTIVE = 'active'
    DRAFT='Draft'
    CHOICES=(
        (ACTIVE,'incomplete'),(DRAFT,'complete')
        )


    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(default="Add a description")
    image = CloudinaryField('PostImage',overwrite= True,format="jpg",null= True)
    video = models.FileField(upload_to='uploads/project_videos/', null=True, blank=True)
    funding_goal = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=False)
    allowed_donors = models.PositiveIntegerField(default=3)
    creator = models.ForeignKey(CustomUser,related_name="projects", on_delete=models.CASCADE)
    category = models.ForeignKey(Category,related_name="projects", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1, choices=[(i, i) for i in range(1, 11)])
    status = models.CharField(max_length=20, choices=CHOICES, default='incomplete')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def update_average_rating(self):
        total_ratings = self.ratings.aggregate(models.Sum('value'))['value__sum']
        total_users = self.ratings.count()
        if total_ratings is not None and total_users > 0:
            self.rating = total_ratings / total_users
            self.save()
    class Meta:
        ordering = ['-created_at']


class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    value = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])

    class Meta:
        unique_together = ('post', 'user')



class Donation(models.Model):
    user = models.ForeignKey(CustomUser, related_name="donations", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="donations", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)


    def __str__(self):
        return f"Donation by {self.user.username}: ${self.amount}"
