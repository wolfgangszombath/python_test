s = 'bla [wichtig] und mehr bla bla'
start = s.find('[')
end = s.find(']')+1
wichtig = s[start:end]
print(wichtig)
#oder
start = s.index('[')
end = s.index(']') + 1
wichtig = s[start:end]
print(wichtig)