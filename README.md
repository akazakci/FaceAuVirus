# FaceAuVirus -- Pistage participatif du Covid-19 

## Notre objectif
Donner au grand public et aux autorités nationales des outils de pistage et de gestion de l'épidémie, dans le plus grand respect des droits et des libertés fondamentaux des citoyens.

## Pistage participatif -- avec anonymisation et chiffrage des données personnelles
Face au virus Covid-19 plusieurs pays tels que la [Chine](https://www.futura-sciences.com/tech/actualites/technologie-chine-debauche-technologies-faire-face-epidemie-coronavirus-79629/) ou le [Singapour](https://www.tech.gov.sg/media/technews/tracetogether-behind-the-scenes-look-at-its-development-process) ont fait appel à la technologie pour faciliter le pistage des cas postifs pour une intervention rapide et efficace. Bien que ces applications ont été utiles, des questions se posent quant à la protection des données et des libertés individuelles.

Le projet FaceAuVirus, lancé par des chercheurs en informatique,  système de pistage et de gestion complète. 

Nous travaillons aujourd'hui sur trois axes complémentaires qui sont les suivants:


## Axe 1. Confidentialité différentielle, Anonymisation et Inférence
A l'autre extrême du spectrum, des applications comme [CovidWatch](https://www.covid-watch.org/) et [PrivateKit](https://privatekit.mit.edu/) ont émergé. Ces applications cherchent à faire des citoyens des acteurs essentiels de la collecte et du traitement des données de localisation et de contact nécessaires au pistage et au control effective de l'épidemie. 

Le point faible de ces applications, dans l'état actuel, c'est qu'ils font abstraction de comment et par quelles méthodes ces données peuvent être sécurisés et anonymisés, tout en gardant la possibilité de faire des inférences effectives pour obtenir des informations pertinentes vis-à-vis de l'épidémie.

## Axe 2. Inférence des personnes immunisées, pour une relaxation progressive du confinement
Face à la propagation du virus Covid-19, la France a été obligé d'appliquer des mesures de confinement importantes. Alors que  la nécessité de ces mesures dans un premier temps paraissent nécessaires, leurs prolongements dans le temps vont créer d'autres problèmes sociaux et économique importants. 

Or, nous [savons](https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200306-sitrep-46-covid-19.pdf?sfvrsn=96b04adf_2) que %80 des cas sont béninges et que %15 des cas surmonte la maladie sans complications majeures. Outre les effets de mutations possible, ceci implique que %95 de la population peut sortir et continuer à leur vie et contribuer à l'activité sociale et économique, sans crainte.

Objectif : Réaliser une estimation de la probabilité d’être immunisé sur la base d’informations clés disponibles. Cette estimation permettra alors de sélectionner les personnes à qui faire passer un test d’immunisation pour recruter le plus efficacement possible des volontaires immunisés.

## Axe 3. Réduction du risque d'exposition par proposition des trajectoires de tranche horaires

Nous proposons une composante de réduction d’exposition anticipée Covid19 par exemple dans les deux situations suivantes : l’exercice physique solitaire en extérieur (marche, jogging), et l’exercice des achats de première nécessité. Ces éléments sont particulièrement pertinents pendant les périodes de confinement, mais peuvent aussi jouer un rôle pendant les périodes intermédiaires.

En ce qui concerne l’exercice physique, il apparaît que le problème principal est de combattre la tendance des usagers à se retrouver dans les mêmes rues passantes et in fine se retrouver sous une plus grande exposition du virus. Pour cela, l’application donnerait des indications de trajets et d’horaire ou l’exposition serait moindre. Le bénéfice pour l’usager serait immédiat même s’il est le seul utilisateur car, somme toute, les rues passantes sont rares. Il y a 2900 km de voies piétonnes à Paris (pour prendre cet exemple), donc toute la population pourrait y déambuler 24h/24 avec plus d’1m d’espacement.  
S’il y a un nombre important d’utilisateurs de l’application les taux globaux d’exposition baisseront et les procédures de confinement seront encore plus efficace pour geler l’épidémie sans avoir à recourir au confinement total, lourd de conséquences.

L'application utilisera toutes les sources d'informations disponibles pour proposer des trajets et des plages horaires pouvant minimiser l'exposition des utilisateurs. En l'absence d'information, une première version utilisera le load balancing (équilibrage de débit) probabiliste entre les rues, ainsi qu'un load balancing temporel, et devrait déjà être efficace (à confirmer par simulation). L'ajout d'informations permettra d'affiner les propositions de trajets (en conservant une composante aléatoire pour répartir les personnes).


# Les grands principes

## Pistage participatif
Une alternative à la collecte et au traitement centralisé des données personnelles par une autorité centrale  Il en revient à la responsabilité de chacun

Vos données seront accessibles et traitées que sur votre consentement explicit et éclairé

## Traitement des données personnelles - sur consentement explicit, de manière anonymisée et chiffrée
Les données personnelles ne devraient être collectées que sur consentement explicite de chaque utilisateur. Les procédures d’anonymisation mis en place par les chercheurs compétents devrait être décrites et documentées.

## Logiciel en accès libre
Les algorithmes qui seront utilisés pour le traitement des données devront être mis en accès libre en grande partie, ce qui permet la vérification mais aussi l'amélioration. Ces algorithmes et les solutions logiciels annexes développés devront être documenté convenablement, pour permettre un accésibilité total. 


# Partenaires officiels
Health Data Hub, APHP,...

# A propos de nous
FaceAuVirus est un projet proposé et lancé par les enseignant-chercheurs de MINES ParisTech et de l'INRIA, qui sont spécialiste de la modélisation des épidémies, de la protection et l'anonymisation des données et de la science citoyenne.

Les porteurs initiaux du projet sont:
-
-
-






# Join the conversation
Join the discussion at [dataagainstcorona.slack.com](corona-ml.slack.com)

# Contact US
Akin Kazakci: [dataagainscorona@gmail.com](dataagainstcorona@gmail.com)
