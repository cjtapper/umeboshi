from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("umeboshi", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="data_pickled",
            field=models.BinaryField(blank=True),
        ),
    ]
