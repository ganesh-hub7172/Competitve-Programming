function getRow(rowIndex) {
    const row = [1]; // First element is always 1

    for (let i = 1; i <= rowIndex; i++) {
        // Compute next element using previous one
        const nextVal = row[i - 1] * (rowIndex - i + 1) / i;
        row.push(nextVal);
    }

    return row;
}

// Examples
console.log(getRow(3)); // Output: [1, 3, 3, 1]
console.log(getRow(0)); // Output: [1]
console.log(getRow(1)); // Output: [1, 1]
