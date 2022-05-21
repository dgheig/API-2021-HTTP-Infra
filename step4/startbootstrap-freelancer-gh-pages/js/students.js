$(() => {
    console.log("Loading students");

    function loadStudents() {
        $.getJSON("/api/students", (students) => {
            console.log(students);
            var message = "Nobody";
            if(students) {
                console.log(students[0]);
                const {firstName, lastName} = students[0];
                message = `${firstName} ${lastName}`
            }
            $(".masthead-subheading").text(message);
        })
    };
    loadStudents();
    setInterval(loadStudents, 2000);
})
