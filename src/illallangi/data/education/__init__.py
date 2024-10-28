import djp
from django.urls import URLPattern, re_path

from illallangi.data.education import checks  # noqa: F401


@djp.hookimpl
def installed_apps() -> list[str]:
    return [
        "illallangi.data.education",
    ]


@djp.hookimpl
def urlpatterns() -> list[URLPattern]:
    from illallangi.data.education import views

    return [
        re_path(
            r"^courses/$",
            views.course_list,
            name="course_list",
        ),
        re_path(
            r"^courses/(?P<slug>[\w\d-]+)/$",
            views.course_detail,
            name="course_detail",
        ),
    ]
