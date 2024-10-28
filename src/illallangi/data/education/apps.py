from django.apps import AppConfig
from django.conf import settings

from illallangi.django.data.signals import ready_for_models
from illallangi.rdf.adapters import EducationAdapter as RDFAdapter


def add_model(
    **_kwargs: dict[str, object],
) -> None:
    from illallangi.django.data.models import Model, Synchronize

    Model.objects.create(
        description="Each lesson unlocks new doors to knowledge, empowering you to shape your future.",
        icon="education/courses.jpg",
        model="illallangi.data.education.models.Course",
        plural="Courses",
        singular="Course",
        url="course_list",
    )

    Synchronize.objects.create(
        callable="illallangi.data.education.apps.synchronize",
    )


class EducationalHistoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "illallangi.data.education"

    def ready(
        self,
    ) -> None:
        ready_for_models.connect(
            add_model,
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
