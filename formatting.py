def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
  return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(
  author, title, original_work, publishing_date
)

print(my_beard_description)

The poem Where the Sidewalk Ends by My Beard was originally published in 1974 in Shel Silverstein.


highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(',')

highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())

print(highlighted_poems_stripped)

# Step 6 create list of lists
highlighted_poems_details = []
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))

titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])

for i in range(0,len(highlighted_poems_details)):
  print("The poem {} was published by {} in {}".format(titles[i],poets[i],dates[i]))

#Output final 
['Afterimages:Audre Lorde:1997', 'The Shadow:William Carlos Williams:1915', 'Ecstasy:Gabriela Mistral:1925', 'Georgia Dusk:Jean Toomer:1923', 'Parting Before Daybreak:An Qi:2014', 'The Untold Want:Walt Whitman:1871', "Mr. Grumpledump's Song:Shel Silverstein:2004", 'Angel Sound Mexico City:Carmen Boullosa:2013', 'In Love:Kamala Suraiyya:1965', 'Dream Variations:Langston Hughes:1994', 'Dreamwood:Adrienne Rich:1987']
The poem Afterimages was published by Audre Lorde in 1997
The poem The Shadow was published by William Carlos Williams in 1915
The poem Ecstasy was published by Gabriela Mistral in 1925
The poem Georgia Dusk was published by Jean Toomer in 1923
The poem Parting Before Daybreak was published by An Qi in 2014
The poem The Untold Want was published by Walt Whitman in 1871
The poem Mr. Grumpledump's Song was published by Shel Silverstein in 2004
The poem Angel Sound Mexico City was published by Carmen Boullosa in 2013
The poem In Love was published by Kamala Suraiyya in 1965
The poem Dream Variations was published by Langston Hughes in 1994
The poem Dreamwood was published by Adrienne Rich in 1987












