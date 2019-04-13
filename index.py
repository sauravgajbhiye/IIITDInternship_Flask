from flask import Flask, render_template,request
import csv
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/letstry", methods=['GET', 'POST'])
def openfie():
    if request.method == 'POST':
        Source = request.form['src']
        Destination = request.form['destn']
    src=0
    dest=0
    list1 = []
    with open('stops.txt') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        for row in csv_reader:
            if(row[2].casefold()==Source.casefold() and src==0):
                src=1
                src_id=row[0]
                #return render_template('content.html', text=src_id)
            if(row[2].casefold()==Destination.casefold() and dest==0):
                dest=1
                des_id=row[0]
        #return render_template('content.html', text=src_id)
    if(src==0):
        return render_template('content.html', text='Source not Found')
    elif(dest==0):
        return render_template('content.html', text='Destination not Found')
    else:
        route=[]
        with open('stop_times.txt') as csv_stopTime:
        csv_reader = csv.DictReader(csv_stopTime)
            for row in csv_reader:
                #print(row['stop_id'])
                list1.append(row['stop_id'])
                route.append(row['trip_id'])
            list2=[]
            for i in range(len(list1)):
                if(list1[i]==src_id):
                    if(list1[i+1]==des_id or list1[i+2]==des_id):
                        list2.append(route[i])
        rName=[]
        with open('routes.txt') as csv_route:
            csv_reader = csv.DictReader(csv_route)
            for row in csv_reader:
                if row['route_id'] in list2:
                    rName.append(row['route_long_name'])
            if(len(rName)==0):
                return render_template('content.html', text='No direct Route Exists')
            return render_template('content.html', text=rName)
            #count=0
        #    for row in csv_reader:
         #       if(row[3]==src_id):
          #          if((row[0]==csv_reader[count+1][0] and csv_reader[count+1][3]==des_id) or ((row[0])==csv_reader[count+2][0] and csv_reader[count+2][3]==des_id)):
           #             #trip_id = row[0]
          #              list1.append(row[0])        
         #       count+=1
        #    return render_template('content.html', text=list1)
    return render_template('content.html', text='No route Found')
if __name__ == '__main__':
    app.run(debug=True)
