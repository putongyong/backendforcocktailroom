from rest_framework import serializers
from .models import Category, Subcategory, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubcategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    subcategory = serializers.CharField(max_length=100)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Product` instance, given the validated data.
        """
        return Subcategory.objects.create(**validated_data)

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    subcategory = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    image = serializers.ImageField()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Product` instance, given the validated data.
        """
        return Product.objects.create(**validated_data)
    
