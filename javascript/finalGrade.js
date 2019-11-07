/*Create a function finalGrade, which calculates the final grade 
of a student depending on two parameters: a grade for the exam and
a number of completed projects.
*/
function finalGrade (exam, projects) {
    let finalGrade = 0;
    if(exam > 90 || projects > 10){
      finalGrade = 100}
    else if (exam > 75 && projects >= 5){
      finalGrade = 90}
    else if(exam > 50 && projects >= 2){
      finalGrade = 75}
    else{
      finalGrade = 0}
    return finalGrade;
  }