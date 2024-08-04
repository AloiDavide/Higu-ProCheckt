
- [ ] To make the taccuino actually update I'll need to both update the json and call a method or function that re-reads the json
- [x] Make text size dynamic
	- base size is 35
	- we can fit about 550 characters at max size between question and answer.
	- [x] sum length of all the displaying text
	- [x] scale it down one pixel every 20 characters?
	- [ ] in the rewrite make this a method of the page object: right.get_tsize()


I'm using an imagebutton to call a python function that does some stuff and then brings up a screen with renpy.show_screen(), but after the new screen appears, the mouse doesn't interact with its elements until I click on it once. Is there a way to give it focus immediately?

### Implementation
- A json contains all the pages.
- Toggle unread status of page in the json, and highlight it if true, turn it false and save when opened.
- Every time the game is loaded, the script reads the json file and either uses it directly or makes a ==Taccuino== object.




## VFX
- [x] main menu still uses corner button
- [x] Fix the mouse focus problem, ask on the discord ⏫
- [x] fix the exclamation reloading when the page is clicked
- [x] fix check face showing up in blank pages
- [x] toggle button stays big and changes color while notes are open?
	- [x] black bg becomes dark red while keeping outlines
- [x] Make the toggle button not duplicate during swipe animations
- [x] Decide on page transitions
	- Maybe blinds for page turn and pixellate for topic change and entering specific page
- [x] Make the toggle button also close it.
- [ ] Figure out a way to make the transition that doesn't steal the mouse focus




## Topics
- [x] Add bookmarks imagebuttons to the side
- [x] Handle the division in the class

## Index Pages
Maybe it does make sense after all to keep objects for the book

- [x] Design object
- [x] implement methods

- [x] Read and show many titles from list
- [x] Implement page change until list is over
	- [x] add page buttons images
	- [x] display them dynamically
	- [x] clicking the page button calls the right method.
	- [x] It shows the new screen and hides the old one
	- [x] call it from the show page method
- [?] Add an option to show consecutive answers as appends?
	- [x] No, if we want the next answer to reiterate on the previous by cutting it off, I'll just invent a syntax for it. Then it gets converted to strikethrough text with html when passing to the json.
- [ ] add a visual flair if question not seen
	- [ ] may require a rewrite of the grid
	- [ ] if the object rewrite works I maybe can use simple vboxes and handle the column splits in backend
	- [ ] make the unread pages bold and glow dark red. on hover just change the outline strength


## Refactoring
Backend
- [ ] Add an effect for unread questions (CHECK FACE), and remove it any time they are viewed by updating the dict.
	- [ ] ==Yo this shit actually needs a rewrite== 
		- [x] make a fucking page object
		- [x] give the page object a constructor that takes the dict and makes itself
		- [x] serialize it to json using `json.dumps(vars(page))`
		- [ ] give Taccuino a list of page objects and pass that around, divide them by topic
		- [ ] make the Taccuino class represent the full json
		- [ ] make all references to the dictionaries in the screens reference the object instead
		- [ ] make the external functions into methods
		- [ ] have a method to update the json with the current state of the Taccuino object
		- [ ] whenever a page is shown,  make it also update the status in the corresponding object and call the dump method of taccuino
		
Frontend
- [ ] Fix the way pages look for the title in the dictionary to use the key
- [ ] make the forward and backward flags not jump around so much
- [ ] unify code for left and right question pages. 
- [ ] Look into vpgrid for automatic gridding off question titles without needing to pad the list.

	
## Question Pages
- [x] Make the titles textbuttons
- [x] Make the buttons call a method to show the specific page
	- [x] Implement the method
	- [x] make button call it with the right arguments
	- [x] make the page screen template
		- [x] make check separator trigger at random if a flag is ticked
			- [x] complete it with horizontal shit
		- [x] manage frames to limit height variation
		- [x] manage fonts
		- [x] test with longer text
	- [x] If list end, right page is empty


## Making and reading the data
- [x] Make  a mock json
- [x] Read and show titles from json
- [x] get the real thing made
	- [x] gather all out text notes
	- [x] divide them in cats
	- [x] Only include ones relevant right now
	- [x] Generate real json from notes
	- [x] Remember to add empty page to json for odd cases
	- [x] Spell check all text files
- [ ] Once the flags start to change dynamically, make a way to generate the txt file from the json


## Unlocking the feature
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

