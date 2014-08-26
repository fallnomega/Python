
def get_next_target(s):
    start_link = s.find('<a href=')
    if start_link== -1:
        return None, 0
    start_quote= s.find('"',start_link)
    end_quote = s.find('"',start_quote+1)
    url = s[start_quote+1:end_quote]
    return url, end_quote

def get_all_links(page):
    links =[]
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl,get_all_links(get_page(page)))
            crawled.append(page)
            
    return crawled        
        
page =('this <a href="test1">link 1</a> is <a href="test2">link 2</a>'
   'a <a href="test3">link 3</a>')
seed = ('https://www.udacity.com/cs101x/index.html')

'''OLD
start_link = page.find('<a href=')
#udacity does
#start_quote = page.find('"',start_link)
#end_quote = page.find('"', start_quote+1)
#url = page[start_quote+1:end_quote]

end_link = page.find('"',start_link +9)
url = page[start_link + 9: end_link]
print (start_link)
print (end_link)
print (url)
'''
links= get_all_links(page)
url, end_quote = get_next_target(page)
print (links)
