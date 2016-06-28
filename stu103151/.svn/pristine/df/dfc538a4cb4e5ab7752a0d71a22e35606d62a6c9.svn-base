import os

from django.db.models import F
os.environ["DJANGO_SETTINGS_MODULE"]="mysite.settings"
import django
django.setup()
from blog import models
from django.db.models import Q
from django.db.models import Avg,Sum,Min,Max,Count

entry = models.Entry.objects.get(pk=3)
ss_blog = models.Blog.objects.get(pk=2)
# entry.blog = ss_blog
# entry.save()
# print(entry,ss_blog)

# joe = models.Author.objects.create(name='Joe')
# ana = models.Author.objects.create(name='Ana')
# rain = models.Author.objects.create(name='Rain')
# haha = models.Author.objects.create(name='Haha')
# entry.authors.add(ana,rain,haha)

# objs = models.Entry.objects.filter(n_comments__lte= F('n_pingbacks'))

# objs = models.Entry.objects.get(
#     # Q(question__startwith='who'),
#     Q(n_comments__lt=F('n_pingbacks')) | Q(pub_date__lt='2016-5-10')
# )
from store import models as book_models
pub_obj = book_models.Publisher.objects.last()
# pub_obj = models.Entry.objects.all().aggregate(Avg('n_pingbacks'),Sum('n_pingbacks'),Min('n_pingbacks'))

# print(pub_obj.name,pub_obj.book_set.select_related())
pub_objs = book_models.Publisher.objects.annotate(book_nums=Count('book'))
# print(pub_obj)
for publisher in pub_objs:
    print(publisher,publisher.book_nums)