# Generated by Django 4.2.6 on 2023-11-02 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='homepage_sections/')),
                ('section_type', models.CharField(choices=[('why_choose_us', 'Why Choose Us'), ('we_help', 'We Help Section'), ('popular_product', 'Popular Product'), ('blog', 'Blog Section')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='testimonials/')),
            ],
        ),
    ]
