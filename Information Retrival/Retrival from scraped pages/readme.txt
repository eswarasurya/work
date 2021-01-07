Movie Inspection

The source code is contained in the file movie_inspection.py

This python code ranks the documents based on a query and shows the top 10 results
If the query is a movie name then it shows the rating of the movie

The query is hardcoded in the program (can be found in the main function). If an incorrect query or a query from out of the scope is given nothing will be printed on the console. 

The output contains document ids of the relevant documents and the titles of those documents.
If the query matches a movie title then the output also contains its ratings.

If the code is running for the first time on the dataset the comment part in the main function needs to be uncommented. This generates the files “output.txt” and “titles.txt”. These files are already included in the code folder so no need to uncommit the code unless the dataset is changed.

The dataset is contained in the folder named “pages”
The dataset folder, output.txt, titles.txt and the python code should be in the same folder.

Few sample queries:
Inception
Leonardo DiCaprio
Avengers
Thor
Robert Downey
Titanic
