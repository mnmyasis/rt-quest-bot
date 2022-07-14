from django.db import models

CHOICES = (
    ('main', 'Главное меню'),
    ('chat', 'Меню в чате')
)
CHOICES_LEN = 5


class Menu(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование.')
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание меню.'
    )
    type_menu = models.CharField(
        max_length=CHOICES_LEN,
        choices=CHOICES,
        verbose_name='Тип меню'
    )
    content = models.ForeignKey(
        'Content',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='menus',
        verbose_name='Контент'
    )
    slug = models.OneToOneField(
        'Slug',
        on_delete=models.CASCADE,
        related_name='menu'
    )

    def __str__(self):
        return self.name


class Slug(models.Model):
    value = models.CharField(
        unique=True,
        max_length=50
    )

    def __str__(self):
        return self.value


class Button(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Наименование кнопки'
    )
    slug = models.ForeignKey(
        Slug,
        on_delete=models.CASCADE,
        help_text='slug для перехода к следующему меню.'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание меню.'
    )
    menu = models.ForeignKey(
        Menu,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='buttons',
        verbose_name='Меню',
        help_text='Укажите меню, к которому относится кнопка.'
    )
    content = models.ForeignKey(
        'Content',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Отоброжаемый контент при нажатии.'
    )

    def __str__(self):
        return self.name


class Content(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование.')
    text = models.TextField(
        blank=True,
        null=True,
        verbose_name='Текст'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='images/',
        blank=True
    )

    def __str__(self):
        return self.name
