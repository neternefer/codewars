function toCamelCase(str){
    /**
     * Convert dash/underscore delimited words into camel casing. 
     * The first word within the output should be capitalized only if 
     * the original word was capitalized (known as Upper Camel Case, 
     * also often referred to as Pascal case). 
     * The next words should be always capitalized.

        Examples
        "the-stealth-warrior" gets converted to "theStealthWarrior"

        "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

        "The_Stealth-Warrior" gets converted to "TheStealthWarrior"
     */
    return str.split(/[\-\_]/).map((e, i, arr) => {
            i != 0 ? arr[i] = e[0].toUpperCase() + e.slice(1) : arr[i];
    }).join("");
    // return arr;
}

console.log(toCamelCase("The-stealth-warrior"));