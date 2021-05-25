

# In[578]:


import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
#from selenium import webdriver
#import time

URL_FILMS_BASE = 'https://www.imdb.com'
URL_FILMS_LISTE = '/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=ZEZSWF427KDNCR9JF090&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1'


# # Récupérer les url de tous les films

# In[102]:


def get_html_from_link(page_link):
    '''
        Get HTML from web page and parse it.

        :param page_link: link of the webpage we want to scrap
        :type page_link: string
        :return: BeautifulSoup object (HTML parsed)
        :rtype: bs4.BeautifulSoup
    '''

    # TODO Code this function
    html = requests.get(page_link)
    soup = BeautifulSoup(html.text)
    return soup


# In[103]:


page_link = f'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
print(get_html_from_link(page_link).prettify())

# In[104]:


HTML = get_html_from_link(page_link)

# In[105]:


liste = HTML.find_all("a", href=True)
print(liste)


# In[106]:


def get_links_to_films(root_html):
    '''
        Extract book links from URL_BOOK_LISTE

        :param root_html: BeautifulSoup Element that contains all books links
        :type book_html: bs4.BeautifulSoup
        :return: List of all book links in the page
        :rtype: list(str)
    '''
    films_links = []
    all_href = root_html.find_all("a", href=True)
    for i in all_href:
        if "/title/" in i["href"]:
            films_links.append(i["href"])
    # TODO Append to books_links all the links refering to Books you may find on this page.
    #  First find all links
    # Then filter the links to keep only relevent ones
    #  May note that they all start with /livres/
    return films_links


# In[ ]:


# In[107]:


html = get_html_from_link(page_link)
films_links = get_links_to_films(html)
films_links

# In[108]:


elementSupprime = films_links.pop(0)
print(films_links)

# In[109]:


new_list = []

for i in films_links:
    if i not in new_list:
        new_list.append(i)

print(new_list)

# In[110]:


films_links = new_list

# In[111]:


films_links

# # Récupérer les données

# ## Récupérer les titres

# In[112]:


url = "https://www.imdb.com/title/tt0111161/"

# In[113]:


HTML = get_html_from_link(url)

# In[114]:


all_titles = HTML.find("h1", {"class": ""})
print(all_titles.text[:-7])


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[115]:


def extract_titles_info(films_html):
    '''
        Extract book infos from URL BOOK HTML

        :param book_html: BeautifulSoup Element that contains book infos
        :type book_html: bs4.element.Tag
        :return:
            - book_title : title of the book
            - book_image_link: link to the image of the book
        :rtype: tuple(string, string, string)
    '''
    # Il y a différentes class en fonction de la longueur du titre
    if HTML.find_all("h1", {"class": ""}):
        all_titles = HTML.find_all("h1", {"class": ""})
        titles_films = all_titles[0].text[:-7]
    else:
        all_titles = HTML.find_all("h1", {"class": "long"})
        titles_films = all_titles[0].text[:-7]

    # TODO : get titles_films

    return titles_films


# In[116]:


link = URL_FILMS_BASE + films_links[0]
print(link)
html = get_html_from_link(link)
extract_titles_info(html)

# In[117]:


liste_titres = []
for link in films_links:
    url = URL_FILMS_BASE + link
    # print(url)
    HTML = get_html_from_link(url)
    print(extract_titles_info(html))
    liste_titres.append(extract_titles_info(html))

# In[118]:


len(liste_titres)


# ## Récupérer les notes

# In[119]:


def extract_note_info(film_html):
    try:
        all_notes = HTML.find_all("span", {"itemprop": "ratingValue"})
        note = all_notes[0].text.strip()
    except:
        note = None

    return note


# In[120]:


link = URL_FILMS_BASE + films_links[0]
print(link)
html = get_html_from_link(link)
extract_note_info(html)

# In[121]:


liste_notes = []
for link in films_links:
    url = URL_FILMS_BASE + link
    HTML = get_html_from_link(url)
    print(extract_note_info(html))
    liste_notes.append(extract_note_info(html))

# In[122]:


len(liste_notes)

# # Récuperer les dates

# In[123]:


test = HTML.find_all("span", {"id": "titleYear"})
print(test[0].text[1:-1])


# In[124]:


def extract_date(book_html):
    all_date = []

    all_date = HTML.find("span", {"id": "titleYear"})
    date = all_date.text[1:-1]

    return date


# In[125]:


link = URL_FILMS_BASE + films_links[0]
# print(link)
html = get_html_from_link(link)
extract_date(html.text)

# In[126]:


all_date = []
for link in films_links:
    url = URL_FILMS_BASE + link
    # print(url)
    HTML = get_html_from_link(url)
    print(extract_date(html.text))
    all_date.append(extract_date(html.text))

# In[127]:


len(all_date)


# ## Récupérer la durée

# In[128]:


def extract_duree_info(book_html):
    all_duree = []

    all_duree = HTML.find("div", {"class": "subtext"})
    duree = all_duree.time.text

    return duree


# In[129]:


link = URL_FILMS_BASE + films_links[0]
# print(link)
html = get_html_from_link(link)
extract_duree_info(html.text)

# In[130]:


liste_duree1 = []
for link in films_links:
    url = URL_FILMS_BASE + link
    # print(url)
    HTML = get_html_from_link(url)
    print(extract_duree_info(html.text))
    liste_duree1.append(extract_duree_info(html.text))

# In[131]:


liste_duree1

# In[132]:


liste_duree2 = []
import re

i = 0
while i < len(liste_duree1):
    s = liste_duree1[i]
    regex = re.compile(r'[\n]')
    s = regex.sub(" ", s)
    liste_duree2.append(s)
    i += 1

# In[133]:


liste_duree = []
import re

i = 0
while i < len(liste_duree2):
    s = liste_duree2[i]
    regex = re.compile(r'[ ]')
    s = regex.sub("", s)
    liste_duree.append(s)
    i += 1

# In[134]:


liste_duree

# In[135]:


len(liste_duree)


# In[ ]:


# In[ ]:


# # Récuperer les genres

# In[136]:


def extract_genre(book_html):
    genre = HTML.find_all("div", {"class": "see-more inline canwrap"})
    for G in genre:
        if G.h4.text == "Genres:":
            return G.text[8:]


# In[137]:


link = URL_FILMS_BASE + films_links[0]
# print(link)
html = get_html_from_link(link)
extract_genre(html.text)

# In[138]:


liste_genre1 = []
for link in films_links:
    url = URL_FILMS_BASE + link
    # print(url)
    HTML = get_html_from_link(url)
    print(extract_genre(html.text))
    liste_genre1.append(extract_genre(html.text))

# In[139]:


liste_genre2 = []
import re

i = 0
while i < len(liste_genre1):
    s = liste_genre1[i]
    regex = re.compile(r'[\n]')
    s = regex.sub(" ", s)
    liste_genre2.append(s)
    i += 1

# In[140]:


liste_genre = []
import re

i = 0
while i < len(liste_genre2):
    s = liste_genre2[i]
    regex = re.compile(r'[|]')
    s = regex.sub(",", s)
    liste_genre.append(s)
    i += 1

# In[141]:


liste_genre

# In[142]:


len(liste_genre)


# In[ ]:


# # Récuperer les acteurs

# In[143]:


def extract_actor(book_html):
    actor = HTML.find_all("div", {"class": "credit_summary_item"})
    for A in actor:
        if A.h4.text == "Stars:":
            return A.text[7:-29]


# In[144]:


link = URL_FILMS_BASE + films_links[0]
# print(link)
html = get_html_from_link(link)
extract_actor(html.text)

# In[148]:


liste_actor1 = []
for link in films_links:
    url = URL_FILMS_BASE + link
    # print(url)
    HTML = get_html_from_link(url)
    print(extract_actor(html.text))
    liste_actor1.append(extract_actor(html.text))

# In[149]:


liste_actor = []
import re

i = 0
while i < len(liste_actor1):
    s = liste_actor1[i]
    regex = re.compile(r'[\n]')
    s = regex.sub(" ", s)
    liste_actor.append(s)
    i += 1

# In[579]:


liste_actor

# In[151]:


len(liste_actor)


# In[ ]:


# # Récuperer les réalisateurs

# In[152]:


def extract_director(book_html):
    try:
        director = HTML.find_all("div", {"class": "credit_summary_item"})
        for D in director:
            if D.h4.text == "Director:":
                director = D.text[10:]
            elif D.h4.text == "Directors:":
                director = D.text[11:]


    except:
        director = None
    return director


# In[153]:


link = URL_FILMS_BASE + films_links[0]
# print(link)
html = get_html_from_link(link)
extract_director(html.text)

# In[154]:


liste_director1 = []
for link in films_links:
    url = URL_FILMS_BASE + link
    # print(url)
    HTML = get_html_from_link(url)
    print(extract_director(html.text))
    liste_director1.append(extract_director(html.text))

# In[ ]:


liste_director1

# In[155]:


liste_director = []
import re

i = 0
while i < len(liste_director1):
    s = liste_director1[i]
    regex = re.compile(r'[\n]')
    s = regex.sub(" ", s)
    liste_director.append(s)
    i += 1

# In[ ]:


liste_director

# In[156]:


len(liste_director)


# # Récuperer les metascores

# In[404]:


def extract_metascore(book_html):
    # try:

    if HTML.find_all("div", {"class": "metacriticScore score_favorable titleReviewBarSubItem"}):
        metascore = HTML.find_all("div", {"class": "metacriticScore score_favorable titleReviewBarSubItem"})
        for M in metascore:
            metascore = M.text
    elif HTML.find_all("div", {"class": "metacriticScore score_mixed titleReviewBarSubItem"}):
        metascore = HTML.find_all("div", {"class": "metacriticScore score_mixed titleReviewBarSubItem"})
        for M in metascore:
            metascore = M.text
    else:
        metascore = 'None'

    # except:
    #     metascore=None

    return metascore


# In[405]:


link = URL_FILMS_BASE + films_links[0]
# print(link)
html = get_html_from_link(link)
extract_metascore(html.text)

# In[406]:


liste_metascore1 = []
for link in films_links:
    url = URL_FILMS_BASE + link
    # print(url)
    HTML = get_html_from_link(url)
    print(extract_metascore(html.text))
    liste_metascore1.append(extract_metascore(html.text))

# In[407]:


liste_metascore1

# In[408]:


len(liste_metascore1)


# In[ ]:


# # Récuperer les budgets

# In[429]:


def extract_budget(book_html):
    try:
        budget = HTML.find_all("div", {"class": "txt-block"})
        for B in budget:
            if B.h4.text == "Budget:":
                budgets = B.text[8:-12]
                return budgets
    except:
        budgets = None


# In[430]:


link = URL_FILMS_BASE + films_links[0]
# print(link)
html = get_html_from_link(link)
extract_budget(html.text)

# In[431]:


liste_budget1 = []
for link in films_links:
    url = URL_FILMS_BASE + link
    # print(url)
    HTML = get_html_from_link(url)
    print(extract_budget(html.text))
    liste_budget1.append(extract_budget(html.text))

# In[432]:


liste_budget1

# In[433]:


len(liste_budget1)


# In[ ]:


# # Récuperer les mois de sorties

# In[171]:


def extract_mois(book_html):
    mois = HTML.find_all("div", {"class": "txt-block"})
    for M in mois:
        if M.h4.text == "Release Date:":
            return M.text[17:-35].strip().lower()


# In[172]:


link = URL_FILMS_BASE + films_links[0]
# print(link)
html = get_html_from_link(link)
extract_mois(html.text)

# In[173]:


liste_mois = []
for link in films_links:
    url = URL_FILMS_BASE + link
    # print(url)
    HTML = get_html_from_link(url)
    print(extract_mois(html.text))
    liste_mois.append(extract_mois(html.text))

# In[194]:


len(liste_mois)


# ## Récuper les nombres de votant

# In[175]:


def extract_votant(book_html):
    all_nb = HTML.find_all("span", {"itemprop": "ratingCount"})
    nb_votant = all_nb[0].text.strip()

    return nb_votant


# In[176]:


link = URL_FILMS_BASE + films_links[0]
# print(link)
html = get_html_from_link(link)

extract_votant(html)

# In[180]:


liste_nb_votant = []
for link in films_links:
    url = URL_FILMS_BASE + link
    # print(url)
    HTML = get_html_from_link(url)
    print(extract_votant(html))
    liste_nb_votant.append(extract_votant(html.text))

# In[193]:


len(liste_nb_votant)


# ## Récupérer User Reviews

# In[182]:


def extract_reviews(book_html):
    reviews = HTML.find_all("div", {"class": "user-comments"})
    nb_reviews = reviews[0].p.text

    return nb_reviews


# In[183]:


link = URL_FILMS_BASE + films_links[0]
# print(link)
html = get_html_from_link(link)

extract_reviews(html)

# In[184]:


liste_reviews = []
for link in films_links:
    url = URL_FILMS_BASE + link
    # print(url)
    HTML = get_html_from_link(url)
    print(extract_reviews(html.text))
    liste_reviews.append(extract_reviews(html.text))

# In[185]:


liste_reviews

# In[192]:


len(liste_reviews)


# # Récupérer la story line

# In[186]:


def extract_story_line(book_html):
    story = HTML.find_all("div", {"class": "inline canwrap"})
    stories = story[0].span.text

    return stories


# In[187]:


link = URL_FILMS_BASE + films_links[0]

html = get_html_from_link(link)

extract_story_line(html)

# In[188]:


liste_story_line = []
for link in films_links:
    url = URL_FILMS_BASE + link
    HTML = get_html_from_link(url)
    print(extract_story_line(html.text))
    liste_story_line.append(extract_story_line(html.text))

# In[190]:


len(liste_story_line)

# # DataFrame:

# In[782]:


df = pd.DataFrame(
    {"titres": liste_titres, "date": all_date, "mois de sortie": liste_mois, "notes": liste_notes, "durée": liste_duree,
     "genre": liste_genre, "acteurs": liste_actor, "story_line": liste_story_line, "réalisateur": liste_director,
     "nombre de votes": liste_nb_votant, "users_reviews": liste_reviews, "metascore": liste_metascore1,
     "budget": liste_budget1})

# In[784]:


df["metascore"] = df[["metascore"]][df["metascore"].str.contains('\n', regex=False)]

# In[785]:


df['metascore'] = df['metascore'].str.replace(r'\n', '')

# In[786]:


df['metascore'].astype(float)

# In[787]:


df_final = df

# In[788]:


df_final["metascore"] = df_final["metascore"].astype(float)
df_final.info()

# #### On nettoie les données

# In[789]:


# Dans la colonne "nombre de votes", pour chaque milliers, les valeurs sont séparées par des ",".
# Ici, on enlève les virgules
df_final["nombre de votes"] = [(str(i).replace(",", "")) for i in df_final["nombre de votes"]]

# In[790]:


# On change le type de notes
df_final["notes"] = df_final["notes"].astype(float)

# In[791]:


df_final["notes_proportionnelles"] = ((df_final['notes']) * 10)

# In[792]:


# On enlève le "\n" dans la colonne budget
df_final["budget"] = [(str(i).replace("\n", "")) for i in df_final["budget"]]

# In[793]:


df_final["durée"] = [(str(i).replace("h", "")) for i in df_final["durée"]]
df_final["durée"] = [(str(i).replace("min", "")) for i in df_final["durée"]]

# On sépare la colonne durée en deux colonnes : heures et minutes
df_final["heures"] = df_final["durée"].str[0]
df_final["min"] = df_final["durée"].str[1:3]

# On sépare la colonne minute en dizaine et unité
df_final["min_dizaine"] = df_final["min"].str[0]
df_final["min_unite"] = df_final["min"].str[1]

# On change le type des colonnes heures et min_dizaine et min_unite
df_final["heures"] = df_final["heures"].astype(float)
df_final["min_dizaine"] = df_final["min_dizaine"].astype(float)
df_final["min_unite"] = df_final["min_unite"].astype(float)

# On créé une nouvelle colonne où la durée du film est écrite en minutes
df_final["durée_minutes"] = ((df_final["heures"] * 60) + (df_final["min_dizaine"] * 10) + df_final["min_unite"])

# On supprime les colonnes durée, heures, minutes, min_dizaine et min_unite

df_final.drop('durée', axis=1, inplace=True)
df_final.drop('heures', axis=1, inplace=True)
df_final.drop('min_dizaine', axis=1, inplace=True)
df_final.drop('min_unite', axis=1, inplace=True)
df_final.drop('min', axis=1, inplace=True)

# In[794]:


df_final["budget"] = df_final[["budget"]][df_final["budget"].str.contains('$', regex=False)]

# In[479]:


df_final

# In[480]:


df_final.info()
