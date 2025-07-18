# Resume Ranker
#### Video Demo:  https://youtu.be/jrS2jLgchp8
#### Description:    TODO
## Introduction:
my project parses resumes for skills you're hiring for and ranks them based on number of skills matched. Additionally it also parses for phone number and email. the ranked resumes alsog with other details are stored in a csv. I choose as it was simple but complex enough and it included almost everything I learned in the course.

## Features:
- skill extraction
- phone number extraction
- email extraction
- ranks based on skills matched ann prints it
- results stored in a csv

## Project Files:
 - `resume_parser.py`: logic for parsing and ranking resumes
 - `skills.txt`: list of skills you're hiring for
 - `test_project.py`: pytest file to test functions
 - `results.csv`: stores ranked results with other details
 - `resumes/`: folder containing example resume files

## How It Works
- How the program flows step by step:
  1. Read resumes and skill list
  2. Extract email, phone, and skills from resumes
  3. Score based on skills matched
  4. Ranking the resumes based on scores
  5. printing the results and storing results in CSV

## Walkthrough of the Program
- The main function first loads folder of resumes whose location you give
- then the skills from the file containig the skills whose location you giveare extracted
- then it lops throught resumes. For each resume:
 - it extracts text and further spits into words
 - from the words it matches for skills
 - extracts email
 - extracts phone number
- each resumes details (like filename, skills, email, phone number, score) are storedin a list of dicts
- the list of dict is then sorted based in the score key of each resume dict
- the sorted resumes filenames is then printed from highest to owest score
- the sorted resumes along with emails, phone numbers etc are stored in a csv

## Code Highlights
 - Extracting test from resumes using pymupdf
 - Use of regex for phone and email
 - using regex for finding and combining 2 word skills
 - How you sort by score
 - How tests are written and structured for more compes programs

## Design Decisions
- uses only pdf's for resumes as they are more simpler to work with not Docx formated resumes
- Add more folders of resumes and skills list for hiring of diffrent positions but be sure to input correct addresses of folders and skills list
- edge cases i handled
  - matching for 2 word sills not ony 1 word skills
  - after extracting files i further extracted only wrd leaving spaces, new lines to avoid unnecessary ooping and easy matching of keywrds
  - matching skills case insensitively
  - Matching and capturng country codes in phone numbers
  - not matching skills which are repeated in resume
- edge cases i didn’t handle
  - Scoring and ranking based on work experence or number of projects done
  - No error handeling when you give resumes which are not pdf's

## Testing
- Test file has 4 testing function which test 4 different functions
- functions tested:
 - results
 - get_skills
 - rank
 - combine_words
- tested only on if the function ouput is equal to expected output
- Mention tools used: `pytest`

## Possible Improvements
- Handle DOCX resumes
- Use NLP for smarter skill matching
- Build a simple command-line interface
- Add GUI or web version

## Conclusion
- working with new modules like pymupdf, os
- File io in more depth
- writing code more in pythonic way
