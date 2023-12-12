from django.db import models
import uuid

class User(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=65)
    age = models.IntegerField()

    # confidentialité et RGPD
    can_be_contacted = models.BooleanField()
    can_data_be_shared = models.BooleanField()

    def __str__(self) -> str:
        return self.username


class Project(models.Model):
    choices = (
                ("BACKEND", "Backend"), 
                ("FRONTEND", "Frontend"),
                ("IOS", "IOS"),
                ("ANDROID", "Android"),
            )
    
    created_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=65)
    description = models.TextField()
    project_type = models.CharField(max_length=65, choices=choices)

    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE, related_name='authored_projects'
        )
    
    def __str__(self) -> str:
        return self.title


class Contributor(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contributors')

    def __str__(self) -> str:
        return self.user


class Issue(models.Model):
    priority_choices = (
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High")
    )
    tag_choices = (
        ("BUG", "Bug"),
        ("FEATURE", "Feature"),
        ("TASK", "Task")
    )
    status_choices = (
        ("TO_DO", "To do"),
        ("IN_PROGRESS", "In progress"),
        ("FINISHED", "Finished")
    )

    created_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues')
    priority = models.CharField(max_length=65, choices=priority_choices)
    tag = models.CharField(max_length=65, choices=tag_choices)
    status = models.CharField(max_length=65, choices=status_choices, default="TO_DO")
    assign_to = models.ForeignKey(Contributor, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="authored_issues")

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_comments')
    link_to_issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        return self.uuid
