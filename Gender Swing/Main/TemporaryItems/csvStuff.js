const csvFilePath = 'Main/Statistics/gender_diff.csv';
const csvDelimiter = ',';
const csvNewLine = '\n';

// Use the fetch API to read the contents of the CSV file
fetch(csvFilePath)
  .then(response => response.text())
  .then(csvString => {
    // Split the CSV string into an array of rows
    const rows = csvString.trim().split(csvNewLine);

    // Loop through each row and split it into an array of values
    const values = rows.map(row => row.split(csvDelimiter));

    // Create a string by joining all rows with the new line character
    const csvAsString = values
      .map(row => row.join(csvDelimiter))
      .join(csvNewLine);

    // Output the CSV string to the console
    console.log(csvAsString);
  });
