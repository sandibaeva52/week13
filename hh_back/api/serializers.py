from rest_framework import serializers
from api.models import Company,Vacancy


class CompanySerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(required=True)
    description = serializers.CharField(max_length=300)
    city = serializers.CharField(max_length=300)
    address = serializers.CharField(max_length=300)

    def create(self,validated_data):
        # company = Company.objects.create(name=validated_data.get('name'))
        company = Company.objects.create(**validated_data)
        return company
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance

class CompanySerializer2(serializers.ModelSerializer):
    class Meta():
        model = Company
        # fields = ('id',)
        fields = '__all__'
    #здесь он привязан к модельке company и
    # имеет доступ к его филдам, то есть может достать все его филды
    # required=True будет все по умолчанию, знает все типы
    # методы create,update уже за нас записаны

class VacancySerializer(serializers.ModelSerializer):
        # Nested Serializers
        salary = serializers.IntegerField(required=False)
        company = CompanySerializer2(read_only=True)
        company_id = serializers.IntegerField(read_only=True)
        class Meta:
            model = Vacancy
            fields = ('id', 'name', 'description','salary','company','company_id',)

class CompanyWithVacanciesSerializer(serializers.ModelSerializer):
        # vacancies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        # vacancies = serializers.StringRelatedField(many=True, read_only=True)
        vacancies = VacancySerializer(many=True, read_only=True)
        class Meta:
            model = Company
            fields = ('id', 'name', 'vacancies')