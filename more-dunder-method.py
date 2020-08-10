class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers

  def __len__(self):
    return(len(self.lawyers))

  def __contains__(self, lawyer):
    return(lawyer in self.lawyers)  

  def __iter__(self):
    return iter(self.lawyers)  
    
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])
print(len(d_and_p))
print("Donelli" in d_and_p)
iter_lst = iter(d_and_p) 
while True: 
    try: 
        print(iter_lst.__next__())  
    except: 
        break
