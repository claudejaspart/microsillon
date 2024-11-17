Installer Django, Django Rest Framework




Some data (directly in db ): 

insert into users_user (id, first_name, last_name, login, hash, salt, address, dob, role)
values
(1, 'Claude', 'Jaspart','Claude', 'cjas', 'no-salt', 1, '23/08/1978', 1),
(2, 'Albert', 'Einstein','Albert', 'aein', 'no-salt', 2, '13/02/1877', 2)


insert into address_address(id, street_number, street_name, postal_code, city, country)
values
(1, '2B', 'Impasse Lebrun Moussier', '13700','Venelles', 'France')



insert into category_category (id, name)
values
(1, 'Punk Rock'),
(2, 'Nu Metal'),
(3, 'Classical'),
(4, 'Country')

insert into album_album (id,title,artist,release_year,description,images,tracks,category_id,stock)
values
(1, 'Smash', 'The Offspring', 1994, 'Smash is the third studio album by American punk rock band The Offspring, released on April 8, 1994, through Epitaph Records. The album was recorded in 20 days between January and February 1994 at Track Record in North Hollywood, California.', '1A', 'Time to relax:Nitro:Bad Habit:Gotta get away:Genocide:Something to believe in:Come out and play:Self Esteem:It will be a long time:Killboy powerhead:What happened to you ?:So alone:Not the one:Smash', 1, 5),
(2, 'Hybrid Theory', 'Linkin Park', 2000, 'Released in 2000, Linkin Park’s debut album “Hybrid Theory” marked a significant turning point in the nu-metal genre. The album’s fusion of rap, rock, and electronica elements created a unique sound that captivated audiences worldwide.', '2A', 'Papercut:One step closer:With you:Points of authority:Crawling:Runaway:By myself:In the End:A place for my head:Forgotten:Cure for the itch:Pushing me away', 2 , 1)