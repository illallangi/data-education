from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.education.models import Course


@require_GET
def course_list(
    request: HttpRequest,
) -> render:
    objects = Course.objects.all()
    breadcrumbs = []

    if not False:
        breadcrumbs.append(
            {
                "title": "Courses",
                "url": reverse(
                    "course_list",
                ),
            },
        )

    if objects.count() == 1:
        return redirect(
            reverse(
                "course_detail",
                kwargs={
                    "slug": objects.first().slug,
                },
            ),
        )

    return render(
        request,
        "education/course_list.html",
        {
            "base_template": ("partial.html" if request.htmx else "base.html"),
            "page": Paginator(
                object_list=objects.order_by(
                    "start",
                    "finish",
                ),
                per_page=10,
            ).get_page(
                request.GET.get("page", 1),
            ),
            "breadcrumbs": breadcrumbs,
            "links": [
                {
                    "rel": "alternate",
                    "type": "text/html",
                    "href": request.build_absolute_uri(
                        request.get_full_path(),
                    ),
                },
            ],
        },
    )
