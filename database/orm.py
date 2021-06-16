from django.conf import settings
from .models import Order, User
from django.db import connection

import json

from django.core import serializers

class Orders():
    def __init__(self):
        print("Query")
        self.print= None  

    def all(self):
        print("all")
        e = Order.objects.all().select_related('user')
        print(e.query)
        orders = e.values()

        data_list= []
        for row in e:
            dic= {}
            dic['name']= row.user.name
            dic['stock']= row.name
            data_list.append(dic)

        print(data_list)
        return data_list

    def update(self):
        print("update")
        User.objects.filter(pk=4).update(age=37)

    def create(self):
        print("create")
        user = User(name='Beatles Blog', age='59')
        user.save()

#https://docs.djangoproject.com/en/3.2/topics/db/sql/
class Raw_query():
    def __init__(self):
        print("raw_query")
        self.print= None  

    def all_manager_method(self):
        print("all_manager_method")
        sql= 'SELECT * FROM test_order'
        e= Order.objects.raw(sql)
        data_list=[]
        for row in e:
            dic= {}
            dic['name']= row.user.name
            dic['age']= row.user.age
            dic['stock']= row.name
            data_list.append(dic)

        print(data_list)
        return data_list

    def all_custom_method(self):
        print("all_custom_method")
        sql= 'SELECT * FROM test_order left join test_user on test_order.user_id = test_user.id'
        data_list=[]
        with connection.cursor() as cursor:
            cursor.execute(sql)
            # print(cursor.description)
            rows = cursor.fetchall()

            dic= {}
            for row in rows:
                print(row)
                dic['name']= row[4]
                dic['age']= row[5]
                dic['stock']= row[2]
                data_list.append(dic)

        print(data_list)
        return data_list

    def update_custom_method(self):
        print("update_custom_method")
        sql= 'update test_user set age= 39 where id= 4'
        with connection.cursor() as cursor:
            cursor.execute(sql)
            print(cursor.description)

    def create_custom_method(self):
        print("create_custom_method")
        sql= " INSERT INTO test_user (name, age) VALUES ('Edson', '46'); "
        with connection.cursor() as cursor:
            cursor.execute(sql)

# class Query():
#     def __init__(self):
#         print("Query")
#         self.print= None  

#     def all(self):
#         print("all")

        # queryset= Sensor.objects.select_related('serialNumber')
        # print(str(queryset))

        # queryset= Sensor.objects.all().values_list()
        # print(str(queryset))

        # q1= Sensor.objects.select_related('serialNumber')
        # print(q1)


# books = Book.objects.all().select_related("author")
# for book in books:
#     print(book.author.name)  # Evaluates the query set, caches in memory results
# first_book = books[1]  # Does not hit db
# print(first_book.author.name)  # Does not hit db 

        # children_ids = ParentModel.objects.filter(name__startswith='A').values_list('child', flat=True)
        # children = ChildModel.objects.filter(pk__in=children_ids)
        
        # heartbeat_ids = Sensor.objects.all().values_list('heartbeat', flat=True)
        # heartbeat = Heartbeat.objects.filter(pk__in=heartbeat_ids)
        # print("aaaaaaaaaaaa", heartbeat_ids)
        # print("bbbbbbbbbbbb", heartbeat.values_list())

        # # Parent.objects.prefetch_related('child_set')
        # # sensors= Sensor.objects.prefetch_related('heartbeat')
        # # print("0000", sensors.values_list())

        # e = Sensor.objects.all().select_related('heartbeat')
        # print("0000", type(e), e.values_list())
        # serializer = SensorSerializer(e, many=True)
        # print("11111", type(serializer), serializer )


        # for sensor in e:
        #     print(sensor.heartbeat.message)  # Does not hit db 

        # data = serializers.serialize('json', e)

        # print("22222", data)
        # print("22222", serializer.data)



        # return serializer.data
        # q1= Sensor.objects.select_related('serialNumber')
        # print(q1)


        # for heartbeat in heartbeats.items():
        #     print( heartbeat['serialNumber'] )

        # serialNumbers= [ heartbeat['serialNumber'] for heartbeat in heartbeats]
        # print(serialNumbers)





    # def getState(self, state):
    #     print("getState")
    #     message= Heartbeats().filter(state)
    #     return message


# class DBRead():
#     def __init__(self):
#         self.print= None
     
#     def ml_test(self, name="hunter"):
#         try:
#             e= Ml_test.objects.filter( name= name )
#         except:
#             raise Http404("can not access to mysql")

#         serializer = Ml_testSerializer( e, many=True)
        
#         if not serializer.data:
#             raise Http404("filename can not found in table")

#         return serializer.data



    # def update(self, filename=None, transcription=None):
    #     try:
    #         e= Teleconference_transcribe.objects.filter( filename= filename )
    #     except:
    #         raise Http404("can not access to mysql")

    #     serializer = Teleconference_transcribeSerializer( e, many=True)
        
    #     if not serializer.data:
    #         raise Http404("filename can not found in table")

    #     row= e.update(transcription_baseline= transcription)
    #     print("successfully update db ")

    #     return serializer.data



     








         
 #print(timeslot)

        # today= datetime.date.today() 
        # TimeslotToday= Timeslot.objects.filter( start_date__range=(today, today + datetime.timedelta(days=1)) )
        # print("TimeslotToday:  ",TimeslotToday)

        # minute = datetime.timedelta(minutes=500)
        # today= datetime.date.today() 
        # now= datetime.datetime.now()
     

        # print("st    ", datetime.datetime(2019, 11, 15, 15, 30) )
        # x=              datetime.datetime.utcnow()
        # x=              datetime.datetime(2019, 11, 15, 16, 30) 
        # x= now
        # print("xx    ", x )
        # print("ed    ", datetime.datetime(2019, 11, 15, 17, 30))

     
        #inSlot_ = Timeslot.objects.filter(start_date__lt= x, end_date__gt= x)

        #inSlot= Timeslot.objects.filter( start_date__lt= now + minute ).filter( end_date__gt= now - minute )

        #inSlot= Timeslot.objects.filter( start_date__lt= now ).filter( end_date__gt= now ) # utc

        # TimeslotToday= Timeslot.objects.filter( start_date__range=(today, today + datetime.timedelta(days=1)) )
        # print("TimeslotToday:  ",TimeslotToday)
        #2019-11-15 15:30:00  -  2019-11-15 16:30:00