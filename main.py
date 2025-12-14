from pyscript import document

# information of clubs
club_info = {
	"marching_band": {
		"name": "Marching Band",
		"adviser": "Mr. Emilio Alumno",
		"venue": "Band Room",
		"schedule": "Tuesday & Wednesday 3:00 PM - 4:30 PM",
	},
	"glee_club": {
		"name": "Glee Club",
		"adviser": "Mr. Denver Martin",
		"venue": "High School Music Room",
		"schedule": "Monday 3:00 PM - 5:00 PM",
	},
	"dance_club": {
		"name": "Dance Club",
		"adviser": "Mr. Alfred Cases",
		"venue": "Teatro Preciosa",
		"schedule": " Tuesday 3:00 PM - 5:00 PM",
	},
	"math_club": {
		"name": "Math Club",
		"adviser": "Mr. Nicole Gabuya",
		"venue": "Room 404",
		"schedule": "Monday 2:30 PM - 3:00 PM",
	},
	"science_club": {
		"name": "Science Club",
		"adviser": "Ms. Jameelyn Maramag",
		"venue": "Room 404",
		"schedule": "Tuesday 3:00 PM - 4:00 PM",
	},
	"comm_art_club": {
		"name": "Communications Art Club",
		"adviser": "Ms. Yannis Fernandez",
		"venue": "Room 406",
		"schedule": "Wednesday 3:00 - 4:00 PM, Friday 3:00 - 4:00 PM",
	},
	"cocc": {
		"name": "COCC",
		"adviser": "SSgt. Jemima David PA (Res)",
		"venue": "Quadrangle/ Teatro Preciosa",
		"schedule": "Wednesday 2:30 - 4:30 PM",
	},
	"social_science": {
		"name": "Social Science Club",
		"adviser": "Mr. Roberto Lim",
		"venue": "Room 409",
		"schedule": "Tuesday 03:00 - 4:00 PM",
	},
	"volleyball_varsity": {
		"name": "Volleyball Varsity",
		"adviser": "Mr. Adrian Ruiz",
		"venue": "Quadrangle",
		"schedule": "Wednesday 03:00 - 04:00 PM",
	},
	"basketball_varsity": {
		"name": "Basketball Varsity",
		"adviser": "Mr. Adrian Ruiz",
		"venue": "Quadrangle",
		"schedule": "Monday 03:00 - 04:00 PM",
	},
}
def render_club_html(key: str) -> str:
    info = club_info.get(key)
    if not info:
        return "<em>Please select a club to see details.</em>"

    html = (
        f"<h2>{info['name']}</h2>"
        f"<p><strong>Adviser:</strong> {info['adviser']}</p>"
        f"<p><strong>Venue:</strong> {info.get('venue', '')}</p>"
    )

    schedule = info.get('schedule')
    if schedule:
        html += f"<p><strong>Schedule:</strong> {schedule}</p>"

    return html


def school_club_information(e=None):
	select = document.getElementById('club-select')
	if not select:
		return
	key = select.value
	details = document.getElementById('club-details')
	details.innerHTML = render_club_html(key)

document.defaultView.school_club_information = school_club_information

#  message
school_club_information()
