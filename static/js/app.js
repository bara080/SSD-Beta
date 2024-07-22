document.addEventListener('DOMContentLoaded', function () {
    const sideMenu = document.querySelector("aside");
    const profileBtn = document.querySelector("#profile-btn");
    const themeToggler = document.querySelector(".theme-toggler");
    const nextDay = document.getElementById('nextDay');
    const prevDay = document.getElementById('prevDay');
    const header = document.querySelector('header');
    const toggle = document.querySelector(".toggle");
    const modeSwitch = document.querySelector(".toggle-switch");
    const modeText = document.querySelector(".mode-text");
    const body = document.querySelector("body");
    const sidebar = document.querySelector(".sidebar");

    if (profileBtn && sideMenu) {
        profileBtn.onclick = function () {
            sideMenu.classList.toggle('active');
        };
    }

    window.onscroll = () => {
        if (sideMenu) {
            sideMenu.classList.remove('active');
        }
        if (header) {
            if (window.scrollY > 0) {
                header.classList.add('active');
            } else {
                header.classList.remove('active');
            }
        }
    };

    if (themeToggler) {
        themeToggler.onclick = function () {
            document.body.classList.toggle('dark-theme');
            themeToggler.querySelector('span:nth-child(1)').classList.toggle('active');
            themeToggler.querySelector('span:nth-child(2)').classList.toggle('active');
        };
    }

    let setData = (day) => {
        const tableBody = document.querySelector('table tbody');
        const timetableHeader = document.querySelector('.timetable div h2');
        if (tableBody && timetableHeader) {
            tableBody.innerHTML = ''; // To clear out previous table data
            let daylist = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
            timetableHeader.innerHTML = daylist[day];
            let schedule = []; // Replace with actual schedule data

            switch (day) {
                case 0: schedule = Sunday; break;
                case 1: schedule = Monday; break;
                case 2: schedule = Tuesday; break;
                case 3: schedule = Wednesday; break;
                case 4: schedule = Thursday; break;
                case 5: schedule = Friday; break;
                case 6: schedule = Saturday; break;
            }

            schedule.forEach(sub => {
                const tr = document.createElement('tr');
                const trContent = `
                    <td>${sub.time}</td>
                    <td>${sub.roomNumber}</td>
                    <td>${sub.subject}</td>
                    <td>${sub.type}</td>
                `;
                tr.innerHTML = trContent;
                tableBody.appendChild(tr);
            });
        }
    };

    let now = new Date();
    let today = now.getDay(); // Will return the present day in numerical value
    let day = today; // To prevent the today value from changing

    function timeTableAll() {
        const timetable = document.getElementById('timetable');
        if (timetable) {
            timetable.classList.toggle('active');
            setData(today);
            document.querySelector('.timetable div h2').innerHTML = "Today's Timetable";
        }
    }

    if (nextDay) {
        nextDay.onclick = function () {
            day <= 5 ? day++ : day = 0; // If else one liner
            setData(day);
        };
    }

    if (prevDay) {
        prevDay.onclick = function () {
            day >= 1 ? day-- : day = 6;
            setData(day);
        };
    }

    setData(day); // To set the data in the table on loading window
    const timetableHeader = document.querySelector('.timetable div h2');
    if (timetableHeader) {
        timetableHeader.innerHTML = "Today's Timetable"; // To prevent overwriting the heading on loading
    }

    // Toggle sidebar
    if (toggle) {
        toggle.addEventListener("click", () => {
            sidebar.classList.toggle("close");
            toggle.classList.toggle("rotate");
        });
    }

    // Dark mode
    const currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;

    if (currentTheme) {
        document.body.classList.add(currentTheme);

        if (currentTheme === 'dark-theme') {
            modeSwitch.classList.add('active');
            modeText.innerText = "Light Mode"; // Update text to indicate switching to light mode
        } else {
            modeText.innerText = "Dark Mode"; // Update text to indicate switching to dark mode
        }
    }

    if (modeSwitch) {
        modeSwitch.addEventListener('click', function () {
            document.body.classList.toggle('dark-theme');

            if (document.body.classList.contains('dark-theme')) {
                localStorage.setItem('theme', 'dark-theme');
                modeSwitch.classList.add('active');
                modeText.innerText = "Light Mode"; // Update text to indicate switching to light mode
            } else {
                localStorage.setItem('theme', 'light-theme');
                modeSwitch.classList.remove('active');
                modeText.innerText = "Dark Mode"; // Update text to indicate switching to dark mode
            }
        });
    }
});
