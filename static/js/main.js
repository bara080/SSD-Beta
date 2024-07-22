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


// TODO : ADD DOM LOADING FOR THE METRICS

document.addEventListener("DOMContentLoaded", function() {
    let income_vs_expense_data = JSON.parse(document.getElementById('income_vs_expense_data').textContent);
    let income_category_data = JSON.parse(document.getElementById('income_category_data').textContent);
    let over_time_expenditure = JSON.parse(document.getElementById('over_time_expenditure').textContent);
    let labels = JSON.parse(document.getElementById('dates_label').textContent);

    // Chart.scaleService.updateScaleDefaults('linear', {
    //     ticks: {
    //         min: 0
    //     }
    // });

    let income_vs_expense_chart = new Chart(document.getElementById('income_vs_expense'), {
        type: 'pie',
        data: {
            labels: ['expense', 'income'],
            datasets: [{
                label: "Income Vs Expenses",
                data: income_vs_expense_data,
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
                text: "Income Vs Expenses",
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

    let income_vs_category_chart = new Chart(document.getElementById('income_vs_category'), {
        type: 'bar',
        data: {
            labels: ['investment', 'rent', 'salary', 'side_hustle'],
            datasets: [{
                label: "Categories Of Income",
                data: income_category_data,
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
                text: "Income Categories",
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

    new Chart(document.getElementById("overtime_expenditure"), {
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
