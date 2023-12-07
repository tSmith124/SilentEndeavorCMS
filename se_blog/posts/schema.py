import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

from posts import models

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class PostsType(DjangoObjectType):
    class Meta:
        model = models.Posts

class CategoryType(DjangoObjectType):
    class Meta:
        model = models.Category

class Query(graphene.ObjectType):
    all_posts = graphene.List(PostsType)
    post_by_slug = graphene.Field(PostsType, slug=graphene.String())
    posts_by_author = graphene.List(PostsType, username=graphene.String())
    posts_by_tag = graphene.List(PostsType, tag=graphene.String())

    def resolve_all_posts(root, info):
        return (
            models.Posts.objects.prefetch_related("categories")
            .select_related("author")
            .all()
        )

    def resolve_post_by_slug(root, info, slug):
        return (
            models.Posts.objects.prefetch_related("categories")
            .select_related("author")
            .get(slug=slug)
        )

    def resolve_posts_by_author(root, info, username):
        return (
            models.Post.objects.prefetch_related("categories")
            .select_related("author")
            .filter(author__user__username=username)
        )

    def resolve_posts_by_category(root, info, tag):
        return (
            models.Post.objects.prefetch_related("categories")
            .select_related("author")
            .filter(tags__name__iexact=categories)
        )
    
schema = graphene.Schema(query=Query)