from autoslug import AutoSlugField
from django.db import models
from partial_date import PartialDateField


class Course(
    models.Model,
):
    # Surrogate Keys

    id = models.AutoField(
        primary_key=True,
    )

    slug = AutoSlugField(
        populate_from="get_slug",
        unique=True,
    )

    # Natural Keys

    label = models.CharField(
        blank=False,
        max_length=63,
        null=False,
        unique=True,
    )

    # Fields

    country = models.CharField(
        blank=False,
        max_length=63,
        null=False,
    )

    finish = PartialDateField(
        null=True,
        blank=True,
    )

    institution = models.CharField(
        blank=False,
        max_length=63,
        null=False,
    )

    locality = models.CharField(
        blank=False,
        max_length=63,
        null=False,
    )

    open_location_code = models.CharField(
        blank=False,
        max_length=11,
        null=False,
    )

    postal_code = models.CharField(
        blank=False,
        max_length=4,
        null=False,
    )

    region = models.CharField(
        blank=False,
        max_length=63,
        null=False,
    )

    start = PartialDateField(
        null=True,
        blank=True,
    )

    street = models.CharField(
        blank=False,
        max_length=63,
        null=False,
    )

    # Methods

    def __str__(
        self,
    ) -> str:
        return self.label

    def get_slug(
        self,
    ) -> str:
        return self.label
