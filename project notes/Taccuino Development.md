
### Implementation
- A json contains all the pages.
- Toggle unread status of page in the json, and highlight it if true, turn it false and save when opened.
- Every time the taccuino is called, the script reads the json file and either uses it directly or makes a ==Taccuino== object.

### UI
- [x] main menu still uses corner button
- [ ] Fix the mouse focus problem

### Pagination
Maybe it does make sense after all to keep objects for the book

- [ ] Design object
- [ ] implement methods

- [ ] Read and show many titles from list
- [ ] Implement page change until list is over
	- [ ] add buttons images
	- [ ] display based on number of items.
### Reading the data
- [x] Make  a mock json
- [ ] Read and show titles from json
- [ ] Reorder all our notes
- [ ] Generate real json from notes


### Unlocking the feature
- [ ] write taccuino miniscene or include it with siringa (check non sa più che pensare e ha bisogno di raccogliere le info dopo che hanabi se ne va)
	- [ ] Hai sbloccato: Appunti di check (in outline orenji)






### Presentation
- When called it shows a custom screen in overlay with a notebook (closed by default)
- You can navigate to a topic by clicking the bookmarks that pop out on hover. Every page falls inside one of the [[Taccuino Topics]].
- Selecting a topic takes you to its index page, where you see just the titles of all the questions in a neat grid.
- You click on any of them to expand them.
- Arrows on both sides at the bottom flip the pages.
- Flipping a page plays a sound and changes the text with a quick fade.
- You have a button to get back to the index.
- The bookmarks are still there.
- Handwritten font
- All pages have this layout: 
	- Title (big)
	- Details
	- Horizontal separator
		- some kind of line
	- Answer
		- Initially blank
		- Can change multiple times



#### Json structure
- [ ] feed the txt file/s into a script to make the json
- [ ] Change to have a list of answers
- [ ] Have a field that indicates what index of answer to show (negative for none)
- [ ] Have a function you can call from inside the scenes to update the pointer and seen status
```Taccuino
{  
    "topics": [  
      {  
         "name" : "-Topic1-",  
         "pages": [  
            {  
            "title":"-title1-",  
            "question":"-question1-",  
            "answer":"-answer1-",  
            "seen":true  
            },  
            {  
            "title":"-title2-",  
            "question":"-question2-",  
            "answer":"-answer2-",  
            "seen":false  
            }  
         ]  
      },  
      {  
         "name" : "-Topic2-",  
         "pages": []  
      }  
   ]  
}
```



Mini scena che lo sblocca con Check che sente la mancanza di larry
