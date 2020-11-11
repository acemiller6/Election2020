# Election2020
Edison data in JSON format for all 50 states.  Python code to process the JSON files

Hat tip to user PedeInspector over at the thedonald.win for most of this.  I have taken what he provided there and made some additional changes to the Python code.  There are 2 main things that I am extracting from the JSON files.  
  1. Lost votes :  This is when the vote total as reported by Edison shrinks from 1 update to the next
  2. Switched votes : This is when votes are changed from Trump to Biden from 1 update to the next

To run this code, you need to call **edisonWrapper.py** and pass in the state you want to inspect.  The state names are not always as you might think.  For instance Tennessee is just 'tenn'.  You can get a listing of all the names you can use with the -h option.
