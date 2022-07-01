from bs4 import BeautifulSoup
import requests

# Scrap info and return list of list
def scrap_info(url):
    my_big_list = []
    my_list = {}
    result = requests.get(url)
    webpage = result.content
    soup=BeautifulSoup(webpage, "html.parser")
    result.close()
    
    cards = soup.findAll('div', {'class':'masonry-grid-item lg:tw-w-1/3 tw-w-2/4 sm:tw-px-3 tw-px-1'})
    for card in cards:
        name = card.find('h2',{'class':'tw-mb-4 sm:tw-mb-6 tw-text-black tw-font-heading tw-text-base tw-leading-22px sm:tw-text-lg sm:tw-leading-4'}).string
        name_content = name.replace("\n", "")
        link = card.find('div',{'class':'card-text tw-relative tw-text-center tw-bg-gray-400 tw-px-2 sm:tw-px-4 tw-pb-5 tw-pt-30px tw-rounded-b-large tw-transform tw-z-20'})
        link_content = link.find('a')['href']
        description_content = card.find('p',{'class':'tw-mb-8 description'}).string
        img_content = card.find('img',{'class': 'tw-object-cover tw-w-100px tw-h-100px tw-mx-auto tw tw-h-auto tw-rounded-full'})['src']
        
        my_list = {'name': name_content, 'link': link_content, 'description':description_content, 'image':img_content}
        my_big_list.append(my_list)
    
    return my_big_list

# print(scrap_info('https://www.letudiant.fr/fiches/etudes/filieres-ecole-d-ingenieurs/secteurs-43+49.html'))