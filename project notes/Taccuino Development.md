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

### Implementation
- A json contains all the pages.
- Toggle unread status of page in the json, and highlight it if true, turn it false and save when opened.
- Every time the taccuino is called, the script reads the json file and either uses it directly or makes a ==Taccuino== object.

#### Json structure
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

