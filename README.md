# FaceAuVirus -- Outils de pistage et de gestion de l'épidémie Covid-19 

## Notre objectif
Donner au grand public et aux autorités sanitaires des outils de pistage et de gestion de l'épidémie, dans le plus grand respect des droits et des libertés fondamentales des citoyens.

## Pistage du Covid-19 -- avec anonymisation et chiffrage des données personnelles
Face au virus Covid-19 plusieurs pays tels que la [Chine](https://www.futura-sciences.com/tech/actualites/technologie-chine-debauche-technologies-faire-face-epidemie-coronavirus-79629/) ou [Singapour](https://www.tech.gov.sg/media/technews/tracetogether-behind-the-scenes-look-at-its-development-process) ont fait appel à la technologie pour faciliter le pistage des cas postifs pour une intervention rapide et efficace. Bien que ces applications ont été utiles, des questions se posent quant à la protection des données et des libertés individuelles. 

L'alternative, qui permettrait un gain en éfficacité dans la gestion de l'épidémie tout en garantissant les droits individuels, consiste à donner au grand public les outils nécessaire pour participer à ce processus, et lui permettre d'ouvrir ses données par consentement et lorsqu'il le souhaite. 

Le projet FaceAuVirus, lancé par des chercheurs en sciences du numérique de différentes spécialités, cherche à 
* mettre en place des procédures de collecte et de traitement des données nécessaires pour un système de pistage et de gestion complète de l'épidémie, 
* de faire en sorte que ces procédures permettent la collecte et les traitements de manière à ne pas compromettre les droits et les libertés individuels
* fournir des informations cléfs pour une gestion efficace face à l'épidémie.

Nous travaillons aujourd'hui sur trois axes complémentaires qui sont les suivants :


## Axe 1. Confidentialité, Anonymisation, Sécurité, et Inférence
Des applications comme [CovidWatch](https://www.covid-watch.org/) et [PrivateKit](https://privatekit.mit.edu/) cherchent à faire des citoyens les acteurs essentiels de la collecte et du traitement des données de localisation et de contact nécessaires au pistage et au control  de l'épidemie. 

Le point faible de ces applications, dans l'état actuel, est qu'elles font abstraction de comment et par quelles méthodes ces données peuvent être sécurisées et anonymisées -- lorse qu'elles seront transmises vers un serveur externe, tout en gardant la possibilité d'effectuer les simulations des modèles mathématiques de la façon la plus efficace possible. 

Dans cet axe, nous cherchons à mettre en place des algorithmes d'anonymisation qui permettront les inférences nécessaires d'une manière fiable.

## Axe 2. Identification des personnes immunisées, pour une sortie progressive du confinement
Face à la propagation du virus Covid-19, la France a été obligée d'appliquer des mesures de confinement strictes. Alors que  ces mesures sont nécessaires dans un premier temps, leur prolongement dans le temps risque d'engendrer des problèmes sociaux et économiques importants. 

Or, d'après l'état actuel de la connaissance sur le virus, nous [savons](https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200306-sitrep-46-covid-19.pdf?sfvrsn=96b04adf_2) que 80% des cas sont bénings et que 15% des cas de ne développent pas de complications majeures. Outre les effets de mutations possibles, ceci implique que 95% de la population peut sortir du confinement et contribuer ainsi à l'activité sociale et économique, avec un risque limité.

Objectif : Réaliser une estimation de la probabilité d’être immunisé sur la base d’informations clés disponibles. Cette estimation permettra alors de sélectionner les personnes à qui faire passer un test d’immunisation pour recruter le plus efficacement possible des volontaires immunisés.

## Axe 3. Réduction du risque d'exposition par proposition des trajectoires de tranche horaires

Nous proposons une composante de réduction d’exposition anticipée Covid19 par exemple dans les deux situations suivantes : l’exercice physique solitaire en extérieur (marche, jogging), et l’exercice des achats de première nécessité. Ces éléments sont particulièrement pertinents pendant les périodes de confinement, mais peuvent aussi jouer un rôle pendant les périodes intermédiaires.

En ce qui concerne l’exercice physique, il apparaît que le problème principal est de combattre la tendance des usagers à se retrouver dans les mêmes rues passantes et in fine se retrouver sous une plus grande exposition du virus. Pour cela, l’application donnerait des indications de trajets et d’horaire ou l’exposition serait moindre. Le bénéfice pour l’usager serait immédiat même s’il est le seul utilisateur car, somme toute, les rues passantes sont rares. Il y a 2900 km de voies piétonnes à Paris (pour prendre cet exemple), donc toute la population pourrait y déambuler 24h/24 avec plus d’1m d’espacement.  
S’il y a un nombre important d’utilisateurs de l’application les taux globaux d’exposition baisseront et les procédures de confinement seront encore plus efficace pour geler l’épidémie sans avoir à recourir au confinement total, lourd de conséquences.

L'application utilisera toutes les sources d'informations disponibles pour proposer des trajets et des plages horaires pouvant minimiser l'exposition des utilisateurs. En l'absence d'information, une première version utilisera le load balancing (équilibrage de débit) probabiliste entre les rues, ainsi qu'un load balancing temporel, et devrait déjà être efficace (à confirmer par simulation). L'ajout d'informations permettra d'affiner les propositions de trajets (en conservant une composante aléatoire pour répartir les personnes).


# Les grands principes

## Pistage participatif
Pour qu'un pistage participatif soit effectif, il en revient à la responsabilité de chacun.e de contribuer au système en soumettant ses données, notamment, s'il/elle a contracté le Covid-19. Ceci permettra au système de déterminer quelles autres personnes qui ont été à proximité du porteur.se sont sous risque de contraction. 

## Traitement des données personnelles - sur consentement explicite, de manière anonymisée et chiffrée
En aucun cas, le système ne révélera l'identité des personnes qui consentent à partager leurs données. Les données personnelles ne sont  collectées que sur consentement explicite de chaque utilisateur/rice. Les procédures d’anonymisation mis en place par les chercheurs compétents seront décrites et documentées.

## Logiciel en accès libre
Les algorithmes qui seront utilisés pour le traitement des données seront mis en accès libre, ce qui permet la vérification mais aussi l'amélioration. Ces algorithmes et les solutions logicielles annexes développées seront documentés convenablement, pour permettre une accésibilité totale. 


# Partenaires officiels
Health Data Hub, CNIL (à confirmer), APHP (à confirmer),...

# A propos de nous
FaceAuVirus est un projet proposé par les chercheur.se.s/enseignant-chercheur.se.s de l'Université PSL (MINES ParisTech, Dauphine),  d'Inria et du CNRS, qui sont spécialistes de la modélisation des épidémies, de la protection et l'anonymisation des données, du Machine Learning, et de la science citoyenne.

- Akin Kazakci, MINES ParisTech - PSL
- Igor Vujic, MINES ParisTech - PSL 
- Jamal Atif, Dauphine - PSL
- Laurent Massoulié, INRIA
- Philippe Jacquet, INRIA
- Aline Carneiro Viana, INRIA
- Cedric Adjih, INRIA
- Terrence Tran, MINES ParisTech - PSL
- Luca Ganassali, INRIA
- Raphael Pinot, Dauphine - PSL
- Yann Chevaleyre, Dauphine - PSL

# Join the conversation
Join the discussion at [FaceAuVirus.slack.com](https://join.slack.com/t/faceauvirus/shared_invite/zt-d7w8rbbq-OSEesNhV6vI0YhhSp6Nu6g)

# Contact Us
 [dataagainscorona@gmail.com](dataagainstcorona@gmail.com)
