from django.db import models

# Create your models here. 

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)  # e.g., "Software Developer" or "Student"
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    resume = models.FileField(upload_to='resume/', blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    leetcode = models.URLField(blank=True)
    
    def __str__(self):
        return self.name

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)  # Comma-separated technologies
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    
    def __str__(self):
        return self.title

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('PROG', 'Programming Languages'),
        ('FRAME', 'Frameworks'),
        ('TOOL', 'Tools & Technologies'),
        ('SOFT', 'Soft Skills'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=80)  # Percentage of proficiency
    
    def __str__(self):
        return self.name