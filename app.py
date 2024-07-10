from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index_2():
    return render_template('index.html')

@app.route('/successfully_registered.html')
def success():
    return render_template('successfully_registered.html')


@app.route('/send_form', methods=['POST'])
def submit():
    if request.method == 'POST':
        data = request.json  # Parse JSON data from the request

        #print(data)

        # Extract relevant fields from data
        # Personal Information
        email = data.get('email')
        first_name = data.get('first-name')
        last_name = data.get('last-name')
        age = data.get('age')
        tshirt_size = data.get('tshirt-size')
        country = data.get('country')
        city = data.get('city')
        mobile_number = data.get('mobile-number')
        emergency_contact_name = data.get('emergency-contact-name')
        emergency_contact_number = data.get('emergency-contact-number')

        # Medical Information
        allergies = data.get('allergies')
        prescribed_medication = data.get('prescribed-medication')
        medical_aid = data.get('medical-aid')
        medical_aid_number = data.get('medical-aid-number')
        medical_aid_plan = data.get('medical-aid-plan')
        principal_member = data.get('principal-member')
        dietary_restrictions = data.get('dietary-restrictions')

        # Payment Information
        pickup_location = data.get('pickup-location')
        dropoff_location = data.get('dropoff-location')
        #proof_of_payment = request.files['proof-of-payment')
        region_specific_cost = data.get('region-specific-cost')
        payment_confirmation = data.get('payment-confirmation')

        # Print values to console
        '''print(f"Email: {email}")
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Age: {age}")
        print(f"T-shirt Size: {tshirt_size}")
        print(f"Country: {country}")
        print(f"City: {city}")
        print(f"Mobile Number: {mobile_number}")
        print(f"Emergency Contact Name: {emergency_contact_name}")
        print(f"Emergency Contact Number: {emergency_contact_number}")
        print(f"Allergies: {allergies}")
        print(f"Prescribed Medication: {prescribed_medication}")
        print(f"Medical Aid: {medical_aid}")
        print(f"Medical Aid Number: {medical_aid_number}")
        print(f"Medical Aid Plan: {medical_aid_plan}")
        print(f"Principal Member: {principal_member}")
        print(f"Dietary Restrictions: {dietary_restrictions}")
        print(f"Pickup Location: {pickup_location}")
        print(f"Dropoff Location: {dropoff_location}")
        print(f"Region Specific Cost: {region_specific_cost}")
        print(f"Payment Confirmation: {payment_confirmation}")'''

        # Database connection
        db = mysql.connector.connect(
            host="193.203.168.104",
            user="u468884535_db_regist",
            password="LqZ$@Z4/m",
            database="u468884535_registration"
        )

        cursor = db.cursor()
        
        sql = """
            INSERT INTO registrations (email, first_name, last_name, age, tshirt_size, country, city, mobile_number, emergency_contact_name, emergency_contact_number, allergies, prescribed_medication, medical_aid, medical_aid_number, medical_aid_plan, principal_member, dietary_restrictions, pickup_location, dropoff_location, region_specific_cost, payment_confirmation)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            email,
            first_name,
            last_name,
            age,
            tshirt_size,
            country,
            city,
            mobile_number,
            emergency_contact_name,
            emergency_contact_number,
            allergies,
            prescribed_medication,
            medical_aid,
            medical_aid_number,
            medical_aid_plan,
            principal_member,
            dietary_restrictions,
            pickup_location,
            dropoff_location,
            region_specific_cost,
            payment_confirmation
        )

        response = ""

        try:
            cursor.execute(sql, values)
            db.commit()
            cursor.close()
            return jsonify({'message': 'Form submitted successfully'}), 200
        except Exception as e:
            db.rollback()
            print(str(e))
            cursor.close()
            return jsonify({'error': str(e)}), 500
            

        #return response

if __name__ == '__main__':
    app.run(debug=True)

