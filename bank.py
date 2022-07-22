# new_user = input("Enter Your Name :")

bank=dict()
bank=bank.fromkeys({"Account No","Name","Mobile No","IFSC","Aadhar No"})

if bank.values() != None:
    new_user_name = input("Enter Your Name :")
    bank.update({"Name":new_user_name})
    new_user_num = input("Enter Your Mobile No :")
    bank.update({"Mobile No":new_user_num})
    new_user_aadhar = input("Enter Aadhar No :")
    bank.update({"bank.pyo":new_user_aadhar})
    bank.update({'Account No':id(new_user_name),'IFSC':'ABCD1234'})
    
    for i in bank:
        print(i,bank.get(i))
