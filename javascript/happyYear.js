//Return the closest year with distinct values
function nextHappyYear(year){
    var toArray, duplicates;
    let happyYear = year + 1;
    while(true){
      toArray = happyYear.toString().split('');
      duplicates = toArray.filter((value, index) => 
      toArray.indexOf(value) != index)
      if(duplicates.length == 0){
        return happyYear
      }
      happyYear += 1;
  }
}