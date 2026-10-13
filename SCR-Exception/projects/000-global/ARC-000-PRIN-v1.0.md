# Principes d'architecture CMA CGM — Domaine Client

> **Template Origin**: Generated | **ArcKit Version**: 6.18.2 | **Command**: `/arckit-principles`

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ARC-000-PRIN-v1.0 |
| **Document Type** | Architecture Principles — Customer Domain |
| **Project** | CMA CGM Customer Domain (Project 000) |
| **Classification** | OFFICIAL |
| **Status** | DRAFT |
| **Version** | 1.0 |
| **Created Date** | 2026-10-13 |
| **Last Modified** | 2026-10-13 |
| **Review Cycle** | Annual |
| **Next Review Date** | 2027-10-13 |
| **Owner** | <TO OBTAIN — propriétaire du PRIN et rôle · owner: EA Domaine Client> |
| **Reviewed By** | [PENDING] |
| **Approved By** | [PENDING] |
| **Distribution** | CMA CGM Enterprise Architecture — Domaine Client; revue à confirmer |

## Revision History

| Version | Date | Author | Changes | Approved By | Approval Date |
|---------|------|--------|---------|-------------|---------------|
| 1.0 | 2026-10-13 | ArcKit AI | Première version proposée à partir des deux référentiels Client présents dans `projects/000-global/external/`. | [PENDING] | [PENDING] |

---

## Executive Summary

Ce document propose les principes d'architecture du domaine Client CMA CGM, couvrant les parcours et capacités de Booking, Documentation, Invoicing, Pricing, Customer Care, Sales/CRM et Value-Added Services (VAS). Le référentiel fourni indique que ces domaines sont associés aux clés Ardoq OR-1048, OR-1058 et OR-1072; ces libellés et clés sont repris comme éléments de source et doivent être revalidés dans Ardoq avant ratification [CCCP-C3].

Le statut est **DRAFT**. Le référentiel de domaine précise qu'il s'agit d'une connaissance d'entrée et non d'une politique automatiquement approuvée [CCCAP-C1]. Les principes CUST-001 à CUST-016 sont conservés depuis la référence principale; les candidats PR-CUST-01 à PR-CUST-14 du second référentiel sont intégrés ou tracés dans la correspondance, sans transformer ses propositions en faits d'environnement. Les valeurs organisationnelles absentes restent explicitement à obtenir [CCCAP-C2] [CCCP-C1].

Ces principes guident les décisions d'architecture; ils ne prescrivent pas de produit, de fournisseur, de plateforme cloud, de langage ou de technologie. Toute exception doit avoir un propriétaire, une justification, des contrôles compensatoires, une date d'expiration et un plan de sortie. L'approbation de l'Architecture Review Board et les rôles de validation restent à confirmer.

**Portée** : domaine Client CMA CGM; les autres domaines et les obligations de groupe non documentées ne sont pas définis par ce PRIN.  
**Autorité** : proposition pour revue par Enterprise Architecture, les responsables métier et les fonctions sécurité, data, privacy et opérations.  
**Classification** : `OFFICIAL` est utilisé comme valeur de la classification générique du rendu ArcKit; le référentiel source porte le marquage `Internal`, dont l'équivalence doit être confirmée par le propriétaire de la classification.

## I. Principes stratégiques

### CUST-001 — Priorité au parcours client, responsabilité explicite des domaines

**Catégorie** : Business / Application  
**Énoncé** : Les solutions MUST optimiser le parcours client de bout en bout tout en conservant une responsabilité explicite, unique et vérifiable pour chaque capacité, règle et transaction métier [CCCAP-C2].

**Justification** : Un parcours peut traverser Sales, Pricing, Booking, Documentation, Invoicing, Care et VAS. Une expérience cohérente ne doit pas transférer implicitement la responsabilité d'exécution métier à un canal ou à une couche centrale.

**Implications** :
- Chaque étape, objet métier, décision et résultat possède un domaine responsable.
- Les canaux peuvent coordonner l'expérience mais ne dupliquent pas les règles métier des domaines.
- Les responsabilités de données, applications, plateformes et processus sont distinguées.

**Contrôles de conformité** :
- [ ] Les capacités du parcours et leurs propriétaires sont documentés.
- [ ] Les responsabilités des canaux et domaines sont séparées.
- [ ] Les transferts, décisions et résultats inter-domaines sont traçables.

**Ancrage** : CUST-001 dans la référence principale; proposition PR-CUST-02 dans la référence candidate.  
**Exceptions** : Une orchestration transitoire exige un propriétaire et une trajectoire approuvée vers la cible.  
**S'applique à** : Tous les domaines Client.

### CUST-002 — Cohérence omnicanale

**Catégorie** : Business / Application  
**Énoncé** : Des intentions client équivalentes MUST produire des résultats métier cohérents quel que soit le canal d'origine, sauf différence justifiée, documentée et autorisée [CCCAP-C2].

**Justification** : Des règles spécifiques à chaque canal créent des traitements divergents, des duplications et des résultats imprévisibles.

**Implications** :
- Les requêtes de canaux différents convergent vers des capacités et contrats métier gouvernés.
- La provenance du canal peut être conservée pour la traçabilité sans modifier les règles métier par défaut.
- Les modules d'interface peuvent évoluer séparément, sous réserve d'interfaces explicites et d'une gouvernance de cohérence; l'usage de micro-frontends reste une option à justifier, pas une obligation.

**Contrôles de conformité** :
- [ ] Une intention équivalente est reliée à la même capacité métier.
- [ ] Les variations par canal ont une justification et un propriétaire.
- [ ] Les statuts et erreurs sont compréhensibles et cohérents entre canaux.

**Ancrage** : CUST-002; proposition PR-CUST-03.  
**Exceptions** : Une contrainte légale, contractuelle, de sécurité ou d'exploitation peut justifier une variation contrôlée.  
**S'applique à** : Booking, Documentation, Invoicing, Pricing, Care, Sales/CRM et VAS.

### CUST-009 — Standard global, variation locale contrôlée

**Catégorie** : Business / Governance  
**Énoncé** : Les capacités du domaine SHOULD suivre des processus et contrats globaux; les variations locales MUST être justifiées par un besoin vérifié, externalisées, traçables et limitées à ce besoin [CCCAP-C2] [CCCP-C1].

**Justification** : Les adaptations non gouvernées augmentent la divergence et le coût d'évolution, alors que certaines obligations locales peuvent nécessiter une variation légitime.

**Implications** :
- Le processus global est défini avant les variations.
- Chaque variation indique juridiction ou contexte, motif, propriétaire, période de validité et tests.
- Les exigences légales, fiscales, douanières, contractuelles ou opérationnelles doivent être confirmées par leurs responsables; elles ne sont pas déduites de ce principe.

**Contrôles de conformité** :
- [ ] La base globale est documentée.
- [ ] Chaque variation a une source et un propriétaire.
- [ ] Les règles locales sont versionnées et révisables.
- [ ] Les variations expirées sont détectables.

**Ancrage** : CUST-009.  
**Exceptions** : Une variation locale durable exige une décision d'architecture et un examen périodique.  
**S'applique à** : Tous les domaines Client.

### CUST-010 — Automatisation avec contrôle humain explicite

**Catégorie** : Business / Application  
**Énoncé** : L'automatisation SHOULD réduire les tâches répétitives; les cas incertains, à risque élevé, exceptionnels ou réglementés MUST être dirigés vers une revue humaine contrôlée, avec motif et éléments de preuve [CCCAP-C2].

**Justification** : Les décisions de booking, documentation, facturation, pricing, care et VAS peuvent avoir des conséquences opérationnelles, financières, juridiques ou client.

**Implications** :
- Les critères d'éligibilité, de confiance, de validation et de repli sont approuvés et testables.
- Un échec ne perd pas silencieusement la demande et expose un statut compréhensible.
- Le réviseur dispose du contexte nécessaire pour accepter, corriger ou rejeter le résultat.
- Une décision autonome exige une acceptation explicite du risque et une preuve de sa pertinence.

**Contrôles de conformité** :
- [ ] Les parcours automatique et manuel sont conçus.
- [ ] Les seuils et exceptions sont approuvés par un responsable.
- [ ] Les erreurs et reprises sont traçables.
- [ ] Les interventions humaines sont auditées.

**Ancrage** : CUST-010.  
**Exceptions** : Aucune exception ne peut supprimer les obligations légales ou les contrôles obligatoires.  
**S'applique à** : Tous les domaines Client, notamment les automatisations et recommandations.

### CUST-011 — VAS comme capacités produit réutilisables

**Catégorie** : Business / Application  
**Énoncé** : Les Value-Added Services MUST être gouvernés comme des capacités produit réutilisables couvrant catalogue, classification, éligibilité, applicabilité, prix, recommandation, vente, exécution, facturation et reporting [CCCAP-C2].

**Justification** : Un modèle partagé réduit la duplication des définitions et permet une traçabilité cohérente de la découverte à la facturation.

**Implications** :
- Les propriétaires du catalogue et des règles VAS sont identifiés.
- Recommandation, éligibilité, prix, exécution et comptabilisation ont des responsabilités distinctes.
- Les définitions produit, codes de charge et relations de revenus sont gouvernés.
- L'inventaire des applications VAS reste à confirmer; aucune application n'est désignée ici comme autorité.

**Contrôles de conformité** :
- [ ] Une définition gouvernée est réutilisée entre canaux.
- [ ] Éligibilité, prix, vente et exécution sont traçables.
- [ ] Les correspondances produit et facturation ont un propriétaire.
- [ ] Les bundles et partages de revenus ont des règles explicites.

**Ancrage** : CUST-011; la référence candidate signale que les applications de vente VAS restent à obtenir [CCCP-C2].  
**Exceptions** : Un pilote local doit rester borné et ne pas devenir un référentiel parallèle.  
**S'applique à** : Sales/CRM, Pricing, Booking, Invoicing, Care et VAS.

### CUST-012 — Autorité du pricing et traçabilité du devis à la facture

**Catégorie** : Business / Data  
**Énoncé** : Les décisions de tarification MUST provenir de la capacité Pricing faisant autorité; la base commerciale MUST rester traçable du devis et du contrat jusqu'au booking, aux charges et à la facture [CCCAP-C2].

**Justification** : Une logique tarifaire dupliquée peut créer incohérences, litiges et erreurs de facturation.

**Implications** :
- Les canaux et domaines consommateurs ne réimplémentent pas les calculs tarifaires de référence.
- Les caches dérivés définissent fraîcheur, expiration et réconciliation.
- Les dérogations et ajustements sont autorisés et audités.
- Les systèmes faisant autorité et les règles de pricing concrètes restent à identifier.

**Contrôles de conformité** :
- [ ] Chaque composant de prix possède une source et un propriétaire désignés.
- [ ] Les dérogations sont approuvées et auditables.
- [ ] Booking, devis/contrat et facture sont reliés par une trace vérifiable.
- [ ] Le traitement tarifaire des VAS est documenté.

**Ancrage** : CUST-012; candidat PR-CUST-08 sur la gouvernance des données de référence.  
**Exceptions** : Un mode déconnecté exige une durée de validité bornée et une réconciliation après reprise.  
**S'applique à** : Pricing, Sales/CRM, Booking, Invoicing et VAS.

## II. Principes de données

### CUST-006 — Source faisant autorité et propriété unique des données métier

**Catégorie** : Data  
**Énoncé** : Chaque objet métier critique et chaque jeu de règles MUST avoir une source faisant autorité déclarée et un propriétaire responsable; les copies sont dérivées, en lecture seule ou synchronisées selon un mécanisme gouverné [CCCAP-C2].

**Justification** : Des sources maîtres multiples et modifiables créent des incohérences et des réconciliations coûteuses.

**Implications** :
- Les documents d'architecture distinguent système de référence, système d'engagement, copie analytique, cache et vue de reporting.
- Les consommateurs utilisent les interfaces ou produits de données approuvés.
- Aucun produit ou référentiel nommé dans la source candidate, notamment MyCDM, n'est déclaré comme autorité actuelle avant confirmation par les propriétaires [CCCP-C1].
- L'extraction analytique sépare les données sources des transformations métier; les responsabilités de transformation sont documentées.

**Contrôles de conformité** :
- [ ] Chaque objet critique a une source et un steward.
- [ ] Les droits de mise à jour sont explicites.
- [ ] Les copies dérivées ont des contrôles de fraîcheur et de rapprochement.
- [ ] Les flux analytiques ont une provenance documentée.

**Ancrage** : CUST-006; candidats PR-CUST-08 et PR-CUST-09; patterns P5, P6 et P7 sont cités dans la référence d'entrée et restent à revalider auprès de leurs propriétaires [CCCP-C4].  
**Exceptions** : Une coexistence transitoire exige des règles de résolution de conflits, un propriétaire et une date de sortie.  
**S'applique à** : Tous les domaines Client, notamment Pricing, Customer Profile, Booking, Invoicing et VAS.

### CUST-007 — Cohérence du profil client et des parties

**Catégorie** : Data / Application  
**Énoncé** : Les identités de client, partenaire, payeur, expéditeur, destinataire et parties associées MUST s'appuyer sur des identifiants gouvernés ou des correspondances approuvées dans les processus du domaine [CCCAP-C2].

**Justification** : L'identification fiable des parties soutient devis, booking, documents, facturation, care, contrôles et éligibilité VAS.

**Implications** :
- Les copies locales conservent le lien avec l'identifiant gouverné.
- Les règles de rapprochement, seuils et cas ambigus sont explicites et vérifiables.
- Une correspondance incertaine est dirigée vers une revue humaine.
- Les noms et capacités des applications Customer Profile mentionnés dans les sources restent des assertions de ces sources jusqu'à validation live [CCCP-C3].

**Contrôles de conformité** :
- [ ] L'identifiant de référence est utilisé ou mappé.
- [ ] Les correspondances ambiguës ne sont pas acceptées silencieusement.
- [ ] Les relations de parties sont vérifiées pour les autorisations.

**Ancrage** : CUST-007; application Customer Profile AP-27735 citée par le document d'entrée, à revalider dans Ardoq [CCCP-C3].  
**Exceptions** : Les identifiants légaux locaux peuvent compléter, mais ne remplacent pas, le lien vers l'identifiant gouverné.  
**S'applique à** : Booking, Documentation, Invoicing, Care, Sales/CRM, Pricing et VAS.

### CUST-008 — Sécurité, vie privée et confidentialité commerciale dès la conception

**Catégorie** : Data / Technology  
**Énoncé** : L'identité, les accès, la vie privée, la confidentialité commerciale, la prévention de fraude, la séparation des tâches et l'audit MUST être pris en compte dès la conception et appliqués selon les politiques approuvées [CCCAP-C2].

**Justification** : Le périmètre peut traiter des données client, commerciales, contractuelles, documentaires, de paiement ou de tarification; les classifications et obligations précises doivent être confirmées.

**Implications** :
- Les accès suivent le moindre privilège et une finalité métier autorisée.
- Les API vérifient l'autorisation sur l'objet concerné, pas seulement l'identité du demandeur.
- Les données personnelles et commerciales sont minimisées dans les flux, journaux, événements, prompts et jeux de test.
- Les classifications, règles de résidence, durées de conservation et bases légales restent à obtenir auprès des responsables compétents [CCCP-C2].

**Contrôles de conformité** :
- [ ] Authentification et autorisation sont distinctes.
- [ ] Les contrôles d'accès objet sont testés.
- [ ] Les données sensibles sont protégées selon une politique approuvée.
- [ ] Les actions privilégiées et financières sont auditables.

**Ancrage** : CUST-008; candidat PR-CUST-10; le pattern P3 est cité comme ancrage de sécurité dans la source candidate, sans revalidation du référentiel PSL [CCCP-C4].  
**Exceptions** : Aucune dérogation ne peut contourner une obligation légale ou un contrôle obligatoire; les autres écarts exigent approbation sécurité et mesures compensatoires.  
**S'applique à** : Tous les domaines Client.

### CUST-013 — Intégrité réglementaire et cycle de vie documentaire

**Catégorie** : Data / Application  
**Énoncé** : Les documents client, factures, instructions et éléments de preuve MUST préserver intégrité, provenance, version, statut juridique et exigences de conservation définies par les responsables compétents [CCCAP-C2].

**Justification** : Les artefacts documentaires peuvent porter des obligations contractuelles, douanières, fiscales, commerciales ou financières; leur applicabilité doit être confirmée selon le contexte.

**Implications** :
- Les états brouillon, émis, amendé, annulé et archivé sont distincts.
- Les documents produits à partir de données et modèles contrôlés sont reproductibles lorsque requis.
- Les modifications conservent un historique d'audit.
- Les règles de conservation et de gel juridique sont obtenues auprès des propriétaires; elles ne sont pas inventées.

**Contrôles de conformité** :
- [ ] Le statut et la version du document sont explicites.
- [ ] Les données d'origine et la version du modèle sont traçables.
- [ ] Les amendements ne détruisent pas l'historique.
- [ ] Les règles d'accès et de conservation sont documentées.

**Ancrage** : CUST-013; périmètre documentaire du domaine dans les deux référentiels [CCCAP-C2] [CCCP-C3].  
**Exceptions** : Aucune dérogation ne peut supprimer une exigence obligatoire d'intégrité ou de conservation.  
**S'applique à** : Documentation, Invoicing, Booking et Care.

## III. Principes d'intégration

### CUST-003 — Contrats de domaine plutôt qu'implémentations internes

**Catégorie** : Application / Integration  
**Énoncé** : Les domaines MUST exposer leurs capacités par des contrats gouvernés; les consommateurs MUST NOT dépendre directement des bases de données, moteurs de workflow ou composants internes d'un autre domaine [CCCAP-C2].

**Justification** : Des contrats stables réduisent le couplage et permettent aux domaines de faire évoluer leurs implémentations indépendamment.

**Implications** :
- Le domaine fournisseur possède la sémantique, la version et le cycle de vie du contrat.
- Le choix API, événement ou autre interaction dépend du besoin métier.
- Les middlewares peuvent transformer les formats et protocoles, mais ne portent pas de logique métier.
- Les transformations et adaptateurs vers les progiciels sont documentés; les patterns spécifiques proposés (dont SAP, IAM ou Private Link) restent à confirmer avant toute prescription [CCCP-C4].

**Contrôles de conformité** :
- [ ] Le propriétaire du contrat est identifié.
- [ ] Versionnement, compatibilité et dépréciation sont définis.
- [ ] Aucun accès direct non approuvé à une base ou un moteur interne n'est créé.
- [ ] Les règles métier restent dans le domaine responsable.

**Ancrage** : CUST-003; candidats PR-CUST-01, PR-CUST-04 et PR-CUST-07; patterns P1 et P3 cités comme propositions de référence [CCCP-C4].  
**Exceptions** : Une intégration legacy temporaire doit avoir un risque accepté, un propriétaire et un plan de retrait.  
**S'applique à** : Tous les domaines et consommateurs client.

### CUST-004 — Événements métier pour les changements d'état inter-domaines

**Catégorie** : Integration / Application  
**Énoncé** : Les changements d'état métier inter-domaines SHOULD être publiés sous forme d'événements gouvernés lorsque découplage, diffusion asynchrone ou plusieurs consommateurs le justifient [CCCAP-C2].

**Justification** : Les événements peuvent permettre aux domaines de partager les faits métier sans dépendre de l'implémentation des producteurs.

**Implications** :
- Un événement exprime un fait ou une demande métier, pas une simple mise à jour technique.
- Le producteur possède la sémantique; les consommateurs possèdent leurs réactions.
- Ordre, livraison, idempotence, rejeu, rétention et erreurs sont décidés par flux.
- Le synchrone reste valable lorsque l'appelant exige une réponse immédiate et autoritaire.

**Contrôles de conformité** :
- [ ] Le schéma et le propriétaire de l'événement sont documentés.
- [ ] Les doublons, retards, erreurs et rejeux sont traités.
- [ ] Les données sensibles sont minimisées.
- [ ] La surveillance et la reprise sont définies.

**Ancrage** : CUST-004; candidat PR-CUST-05; pattern P4 cité dans la référence candidate et à revalider par le propriétaire PSL [CCCP-C4].  
**Exceptions** : Une interaction synchrone est appropriée si une réponse immédiate est nécessaire.  
**S'applique à** : Tous les domaines Client.

### CUST-005 — Corrélation et audit de bout en bout

**Catégorie** : Application / Integration  
**Énoncé** : Toute demande client traversant plusieurs systèmes ou domaines MUST porter une référence de corrélation permettant de relier intake, exécution, statut, intervention humaine et clôture [CCCAP-C2].

**Justification** : La traçabilité soutient le service client, l'exploitation, l'audit et l'analyse des incidents.

**Implications** :
- Les identifiants locaux sont reliés à une référence de parcours contrôlée.
- Les journaux et événements reconstruisent le parcours sans exposer de données inutiles.
- La conservation et les règles de corrélation sont alignées aux politiques approuvées.

**Contrôles de conformité** :
- [ ] La corrélation démarre à un point d'entrée contrôlé.
- [ ] Les composants participants propagent ou associent la référence.
- [ ] Les équipes de support peuvent reconstruire le parcours autorisé.

**Ancrage** : CUST-005; candidat PR-CUST-13 sur la documentation et la traçabilité des actifs.  
**Exceptions** : Un système legacy incapable de propager la référence nécessite un mapping et un plan de sortie.  
**S'applique à** : Tous les domaines Client.

## IV. Qualités opérationnelles

### CUST-014 — Résilience proportionnée à l'impact client et opérationnel

**Catégorie** : Technology / Quality  
**Énoncé** : Les besoins de disponibilité, performance, reprise et continuité MUST être déterminés à partir de l'impact métier et de la criticité opérationnelle, puis approuvés par les responsables [CCCAP-C2].

**Justification** : Une interruption peut affecter des parcours, opérations, obligations ou revenus; les niveaux de service propres à ces processus ne sont pas documentés dans les sources consultées [CCCP-C2].

**Implications** :
- Les parcours critiques, périodes de charge et dépendances sont identifiés.
- Les modes dégradés, files, délais, reprises et dépendances sont explicites.
- Les valeurs RTO, RPO, SLA et volumes restent des placeholders jusqu'à validation.
- L'infrastructure reproductible et les pratiques de reprise peuvent être évaluées, sans imposer un fournisseur ou un outil.

**Contrôles de conformité** :
- [ ] Les parcours métier critiques sont priorisés.
- [ ] Le comportement lors de l'échec d'une dépendance est défini.
- [ ] Des preuves de charge et de résilience sont disponibles.
- [ ] Les objectifs de reprise sont approuvés et testés.

**Ancrage** : CUST-014; candidats PR-CUST-06 et PR-CUST-11.  
**Exceptions** : Une résilience réduite temporaire exige une acceptation de risque et une date de remédiation.  
**S'applique à** : Tous les domaines Client.

### CUST-015 — Observabilité en termes métier

**Catégorie** : Technology / Quality  
**Énoncé** : Les services MUST fournir une observabilité technique et métier permettant de suivre progression, erreurs, reprises, résultats d'automatisation et impacts client [CCCAP-C2].

**Justification** : La santé technique seule ne confirme pas que bookings, documents, factures, demandes ou commandes VAS aboutissent.

**Implications** :
- La télémétrie relie les états métier aux références de corrélation.
- Les alertes désignent un propriétaire et une action opérationnelle.
- Les indicateurs évitent les données personnelles ou commerciales non nécessaires.
- Les produits d'observabilité nommés dans les propositions candidates ne sont pas imposés et doivent être confirmés par les standards d'entreprise [CCCP-C1].

**Contrôles de conformité** :
- [ ] Succès et échec métier sont mesurables.
- [ ] Les alertes ont un propriétaire, une sévérité et un runbook.
- [ ] Les parcours inter-domaines sont traçables.
- [ ] Les files manuelles et automatisées sont observées.

**Ancrage** : CUST-015; candidats PR-CUST-11 et PR-CUST-13.  
**Exceptions** : La profondeur peut être déployée par phase, avec plan approuvé pour les services critiques.  
**S'applique à** : Tous les domaines Client.

## V. Pratiques de développement et de gouvernance

### CUST-016 — Réutiliser avant de construire, simplifier avant d'automatiser

**Catégorie** : Governance / Development  
**Énoncé** : Les équipes MUST évaluer les capacités, contrats, plateformes et services partagés existants avant de créer un composant; les processus SHOULD être simplifiés avant automatisation [CCCAP-C2].

**Justification** : La duplication locale augmente les coûts, incohérences et charges de support.

**Implications** :
- Les décisions build, buy, reuse ou retire documentent les options et leur adéquation.
- L'automatisation ne conserve pas par défaut une complexité évitable.
- La réutilisation est évaluée contre besoins fonctionnels, sécurité, performance et cycle de vie.
- Les patterns PSL sont des références proposées dans le document d'entrée; leur version et leur applicabilité doivent être validées avant adoption [CCCP-C4].

**Contrôles de conformité** :
- [ ] Les capacités existantes sont évaluées.
- [ ] La duplication est justifiée par une contrainte mesurable.
- [ ] La simplification du processus est examinée.
- [ ] La propriété et le support du composant sont définis.

**Ancrage** : CUST-016; candidat PR-CUST-14.  
**Exceptions** : Un composant tactique doit avoir un propriétaire et une trajectoire de convergence ou de retrait.  
**S'applique à** : Tous les domaines Client.

### PR-CUST-11 — Déploiement automatisé et maîtrisé

**Catégorie** : Technology / Development — principe proposé, non ratifié  
**Énoncé proposé** : Les nouvelles capacités SHOULD être déployées sur des environnements approuvés par CMA CGM et SHOULD utiliser des processus reproductibles, versionnés et contrôlés pour leur configuration et leur exploitation [CCCP-C1].

**Justification** : La répétabilité, l'audit et la maîtrise opérationnelle sont des objectifs de conception proposés; les clouds autorisés, outils, normes et contrôles effectifs restent à obtenir.

**Implications** :
- Confirmer les environnements cloud autorisés et leurs propriétaires avant de les prescrire.
- Évaluer l'automatisation de l'infrastructure, les revues de changement, la reprise et l'observabilité.
- Ne pas traiter Terraform, AWS, Private Link ou un produit cité dans un candidat comme standard approuvé sans confirmation [CCCP-C1].

**Contrôles de conformité** :
- [ ] Les environnements autorisés sont référencés par une source approuvée.
- [ ] Les changements sont traçables et reproductibles.
- [ ] Les exigences de reprise et de surveillance sont approuvées.

**Ancrage** : candidat PR-CUST-11; détails d'environnement explicitement à obtenir [CCCP-C1] [CCCP-C2].  
**Exceptions** : À définir après validation du standard de déploiement applicable.  
**S'applique à** : Capacités applicatives et plateformes du domaine Client.

### PR-CUST-12 — Coût et usage des ressources comme attributs de conception

**Catégorie** : Business / Technology — principe proposé, non ratifié  
**Énoncé proposé** : Les décisions d'architecture SHOULD considérer et suivre les coûts de cycle de vie et l'usage des ressources, avec une attribution et des revues adaptées à la gouvernance financière approuvée [CCCP-C1].

**Justification** : Une évaluation explicite du coût peut soutenir des arbitrages durables; aucun budget, modèle de refacturation, seuil ou objectif d'économie n'est fourni [CCCP-C2].

**Implications** :
- Documenter les principaux coûts et hypothèses dans les options d'architecture.
- Définir avec Finance les règles d'attribution, de seuil et de fréquence avant de les rendre obligatoires.
- Éviter toute cible d'économie ou économie estimée sans baseline vérifiable.

**Contrôles de conformité** :
- [ ] Les coûts et hypothèses significatifs sont documentés.
- [ ] Les propriétaires financiers et règles d'attribution sont confirmés.
- [ ] Toute cible est approuvée et mesurable.

**Ancrage** : candidat PR-CUST-12; FinOps Operating Model et Right-Sizing sont cités par la source candidate comme références à vérifier [CCCP-C4].  
**Exceptions** : Une analyse détaillée peut être proportionnée à la matérialité du changement, selon des seuils à valider.  
**S'applique à** : Décisions d'investissement et d'exploitation du domaine Client.

## VI. Principes de données — complément domaine

### CUST-017 — Analytique gouvernée et extraction sans logique métier

**Catégorie** : Data / Integration — proposition issue du référentiel candidat  
**Énoncé proposé** : Les usages analytiques SHOULD séparer extraction, transformation et consommation; les transformations métier MUST rester dans des capacités gouvernées plutôt que d'être cachées dans un flux d'extraction [CCCP-C1].

**Justification** : La séparation des responsabilités aide à préserver provenance, qualité et cohérence des données.

**Implications** :
- Cartographier source, transformations, destinations, owners et usages.
- Confirmer la plateforme analytique et les patterns autorisés avant de les nommer.
- Protéger les systèmes opérationnels contre les extractions non maîtrisées.

**Contrôles de conformité** :
- [ ] Les flux et transformations sont documentés.
- [ ] Les transformations métier ont un propriétaire.
- [ ] Les usages et accès analytiques sont autorisés.

**Ancrage** : candidat PR-CUST-09; pattern P7 et Reverse ETL mentionnés dans la référence candidate, à valider [CCCP-C4].  
**Exceptions** : Toute transformation exceptionnelle doit être documentée, limitée et revue.  
**S'applique à** : Échanges entre données opérationnelles et analytiques du domaine Client.

## VII. Processus d'exception

Une dérogation à un principe nécessite une justification métier ou technique, les options examinées, une évaluation du risque, des contrôles compensatoires, un responsable, une date d'expiration et un plan de remédiation. Le forum d'approbation et les seuils de décision restent à obtenir; aucune instance n'est réputée approuvée par ce document [CCCAP-C2] [CCCP-C2].

### Informations minimales d'une demande

- Principe et contrôle concernés, avec preuves de l'écart.
- Motif et durée; conséquences pour les clients, opérations, données et sécurité.
- Options de conformité examinées et justification du choix.
- Mesures compensatoires, risque résiduel, owner et échéance.
- Autorité approbatrice à confirmer selon la gouvernance applicable.

### Cycle de vie

1. Le responsable du projet documente la demande et les preuves.
2. Les responsables architecture, métier, données, sécurité et autres fonctions concernées l'examinent.
3. L'autorité compétente, une fois confirmée, approuve, rejette ou demande des compléments.
4. L'exception approuvée est inscrite au registre du projet et revue avant expiration.
5. La clôture vérifie la remédiation ou renouvelle l'exception par nouvelle décision.

## VIII. Gouvernance et conformité

### Portes de revue proposées

**Cadrage**
- [ ] Périmètre, capacités, parties prenantes et propriétaires identifiés.
- [ ] Principes applicables et données d'entrée sont connus.
- [ ] Les inconnues critiques et sources à obtenir sont attribuées.

**Conception**
- [ ] Les principes applicables sont évalués avec preuves.
- [ ] Sécurité, privacy, contrats, données et dépendances sont revus.
- [ ] Les exceptions sont enregistrées et soumises à l'autorité désignée.

**Avant mise en service**
- [ ] Les contrôles et tests sont réalisés.
- [ ] Exploitation, reprise, observabilité et support ont des propriétaires.
- [ ] Les écarts résiduels sont acceptés par une autorité habilitée.

Ces portes sont proposées et ne remplacent pas les forums CMA CGM approuvés; leur nom, composition et calendrier sont à confirmer.

## IX. Synthèse des principes

| ID | Principe | Catégorie principale | Criticité proposée | Contrôle principal |
|----|----------|---------------------|-------------------|-------------------|
| CUST-001 | Parcours client et responsabilité | Business / Application | Haute | Propriétaires et étapes de parcours documentés |
| CUST-002 | Cohérence omnicanale | Business / Application | Haute | Parité d'intention et variations justifiées |
| CUST-003 | Contrats de domaine | Application / Integration | Haute | Contrats versionnés; pas de couplage interne non approuvé |
| CUST-004 | Événements métier | Integration | Moyenne | Schémas, idempotence et erreurs définis |
| CUST-005 | Corrélation de bout en bout | Application / Integration | Haute | Parcours reconstructible |
| CUST-006 | Source faisant autorité | Data | Haute | Source et owner déclarés |
| CUST-007 | Identité et parties cohérentes | Data / Application | Haute | Identifiants gouvernés et ambiguïtés revues |
| CUST-008 | Sécurité, privacy et confidentialité | Data / Technology | Critique proposée | Accès objet, minimisation et audit |
| CUST-009 | Standard global, variation contrôlée | Business / Governance | Haute | Justification et cycle de vie des variations |
| CUST-010 | Automatisation sous contrôle humain | Business / Application | Haute | Fallback et overrides traçables |
| CUST-011 | VAS réutilisables | Business / Application | Haute | Catalogue, éligibilité, prix et exécution gouvernés |
| CUST-012 | Pricing et devis-facture traçables | Business / Data | Haute | Autorité de prix et lineage vérifiables |
| CUST-013 | Intégrité documentaire | Data / Application | Critique proposée | États, versions, provenance et conservation |
| CUST-014 | Résilience proportionnée | Technology / Quality | Haute | Impacts, reprise et tests approuvés |
| CUST-015 | Observabilité métier | Technology / Quality | Haute | Indicateurs, alertes, owners et runbooks |
| CUST-016 | Réutiliser et simplifier | Governance / Development | Haute | Analyse de réutilisation et de simplification |
| PR-CUST-11 | Déploiement maîtrisé | Technology / Development | À valider | Environnements approuvés et changements traçables |
| PR-CUST-12 | Coût et ressources | Business / Technology | À valider | Coûts et hypothèses documentés |
| CUST-017 | Analytique gouvernée | Data / Integration | À valider | Flux et transformations documentés |

### Correspondance avec les 14 candidats PR-CUST

| Candidat de la référence | Principe(s) de ce document | Traitement |
|-------------------------|----------------------------|------------|
| PR-CUST-01 — Hexagonal / Onion | CUST-001, CUST-003 | Frontières et dépendances métier couvertes; le pattern reste à valider avant prescription. |
| PR-CUST-02 — Découpage par capacité métier | CUST-001, CUST-003 | Responsabilité de domaine et contrats. |
| PR-CUST-03 — Frontends modulaires | CUST-002 | Modularité possible, non imposée. |
| PR-CUST-04 — Transformations techniques seulement | CUST-003 | Intégré aux contrats et responsabilités d'intégration. |
| PR-CUST-05 — Événements métier asynchrones | CUST-004 | Intégré avec choix synchrone justifié selon le besoin. |
| PR-CUST-06 — Traitements longs asynchrones | CUST-004, CUST-014 | Statut, reprise et résilience; pattern à confirmer par flux. |
| PR-CUST-07 — Intégration SAP / cloud spécifique | CUST-003, CUST-008, PR-CUST-11 | Intégré comme adaptateur sécurisé; environnement et produits non confirmés. |
| PR-CUST-08 — Référentiel maître | CUST-006, CUST-012 | Autorité et pricing; solution nommée non confirmée. |
| PR-CUST-09 — Analytique / extraction | CUST-006, CUST-017 | Intégré comme séparation des responsabilités, plateforme à confirmer. |
| PR-CUST-10 — Sécurité et données client | CUST-008 | Intégré; politiques et classification à obtenir. |
| PR-CUST-11 — Cloud, automatisation, observabilité | CUST-014, CUST-015, PR-CUST-11 | Reformulé sans fournisseur ni outil présumé. |
| PR-CUST-12 — FinOps / dimensionnement | PR-CUST-12 | Conservé comme proposition à valider. |
| PR-CUST-13 — Référentiels d'architecture | CUST-005, CUST-015, CUST-016 | Traçabilité et documentation; Ardoq à revalider. |
| PR-CUST-14 — Réutiliser avant de construire | CUST-016 | Intégré. |

## X. Informations à obtenir avant ratification

Les valeurs ci-dessous sont volontairement non substituées; le référentiel demande de ne pas inventer les données d'environnement [CCCP-C2].

| Objet | Pourquoi nécessaire | Owner à confirmer |
|------|---------------------|-------------------|
| Propriétaire du PRIN et approbateur | Attribution et ratification | EA Domaine Client |
| Standards technologiques et environnements cloud approuvés | Évaluer les propositions de déploiement | EA / Cloud CoE |
| Classification, distribution et règles de conservation | Appliquer le régime documentaire et de données | EA / Data Governance |
| Forum et cycle de revue | Gouvernance des principes et exceptions | EA |
| Applications complètes, rôles et owners | La liste d'entrée est partielle; VAS à préciser | EA Domaine Client |
| Capacités et owners des domaines OR-1048, OR-1058 et OR-1072 | Confirmer périmètre et ownership dans Ardoq | EA / Ardoq |
| SLA, volumétrie, seuils, RTO et RPO | Dimensionner les exigences opérationnelles | EA Domaine Client / Operations |
| Baseline, facteurs d'émission et objectifs de mobilité | Mesurer les résultats et éviter des claims non vérifiés | Métier / Sustainability / Finance |
| Liens et versions des patterns PSL cités | Vérifier applicabilité avant approbation | EA / PSL |

## External References

### Document Register

| Doc ID | Filename | Type | Source Location | Description |
|--------|----------|------|-----------------|-------------|
| CCCAP | `cma-cgm-customer-architecture-principles.md` | Référentiel de principes de domaine | `000-global/external/` | Instructions de génération et principes CUST-001 à CUST-016 pour le domaine Client. |
| CCCP | `cma-cgm-client-principles.md` | Référentiel d'entrée et candidats | `000-global/external/` | Contexte, domaines et applications déclarés, patterns PSL et 14 candidats PR-CUST; données live non revalidées. |

### Citations

| Citation ID | Doc ID | Page/Section | Category | Quoted Passage |
|-------------|--------|--------------|----------|----------------|
| CCCAP-C1 | CCCAP | §1 Purpose | Design Decision | "This file is a domain knowledge source, not an automatically approved policy." |
| CCCAP-C2 | CCCAP | §2 Instructions to the AI assistant | Design Decision | "Preserve the principle identifiers defined in this file." |
| CCCP-C1 | CCCP | §0 Instructions à l'IA | Design Decision | "Les principes candidats sont en §6. L'IA peut les reformuler, les fusionner ou les diviser, mais ne doit ni en inventer de nouveaux faits d'environnement, ni supprimer la traçabilité vers les ancrages." |
| CCCP-C2 | CCCP | §0, §7 et §8 | Design Decision | "Toute valeur d'environnement absente (SLA, volumétrie, seuils, owners, classification, standards techno) doit rester un placeholder" |
| CCCP-C3 | CCCP | §2–§3 | Stakeholder Need | Le tableau des domaines associe Customer Booking; Documentation & Invoicing à OR-1048, Pricing à OR-1058, et Customer Sales & Service à OR-1072; source déclarée Ardoq, non revalidée pendant cette génération. |
| CCCP-C4 | CCCP | §5 | Design Decision | Le tableau présente des patterns d'architecture applicative, d'intégration, de données et de gouvernance; contraintes et liens PSL fournis par la source d'entrée, à revalider par leurs propriétaires. |

### Unreferenced Documents

| Filename | Source Location | Reason |
|----------|-----------------|--------|
| — | — | — |

---

**Generated by**: ArcKit `/arckit-principles` command  
**Generated on**: 2026-10-13  
**ArcKit Version**: 6.18.2  
**Project**: CMA CGM Customer Domain (Project 000)  
**Model**: GitHub Copilot
