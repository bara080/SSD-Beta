from flask import Blueprint, render_template, request, redirect, url_for
from app.services.advisor_services import create_advisor, read_advisor, update_advisor, delete_advisor

advisor_bp = Blueprint('advisor', __name__)

@advisor_bp.route('/advisors')
def list_advisors():
    # Implement reading all advisors
    return render_template('advisor/advisor_list.html')

@advisor_bp.route('/advisor/create', methods=['GET', 'POST'])
def create_advisor_view():
    if request.method == 'POST':
        # Extract form data and call create_advisor function
        return redirect(url_for('advisor.list_advisors'))
    return render_template('advisor/advisor_form.html')

# Additional routes for update and delete as needed
