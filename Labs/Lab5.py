str=input("Type in your sentence or phrase!: ");
vowels=0
consonants=0
for i in str:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vowels=vowels+1;
    else:
        consonants=consonants+1;
        
print("This is the number of vowels in your input:",vowels);

print("\nAnd here is the number of consonants:",consonants);
