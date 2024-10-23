from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_migrate

from illallangi.rdf.adapters import EducationAdapter as RDFAdapter


def add_model(
    **_kwargs: dict[str, object],
) -> None:
    from illallangi.django.data.models import Model, Synchronize

    Model.objects.update_or_create(
        description="Each lesson unlocks new doors to knowledge, empowering you to shape your future.",
        icon="education/courses.jpg",
        model="illallangi.data.education.models.Course",
        plural="Courses",
        singular="Course",
        url="courses_html",
    )

    Synchronize.objects.update_or_create(
        callable="illallangi.data.education.apps.synchronize",
    )


class EducationalHistoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "illallangi.data.education"

    def ready(
        self,
    ) -> None:
        post_migrate.connect(
            add_model,
            sender=self,
        )


def synchronize() -> None:
    from illallangi.data.education.adapters import (
        EducationAdapter as DjangoAdapter,
    )

    src = RDFAdapter(
        **settings.RDF,
    )
    dst = DjangoAdapter()

    src.load(
        **settings.EDUCATION,
    )
    dst.load()

    src.sync_to(dst)
