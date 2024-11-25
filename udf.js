function transform(line) {
    // Split the line into values
    var values = line.split(',');

    // Ensure the line has at least 3 fields
    if (values.length < 3) {
        console.error("Invalid line: ", line);
        return null; // Skip malformed lines
    }

    // Create an object with the parsed values
    var obj = new Object();
    obj.rank = parseInt(values[0]) || 0; // Default rank to 0 if missing or invalid
    obj.name = values[1].trim(); // Remove extra spaces from player name
    obj.country = values[2].trim().toUpperCase(); // Standardize country names to uppercase

    // Add derived metrics
    obj.isTopPlayer = obj.rank <= 10; // Flag for top-ranked players

    // Convert to JSON string and return
    var jsonString = JSON.stringify(obj);
    return jsonString;
}
