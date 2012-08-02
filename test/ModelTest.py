# -*- coding:utf-8 -*-
#测试模型的
from books.models import Publisher

if __name__ == '__main__':
    p1 = Publisher(name='Apress',
                   address="2855 Telegraph Ave",
                   city="Berkeley",
                   state_province="CA",
                   country="USA",
                   website='http://www.apress.com/')
    p1.save()
    
    p2=Publisher.objects.create(name="O'Reilly",
                                address='10 Fawcett St.',
                                city="Cambridge",
                                state_province="MA",
                                country="USA",
                                website="http://www.oreilly.com")
    publisher_list=Publisher.objects.all()
    print publisher_list
    p1.name='Apress Publishing'
    p1.save()
    print p1.name
    publisher_list=Publisher.objects.filter(country="USA").order_by("-name")
    print publisher_list
    print Publisher.objects.order_by('name')[0]
    print Publisher.objects.all().count()
    print Publisher.objects.all().delete()
    print Publisher.objects.all()
    
    