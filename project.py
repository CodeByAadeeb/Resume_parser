import re
import pymupdf
import os
from csv import DictWriter

resumes = []
def main():
    # 1. Prompt user for:
    #    - Resume folder path
    folder = input("Enter the folder path containing PDF resumes: ")
    #    - Skills list file (default: skills.txt)
    skills = input("Enter path to skills list file (default: skills.txt): ")

    # 2. Load skills from the skills file into a list
    skills_list = get_skills(skills)
    #print(skills_list)


    # 3. For each PDF file in the resume folder:
    for pdf in os.listdir(folder):

        #    a. Extract text using PyMuPDF
        with pymupdf.open(os.path.join(folder, pdf)) as doc:
            text = ""
            Matched_skills = []
            Matched_skills_count = 0
            num = ""
            for page in doc:
                text += page.get_text()
                extracted_words = re.split(r"[ \n]+", text)

            # b. Parse for:
            for j, word in enumerate(extracted_words):

                if j<len(extracted_words)-1:
                    word2 = extracted_words[j+1]
                    word = combine_words(word, word2, skills_list, extracted_words)

                # Matched skills (from skills list)
                if word.lower() in [skill.lower() for skill in skills_list]:
                    if word not in Matched_skills:
                        Matched_skills_count += 1
                        Matched_skills.append(word)

                    # (Optional) Email using regex
                if match := re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', word):
                    email = word

                    # (Optional) Phone number using regex
                if num_match:= re.search(r"(^\(?[0-9][0-9]?[0-9]?[0-9]?[0-9]?\)?[ .-]?[0-9][0-9]?[0-9]?[0-9]?[0-9]?[ .-]?[0-9][0-9]?[0-9]?[0-9]?[0-9]?[ .-]?[0-9][0-9]?[0-9]?[0-9]?[0-9]?$)", word):
                    num += num_match.group(1)

            # 4. Store results (filename, matched skills, email, score)
            resumes.append({"filename": pdf, "skills": Matched_skills, "email": email, "phone": num, "score": Matched_skills_count})



    # 5. Sort results by score (highest to lowest)
    results(resumes)

def results(resumes):
    i = 1
    with open("results.csv", "w") as file:
        writer = DictWriter(file, fieldnames=["filename","skills","email","phone","score"])
        writer.writeheader()

        for cand in rank(resumes):
            # 6. Print top candidates in terminal
            print(f"{i} {cand["filename"]}")
            i = i + 1
            # 7. Save results to results.csv file
            writer.writerow(cand)


    #       - (Optional) Experience years
def get_skills(a):
     x = []
     with pymupdf.open(a, filetype="txt") as doc:
        for page in doc:
            text = page.get_text()
            x.extend(re.findall(r'"(.*?)"', text))

        return x

def combine_words(word, word2, skills_list, extrcted_words):
    # if there is space in any word in skills list
    spaced_skills = []
    for space in skills_list:
        if " " in space:
            # store those words in another list
            spaced_skills.append(space)

    # take each word from new list and split on space and only store the first word in another new list
    first_word = []
    second_word = []
    for words in spaced_skills:
        first, second = words.split(" ")
        first_word.append(first)
        second_word.append(second)


    # check for 1st part of a number
    first_num = re.search(r"^\+?[0-9][0-9]?[0-9]?[0-9]?$", word)
    if first_num:
        j = extrcted_words.index(word) # use the nest wrd from resume ot extrcted_words
        word += extrcted_words[j+1]

    # check if word in the new 1st word list and word+1 in
    if word in first_word and word2 in second_word:
        word += " "
        word += word2
    return word

def rank(b):
    return sorted(b, key=lambda score: score["score"], reverse=True)

if __name__=="__main__":
    main()


# /workspaces/172884394/finalProject/resume_folder
# /workspaces/172884394/finalProject/skill.txt
