# TUTOR-TPU-
Système d'apprentissage basé sur l'IA adaptatives et les modèles cognitifs 
# Cours sur l'IA Adaptative et les Modèles Cognitifs

## Cours 1 : Introduction à l'IA Adaptative  
L'IA adaptative se réfère aux systèmes capables de modifier leur comportement en fonction de nouvelles données.  
- Exemples : Systèmes de recommandation, assistants vocaux, etc.

---

## Cours 2 : Principes des Modèles Cognitifs  
Les modèles cognitifs visent à simuler le fonctionnement de la pensée humaine.  
- Exemples : ACT-R, SOAR, réseaux de neurones symboliques.

---

## Cours 3 : Applications combinées  
- Enseignement intelligent (tuteurs intelligents)  
- Interface cerveau-machine  
- Personnalisation dans les jeux et formations

---

## Exercice Pratique 1  
Créez une fonction Python qui simule une mémoire adaptative :

```python
memoire = {}

def ajouter_ou_mettre_a_jour(cle, valeur):
    memoire[cle] = valeur
    return memoire

# Exemple d’usage
print(ajouter_ou_mettre_a_jour('cours1', 'IA adaptative'))
def tuteur_intelligent(note):
    if note >= 15:
        return 'Très bien, continue comme ça !'
    elif note >= 10:
        return 'Pas mal, mais tu peux faire mieux.'
    else:
        return 'Révise le cours et essaie encore.'

# Exemple d’usage
for note in [18, 12, 7]:
    print(note, "→", tuteur_intelligent(note))
