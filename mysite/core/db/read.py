from .models import Timeslot, Reports_assessments
import datetime 
import pytz
utc=pytz.UTC

class DBRead():
    def __init__(self):
        self.print= None

    def test(self):
        start_date= Timeslot.objects.values_list(key, flat=True)
        return list(start_date)

    def insert(self):
        newRow = Timeslot(appointment_id= 185, title= "as")
        newRow.save()


    def timeslot(self):#list of object
        #now= datetime.datetime(2019, 11, 15, 16, 30) 
        now= datetime.datetime.utcnow()
        now= utc.localize(now)
        print( "<----------NOW TIME----------->\n", str(now), "\n<----------------------------->")
        rows= list( Timeslot.objects.values('id', 'appointment_id', 'account_id', 'start_date', 'end_date') )
        inSlots= []
        for row in rows:
            #print( row['start_date'], now, '<', now,  '<', row['end_date'])
            if row['start_date'] < now  and now < row['end_date']:
                inSlots.append(row)
               
        print(inSlots)
        return inSlots

    def reports_assessments(self, session_id, patient_id):
        print(session_id, patient_id)

        print( "reports_assessments")
        Reports_assessments.objects.all()

        rows= list( Reports_assessments.objects.filter(session_id=session_id, patient_id=patient_id).values('id', 'session_id', 'patient_id') )
        
        self.print= str(rows)

        return str(rows)
        
    def alert(self):
        inSlots= self.timeslot()  
        
        for inSlot in inSlots:
            print(inSlot)
            session_id= inSlot['appointment_id'] #session_id
            patient_id= inSlot['account_id'] #patient_id
            print(session_id, patient_id)
            #self.reports_assessments( session_id,  patient_id )
        

        return  self.print






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