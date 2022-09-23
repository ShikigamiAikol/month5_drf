from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название фильма")
    description = models.TextField(null=True, blank=True, verbose_name="Описание фильма")
    duration = models.IntegerField(default=100)
    director = models.ForeignKey(to=Director, verbose_name="Режиссер",
                                 related_query_name="movies", on_delete=models.SET_NULL,
                                 null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.director}"


class Review(models.Model):
    text = models.TextField("Не забудьте оставить отзыв")
    movie = models.ForeignKey(to=Movie, verbose_name="Ваш отзыв к фильму",
                              related_name="reviews", on_delete=models.SET_NULL,
                              null=True, blank=True)

    def __str__(self):
        return f"{self.movie}"
