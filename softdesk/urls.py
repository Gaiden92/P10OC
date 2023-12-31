"""
URL configuration for softdesk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as n_routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
    )

from authentication.views import UserViewSet
from api.views import (
    ProjectViewSet,
    IssueViewSet,
    CommentViewSet,
    ContributorViewSet
    )


router = routers.SimpleRouter()

router.register("users", UserViewSet, basename="users")
router.register(r"projects", ProjectViewSet, basename="projects")

project_router = n_routers.NestedSimpleRouter(router,
                                              r"projects",
                                              lookup="project")
project_router.register(r"contributors",
                        ContributorViewSet,
                        basename="projects")
project_router.register(r"issues",
                        IssueViewSet,
                        basename="project-issues")

issue_router = n_routers.NestedSimpleRouter(project_router,
                                            r"issues",
                                            lookup="issue")
issue_router.register(r"comments",
                      CommentViewSet,
                      basename="issue-comments")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/login/",
         TokenObtainPairView.as_view(),
         name="token-obtain-pair"),
    path("api/token-refresh/",
         TokenRefreshView.as_view(),
         name="token-refresh"),
    path("api/", include(router.urls)),
    path("api/", include(project_router.urls)),
    path("api/", include(issue_router.urls)),
]
