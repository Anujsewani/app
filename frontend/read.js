document.getElementById("readForm").addEventListener("submit", async function (event) {
    event.preventDefault();
    if (event.target.id !== "readForm") return; 
    const empId = document.getElementById("empID").value;
    let url = `http://127.0.0.1:5000/read?empID=${empId}`;

    try {
        const response = await fetch(url);
        const result = await response.json();

        const readResults = document.getElementById("readResults");
        readResults.innerHTML = ""; // Clear previous results

        if (response.ok && result.result) {
            // If data is fetched successfully, display it
            const record = document.createElement("p");
            record.textContent = JSON.stringify(result.result, null, 2);
            readResults.appendChild(record);
            
        } else {
            // If there's an error in the result, show it
            alert(result.error || "Record not found!");
        }
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred while fetching the data!");
    }
});
