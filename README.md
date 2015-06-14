# TedTalks
Curated List of Good TED Talks

This project was started in high school when I watched a bunch of TED talks and wanted to keep track of the ones I really liked. It started as just a simple list, but categories soon formed.

Later in life, enough friends asked me to share my list with them that I was nudged to sharing it online. Not one for writing many words, a blog did not appeal to me,
but just posting [a barebones list](Good Ted Talks.md) was enough.

However, the categories I used to have no longer made sense, but the number of talks I wanted to share was just a smidge too large to make re-sorting them easy.
Naturally, the first solution I reached for was to cluster them based on their transcripts, which brings me to the current state of this project.

### Notes

#### VirtualEnv setup
`source venv/bin/activate`

#### Testing distance computation
`python compute_distances.py`

#### Storing requirements
`pip freeze > requirements.txt`

### TODO
- Populate database with objects
- Scrape transcripts of talks to html files
- Add function to add a new talk to the database
- Basic web server to serve same content on a website

- Draft designs for UI
- Build basic D3 web animation
- Add spring physics based on weights

- Investigate clustering algorithms
  - TF-IDF with hiercharchical clustering?
  - LDA?
- Implement TF-IDF hierarchical algorithm that outputs similarity scores
- Determine aesthetically pleasing parameters
  - Term-frequency metric
  - Cut-off for including edges
