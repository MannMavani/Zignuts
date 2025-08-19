function sumCommaSeparatedNumbers(str) {
    let numbers = str.split(",").map(num => parseFloat(num));
    return numbers.reduce((sum, num) => sum + num, 0);
}

console.log(sumCommaSeparatedNumbers("1.5, 2.3, 3.1, 4, 5.5, 6, 7, 8, 9, 10.9"));
