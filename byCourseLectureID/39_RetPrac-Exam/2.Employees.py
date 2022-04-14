import re
n = int(input())
imp_list = list()
temp_ord_list = list()
temp_message = ''
final_message = ''
final_print = list()
for i in range(n):
    imp_list.append(input())
for i, line in enumerate(imp_list):
    pattern1 = re.compile("(?P<firstname>^[A-Z][a-z]{2,})( )(?P<lastname>[A-Z][a-z]{2,})(#+)(?P<jobp1>[A-Z][a-z]+)([0-9]{2})(?P<Companyn1>[A-Z][a-zA-Z]+)( )(?P<Companyn2>JSC|Ltd.)")
    pattern2 = re.compile("(?P<firstname>^[A-Z][a-z]{2,})( )(?P<lastname>[A-Z][a-z]{2,})(#+)(?P<jobp1>[A-Z][a-z]+)&(?P<jobp2>[A-Z][a-z]+)([0-9]{2})(?P<Companyn1>[A-Z][a-zA-Z]+)( )(?P<Companyn2>JSC|Ltd.)")
    pattern3 = re.compile("(?P<firstname>^[A-Z][a-z]{2,})( )(?P<lastname>[A-Z][a-z]{2,})(#+)(?P<jobp1>[A-Z][a-z]+)&(?P<jobp2>[A-Z][a-z]+)&(?P<jobp3>[A-Z][a-z]+)([0-9]{2})(?P<Companyn1>[A-Z][a-zA-Z]+)( )(?P<Companyn2>JSC|Ltd.)")
    if pattern1.match(line):
        first_name = pattern1.search(line).group("firstname")
        last_name = pattern1.search(line).group("lastname")
        job_position = pattern1.search(line).group("jobp1")
        company = pattern1.search(line).group("Companyn1") + " " + pattern1.search(line).group("Companyn2")
        final_print.append(f"{first_name} {last_name} is {job_position} at {company}")
    elif pattern2.match(line):
        first_name = pattern2.search(line).group("firstname")
        last_name = pattern2.search(line).group("lastname")
        job_position = pattern2.search(line).group("jobp1") + " " + pattern2.search(line).group("jobp2")
        company = pattern2.search(line).group("Companyn1") + " " + pattern2.search(line).group("Companyn2")
        final_print.append(f"{first_name} {last_name} is {job_position} at {company}")
    elif pattern3.match(line):
        first_name = pattern3.search(line).group("firstname")
        last_name = pattern3.search(line).group("lastname")
        job_position = pattern3.search(line).group("jobp1") + " " + pattern3.search(line).group("jobp2") + " " + pattern3.search(line).group("jobp3")
        company = pattern3.search(line).group("Companyn1") + " " + pattern3.search(line).group("Companyn2")
        final_print.append(f"{first_name} {last_name} is {job_position} at {company}")
print(*final_print, sep='\n')
