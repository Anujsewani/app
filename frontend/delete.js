document.getElementById("deleteForm").addEventListener("submit", async function (event) {
    event.preventDefault();
    if (event.target.id !== "deleteForm") return; 
    const empId = document.getElementById("deleteEmpID").value;
    let url = `http://127.0.0.1:5000/delete?empID=${empId}`;

    try {
        const response = await fetch(url,{method: "DELETE"});
        const result = await response.json();

        // const readResults = document.getElementById("readResults");
        // readResults.innerHTML = ""; // Clear previous results

        if (response.ok) {
           alert(result.message|| "Data Deleted Successfully")
           location.reload()
            
        } else {
            // If there's an error in the result, show it
            alert(result.error || "Error Deleting Data");
            location.reload()
        }
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred while deleting the data!");
        location.reload()
    }
});