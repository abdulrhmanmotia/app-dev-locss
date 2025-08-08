from django.shortcuts import render

def index(request):
    name = {"fname": "Abdulrhman Sinan"}
    return render(request, 'index.html', name)

def home(request):
    return render(request, 'home.html')

def list_students(request):
    students_list = [
        {
            "id": 1,
            "name": " عبدالرحمن سنان",
            "marks": [90, 95, 98, 97],
            "eachsub": {
                "Software Engineering": 96,
                "Image Processing": 94,
                "Client and Server Programming": 96
            }
        },
        {
            "id": 2,
            "name": "أحمد محمد",
            "marks": [85, 92, 88, 95],
            "eachsub": {
                "Software Engineering": 88,
                "Image Processing": 90,
                "Client and Server Programming": 92
            }
        },
        {
            "id": 3,
            "name": "سارة علي",
            "marks": [92, 94, 96, 98],
            "eachsub": {
                "Software Engineering": 95,
                "Image Processing": 93,
                "Client and Server Programming": 97
            }
        }
    ]
    return render(request, 'showstudents.html', {'students': students_list})

def edit_students(request):
    students_list = [
        {
            "id": 1,
            "name": " عبدالرحمن سنان",
            "total": 286,
            "marks": {
                "Software Engineering": 96,
                "Image Processing": 94,
                "Client and Server Programming": 96
            }
        },
        {
            "id": 2,
            "name": "أحمد محمد",
            "total": 275,
            "marks": {
                "Software Engineering": 88,
                "Image Processing": 90,
                "Client and Server Programming": 92
            }
        }
    ]
    return render(request, 'editstudents.html', {'students': students_list})

def delete_students(request):
    students_list = [
        {"id": 1, "name": "Abdulrhman Sinan"},
        {"id": 2, "name": "أحمد محمد"},
        {"id": 3, "name": "سارة علي"}
    ]
    return render(request, 'deletestudents.html', {'students': students_list})