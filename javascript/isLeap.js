//Given a year, check if it's a leap year
function isLeapYear(year) {
  if(year % 4 == 0){
    if(year % 100 != 0){ return true }
  else if(year % 400 == 0){ return true }
  }
  return false
}