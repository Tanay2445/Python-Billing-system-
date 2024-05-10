#START of code
import mysql.connector

#perchase is to get input of user
def purchase(List):
    L = List  # assign list with variable name 'L'.
    a_name = input("Please enter your name: ")
    print("\nHello " + a_name + "! Welcome to our RANA Electronic Store.\nPlease select product as per your choice.")
    q = {}  # assign empty dictionary with variable name 'q'.
    flag = "Y"
    while flag.upper() == "Y":  # check and go if flag is 'Y' or 'y'.
        product = input("\nWhat product do you want to buy? ")
        product_name = product.upper()  # change the string value in the upper case.

        if product_name == L[0][0].upper() \
                or product_name == L[1][0].upper() \
                or product_name == L[2][0].upper() \
                or product_name == L[3][0].upper() \
                or product_name == L[4][0].upper() \
                or product_name == L[5][0].upper():
            p = True
            while p == True:
                try:
                    p_quantity = int(input("How many " + product + " do you want to buy: "))
                    p = False
                except:  # executes, if customer entered unexpected value.
                    print("\t\tError!!!\nPlease enter integer value!! ")
            if product_name == L[0][0].upper() and p_quantity <= int(L[0][2]):
                q[product_name] = p_quantity
            elif product_name == L[1][0].upper() and p_quantity <= int(L[1][2]):
                q[product_name] = p_quantity
            elif product_name == L[2][0].upper() and p_quantity <= int(L[2][2]):
                q[product_name] = p_quantity
            elif product_name == L[3][0].upper() and p_quantity <= int(L[3][2]):
                q[product_name] = p_quantity
            elif product_name == L[4][0].upper() and p_quantity <= int(L[4][2]):
                q[product_name] = p_quantity
            elif product_name == L[5][0].upper() and p_quantity <= int(L[5][2]):
                q[product_name] = p_quantity
            else:
                print(
                    "\nSorry!! " + a_name + "!, " + product + " is out of stock.\nWe will add stock of " + product + " later. \nLets hope, you will get this product after next shopping.\n")

            flag = (input(a_name + " do you want buy more products?(Y/N)"))
        else:
            print("sorry!! " + product + " is not available in our store.")
            print("\nChoose from following products please!")
            print("--------------------------------------------")
            print("PRODUCT\t\tPRICE\t\tQUANTITY")
            print("--------------------------------------------")
            for i in range(len(L)):
                print(L[i][0], "\t\t", L[i][1], "\t\t",
                      L[i][2])  # print, last updated product name, quantity and price.
            print("--------------------------------------------")

    print("\nYou Choosed Items and it's Quantity respectively:\n", q, "\n")

#Check the input and following code is applied

    f_amount = 0  # final amount
    for keys in q.keys():
        if keys == L[0][0].upper():  # executes this operation if product is phone entered by customer.
            p_price = int(L[0][1])
            p_num = int(q[keys])
            p_amount = (p_price * p_num)
            f_amount += (p_price * p_num)
            pst_amount=p_amount+p_amount*0.18
            ip=p_amount*0.18
            print("\nTotal cost for phone: ", p_amount)
        elif keys == L[1][0].upper():  # executes this operation if product is laptop entered by customer.
            l_price = int(L[1][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            lst_amount=l_amount+l_amount*0.18
            il=l_amount*0.18
            print("Total cost for laptop: ", l_amount)
        elif keys == L[2][0].upper():  # executes this operation if product is laptop entered by customer.
            h_price = int(L[2][1])
            h_num = int(q[keys])
            h_amount = (h_price * h_num)
            f_amount += (h_price * h_num)
            hst_amount=h_amount+h_amount*0.18
            ih=h_amount*0.18
            print("Total cost for HDD: ", h_amount)
        elif keys == L[3][0].upper():  # executes this operation if product is laptop entered by customer.
            c_price = int(L[3][1])
            c_num = int(q[keys])
            c_amount = (c_price * c_num)
            f_amount += (c_price * c_num)
            cst_amount=c_amount*c_amount*0.18
            ic=c_amount*0.18
            print("Total cost for CPU: ", c_amount)
        elif keys == L[4][0].upper():  # executes this operation if product is laptop entered by customer.
            r_price = int(L[4][1])
            r_num = int(q[keys])
            r_amount = (r_price * r_num)
            f_amount += (r_price * r_num)
            rst_amount=r_amount+r_amount*0.18
            ir=r_amount*0.18
            print("Total cost for RAM: ", r_amount)
        else:  # executes this operation if product is hdd entered by customer.
            s_price = int(L[5][1])
            s_num = int(q[keys])
            s_amount = (s_price * s_num)
            f_amount += (s_price * s_num)
            sst_amount=s_amount+s_amount*0.18
            ist=s_amount*0.18
            print("Total cost for SSD: ", s_amount)

#Calculation of GST

        st_amount=f_amount + f_amount*0.18
        gst=st_amount-f_amount
        print("GST : 18% ")
        print("Your payable amount is: ", st_amount)

####Creation of INVOICE####

#import datetime is used to get information for invoice

    import datetime  # import system date and time for create a unique invoive name.
    dt = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day) + "-" + str(datetime.datetime.now().hour) + "-" + str(
        datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second)
    invoice = str(dt)  # unique invoice
    t = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day)  # date
    d = str(t)  # date
    u = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(
        datetime.datetime.now().second)  # time
    e = str(u)  # time

    file = open(invoice + " (" + a_name + ").txt", "w")  # generate a unique invoive name and open it in write mode.
    file.write("==============================================================================")
    file.write("\nRANA ELECTRONIC STORE\t\t\t\tINVOICE")
    file.write("\n\nInvoice: " + invoice + "\t\tDate: " + d + "\n\t\t\t\t\tTime: " + e + "")
    file.write("\nName of Customer: " + str(a_name) + "")
    file.write("\n============================================================================")
    file.write("\nPARTICULAR\tQUANTITY\tUNIT PRICE\tGST(18%)\tTOTAL")
    file.write("\n----------------------------------------------------------------------------")

    name=a_name
    zz=d
    psql=q
    asql=st_amount
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "[mysql password]",
        database = "sales"
    )

    cursor = mydb.cursor()
    
    sql='insert into data(name,date,product,amount) values("{}","{}","{}","{}");'.format(name,zz,psql,asql)
    cursor.execute(sql)
    mydb.commit()

    for keys in q.keys():  # In this loop, write in a file only those product which is purchase by user.
        if keys == "PHONE":
            file.write(
                str("\n" + str(keys) + " \t\t " + str(q['PHONE']) + " \t\t " + str(L[0][1]) +" \t\t "+str(ip)+" \t\t" + str(pst_amount)))
        elif keys == "LAPTOP":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['LAPTOP']) + " \t\t " + str(L[1][1]) + " \t\t "+str(il)+" \t\t " + str(lst_amount)))
        elif keys == "HDD":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['HDD']) + " \t\t " + str(L[2][1]) +" \t\t "+str(ih)+ " \t\t " + str(hst_amount)))
        elif keys == "CPU":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['CPU']) + " \t\t " + str(L[3][1]) +" \t\t "+str(ic)+ " \t\t " + str(cst_amount)))
        elif keys == "RAM":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['RAM']) + " \t\t " + str(L[4][1]) +" \t\t "+str(ir)+ " \t\t " + str(rst_amount)))
        else:
            file.write(
                str("\n" + str(keys) + " \t\t " + str(q['SSD']) + " \t\t " + str(L[5][1]) +" \t\t "+str(ist)+ " \t\t " + str(sst_amount)))

    st_amount=f_amount + f_amount*0.18
    file.write("\n----------------------------------------------------------------------------")
    file.write("\n\t\t\t\t"+str(f_amount)+"\t\t"+str(gst)+"\t\t"+str(st_amount))
    file.write("\n----------------------------------------------------------------------------")
    file.write("\n\t\t\t TOTAL PAYABLE AMOUNT: " + str(st_amount))
    file.write("\n----------------------------------------------------------------------------")
    file.write("\n\n\t\t\tThank You " + a_name + " for your shopping.\n\t\t\t\tSee you again!")
    file.write("\n============================================================================")
    file.close()
    return q


# read_file is used to open and read product.txt 

def read_file():    # Function is defined with name : 'read_file'
    file = open("products.txt", "r")    # open stock file (products.txt) in read mode.
    lines = file.readlines()
    L = []  # assign empty list with name 'L'
    for line in lines:
        L.append(line.replace("\n", "").split(","))
    file.close()
    print("Following products are avilable in our Store")
    print("--------------------------------------------")
    print("PRODUCT\t\tPRICE\t\tQUANTITY")
    print("--------------------------------------------")
    for i in range(len(L)):
        print(L[i][0], "\t\t", L[i][1], "\t\t", L[i][2])    # prints the available product, price and quantity
    print("--------------------------------------------")
    return L

#over_write is used to update the product list in product.txt file

def over_write(List, Dictionary):   # an overwrite function
    L = List    # assign list with variable name 'L'
    d = Dictionary    # assign Dictionary with variable name 'd'
   
    for keys in d.keys():
        if keys == "PHONE":
            L[0][2] = str(int(L[0][2])-d['PHONE'])
        elif keys == "LAPTOP":
            L[1][2] = str(int(L[1][2])-d['LAPTOP'])
        elif keys == "HDD":
            L[2][2] = str(int(L[2][2])-d['HDD'])
        elif keys == "CPU":
            L[3][2] = str(int(L[3][2])-d['CPU'])
        elif keys == "RAM":
            L[4][2] = str(int(L[4][2])-d['RAM'])
        else:
            L[5][2] = str(int(L[5][2])-d['SSD'])
        
    files = open("products.txt", "w")  # opens stock file (products.txt) file in write mode.
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()
    return

#Main code displayed to the user

again = "Y"
while again.upper() == "Y":
    a = read_file()
    b = purchase(a)
    over_write(a, b)
    again = input("\nAre there any new customers waiting to buy product? ")
print("\nThank you for shopping from our store!!")
print("Please check your invoice for your shopping details, \nWhich we have created in .txt file format.")

#END
