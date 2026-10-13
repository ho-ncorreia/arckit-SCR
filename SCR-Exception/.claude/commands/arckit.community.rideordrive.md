---
description: Génère une vision stratégique Ride-or-Drive à partir du contexte ArcKit
argument-hint: "<ID ou nom du projet>"
---

Tu es l'assistant ArcKit chargé de produire une vision stratégique Ride-or-Drive pour les déplacements domicile-travail.

## Entrée

```text
${input:topic:ID ou nom du projet}
```

## Objectif

Créer une vision stratégique à moyen/long terme qui définit comment l'organisation aide ses usagers à choisir entre vélo et voiture de façon sûre, explicable et compatible avec ses objectifs de mobilité durable. La météo peut éclairer un cas d'usage, mais une prévision d'une seule journée ne constitue pas une stratégie.

## Instructions

1. **Identifier le projet**
   - Utilise l'ID ou le nom fourni et le contexte ArcKit pour trouver le dossier projet correspondant.
   - Si le dossier n'existe pas et que l'utilisateur a fourni un ID, crée le dossier sous `projects/{PROJECT_ID}/` et utilise un nom de projet descriptif clairement marqué comme provisoire.
   - Ne réutilise pas `projects/000-global` comme dossier d'un projet nommé.

2. **Lire les éléments de contexte**
   - Lis `.arckit/templates-custom/rideordrive-template.md`.
   - Lis les artefacts disponibles du projet (vision, exigences, parties prenantes, stratégie, risques, politiques de déplacement, données de mobilité et objectifs carbone).
   - Utilise les principes et politiques d'entreprise réellement présents dans le dépôt. N'invente ni organisation, ni volumes, ni budget, ni objectifs approuvés.
   - Si le dossier est vide ou les preuves limitées, produis une première version de travail : identifie explicitement les hypothèses, les inconnues et les décisions à obtenir. Ne bloque pas sur des données absentes.

3. **Construire la vision stratégique**
   - Décris l'ambition, le problème métier, la valeur attendue, les principes, les résultats mesurables, les options stratégiques, l'état cible, les capacités, la gouvernance, les risques et une feuille de route par phases.
   - Compare au minimum le statu quo, une aide à la décision ponctuelle fondée sur la météo, et une capacité de mobilité intégrée à plus long terme.
   - Formule une recommandation progressive et justifie-la par les éléments disponibles; distingue les faits, les hypothèses et les propositions.
   - Traite la sécurité, l'accessibilité, la protection des données de localisation, la disponibilité des fournisseurs météo, les alertes officielles et les limites des prévisions comme des garde-fous stratégiques.
   - Mesure les émissions uniquement si une référence, des trajets, des modes et des facteurs d'émission sont disponibles. Sinon, définis les données à collecter et laisse les objectifs chiffrés à valider.
   - N'infère jamais l'état des routes ou pistes cyclables à partir de la météo. Ne transforme pas une recommandation quotidienne en garantie de sécurité.
   - Un exemple météo daté peut illustrer le fonctionnement, mais doit être identifié comme un instantané, sourcé, et séparé des objectifs de long terme.

4. **Rédiger le document**
   - Remplis `.arckit/templates-custom/rideordrive-template.md` comme structure de référence; conserve le marqueur `<!-- DOC-CONTROL-HEADER -->`.
   - Écris le livrable complet dans `projects/{PROJECT_ID}/ARC-{PROJECT_ID}-RODS-v1.0.md`.
   - Ne modifie pas le template lors de la génération.
   - Rédige en français, avec dates, unités, sources et liens vérifiables. Utilise `[À VALIDER]` pour les décisions non approuvées et une section explicite « Hypothèses et inconnues ».

5. **Restituer**
   - Après écriture, affiche uniquement un résumé de la vision, la recommandation stratégique, les principales hypothèses/décisions ouvertes et le chemin du document créé.
   - Ne reproduis pas le document complet dans la réponse.

## Identifiants

- ID d'artefact : `RODS` (Ride-or-Drive Strategy)
- Nom de sortie : `ARC-{PROJECT_ID}-RODS-v1.0.md`
- Commande : `/arckit-community.rideordrive`
