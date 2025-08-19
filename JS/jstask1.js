function sumNumbersInString(str) {
    let sum = 0;
    let temp = "";

    for (let char of str) {
        if (!isNaN(char) && char !== " ") { 
            temp += char; 
        } else {
            if (temp !== "") {
                sum += parseInt(temp);
                temp = "";
            }
        }
    }

    if (temp !== "") {
        sum += parseInt(temp);
    }

    return sum;
}

console.log(sumNumbersInString("foo8bar8cat2tc2"));
console.log(sumNumbersInString("ab12cd34ef5")); 
