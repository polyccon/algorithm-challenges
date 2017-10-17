// PIG LATIN

//Translate the provided string to pig latin.
//Pig Latin takes the first consonant (or consonant cluster) of an English word, moves it to the end of the word and suffixes an "ay".
//If a word begins with a vowel you just add "way" to the end.
//Input strings are guaranteed to be English words in all lowercase.

function isVowel(char) {
   return (char === "a" || char === "o" || char === "e" || char === "i" || char === "u");
}
function firstvowelindex (str){
  for (i=1; i<str.length; i++){
      if (isVowel(str[i])){
        return i;
      }
  } return 0;
}
function translatePigLatin(str) {

  if (isVowel(str[0])){
    return str+'way';
  }
  else {
      var i = firstvowelindex(str);
        return str.substr(i,str.length-1)+str.substr(0,i)+'ay';
      }
}


translatePigLatin("california"); //should return "aliforniacay".
translatePigLatin("paragraphs"); //should return "aragraphspay".
translatePigLatin("glove"); //should return "oveglay".
translatePigLatin("algorithm"); //should return "algorithmway".
translatePigLatin("eight"); //should return "eightway".
