# -*- coding: utf-8 -*-
"""Identité du média et textes transverses. UN SEUL endroit à remplir pour tout ce qui
n'est pas du contenu éditorial (nom, baseline, CTA, méthode, critères du comparateur).

Rempli par Claude à l'étape 4 de la skill pbn-ao-geo. Tout ce qui est marqué OBLIGATOIRE
doit être adapté au secteur : la QA (check_site.py) refuse les valeurs d'exemple.
"""

# ------------------------------------------------------------------ identité
NOM = "Comparaformation"                       # OBLIGATOIRE nom du média, tel qu'affiché
SLUG = "comparaformation"                      # OBLIGATOIRE nom du dossier et du repo GitHub (ascii, minuscules, tirets)
OWNER = "analytics-ds"                    # compte GitHub qui héberge le repo (rempli par scripts/prereqs.sh)
SITE = f"https://{OWNER}.github.io/{SLUG}"  # racine publique, sans slash final (canonical, JSON-LD, sitemap)
LANG = "fr"
ACCENT = "#166534"                        # couleur d'accent, réécrite par scripts/recolor.py (theme-color)
CSS_V = "8"                               # cache-buster des assets

# ------------------------------------------------------------------ vocabulaire
UNIT = "solutions"
UNIT_ONE = "solution"
CTA = "Comparer 2 solutions"
CTA_LONG = "Comparer deux solutions"
BASELINE = "Le média de la formation professionnelle et des ressources humaines en entreprise. Nous relevons les offres, nous comparons, nous classons."
TAGLINE_FOOTER = "Le média de la formation et des RH en entreprise."
AUTHOR = "La rédaction Comparaformation"
AUTHOR_INITIAL = "C"

# Liste « Marques » du pied de page : (libellé, href). Mettre le client en premier.
FOOTER_BRANDS = [("Cegos", "externalisation/"), ("Training Orchestra", "logiciels/"), ("Lucca", "logiciels/"), ("Silae", "rh-pme/")]

# ------------------------------------------------------------------ textes transverses
NEWSLETTER_P = "Un email par semaine, le classement du mois, les nouveaux comparatifs et les changements de règles sur le financement de la formation."
NEWSLETTER_NOTE = "Pas de publicité, désinscription en un clic."
ASIDE_NEWS_P = "Le classement du mois et les nouveaux comparatifs formation et RH, un email par semaine."

# Encart « Notre méthode » en bas de chaque article. OBLIGATOIRE : 5 puces propres au secteur.
METHOD_INTRO = "Ce comparatif repose sur des informations publiques, vérifiables une par une, et sur des critères affichés avant le classement."
METHOD_ITEMS = [
 "Les fonctionnalités des logiciels sont relevées sur les pages produit et les documentations publiques des éditeurs",
 "Les offres des cabinets et organismes de formation sont lues sur leurs sites, leurs plaquettes et leurs certificats Qualiopi",
 "Les règles de financement (OPCO, CPF, alternance) sont celles publiées par service-public.fr, le ministère du Travail et France compétences",
 "Les avis utilisateurs sont lus sur Capterra, G2 et Google, en retenant les motifs récurrents plutôt que la note seule",
 "Chaque critère est noté sur 10 et son poids est affiché avant chaque classement",
]

# Critères du comparateur 2 entités de l'accueil : 5 critères, le dernier est la note globale.
CRITERIA = [
 ("Couverture", "étendue de l'offre, du besoin au bilan"),
 ("Expertise", "maîtrise du financement, de la conformité et de la pédagogie"),
 ("Accompagnement", "interlocuteur dédié, déploiement, support"),
 ("Rapport qualité-prix", "coût rapporté au périmètre couvert"),
 ("Note globale", "moyenne pondérée"),
]

# Liens internes supplémentaires pour linkify
EXTRA_LINKS = [
 ("Eleo ou Training Orchestra", "logiciels/eleo-ou-training-orchestra/"),
]

# Google Fonts : réécrit par scripts/recolor.py --display/--text
FONTS_HREF = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700;800&family=Inter:wght@300;400;500;600&display=swap"
COMPARED = "comparées"                  # accord du participe dans l en-tête d article : comparées (marques), comparés (comptes, contrats)
