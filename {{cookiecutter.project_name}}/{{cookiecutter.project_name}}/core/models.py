from django.conf import settings
from django.db import models
from django_tools.middlewares import ThreadLocal


class GlobalPermissionHolder(models.Model):
    "A non-managed model to be used as a holder for global permissions"

    class Meta:
        managed = (
            False
        )  # No database table creation or deletion operations will be performed for this model.
        permissions = (("user", "Application user"), ("admin", "Application admin"))


class UserDateAbstractModel(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True, verbose_name="Created date",
    )
    modified_on = models.DateTimeField(
        auto_now=True, verbose_name="Modified date",
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name="Created by",
        related_name="%(class)s_created",
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name="Modified by",
        related_name="%(class)s_modified",
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = ThreadLocal.get_current_user()
        if user:
            if not self.pk:
                self.created_by = user

            self.modified_by = user
        super(UserDateAbstractModel, self).save(*args, **kwargs)
