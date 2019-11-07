//Given a string, replace Polish letters 
function correctPolishLetters (string) {
    const dia = "ąćęłńóśźż";
    const rep = "acelnoszz"
    for(const el of string){
      if(dia.includes(el)){
        string = string.replace(el, rep[dia.indexOf(el)])
      }
    }
    return string
}
    
          
  