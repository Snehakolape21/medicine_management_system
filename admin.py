# update() Method Redundancy: You're re-adding the same medicine object to the dictionary. It's valid, but maybe a better pattern would be to update only specific fields — unless full replacement is the goal (which is fine too!).

# Improve getall() Formatting: If no medicines exist, it could give a more informative message.


class medicineopration():
    def __init__(self):
        self.medicine={}

    def add(self,newmedicine): 
        self.medicine.update({newmedicine.id:newmedicine}) 
        print('medicine added successfully !!')  

    def update(self,medicine):  
        if medicine.id in self.medicine:  
            self.medicine.update({medicine.id:medicine})   
            print('medicine updated successfully !!') 
        else:
            print("Sorry! Please provide the valid medicine id")     
        

    def delete(self,medicineid): 
        if medicineid in self.medicine:     
            self.medicine.pop(medicineid)
            print("medicine deleted successfully")  
        else:
            print("Sorry! Please provide the valid medicine id") 
      

    def view(self,medicineid):
        if medicineid in self.medicine:
            print(self.medicine.get(medicineid))
        else: 
            print("ERROR ==> Sorry! Please provide the valid medicine id")
            
    def getall(self):
        for medicine in self.medicine.values():
            print(medicine)
       