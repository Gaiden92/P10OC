from django.db import models
import uuid

from softdesk.settings import AUTH_USER_MODEL


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
        to=AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name='authored_projects', blank=True
        )

    def __str__(self) -> str:
        return self.title


class Contributor(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='contributors',
                                blank=True)

    class Meta:
        unique_together = ('user', 'project')

    def __str__(self) -> str:
        return self.user.username


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
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name='issues',
                                blank=True)
    priority = models.CharField(max_length=65, choices=priority_choices)
    tag = models.CharField(max_length=65, choices=tag_choices)
    status = models.CharField(max_length=65,
                              choices=status_choices,
                              default="TO_DO")
    assign_to = models.ForeignKey(Contributor,
                                  on_delete=models.CASCADE,
                                  blank=True)
    author = models.ForeignKey(AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="authored_issues",
                               blank=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    issue = models.ForeignKey(Issue,
                              on_delete=models.CASCADE,
                              related_name='comments',
                              blank=True)
    text = models.TextField()
    author = models.ForeignKey(AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='authored_comments',
                               blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        return self.uuid
