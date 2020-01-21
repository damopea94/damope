#!/usr/bin/env python
# coding: utf-8

# In[134]:


from csv import reader 

opened_file = open('googleplaystore.csv') # Prints the length of the Apple Store csv
read_file = reader(opened_file)
googleplay = list(read_file)
googleplay_header = googleplay[0]
googleplay = googleplay[1:]
# Prints the length of the Apple Store csv


opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
ios = list(read_file)
ios_header = ios[0]
ios= ios[1:]


# In[129]:


def element_data(dataset, start, end, rows_and_columns=True): 
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
print(googleplay_header)
print('\n')
element_data(googleplay, 0,5, True)


# In[136]:


print(ios_header)
print('\n')
element_data(ios, 0,5, True)


# In[138]:


print(googleplay[10472])  # incorrect row
print('\n')
print(googleplay_header)  # header
print('\n')
print(googleplay[0])  


# In[137]:



for element in googleplay:
    if len(element) !=13:
        del(element)
del googleplay[10472]
print(len(googleplay))


# In[144]:


duplicate_apps = []
unique_apps = []

for app in googleplay:
    name = app[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)
    
print('Number of duplicate apps:', len(duplicate_apps))
print('\n')


# In[151]:


reviews_apps={}

for apps in googleplay:
    name=apps[0]
    n_reviews=float(apps[3])
    
    if name in reviews_apps and reviews_apps[name] < n_reviews:
        reviews_apps[name] = n_reviews
        
    elif name not in reviews_apps:
        reviews_apps[name] = n_reviews
print('initial length:', len(googleplay))
print('Actual length:', len(reviews_apps))


# In[201]:


googleplay_clean = []
already_added = []

for apps in googleplay:
    name=apps[0]
    n_reviews=float(apps[3])
    
    if (reviews_apps[name] == n_reviews) and (name not in already_added):
        googleplay_clean.append(apps)
        already_added.append(name)
    
print(len(googleplay_clean))


# In[168]:


def check_english (string):
    for alphabet in string:
        if ord(alphabet)>127:
            return False 
    return True
        


# In[169]:


check_english('boy')


# In[170]:


check_english('欢乐')


# In[171]:


check_english('Instachat 😜')


# In[199]:


def check1_english(string):
    in_english = 0
    for alphabet in string:
        if ord(alphabet)>127:
            in_english +=1
    if in_english > 3:
            return False
    else:
            return True 


# In[183]:


check1_english('Instachat 😜😜😜')


# In[202]:


googleplay_english = []
googleplay_not_english = []

for app in googleplay_clean:
    string_name = app[0]
    if (check1_english(string_name)) is True:
        googleplay_english.append(app)
        
    else:
        googleplay_not_english.append(app)
print(len(googleplay_english))
print(len(googleplay_not_english))


# In[203]:


ios_english = []
ios_not_english = []

for app in ios:
    ios_name = app[1]
    if (check1_english(ios_name)) is True:
        ios_english.append(app)
        
    else:
        ios_not_english.append(app)
print(len(ios_english))
print(len(ios_not_english))


# In[212]:


googleplay_final = []
ios_final = []

for app in googleplay_english:
    price = app[7]
    if price == '0':
        googleplay_final.append(app)
        
for app in ios_english:
    price = app[4]
    if price == '0.0':
        ios_final.append(app)
        
print(len(googleplay_final))
print(len(ios_final))


# In[217]:


ios_genres={}
googleplay_genres={}

for app in ios_english:
    category =app[11] #category are on row 11
    if category not in ios_genres:
        ios_genres[category] = 1
    else:
        ios_genres[category]+=1
print(ios_genres)
print('\n')

for app in googleplay_english:
    category =app[9] #category are on row 9
    if category not in googleplay_genres:
        googleplay_genres[category] = 1
    else:
        googleplay_genres[category]+=1

print(googleplay_genres)
print('\n')


# In[219]:


def freq_table(dataset, index):
    table = {}
    total = 0
    
    for row in dataset:
        total += 1
        value = row[index]
        if value in table:
            table[value] += 1
        else:
            table[value] = 1
    
    table_percentages = {}
    for key in table:
        percentage = (table[key] / total) * 100
        table_percentages[key] = percentage 
    
    return table_percentages


def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)
        
    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])
display_table(ios_final, 11) #apple data to analyze



# In[220]:


display_table(googleplay_final, 9) #analyze


# In[222]:



genres_ios = freq_table(ios_final, -5)

for genre in genres_ios:
    total = 0
    len_genre = 0
    for app in ios_final:
        genre_app = app[-5]
        if genre_app == genre:            
            n_ratings = float(app[5])
            total += n_ratings
            len_genre += 1
    avg_n_ratings = total / len_genre
    print(genre, ':', avg_n_ratings)


# In[223]:


display_table(googleplay_final, 5) # the Installs columns how many times they were downloaded 


# In[227]:


categories_googleplay = freq_table(googleplay_final, 1)
popular_installs=[]

for category in categories_googleplay:
    total = 0
    len_category = 0
    for app in googleplay_final:
        category_app = app[1]
        if category_app == category:            
            n_installs = app[5]
            n_installs = n_installs.replace(',', '')
            n_installs = n_installs.replace('+', '')
            total += float(n_installs)
            len_category += 1
    avg_n_installs = total / len_category
    if avg_n_installs > 9000:
        popular_installs.append(category)

print(category, ':', avg_n_installs) #most popular app insalled 


# In[238]:


for app in ios_final:
    if app[-5] == 'Games':
        print(app[1], ':', app[5])


# In[240]:


for app in ios_final:
    if app[-5] == 'Games' and int(app[5]) > 700000:
            print(app[1])


# # 
