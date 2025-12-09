class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()


    def menu(self):
        user_input = input("""Welcome To Chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. press 2 to signin
                           3. press 3 to write a post
                           4. press 4 to message a friend 
                           5. press any other key to exit""")
        if user_input =='1':
            self.signup()
        elif user_input =='2':
            self.signin()
        elif user_input =='3':
            self.my_post()
        elif user_input =='4':
            self.send_msg()
        else:
            exit()

    def signup(self):
        email = input("enter your email here ->")
        password = input ("setup ur password here ->")
        self.username =email
        self.password= password
        print("You have signed up sucessfully!!")
        print("\n")
        self.menu()
    def signin(self):
        if self.username == '' and self.password=='':
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname=input("enter your emailor username here")
            password=input("enter your password here")
            if self.username==uname and self.password == password:
                print('you have sign in sucessfully')
                self.loggedin = True
            else:
                print("Please input the correct credential")
        print('\n')
        self.menu()

    def my_post(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            print(f"Following content has been posted -> {txt}")
         
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()
    def send_msg(self):
        if self.loggedin == True:
            txt=input("Enter your msg here")
            frnd= input("whom to send the msg")
            print(f"Your msg has been sent to {frnd}")
        else:
            print("You need to signin first to post smthing ")
        print('\n')
        self.menu()    



obj=chatbook()