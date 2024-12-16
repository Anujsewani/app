document.addEventListener("DOMContentLoaded", function () {
    // Attach the event listener to the form
    const updateForm = document.getElementById("updateForm");

    if (!updateForm) {
        console.error("Update form not found");
        return;
    }

    updateForm.addEventListener("submit", async function (event) {
        event.preventDefault(); // Prevent default form submission

        // Get form data
        const username = document.getElementById("update-username").value.trim();
        const designation = document.getElementById("update-designation").value;
        const empId = document.getElementById("updateEmpID").value;
        console.log("Username:", username);
        console.log("Designation:", designation);
        console.log("EmpID:", empId);


        if (!username || !designation) {
            alert("Please fill in all fields.");
            return;
        }

        const payload = {
            empID: parseInt(empId), // Ensure empID is a number
            updated_data: {
                username: username,
                designation: designation,
            },
        };

    
    try {
        
        const response = await fetch(`${apiUrl}update`,{
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            const result = await response.json();
            alert("Data updated successfully!");
            location.reload()
        } else {
            alert("Error updating data!");
            location.reload()
        }
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred!");
        location.reload()
        
    }
});

});