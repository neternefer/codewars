/* Return a list of string values stating whether the respective
 member is to be placed in the senior (age >= 55, handicap > 7)
 or open category*/
function openOrSenior(data){
  return data.map(function(elem){
    return (elem[0] >= 55 && elem[1] > 7) ? 'Senior' : 'Open'});
}