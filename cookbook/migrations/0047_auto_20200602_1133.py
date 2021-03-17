# Generated by Django 3.0.5 on 2020-06-02 09:33

from django.db import migrations
from django.utils.translation import gettext as _
from django_scopes import scopes_disabled


def migrate_meal_types(apps, schema_editor):
    with scopes_disabled():
        MealPlan = apps.get_model('cookbook', 'MealPlan')
        MealType = apps.get_model('cookbook', 'MealType')

        breakfast = MealType.objects.create(
            name=_('Breakfast'),
            order=0,
        )

        lunch = MealType.objects.create(
            name=_('Lunch'),
            order=0,
        )

        dinner = MealType.objects.create(
            name=_('Dinner'),
            order=0,
        )

        other = MealType.objects.create(
            name=_('Other'),
            order=0,
        )

        for m in MealPlan.objects.all():
            if m.meal == 'BREAKFAST':
                m.meal_type = breakfast
            if m.meal == 'LUNCH':
                m.meal_type = lunch
            if m.meal == 'DINNER':
                m.meal_type = dinner
            if m.meal == 'OTHER':
                m.meal_type = other

            m.save()


class Migration(migrations.Migration):
    dependencies = [
        ('cookbook', '0046_auto_20200602_1133'),
    ]

    operations = [
        migrations.RunPython(migrate_meal_types),
    ]
