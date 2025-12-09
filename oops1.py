class employee:
    def __init__(self):
        self.id =123
        self.salary=50000
        self.designation="SDE"
#creating an obj\instance of the class 
    def travel(self,destination):
        print(f"Emplyoee is now travelling to {destination}")

sam=employee()


print(sam.id)
sam.travel('nkathmandu')
print(type(sam))