from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateField()

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance


# python manage.py shell
# (InteractiveConsole)
# >>> from restful_basic.models import Article
# >>> from restful_basic.serializers import ArticleSerializer
# >>> from rest_framework.renderers import JSONRenderer
# >>> from rest_framework.parsers import JSONParser
# >>> a = Article(title='ArticleTitle', author='Snehar', email='snehar@email.com')
# >>> a.save()
# >>> a = Article(title='ArticleTitleUpdated', author='Snehar', email='snehar@email.com')
# >>> a.save()
# >>> serializer = ArticleSerializer(a) 
# >>> serializer.data
# {'title': 'ArticleTitleUpdated', 'author': 'Snehar', 'email': 'snehar@email.com', 'date': '2020-01-15'}
# >>> content = JSONRenderer().render(serializer.data)
# >>> content
# b'{"title":"ArticleTitleUpdated","author":"Snehar","email":"snehar@email.com","date":"2020-01-15"}'
# >>>
# >>> Serializing a queryset
# >>> serializer = ArticleSerializer(Article.objects.all(), many=True)
# >>> serializer.data
# [OrderedDict([('title', 'ArticleTitle'), ('author', 'Snehar'), ('email', 'snehar@email.com'), ('date', '2020-01-15')]), OrderedDict([('title', 'ArticleTitleUpdated'), ('author', 'Snehar'), ('email', 'snehar@email.com'), ('date', '2020-01-15')])]


class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ['id', 'title', 'author','date']
        fields = '__all__'
        
# >>> from restful_basic.serializers import ArticleModelSerializer 
# >>> serializer = ArticleModelSerializer()
# >>> print(repr(serializer))
# ArticleModelSerializer():
#     id = IntegerField(label='ID', read_only=True)
#     title = CharField(max_length=100)
#     author = CharField(max_length=100)
#     date = DateField(read_only=True)
  