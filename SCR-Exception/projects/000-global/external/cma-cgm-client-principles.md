# CMA-CGM — Référentiel d'entrée pour `arckit:principles`
## Domaine Client : Booking · Documentation · Invoicing · Pricing · Care · Sales & VAS

> **Emplacement recommandé** : `projects/000-global/external/cma-cgm-customer-domain-principles-input.md`
> (référentiel transverse, le PRIN est généré dans `000-global`. Si les principes ne doivent viser qu'un projet donné, placer plutôt dans `projects/<projet>/external/`.)

---

## 0. Instructions à l'IA exécutant `/arckit:principles`

1. Générer le document PRIN « Principes d'architecture — CMA-CGM — Domaine Client » à partir **exclusivement** de ce référentiel et des artefacts ArcKit existants (REQ, RISK, templates projet).
2. Chaque principe doit comporter : **ID** (`PR-CUST-NN`), **nom**, **énoncé**, **justification**, **implications** (obligations concrètes), **métriques/contrôles de conformité**, **ancrages** (patterns PSL §5, domaines Ardoq §2, applications §3).
3. Les principes candidats sont en §6. L'IA peut les reformuler, les fusionner ou les diviser, mais **ne doit ni en inventer de nouveaux faits d'environnement, ni supprimer la traçabilité** vers les ancrages.
4. Toute valeur d'environnement absente (SLA, volumétrie, seuils, owners, classification, standards techno) doit rester un **placeholder** de la forme `<TO OBTAIN — objet · owner à confirmer>` — voir §8. Ne jamais substituer une valeur plausible.
5. Distinguer visuellement le contenu **sourcé** (marqueur `[SOURCE: …]`) du contenu **proposé/inféré** (marqueur `[PROPOSED]`).
6. Après génération : relire et vérifier que chaque lien pointe vers un source listée en §9 ; tout lien non listé est supprimé.

---

## 1. Contexte entreprise

- CMA-CGM : groupe mondial de transport et de logistique (maritime, terrestre, logistique contractuelle), opérant sous plusieurs marques.
- Le domaine client couvre le cycle commercial de bout en bout : quotation → booking → documentation → facturation, avec le pricing en amont et le care / la vente de Value-Added Services (VAS) sur toute la durée de vie du client.
- Ambition digitale : parcours client omnicanal, digitalisation de la documentation et de la facturation, monétisation des services à valeur ajoutée.

## 2. Périmètre du domaine (ancrage catalogue Ardoq — Architecture Areas, live)

[SOURCE: Ardoq, workspace Organization, consulté le 2026-10-13]

| Domaine Ardoq (label exact) | Clé Ardoq | Sous-périmètres couverts |
|---|---|---|
| Customer Booking; Documentation & Invoicing | OR-1048 | Booking, Documentation, Invoicing |
| Pricing | OR-1058 | Pricing, tarification, quotation |
| Customer Sales & Service | OR-1072 | Sales, VAS, Customer Care |

- Domaine connexe à ne pas confondre : **Customs, Documentation & Trade Operation** (OR-1290) — documentation douanière ; hors périmètre sauf interfaces.
- Les libellés ci-dessus sont les libellés live du catalogue : les utiliser tels quels dans le PRIN, sans paraphrase.

## 3. Paysage applicatif du domaine (extrait Ardoq live — rôles exacts à confirmer par l'EA)

[SOURCE: Ardoq, workspace Applications, consulté le 2026-10-13]

| Thème | Application (nom exact Ardoq) | Clé |
|---|---|---|
| Booking & SI | eCommerce - Booking Request/Shipping Instructions | AP-26867 |
| Booking & SI | AR AQUA Invoice Booking Automation | AP-26822 |
| Documentation | eCommerce - Documentation | AP-26761 |
| Documentation | Customer Export Documentation | AP-26831 |
| Facturation | eCommerce - Invoicing | AP-25583 |
| Facturation | Customer Billing | AP-27892 |
| Facturation / compta | LISA Accounting | AP-26417 |
| Intégration | Lisa Integration Suite | AP-25974 |
| Pricing | Aqua – SETUP Pricing Group Administration | AP-27185 |
| Pricing | Aqua - SPOT | AP-26082 |
| Pricing | eCommerce - Charge finder | AP-25900 |
| Pricing | eCommerce - Tariff finder | AP-28092 |
| Quotation | eCommerce - Quotation request | AP-27869 |
| Portails / e-commerce | AQUA | AP-26144 |
| Portails / e-commerce | eCommerce | AP-27081 |
| Portails / e-commerce | eCommerce Customer Journey | AP-28144 |
| Portails / e-commerce | CUSTOMER PORTAL | AP-26510 |
| Portails / e-commerce | eCommerce - ANL website · eCommerce - APL Website · eCommerce - CNC websites | AP-26266 / AP-25901 / AP-27684 |
| Sales & VAS | eCommerce - Line and Services | AP-28387 |
| Care | Customer Assistant | AP-26751 |
| Care | Nova - My Customer Service | AP-28076 |
| Master data client | Customer Profile | AP-27735 |
| Master data client | MyCustomerProfile - KM Platform | AP-26794 |
| Risque client | Customer Risk Profile | AP-27797 |

Notes pour l'IA :
- Ce tableau est un **extrait ciblé**, pas l'inventaire complet du domaine. Compléter via Ardoq si besoin, sans paraphraser les noms.
- Les applications supportant spécifiquement la **vente des VAS** ne sont pas identifiées dans cet extrait : `<TO OBTAIN — liste des applications VAS et de leurs owners · owner: EA Domaine Client>`.

## 4. Drivers d'architecture du domaine

- [PROPOSED] Omnicanalité et multi-marque : le paysage e-commerce couvre plusieurs marques (sites ANL, APL, CNC — cf. §3) ; les principes doivent garantir une expérience cohérente avec des backends partagés.
- [PROPOSED] Le booking, la documentation et la facturation forment une chaîne : la cohérence bout-en-bout (eventualité, traçabilité) est un driver majeur.
- [PROPOSED] Le pricing est référentiel volatile et transverse : unicité de la source de vérité.
- [PROPOSED] Le care et les données client impliquent une exigence forte de protection des données personnelles.

## 5. Patterns de référence (source : espace Confluence PSL, bibliothèques RAG « Patterns »)

À citer dans le PRIN comme règles applicables, avec ces liens :

| # | Pattern | Bibliothèque | Lien Confluence | Ce qu'il impose |
|---|---|---|---|---|
| P1 | Hexagonal & Onion Architecture | Software Engineering | [Hexagonal & Onion Architecture](https://cmacgm.atlassian.net/wiki/spaces/PSL/pages/3161753820/Hexagonal+%26+Onion+Architecture) | Logique métier isolée ; sens des dépendances strict Infrastructure → Application → Domaine ; couche Domaine sans dépendance externe ; non applicable aux ERP/packagés |
| P2 | Microservices | Software Engineering | [Microservices](https://cmacgm.atlassian.net/wiki/spaces/PSL/pages/3213525192/Microservices) | Services autonomes alignés sur les capacités métier ; base de données dédiée par service ; observabilité dès le départ ; déploiements indépendants |
| P3 | Remote Procedure Invocation - API Request Transformation | Integration | [RPI - API Request Transformation](https://cmacgm.atlassian.net/wiki/spaces/PSL/pages/3154118896/Remote+Procedure+Invocation+-+API+Request+Transformation) | Transformation d'API **technique uniquement**, sans logique métier embarquée ; transformations minimales ; sécurité by design |
| P4 | Business Event Transformation | Integration | [Business Event Transformation](https://cmacgm.atlassian.net/wiki/spaces/PSL/pages/3161751908/Business+Event+Transformation) | Normalisation/enrichissement des événements en file ; intégrité des données ; découplage producteur/consommateur |
| P5 | Master Data Provisionning - ETL | Data & Analytics | [Master Data Provisionning - ETL](https://cmacgm.atlassian.net/wiki/spaces/PSL/pages/3152709039/Master+Data+Provisionning+-+ETL) | Alimentation MdM (MyCDM) en batch asynchrone ; validation centralisée dans le MdM ; robustesse de gestion d'erreurs |
| P6 | Master Data Consumption - Event Driven | Data & Analytics | [Master Data Consumption - Event Driven](https://cmacgm.atlassian.net/wiki/spaces/PSL/pages/3154119055/Master+Data+Consumption+-+Event+Driven) | Diffusion des référentiels par événements (MyCDM/Semarchy + broker + middleware) ; idempotence, découplage, isolation des défaillances |
| P7 | Data Extraction | Data & Analytics | [Data Extraction](https://cmacgm.atlassian.net/wiki/spaces/PSL/pages/3161752543/Data+Extraction) | Extraction uniquement de données master/référentielles ; **aucune transformation métier** à l'extraction ; pipelines automatisées vers la CDP |
| P8 | Functionality Document Architecture Assets | IT Governance | [Document Architecture Assets](https://cmacgm.atlassian.net/wiki/spaces/PSL/pages/4158619649/Functionality+Document+Architecture+Assets) | Documentation des actifs d'architecture dans des référentiels centralisés, templates approuvés, versioning, contrôle d'accès par rôle |

Patterns complémentaires mobilisables si le PRIN les exige (sans lien récupéré ici, citer alors nom + bibliothèque) : RPI - API Long Time Running Tasks (Integration) ; Master Data Consumption - API et - Analytics, Reverse ETL (Data & Analytics) ; SAP Integration Patterns - AWS Services Integrations (Integration) ; Microfrontend, Single Tenant (Software Engineering) ; FinOps Operating Model, Right-Sizing (IT Governance).

## 6. Principes candidats pour le PRIN

> Formulation libre autorisée, ancrages obligatoires. ID proposés `PR-CUST-01…14`.

### Thème A — Architecture applicative

**PR-CUST-01 — Isoler la logique métier du domaine client** [ancrage : P1]
- *Énoncé* : toute application custom du domaine (règles de booking, calcul tarifaire, catalogue VAS, cycle de facturation) sépare sa logique métier (Domain) de ses préoccupations techniques (Infrastructure) via une couche Application ; le sens des dépendances est Infrastructure → Application → Domain, la couche Domain restant sans dépendance externe.
- *Implications* : validation des entrées en couche Application, règles métier en couche Domain ; tests du Domain sans mocks ; non applicable aux progiciels/ERP du domaine.

**PR-CUST-02 — Découper selon les capacités métier du domaine** [ancrage : P2 ; §2]
- *Énoncé* : les composants applicatifs s'alignent sur les périmètres Booking / Documentation / Invoicing / Pricing / Care / Sales & VAS (domaines Ardoq OR-1048, OR-1058, OR-1072), avec frontières explicites, données dédiées par service et découplage opérationnel.
- *Implications* : découpage microservices réservé aux cas justifiant autonomie, isolation des pannes et scalabilité indépendante ; pas de base de données partagée entre services ; modernisation progressive du legacy plutôt que big bang.

**PR-CUST-03 — Frontends modulaires alignés sur les contextes métier** [ancrage : Microfrontend (Software Engineering) ; §3]
- *Énoncé* : les portails et parcours e-commerce du domaine sont décomposés en modules autonomes déployables indépendamment, alignés sur les contextes métier (booking, tracking, facturation…), communiquant par interfaces explicites — jamais par état global partagé.
- *Implications* : gouvernance des technologies front pour éviter la fragmentation ; bibliothèques partagées standardisées ; monitoring de performance par module.

### Thème B — Intégration

**PR-CUST-04 — Aucune logique métier dans les middlewares d'intégration** [ancrage : P3]
- *Énoncé* : les transformations réalisées par la couche d'intégration sont strictement techniques (format, protocole, sécurité, enrichissement d'interopérabilité) et minimales ; les règles métier restent dans les applications du domaine.
- *Implications* : documenter explicitement chaque transformation ; privilégier les middlewares standards ; contrôler les performances des transformations.

**PR-CUST-05 — Diffusion des états du cycle client par événements, asynchrone par défaut** [ancrage : P4, P6]
- *Énoncé* : les changements d'état du cycle (booking confirmé, SI reçues, émis facture, mise à jour référentiel tarifaire) sont publiés comme événements normalisés consommés de manière asynchrone, découplée et idempotente.
- *Implications* : consumers idempotents ; isolation des défaillances ; monitoring des files ; les flux synchrones restent réservés aux interactions requérant une réponse immédiate (API).

**PR-CUST-06 — Traitements longs découplés avec suivi de statut** [ancrage : RPI - API Long Time Running Tasks]
- *Énoncé* : les traitements resource-intensive du domaine (batchs de facturation, génération de rapports, reprises documentaires) s'exécutent de manière asynchrone avec suivi de statut explicite, sans bloquer les appelants.

**PR-CUST-07 — Intégration sécurisée avec l'écosystème progiciel** [ancrage : SAP Integration Patterns - AWS Services Integrations]
- *Énoncé* : les intégrations avec l'écosystème SAP/packagé passent par des adapters natifs du middleware d'intégration, avec authentification par rôle IAM et connectivité privée (Private Link), sans exposition publique.

### Thème C — Données

**PR-CUST-08 — Une source dorée unique pour les référentiels du domaine** [ancrage : P5, P6, P7]
- *Énoncé* : les données de référence du domaine (client, contrat/tarif, référentiels pricing) sont gérées dans le MdM du groupe (MyCDM) en source dorée unique ; alimentation par ETL batch pour les gros volumes, consommation par API pour les petits volumes, diffusion par événements pour la propagation temps quasi-réel.
- *Implications* : validation centralisée dans le MdM ; pas de référentiel parallèle local ; toute application du domaine consomme le référentiel doré, elle ne le recopie pas.

**PR-CUST-09 — L'analytique passe par la plateforme data, sans transformation métier à l'extraction** [ancrage : P7, Reverse ETL]
- *Énoncé* : l'exploitation analytique des données du domaine (pricing analytics, churn, performance commerciale) transite par la plateforme data (CDP) : extraction brute des données master, transformations dans la plateforme, consommation analytique via les référentiels existants ; le retour vers les applications opérationnelles (reverse ETL) ne se fait qu'au départ d'un entrepôt autoritaire, en protégeant ses performances.

**PR-CUST-10 — Sécurité et protection des données client by design** [ancrage : P3 (sécurité by design) ; app Customer Risk Profile AP-27797]
- *Énoncé* : les données personnelles et commerciales des clients sont protégées dès la conception : minimisation, classification, contrôle d'accès par rôle, chiffrement des flux, et gestion du risque client intégrée au parcours commercial.
- *Implications* : conformité RGPD et réglementations locales applicables ; DPIA pour les nouveaux traitements de données personnelles ; traçabilité des accès.

### Thème D — Cloud & run

**PR-CUST-11 — Déploiement sur cloud validé CMA-CGM, automatisé et observable** [ancrage : Single Tenant (Software Engineering)]
- *Énoncé* : toute nouvelle application du domaine est déployée sur un cloud validé par le CMA-CGM, avec provisioning automatisé (infrastructure as code, ex. Terraform) et observabilité centralisée dès le premier jour (ex. ELK, Dynatrace, Splunk).
- *Implications* : pas d'environnement provisionné manuellement ; exigences de scalability, backup et DR traitées dès la conception.

**PR-CUST-12 — FinOps dès la conception** [ancrage : FinOps Operating Model, Right-Sizing (IT Governance)]
- *Énoncé* : chaque composant du domaine intègre le coût comme attribut d'architecture : dimensionnement au plus juste, taggage systématique des ressources, revue périodique de consommation.
- *Implications* : KPIs de suivi ; budgets et alertes ; optimisation continue pilotée par l'observabilité.

### Thème E — Gouvernance

**PR-CUST-13 — Les actifs d'architecture du domaine sont documentés dans les référentiels centraux** [ancrage : P8 ; catalogue Ardoq]
- *Énoncé* : applications, flux, interfaces et principes du domaine client sont documentés dans les référentiels d'architecture du groupe (templates approuvés, versioning, contrôle d'accès par rôle) et maintenus dans le catalogue Ardoq (noms exacts, pas de paraphrase).
- *Implications* : le catalogue Ardoq est la référence live des domaines (OR-1048, OR-1058, OR-1072) et des applications ; toute évolution du domaine met à jour le catalogue.

**PR-CUST-14 — Réutiliser avant de construire** [ancrage : espace PSL §5]
- *Énoncé* : avant tout nouveau développement, les patterns approuvés de l'espace PSL et les services des équipes transverses (ex. catalogue de services Cloud CoE) sont consultés ; un écart à un pattern existant doit être justifié dans un ADR.
- *Implications* : chaque ADR du domaine cite les patterns écartés avec justification ; revue périodique de conformité aux principes PR-CUST.

## 7. Contraintes et standards transverses (à compléter avant finalisation du PRIN)

- Standards technologiques du groupe : `<TO OBTAIN — référentiel de standards techno applicable · owner: EA>`
- Classification des documents et données : `<TO OBTAIN — classification interne applicable · owner: EA>`
- Forum de gouvernance applicable (Architecture Review Board / TDA) : `<TO OBTAIN — forum et cycle de revue · owner: EA>`
- Règles de nommage, environnements non-prod obligatoires, exigences DR/BCP du domaine : `<TO OBTAIN — valeurs · owner: EA Domaine Client>`

## 8. Informations requises avant implémentation (placeholders à lever)

| Objet | Pourquoi | Owner à confirmer |
|---|---|---|
| Liste exhaustive des applications du domaine + owners (Ardoq `get_component_fields`) | Table §3 partielle | EA Domaine Client |
| Applications supportant la vente des VAS | Non identifiées dans l'extrait | EA Domaine Client |
| Capacités métier rattachées à OR-1048 / OR-1058 / OR-1072 | Vue capacités absente de l'extrait | EA / Ardoq |
| SLA, volumétrie, seuils du domaine (booking/jour, factures/mois…) | Aucune valeur inventée | EA Domaine Client |
| Standards techno, classification, forum de gouvernance | §7 | EA |
| Liens Confluence des patterns complémentaires cités sans lien | §5 note | EA |

## 9. Traçabilité des sources de ce référentiel

- Catalogue Ardoq (live, 2026-10-13) : domaines OR-1048, OR-1058, OR-1072 (workspace Organization) ; applications citées avec clés AP-… (workspace Applications).
- Patterns : espace Confluence PSL, bibliothèques RAG « Patterns » (Integration, Software Engineering, Data & Analytics, IT Governance) — liens Confluence en §5.
- Le reste (drivers §4, principes §6) est une proposition à valider par l'EA du domaine.