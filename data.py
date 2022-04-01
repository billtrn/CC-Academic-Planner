import json

with open("classes.json", "r") as f:
    course_data = json.load(f)


def toString(crn):
    return "  ".join(
        [
            course_data[crn]["dept"],
            course_data[crn]["code"],
            course_data[crn]["name"],
            course_data[crn]["section"],
        ]
    )


def getDepartmentList():
    departments = set()
    for course in course_data:
        departments.add(course_data[course]["dept"])
    return list(departments)


def getCourseList():
    courses = []
    for course in course_data:
        courses.append(toString(course))
    return courses


def getDeptCourses(dept):
    if dept == "ALL DEPTS":
        return getCourseList()
    else:
        dept_courses = []
        for course in course_data:
            if course_data[course]["dept"] == dept:
                dept_courses.append(toString(course))
        return dept_courses


def getAttr(crn):
    attrs = course_data[crn]["attrs"]
    if attrs:
        return course_data[crn]["attrs"].strip().split(", ")
    else:
        return []


def getCRN(dept, num, sect):
    for course in course_data:
        if course_data[course]["dept"] == dept and \
                course_data[course]["code"] == num and \
                course_data[course]["section"] == sect:
            return course


def getDays(crn):
    dates = course_data[crn]["date"]
    if len(dates) >= 2:
        return [" ".join(dates)]
    else:
        return [" ".join(dates[0])]


def getTimes(crn):
    times = []
    for time in course_data[crn]["time"]:
        start, end = time.split(" - ")
        times.append(f"{_convert_time(start)}-{_convert_time(end)}")
    return times


def getCredits(crn):
    return int(float(course_data[crn]["credits"]))


def _convert_time(time):
    time_, sign = time.strip().split()
    hour, minute = time_.split(":")
    if sign == "pm":
        return str((12 + int(hour)) * 100 + int(minute))
    else:
        converted_time = int(hour) * 100 + int(minute)
        if converted_time < 1000:
            return "0" + str(converted_time)
        else:
            return str(converted_time)
