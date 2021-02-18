duration = int(input('Insert duration in seconds: '))

seconds = int(duration % 60)
minutes = int(duration % 3600 / 60)
hours = int(duration % 86400 / 3600)
days = int(duration % 604800 / 86400)
weeks = int(duration % 2678400 / 604800)
months = int(duration % 31622400 / 2678400)
years = int(duration // 31622400)

print('<y>', years, '<m>', months, '<w>', weeks, '<d>', days, '<h>', hours, '<m>', minutes, '<s>', seconds)
