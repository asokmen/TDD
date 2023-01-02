class BANK:
    def __init__(self,user,password,total_money):
        self.user=user
        self.password=password
        self.total_money=total_money
     
    def bank_user_control(self,password,user_password):
        if(user_password==password):
            return True
            print("BANKAYA HOSGELDINIZ")
        else:
            return False

    def bank_transactions_choice(self):
        print("1-PARA CEKME")
        print("2 BAKIYE SORGULAMA")
        print("3 PARA YATIRMA")

        users_transactions_choice = int ( input ( "Lütfen işlemleri seçiniz: " ))
        if(users_transactions_choice==1):
            return 1
        elif(users_transactions_choice==2):
            return 2
        elif(users_transactions_choice==3):
            return 3

    def withdraw_money(self):
        user_withdraw_money = int ( input ( "Çekilecek Tutar: " ))
        self.total_money-=user_withdraw_money
        print('Sayın : {}'.format(self.user))
        print("kalan tutar:",self.total_money)
    
    def remainder_question(self):
        print('Bakiyeniz : {}'.format(self.total_money))

    def deposit_money(self):
        user_deposit_money = int ( input ( "Yatirilacak Tutar: " ))
        self.total_money+=user_deposit_money
        print('Sayin : {}'.format(self.user))
        print("kalan tutar:",self.total_money)
    


user_1=BANK(user="AYBUKE",password=1234,total_money=5000)        

user_password=int(input("4 haneli sifre gir:"))
if(user_1.bank_user_control(user_password,user_1.password)):
        if(user_1.bank_transactions_choice()==1):
            user_1.withdraw_money()
        elif(user_1.bank_transactions_choice()==2):
            user_1.remainder_question()
        elif(user_1.bank_transactions_choice()==3):
            user_1.deposit_money()
else:
    print("hata")


# *************************TEST****************************
import unittest

user_id=BANK(user="AYBUKE",password=1234,total_money=5000)     
user_withdraw_money = 200
user_deposit_money = 200

class TestMethods(unittest.TestCase):
    def test_bank_user(self):
        message="NAME OK"
        self.assertEquals(user_1.user,user_id.user,message)

    def test_bank_user_control(self):
        self.assertEquals(user_1.password, user_id.password)

    def test_withdraw_money(self):
        user_1.total_money-=user_withdraw_money
        self.assertGreaterEqual(user_1.total_money,user_id.total_money) #a=<b

    def test_remainder_question(self):
        self.assertGreaterEqual(user_1.total_money,user_id.total_money)#a>=b

    def test_deposit_money(self):
        user_1.total_money+=user_deposit_money
        self.assertGreater(user_1.total_money,user_id.total_money)

if __name__ == '__main__':
    unittest.main()