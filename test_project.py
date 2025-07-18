import pytest
from finalProject.project import results, get_skills, rank, combine_words

# resumes = [[{'filename': 'test resume.pdf', 'skills': [Tinkercad, AutoCAD], 'email': 'harper.stewart@gmail.com', 'phone': '(351)682-9937', 'score': 2}, ]]
def test_results():
    assert results([{'filename': 'engineering-manager-resume-example.pdf', 'skills': [], 'email': 'yourname@email.com', 'phone': '(351)682-9937', 'score': 0},
                 {'filename': 'engineering-resume-example.pdf', 'skills': ['Autocad'], 'email': 'harper.stewart@gmail.com', 'phone': '(323)721-1984', 'score': 1},
                 {'filename': 'test resume.pdf', 'skills': ['Autocad', 'Tinkrcad'], 'email': 'harper.stewart@gmail.com', 'phone': '(351)682-9937', 'score': 2}]) == None
def test_get_skills():
    assert get_skills("/workspaces/172884394/finalProject/skill.txt") == ['Java', 'python', 'javascript', 'deep learning', 'sql']

def test_rank():
    assert rank([{'filename': 'engineering-manager-resume-example.pdf', 'skills': [], 'email': 'yourname@email.com', 'phone': '(351)682-9937', 'score': 0},
                 {'filename': 'engineering-resume-example.pdf', 'skills': ['Autocad'], 'email': 'harper.stewart@gmail.com', 'phone': '(323)721-1984', 'score': 1},
                 {'filename': 'test resume.pdf', 'skills': ['Autocad', 'Tinkrcad'], 'email': 'harper.stewart@gmail.com', 'phone': '(351)682-9937', 'score': 2}]) == [{'filename': 'test resume.pdf', 'skills': ['Autocad', 'Tinkrcad'], 'email': 'harper.stewart@gmail.com', 'phone': '(351)682-9937', 'score': 2},
                      {'filename': 'engineering-resume-example.pdf', 'skills': ['Autocad'], 'email': 'harper.stewart@gmail.com', 'phone': '(323)721-1984', 'score': 1},
                      {'filename': 'engineering-manager-resume-example.pdf', 'skills': [], 'email': 'yourname@email.com', 'phone': '(351)682-9937', 'score': 0}]

def test_combine_words():
    assert combine_words('process', 'engineer', ['process engineer', 'python', 'javascript', 'deep learning', 'sql'], ['process', 'engineer']) == 'process engineer'

