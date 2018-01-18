from __future__ import division

import mysql.connector, subprocess, os

def shellscript():
    #bashCommand1 = "sshpass -p 'vagrant' scp ~/remy/vagrant/mysql/caloricdata vagrant@172.31.255.196:/tmp/mydata.txt"
    #process1 = subprocess.Popen(bashCommand1.split(), stdout=subprocess.PIPE)
    #output, error = process1.communicate()

    #bashCommand2 = "ssh vagrant@"
    #process2 = subprocess.Popen(bashCommand2.split(), stdout=subprocess.PIPE)
    #output, error = process2.communicate()
    os.system("sshpass -p 'vagrant' ssh -o StrictHostKeyChecking=no vagrant@172.31.255.196 ls -l /tmp")

def macroCalc(food,grams):

    cal_sum = 0
    fat_sum = 0
    carb_sum = 0
    prot_sum = 0

    con = mysql.connector.connect(user='root', password='root',
                                  host='172.31.255.196',
                                  database='calo')

    cnx = con.cursor()
    cnx.execute("SELECT * FROM rie")

    for row in cnx.fetchall():
       # print food

        for k in range(len(food)):
            if food[k] == row[0] and row[0] == str(food[k]) and int(grams[k]) == 100:
                print row[0], "Calories", row[1], "Fat", row[2], "Carbs", row[3], "Proteins", row[4]
                cal_sum += row[1]
                fat_sum += row[2]
                carb_sum += row[3]
                prot_sum += row[4]

            elif food[k] == row[0] and row[0] == str(food[k]) and int(grams[k]) != 100:
                print row[0], "Calories", float(int(grams[k]) / 100) * float(row[1]), \
                    "Fat", float(int(grams[k]) / 100) * float(row[2]), "Carbs", float(int(grams[k]) / 100) * float(row[3]), \
                    "Proteins", float(int(grams[k]) / 100) * float(row[4])
                cal_sum += float(int(grams[k]) / 100) * float(row[1])
                fat_sum += float(int(grams[k]) / 100) * float(row[2])
                carb_sum += float(int(grams[k]) / 100) * float(row[3])
                prot_sum += float(int(grams[k]) / 100) * float(row[4])

    print "SUM: Calories", cal_sum, "Fat", fat_sum, "Carb", carb_sum, "Protein", prot_sum

    con.close()

meal = ["wolowina","papryki","wolowina","papryki"]
grams = ["200", "100","100", "200"]

macroCalc(raw_input("Meal: ").split(),raw_input("Grams: ").split())
#macroCalc(meal,grams)

#macroCalc("chicken",230)

#print meal["chicken"], chicken["fat"]
#i = 0
#for i in range(len(meal)):
#    print meal[i], grams[i]