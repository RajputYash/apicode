import paho.mqtt.client as mqtt
from celery import Celery
from .models import Consumption
app = Celery('tasks', broker='amqp://guest@localhost//')


@app.task
def mqtt_client():

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("/Acclivate/iOmniControl/#")
        client.subscribe("/sem/iOmniControl/+/+/+/+/state", 1)
        client.subscribe("/AVC_510_delhivery/#")


        # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        #print(msg.topic+" "+str(msg.payload))
        print("MESSAGE:@@@@@@@@@@@@@@@@@@@@@@22")
        print(msg)

        print ("########## Topic ############")
        print ("Topic: ", msg.topic + '  Message: ' + str(msg.payload))
        print ("######################")
        message=str(msg.payload)
        print ("*******************")
        print (message)
        print ("*******************")

        data = (msg.topic).split("/")[2]
        print ("$$$$yyyyy$$$$$$")
        #data_js=json.dump(data)
        print (data)
        print ("$$$$$jjjjj$$$$$")
        if(len(message.split(",")) == 8):
            print ("These are the values")
            Bal=str(message.split(",")[0])
            read=str(message.split(",")[1])
            cost=str(message.split(",")[2])
            current_time=str(message.split(",")[3])
            cummulative_units=str(message.split(",")[4])
            total_property=str(message.split(",")[5])

            room=str(message.split(",")[6])
            value7=str(message.split(",")[7])

            print('#####################')

            #
            # print("Balance is:",Bal)
            # print("reading is",read)
            # print("cost is :",cost)
            # print("current_time :",current_time)
            # print("cummulative units:",cummulative_units)
            # print("total property: ",total_property)
            # print("room is :",room)
            # print("value :",value7)

            Consumtion = float((read.split(":"))[1])
            print("ccccccccccc")
            print(Consumtion)

            Balance=float((Bal.split(":"))[1])
            print(Balance)

            Cost = float((cost.split(":"))[1])
            print('cost: ', Cost)

            Current_time=current_time.split(":")[1]
            print("current_type",Current_time)
            print ("ccccccccccc")

            Cummulative_units = float((cummulative_units.split(":"))[1])
            print("cummulative:", Cummulative_units)

            Total_property_cummulative = float((total_property.split(":"))[1])
            print("total_property:", Total_property_cummulative)

            Room_id = int((room.split(":"))[1])
            print('room_id : ',Room_id)

            Current_type=float((message.split(":"))[1])
            print("current_type:", Current_type)




            # print ("BALANCE={}, READING={}, ROOM_ID={}".format(Balance,Consumtion,Room_id))
            # Consumption.objects.create(user_consumption=Consumtion,date=Current_time)
            #print('consumption is : ',c)

            #DailySiteReading.objects.create(unit_consumption=Consumtion)




        else:
            print("This message is not for consumption")





    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("127.0.0.1", 5003, 60)
    client.loop_forever()

# if __name__ == "__main__":
#  # if you call this script from the command line (the shell) it will
#  # run the 'main' function
#     mqtt_client()