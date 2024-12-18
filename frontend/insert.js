document.addEventListener("DOMContentLoaded", function () {
    // Attach the event listener to the form
    const insertForm = document.getElementById("insertForm");
    
    if (!insertForm) {
        console.error("Insert form not found");
        return;
    }

    insertForm.addEventListener("submit", async function (event) {
        event.preventDefault(); // Prevent default form submission

        // Get form data
        const username = document.getElementById("username").value.trim();
        const designation = document.getElementById("designation").value;

        if (!username || !designation) {
            alert("Please fill in all fields.");
            return;
        }


    const payload = {
        emp_data: [
            {
                username: username,
                designation: designation
            }
        ]
    };
 

    try {
        const response = await fetch(`${apiUrl}insert`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            const result = await response.json();
            alert("Data submitted successfully!");
            location.reload()
        } else {
            alert("Error submitting data!");
            location.reload()
        }
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred!");
        location.reload()
        
    }
});

});