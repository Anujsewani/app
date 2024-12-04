document.querySelector("form").addEventListener("submit", async function (event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const designation = document.getElementById("designation").value;

    const payload = {
        emp_data: [
            {
                //empID: 2, 
                username: username,
                designation: designation
            }
        ]
        // username: username,
        // designation: designation
    };
   // console.log("Payload:", payload); // Debug payload

    try {
        const response = await fetch("http://127.0.0.1:5000/insert",{
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            const result = await response.json();
            alert("Data submitted successfully!");
        } else {
            alert("Error submitting data!");
        }
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred!");
    }
});