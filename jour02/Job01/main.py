class Personne:
  def __init__(self, nom, prenom):
    self.nom = nom
    self.prenom = prenom

  def SePresenter(self):
    print("Bonjour mon nom est " + self.nom)
    print("Bonjour mon prénom est " + self.prenom)

  
  def get_nom(self):
        return self.nom

  def get_prenom(self):
        return self.prenom

  def set_nom(self, nom):
    self.nom = nom

  def set_prenom(self, prenom):
    self.prenom = prenom



p2 = Personne("Fauvel", "Grégory")
print("Prénom :", p2.get_prenom())
p2.set_prenom("Greg")    


p1.SePresenter()
p2.SePresenter()






    


