# Profold
programmming Theory
case: Protein Pow(d)er

In deze case gaan wij aan de slag met een proteïne opgebouwd uit twee aminozuren: Hydrophobe (H) aminozuren en Polaire (P) aminozuren. Het doel is om de proteïne zo stabiel mogelijk in elkaar te vouwen. De stabiliteit in een proteïne wordt gecreëerd door H aminozuren naast elkaar 'te leggen'. Dat wil zeggen dat ze niet rechstreeks met elkaar verbinden zijn, maar wel aangrenzende posities naast elkaar bekleden. Wij zijn op zoek naar de 
lowest energy state van onze proteïne zodat deze zo stabiel mogelijk blijft. Door de (H) aminozuren naast elkaar te leggen scoort onze we -1 in onze stabiliteit P H en H P geven geen toevoeging aan onze stabiliteit.

Het doel voor deze case is om verschillende algoritmes te gebruiken en specifieke heuristieken toe te passen om tot de best vouwingen(folds) in onze proteins te komen.

## Getting Started
```command 
pip install numpy 1.18.5
pip install matplotlib 3.2.1
```
## Usage 
Type een integer tussen 1-4 om te kiezen welke string je wilt gebruiken, daarna voer je het algoritme wat je wilt gebruiken in.
```command
Example:
1: HHPHHHPHPHHHPH
2: HPHPPHHPHPPHPHHPPHPH
python main.py 1 greedy
python3 main.py 2 random
```
### Structuur

Hier kan men de structuur zien die wij hebben aangehouden bij ons project:

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor algoritmes
  - **/code/classes**: bevat de benodigde classes voor deze case
  - **/code/helpers**: bevat ondersteunende functies voor main
  - **/code/visualisation**: bevat de code voor de visualisatie

## Auteurs
- Tim huijsmans
- Ivo van der Zeyst
- Willem Steenstra Toussaint
