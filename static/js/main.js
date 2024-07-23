// TODO : SEARCH BUTTON


// document.addEventListener("DOMContentLoaded", () => {
//     console.log("Main JS loaded.");

//     const body = document.querySelector("body"),
//           sidebar = document.querySelector(".sidebar"),
//           toggle = document.querySelector(".toggle"),
//           searchBtn = document.querySelector(".search-box a"),
//           modeSwitch = document.querySelector(".toggle-switch"),
//           modeText = document.querySelector(".mode-text");

//     if (toggle) {
//         toggle.addEventListener("click", () => {
//             console.log("Testing toggling if it works");
//             sidebar.classList.toggle("close");
//         });
//     } else {
//         console.log("Toggle button not found");
//     }

//     if (searchBtn) {
//         searchBtn.addEventListener("click", (event) => {
//             event.preventDefault();
//             console.log("Testing search if it works");
//             sidebar.classList.remove("close");
//         });
//     } else {
//         console.log("Search button not found");
//     }

//     if (modeSwitch) {
//         modeSwitch.addEventListener("click", () => {
//             console.log("Testing mode switch if it works");
//             body.classList.toggle("dark");

//             if (body.classList.contains("dark")) {
//                 modeText.innerText = "Light Mode";
//             } else {
//                 modeText.innerText = "Dark Mode";
//             }
//         });
//     } else {
//         console.log("Mode switch not found");
//     }
// });

//   // TODO: REGISTER USER

//   // document.getElementById("registrationForm").addEventListener("submit", function(event) {
//   //     event.preventDefault();
//   //     var username = document.getElementById("username").value;
//   //     var email = document.getElementById("email").value;
//   //     var password = document.getElementById("password").value;
//   //     // You can perform further validation or send the form data to a server here
//   //     console.log("Username: " + username);
//   //     console.log("Email: " + email);
//   //     console.log("Password: " + password);
//   //     alert("Registration successful!");
//   // });

//   // TODO: SAVE USER NAME ON STORAGE
document.addEventListener("DOMContentLoaded", function() {
    let student_vs_advisor_data = JSON.parse(document.getElementById('student_vs_advisor_data').textContent);
    let student_semesters_data = JSON.parse(document.getElementById('student_semesters_data').textContent);
    let over_time_expenditure = JSON.parse(document.getElementById('over_time_expenditure').textContent);
    let labels = JSON.parse(document.getElementById('dates_label').textContent);

    let student_vs_advisor_chart = new Chart(document.getElementById('student_vs_advisor'), {
        type: 'pie',
        data: {
            labels: ['Advisors', 'Students'],
            datasets: [{
                label: "Student Vs Advisor",
                data: student_vs_advisor_data,
                backgroundColor: ['#5DA5DA', '#FAA43A', '#60BD68', '#B276B2', '#E16851', '#FB8267'],
                borderWidth: 1,
                hoverBorderColor: "black",
                hoverBorderWidth: 2,
                hoverBackgroundColor: 'rgba(154, 245, 140)',
                pointHoverRadius: 5
            }],
        },
        options: {
            title: {
                display: true,
                text: "Student Vs Advisor",
                fontSize: 20,
            },
            legend: {
                position: "right",
                labels: {
                    fontColor: "gray"
                },
                display: true,
            },
            elements: {
                hitRadius: 3,
            }
        }
    });

    let student_vs_semesters_chart = new Chart(document.getElementById('student_vs_semesters'), {
        type: 'bar',
        data: {
            labels: ['Spring', 'Summer', 'Fall', 'Winter'],
            datasets: [{
                label: "Semester Of Student",
                data: student_semesters_data,
                backgroundColor: ['#5DA5DA', '#FAA43A', '#60BD68', '#B276B2', '#E16851', '#FB8267'],
                borderWidth: 1,
                hoverBorderColor: "black",
                hoverBorderWidth: 2,
                hoverBackgroundColor: 'rgba(154, 245, 140)',
                pointHoverRadius: 5
            }],
        },
        options: {
            title: {
                display: true,
                text: "Student Semesters",
                fontSize: 20,
            },
            legend: {
                position: "right",
                labels: {
                    fontColor: "gray"
                },
                display: true,
            },
            elements: {
                hitRadius: 3,
            }
        }
    });

    new Chart(document.getElementById("student_courses"), {
        type: "line",
        data: {
            labels: labels,
            datasets: [{
                label: "Expenditure Over Time",
                data: over_time_expenditure,
                fill: false,
                borderColor: "rgb(75, 192, 192)",
                lineTension: 0.1
            }]
        },
        options: {}
    });
});