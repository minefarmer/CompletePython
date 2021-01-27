courses = {
    "js": "Javascript 101",
    "python": ["Python 101", "Python 201"],
    "html": "html 101"
}
print(courses.get("js", None))  # Javascript 101

print(courses.get("css", None))  # None

print(courses.get("css", "Default text in here"))  # Default text in here

print(courses.get("css", "CSS 101"))  # CSS 101 same as above 'Default text in here'
